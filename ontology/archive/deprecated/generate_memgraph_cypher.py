#!/usr/bin/env python3
"""
context.txt를 파싱하여 Memgraph용 Cypher 쿼리 생성
"""

import re
from typing import List, Dict, Tuple

def parse_context_txt(filepath: str) -> Tuple[List[Dict], List[Dict]]:
    """
    context.txt 파싱하여 분류와 용어 데이터 추출

    Returns:
        (classifications, terms) 튜플
    """
    classifications = []
    terms = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 도메인별로 분할
    sections = re.split(r'^---$', content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        # 도메인 제목 추출 (예: ## 01. 공공 | Public Sector)
        domain_match = re.search(r'^## (\d+)\. (.+?) \| (.+?)$', section, re.MULTILINE)
        if not domain_match:
            continue

        domain_code = domain_match.group(1)
        domain_name_ko = domain_match.group(2)
        domain_name_en = domain_match.group(3)

        # [분류 체계] 섹션 파싱
        clsf_section = re.search(r'### \[분류 체계\](.*?)### \[핵심 용어\]', section, re.DOTALL)
        if clsf_section:
            clsf_text = clsf_section.group(1)
            parse_classifications(clsf_text, domain_code, classifications)

        # [핵심 용어] 섹션 파싱
        term_section = re.search(r'### \[핵심 용어\](.*?)$', section, re.DOTALL)
        if term_section:
            term_text = term_section.group(1)
            parse_terms(term_text, domain_code, terms)

    return classifications, terms

def parse_classifications(text: str, domain_code: str, classifications: List[Dict]):
    """분류 체계 파싱"""
    lines = text.strip().split('\n')
    parent_stack = []

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue

        # 전체 라인에서 ID와 이름 추출
        match = re.search(r'([CT]\d{8})\s+(.+)$', line)
        if not match:
            continue

        clsf_id = match.group(1)
        clsf_name = match.group(2).strip()

        # 트리 기호로 레벨 판단
        # - C01000001 공공              -> level 0 (루트)
        #   ├ C01010001                 -> level 1 (2칸 공백)
        #   │ └ C01010002               -> level 2 (2칸 + │)
        #     └ C01060001               -> level 1 (2칸 공백)
        #       ├ C01060002             -> level 2 (4칸 공백)

        # 트리 기호 앞 부분 추출
        tree_symbols = line.split(clsf_id)[0]

        # 공백 개수와 │ 문자 개수로 레벨 판단
        indent = len(tree_symbols) - len(tree_symbols.lstrip(' '))
        pipe_count = tree_symbols.count('│')

        if line.strip().startswith('-'):  # 루트
            level = 0
            parent_id = None
            parent_stack = [(clsf_id, level)]
        elif pipe_count > 0:  # │ 가 있으면 pipe_count + 1
            level = pipe_count + 1
            while parent_stack and parent_stack[-1][1] >= level:
                parent_stack.pop()
            parent_id = parent_stack[-1][0] if parent_stack else None
            parent_stack.append((clsf_id, level))
        else:  # │ 가 없으면 공백으로 판단
            # 2칸: level 1, 4칸: level 2, 6칸: level 3
            level = indent // 2
            while parent_stack and parent_stack[-1][1] >= level:
                parent_stack.pop()
            parent_id = parent_stack[-1][0] if parent_stack else None
            parent_stack.append((clsf_id, level))

        # GROUP_YN 결정
        # ID 패턴으로 판단: CDD000001 (도메인), CDDLL0001 (중분류)는 group=true
        # CDDLLSSSS (소분류, SSSS > 0001)는 group=false
        id_suffix = clsf_id[-4:]
        mid_code = clsf_id[3:7]

        if mid_code == '0000':  # 도메인
            group = True
        elif id_suffix == '0001':  # 중분류
            group = True
        else:  # 소분류
            group = False

        classifications.append({
            'id': clsf_id,
            'name': clsf_name,
            'parent_id': parent_id,
            'group': group,
            'level': level
        })

def parse_terms(text: str, domain_code: str, terms: List[Dict]):
    """용어 파싱"""
    lines = text.strip().split('\n')

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue

        # 형식: - T01010001 지방시대 | Local Era
        # 또는: - T02010003 공개시장운영 | Open Market Operations [OMO]
        term_match = re.match(r'^-\s+([T]\d{8})\s+([^|]+)\|\s+([^\[]+)(?:\[([^\]]+)\])?', line)
        if not term_match:
            continue

        term_id = term_match.group(1)
        term_name_ko = term_match.group(2).strip()
        term_name_en = term_match.group(3).strip()
        acronym = term_match.group(4).strip() if term_match.group(4) else ''

        # 연결 분류 ID 추출 (도메인+중분류)
        # T01010001 -> C01010001
        # T[1:5] = 0101 (도메인 2자리 + 중분류 2자리)
        linked_clsf_id = 'C' + term_id[1:5] + '0001'

        terms.append({
            'id': term_id,
            'name_ko': term_name_ko,
            'name_en': term_name_en,
            'acronym': acronym,
            'linked_clsf_id': linked_clsf_id
        })

def generate_memgraph_cypher(classifications: List[Dict], terms: List[Dict], output_file: str):
    """Memgraph용 Cypher 쿼리 생성"""

    with open(output_file, 'w', encoding='utf-8') as f:
        # 헤더
        f.write("// Memgraph Cypher 쿼리\n")
        f.write("// Auto-generated from context.txt\n")
        f.write("// Generated by generate_memgraph_cypher.py\n\n")

        # 인덱스 및 제약 조건
        f.write("// 인덱스 및 제약 조건\n")
        f.write("CREATE CONSTRAINT ON (c:Classification) ASSERT c.id IS UNIQUE;\n")
        f.write("CREATE CONSTRAINT ON (t:Term) ASSERT t.id IS UNIQUE;\n\n")

        # 분류 노드 생성
        f.write("// ======================================\n")
        f.write("// 분류(Classification) 노드 생성\n")
        f.write("// ======================================\n\n")

        for clsf in classifications:
            f.write(f"// {clsf['name']}\n")
            f.write(f"CREATE (c:Classification {{\n")
            f.write(f"  id: '{clsf['id']}',\n")
            f.write(f"  name: '{escape_quotes(clsf['name'])}',\n")
            f.write(f"  display_name: '{escape_quotes(clsf['name'])} (Classification)',\n")
            f.write(f"  group: {str(clsf['group']).lower()},\n")
            f.write(f"  level: {clsf['level']}\n")
            f.write(f"}});\n\n")

        # 분류 계층 관계 생성
        f.write("// ======================================\n")
        f.write("// 분류 계층 관계(PARENT_OF)\n")
        f.write("// ======================================\n\n")

        for clsf in classifications:
            if clsf['parent_id']:
                f.write(f"// {clsf['name']} -> {clsf['parent_id']}\n")
                f.write(f"MATCH (parent:Classification {{id: '{clsf['parent_id']}'}})\n")
                f.write(f"MATCH (child:Classification {{id: '{clsf['id']}'}})\n")
                f.write(f"CREATE (parent)-[:PARENT_OF]->(child);\n\n")

        # 용어 노드 생성
        f.write("// ======================================\n")
        f.write("// 용어(Term) 노드 생성\n")
        f.write("// ======================================\n\n")

        for term in terms:
            f.write(f"// {term['name_ko']}\n")
            f.write(f"CREATE (t:Term {{\n")
            f.write(f"  id: '{term['id']}',\n")
            f.write(f"  name_ko: '{escape_quotes(term['name_ko'])}',\n")
            f.write(f"  name_en: '{escape_quotes(term['name_en'])}',\n")
            if term['acronym']:
                f.write(f"  acronym: '{escape_quotes(term['acronym'])}',\n")
            f.write(f"  display_name: '{escape_quotes(term['name_ko'])} (Term)'\n")
            f.write(f"}});\n\n")

        # 용어-분류 연결 관계
        f.write("// ======================================\n")
        f.write("// 용어-분류 연결 관계(BELONGS_TO)\n")
        f.write("// ======================================\n\n")

        for term in terms:
            f.write(f"// {term['name_ko']} -> {term['linked_clsf_id']}\n")
            f.write(f"MATCH (term:Term {{id: '{term['id']}'}})\n")
            f.write(f"MATCH (clsf:Classification {{id: '{term['linked_clsf_id']}'}})\n")
            f.write(f"CREATE (term)-[:BELONGS_TO]->(clsf);\n\n")

        f.write("// ======================================\n")
        f.write("// 완료\n")
        f.write("// ======================================\n")

def escape_quotes(text: str) -> str:
    """작은따옴표 이스케이프"""
    return text.replace("'", "\\'")

if __name__ == '__main__':
    input_file = 'context.txt'
    output_file = 'memgraph.cypher'

    print(f"Reading {input_file}...")
    classifications, terms = parse_context_txt(input_file)

    print(f"Parsed {len(classifications)} classifications")
    print(f"Parsed {len(terms)} terms")

    print(f"\nGenerating {output_file}...")
    generate_memgraph_cypher(classifications, terms, output_file)

    print(f"✓ Generated {output_file}")
