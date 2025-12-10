#!/usr/bin/env python3
"""
context.txt를 파싱하여 mc_clsf.sql, mc_term.sql 생성
"""

import re
from typing import List, Dict, Tuple

# 상수
ROOT_CLSF_ID = '03facd74b2d24f7cab807b8980391649'
ROOT_TERM_ID = '4147179070a84d3887b97eb57085d850'

def parse_context_txt(filepath: str) -> Tuple[List[Dict], List[Dict]]:
    """
    context.txt 파싱하여 분류와 용어 데이터 추출
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

        # 도메인 제목 추출
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
            parse_classifications(clsf_text, domain_code, domain_name_ko, domain_name_en, classifications)

        # [핵심 용어] 섹션 파싱
        term_section = re.search(r'### \[핵심 용어\](.*?)$', section, re.DOTALL)
        if term_section:
            term_text = term_section.group(1)
            parse_terms(term_text, domain_code, domain_name_ko, domain_name_en, terms)

    return classifications, terms

def parse_classifications(text: str, domain_code: str, domain_name_ko: str, domain_name_en: str, classifications: List[Dict]):
    """분류 체계 파싱"""
    lines = text.strip().split('\n')
    parent_stack = []

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue

        # ID와 이름 추출
        match = re.search(r'([C]\d{8})\s+(.+)$', line)
        if not match:
            continue

        clsf_id = match.group(1)
        clsf_name = match.group(2).strip()

        # 트리 기호 앞 부분 추출
        tree_symbols = line.split(clsf_id)[0]
        indent = len(tree_symbols) - len(tree_symbols.lstrip(' '))
        pipe_count = tree_symbols.count('│')

        # 레벨 계산
        if line.strip().startswith('-'):
            level = 0
            parent_id = ROOT_CLSF_ID
            parent_stack = [(clsf_id, level)]
        elif pipe_count > 0:
            level = pipe_count + 1
            while parent_stack and parent_stack[-1][1] >= level:
                parent_stack.pop()
            parent_id = parent_stack[-1][0] if parent_stack else ROOT_CLSF_ID
            parent_stack.append((clsf_id, level))
        else:
            level = indent // 2
            while parent_stack and parent_stack[-1][1] >= level:
                parent_stack.pop()
            parent_id = parent_stack[-1][0] if parent_stack else ROOT_CLSF_ID
            parent_stack.append((clsf_id, level))

        # GROUP_YN 결정
        id_suffix = clsf_id[-4:]
        mid_code = clsf_id[3:7]

        if mid_code == '0000':
            group = 'Y'
        elif id_suffix == '0001':
            group = 'Y'
        else:
            group = 'N'

        classifications.append({
            'id': clsf_id,
            'name': clsf_name,
            'parent_id': parent_id,
            'group': group,
            'level': level,
            'domain_code': domain_code,
            'domain_name_ko': domain_name_ko,
            'domain_name_en': domain_name_en
        })

def parse_terms(text: str, domain_code: str, domain_name_ko: str, domain_name_en: str, terms: List[Dict]):
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
        acronym = term_match.group(4).strip() if term_match.group(4) else None

        # 연결 분류 ID
        linked_clsf_id = 'C' + term_id[1:5] + '0001'

        terms.append({
            'id': term_id,
            'name_ko': term_name_ko,
            'name_en': term_name_en,
            'acronym': acronym,
            'linked_clsf_id': linked_clsf_id,
            'domain_code': domain_code,
            'domain_name_ko': domain_name_ko,
            'domain_name_en': domain_name_en
        })

def generate_mc_clsf_sql(classifications: List[Dict], output_file: str):
    """mc_clsf.sql 생성"""

    with open(output_file, 'w', encoding='utf-8') as f:
        # 헤더
        f.write("------------------------------------------------------------\n")
        f.write("-- MC_CLSF : 분류 체계\n")
        f.write("-- context.txt 기준 ID 체계 적용\n")
        f.write("--\n")
        f.write("-- ID 체계: C + DD(도메인) + LL(중분류) + SSSS(일련번호)\n")
        f.write("-- 예: C01010001 = 도메인01 + 중분류01 + 일련번호0001\n")
        f.write("--\n")
        f.write("-- 간소화 INSERT (DELETE_YN, CREATE_ID, CREATE_DT 제외 - 기본값 사용)\n")
        f.write(f"-- 최상위 PRT_CLSF_ID : '{ROOT_CLSF_ID}'\n")
        f.write("------------------------------------------------------------\n\n")

        current_domain = None

        for clsf in classifications:
            # 도메인 변경 시 섹션 헤더
            if clsf['domain_code'] != current_domain:
                current_domain = clsf['domain_code']
                f.write("\n")
                f.write("------------------------------------------------------------\n")
                f.write(f"-- {clsf['domain_code']}. {clsf['domain_name_ko']} | {clsf['domain_name_en']}\n")
                f.write("------------------------------------------------------------\n\n")

            # 중분류 주석
            if clsf['level'] == 1:
                f.write(f"-- {clsf['domain_code']}-{clsf['id'][3:5]}. {clsf['name']}\n")

            # INSERT 문
            desc = generate_clsf_desc(clsf)
            readme = generate_clsf_readme(clsf)

            f.write("INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)\n")
            f.write(f"VALUES ('{clsf['id']}', '{escape_quotes(clsf['name'])}', '{escape_quotes(desc)}', '{clsf['parent_id']}', '{clsf['group']}',\n")
            f.write(f"'{escape_quotes(readme)}');\n\n")

def generate_mc_term_sql(terms: List[Dict], output_file: str):
    """mc_term.sql 생성"""

    with open(output_file, 'w', encoding='utf-8') as f:
        # 헤더
        f.write("------------------------------------------------------------\n")
        f.write("-- MC_TERM : 용어 체계\n")
        f.write("-- context.txt 기준 ID 체계 적용\n")
        f.write("--\n")
        f.write("-- ID 체계: T + DD(도메인) + LL(중분류) + SSSS(일련번호)\n")
        f.write("-- 예: T01010001 = 도메인01 + 중분류01 + 일련번호0001\n")
        f.write("--\n")
        f.write("-- 간소화 INSERT (DELETE_YN, CREATE_ID, CREATE_DT 제외 - 기본값 사용)\n")
        f.write("-- TERM_NAME_EN: 영문명, ACRONYM: 약어, TERM_DESC: 설명, README: 관련 분류 ID\n")
        f.write(f"-- 최상위 PRT_TERM_ID : '{ROOT_TERM_ID}'\n")
        f.write("------------------------------------------------------------\n\n")

        current_domain = None
        current_category = None

        for term in terms:
            # 도메인 변경 시 섹션 헤더
            if term['domain_code'] != current_domain:
                current_domain = term['domain_code']
                f.write("\n")
                f.write("------------------------------------------------------------\n")
                f.write(f"-- {term['domain_code']}. {term['domain_name_ko']} | {term['domain_name_en']}\n")
                f.write("------------------------------------------------------------\n\n")

            # 중분류 변경 시 주석
            category_code = term['id'][1:5]
            if category_code != current_category:
                current_category = category_code
                f.write(f"-- {term['domain_code']}-{term['id'][3:5]} 관련 용어\n")

            # INSERT 문
            desc = generate_term_desc(term)
            acronym_value = f"'{term['acronym']}'" if term['acronym'] else 'NULL'

            f.write("INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)\n")
            f.write(f"VALUES ('{term['id']}', '{escape_quotes(term['name_ko'])}', '{escape_quotes(term['name_en'])}', {acronym_value},\n")
            f.write(f"'{escape_quotes(desc)}',\n")
            f.write(f"'{ROOT_TERM_ID}', 'T', '{term['linked_clsf_id']}');\n\n")

def generate_clsf_desc(clsf: Dict) -> str:
    """분류 설명 생성"""
    if clsf['level'] == 0:
        return f"{clsf['name']} 부문 정책 및 제도 전반을 다루는 최상위 분류"
    elif clsf['level'] == 1:
        return f"{clsf['name']}을(를) 다루는 분류"
    else:
        return f"{clsf['name']} 관련 분류"

def generate_clsf_readme(clsf: Dict) -> str:
    """분류 README 생성"""
    if clsf['level'] == 0:
        return f"도메인 {clsf['domain_code']}. {clsf['name']} 부문 전반을 포괄."
    elif clsf['level'] == 1:
        return f"중분류 {clsf['domain_code']}-{clsf['id'][3:5]}. {clsf['name']} 관련 정책 및 제도 포함."
    else:
        return f"소분류. {clsf['name']} 관련."

def generate_term_desc(term: Dict) -> str:
    """용어 설명 생성"""
    return f"{term['name_ko']} ({term['name_en']})"

def escape_quotes(text: str) -> str:
    """작은따옴표 이스케이프"""
    return text.replace("'", "''")

if __name__ == '__main__':
    input_file = 'context.txt'
    clsf_output = 'mc_clsf.sql'
    term_output = 'mc_term.sql'

    print(f"Reading {input_file}...")
    classifications, terms = parse_context_txt(input_file)

    print(f"Parsed {len(classifications)} classifications")
    print(f"Parsed {len(terms)} terms")

    print(f"\nGenerating {clsf_output}...")
    generate_mc_clsf_sql(classifications, clsf_output)

    print(f"Generating {term_output}...")
    generate_mc_term_sql(terms, term_output)

    print(f"\n✓ Generated {clsf_output}")
    print(f"✓ Generated {term_output}")
