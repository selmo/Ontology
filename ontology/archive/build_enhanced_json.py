#!/usr/bin/env python3
"""
enhanced_data.py의 상세 정보를 포함하여 context.json 재생성
표준 레퍼런스(standardRefs) 포함
"""

import json
import re
from typing import List, Dict
from datetime import datetime
from enhanced_data import (
    CLASSIFICATION_README,
    TERM_DESCRIPTIONS,
    TERM_SYNONYMS,
    TERM_RELATED,
    TERM_HIERARCHY
)
from standards_registry import (
    STANDARDS_REGISTRY,
    CLASSIFICATION_STANDARD_REFS,
    TERM_STANDARD_REFS,
    DOMAIN_PRIMARY_STANDARDS,
    get_classification_refs,
    get_term_refs,
)

ROOT_CLSF_ID = '03facd74b2d24f7cab807b8980391649'
ROOT_TERM_ID = '4147179070a84d3887b97eb57085d850'

def build_standards_metadata() -> Dict:
    """표준 레지스트리 메타데이터 생성"""
    standards_list = []
    for std_id, std_info in STANDARDS_REGISTRY.items():
        standards_list.append({
            "id": std_id,
            "code": std_info["code"],
            "name_ko": std_info["name_ko"],
            "name_en": std_info["name_en"],
            "type": std_info["type"],
            "scope": std_info["scope"],
            "organization": std_info["organization"],
            "version": std_info["version"],
            "uri": std_info["uri"],
            "description": std_info["description"],
        })
    return {
        "count": len(standards_list),
        "registry": standards_list
    }

def parse_context_txt(filepath: str):
    """context.txt 파싱"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        "metadata": {
            "version": "3.2.0",
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "description": "MC 분류·용어 통합 체계 (상세 설명, 관계, 표준 레퍼런스 포함)"
        },
        "id_schema": {
            "classification": "C + DD(도메인) + LL(중분류) + SSSS(일련번호)",
            "term": "T + DD(도메인) + LL(중분류) + SSSS(일련번호)"
        },
        "constants": {
            "root_clsf_id": ROOT_CLSF_ID,
            "root_term_id": ROOT_TERM_ID
        },
        "standards": build_standards_metadata(),
        "domains": []
    }

    sections = re.split(r'^---$', content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        domain_match = re.search(r'^## (\d+)\. (.+?) \| (.+?)$', section, re.MULTILINE)
        if not domain_match:
            continue

        domain_code = domain_match.group(1)
        domain = {
            "code": domain_code,
            "name_ko": domain_match.group(2),
            "name_en": domain_match.group(3),
            "description": f"{domain_match.group(2)} 부문 정책 및 제도 전반",
            "primary_standards": DOMAIN_PRIMARY_STANDARDS.get(domain_code, []),
            "classifications": [],
            "terms": []
        }

        # 분류 파싱
        clsf_section = re.search(r'### \[분류 체계\](.*?)### \[핵심 용어\]', section, re.DOTALL)
        if clsf_section:
            parse_classifications(clsf_section.group(1), domain)

        # 용어 파싱
        term_section = re.search(r'### \[핵심 용어\](.*?)$', section, re.DOTALL)
        if term_section:
            parse_terms(term_section.group(1), domain)

        data["domains"].append(domain)

    return data

def parse_classifications(text: str, domain: Dict):
    """분류 파싱 및 계층 구조 생성"""
    lines = text.strip().split('\n')
    parent_stack = []
    flat_list = []

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue

        match = re.search(r'([C]\d{8})\s+(.+)$', line)
        if not match:
            continue

        clsf_id = match.group(1)
        clsf_name = match.group(2).strip()

        tree_symbols = line.split(clsf_id)[0]
        indent = len(tree_symbols) - len(tree_symbols.lstrip(' '))
        pipe_count = tree_symbols.count('│')

        if line.strip().startswith('-'):
            level = 0
            parent_id = None
        elif pipe_count > 0:
            level = pipe_count + 1
            while parent_stack and parent_stack[-1]['level'] >= level:
                parent_stack.pop()
            parent_id = parent_stack[-1]['id'] if parent_stack else None
        else:
            level = indent // 2
            while parent_stack and parent_stack[-1]['level'] >= level:
                parent_stack.pop()
            parent_id = parent_stack[-1]['id'] if parent_stack else None

        id_suffix = clsf_id[-4:]
        mid_code = clsf_id[3:7]
        group = mid_code == '0000' or id_suffix == '0001'

        # 상세 정보 추가
        description = generate_clsf_desc(clsf_name, level)
        readme = CLASSIFICATION_README.get(clsf_id, f"{clsf_name} 관련.")

        # 표준 레퍼런스 추가
        standard_refs = get_classification_refs(clsf_id)
        primary_standard = standard_refs[0]['standard_id'] if standard_refs else None

        clsf_obj = {
            "id": clsf_id,
            "name": clsf_name,
            "description": description,
            "readme": readme,
            "group": group,
            "level": level,
            "parent_id": parent_id,
            "standard_refs": standard_refs,
            "primary_standard": primary_standard,
            "children": []
        }

        flat_list.append(clsf_obj)
        parent_stack.append(clsf_obj)

    domain['classifications'] = build_hierarchy(flat_list)

def parse_terms(text: str, domain: Dict):
    """용어 파싱 및 계층 구조 생성"""
    lines = text.strip().split('\n')
    flat_list = []

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue

        term_match = re.match(r'^-\s+([T]\d{8})\s+([^|]+)\|\s+([^\[]+)(?:\[([^\]]+)\])?', line)
        if not term_match:
            continue

        term_id = term_match.group(1)
        term_name_ko = term_match.group(2).strip()
        term_name_en = term_match.group(3).strip()
        acronym = term_match.group(4).strip() if term_match.group(4) else None

        linked_clsf_id = 'C' + term_id[1:5] + '0001'
        parent_id = TERM_HIERARCHY.get(term_id, None)

        # 상세 설명 추가
        description = TERM_DESCRIPTIONS.get(term_id, f"{term_name_ko} ({term_name_en})")

        # 동의어 추가
        synonyms = TERM_SYNONYMS.get(term_id, [])

        # 연관 용어 추가
        related_terms = TERM_RELATED.get(term_id, [])

        # 표준 레퍼런스 추가
        standard_refs = get_term_refs(term_id)
        primary_standard = standard_refs[0]['standard_id'] if standard_refs else None

        term_obj = {
            "id": term_id,
            "name_ko": term_name_ko,
            "name_en": term_name_en,
            "acronym": acronym,
            "description": description,
            "synonyms": synonyms,
            "related_terms": related_terms,
            "linked_clsf_id": linked_clsf_id,
            "parent_id": parent_id,
            "standard_refs": standard_refs,
            "primary_standard": primary_standard,
            "children": []
        }

        flat_list.append(term_obj)

    domain['terms'] = build_hierarchy(flat_list)

def build_hierarchy(flat_list: List[Dict]) -> List[Dict]:
    """평면 리스트를 계층 구조로 변환"""
    id_map = {item['id']: item for item in flat_list}
    root_items = []

    for item in flat_list:
        parent_id = item.get('parent_id')
        if parent_id and parent_id in id_map:
            id_map[parent_id]['children'].append(item)
        else:
            root_items.append(item)

    return root_items

def generate_clsf_desc(name: str, level: int) -> str:
    """분류 설명 생성"""
    if level == 0:
        return f"{name} 부문 정책 및 제도 전반을 다루는 최상위 분류"
    elif level == 1:
        return f"{name}을(를) 다루는 분류"
    else:
        return f"{name} 관련 분류"

def count_items(items: List[Dict]) -> int:
    """재귀적으로 아이템 개수 세기"""
    count = len(items)
    for item in items:
        count += count_items(item.get('children', []))
    return count

if __name__ == '__main__':
    input_file = 'context.txt'
    output_file = 'context.json'

    print(f"Parsing {input_file}...")
    data = parse_context_txt(input_file)

    print(f"Writing {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 통계 출력
    total_clsf = sum(count_items(d['classifications']) for d in data['domains'])
    total_terms = sum(count_items(d['terms']) for d in data['domains'])

    # 동의어 및 연관 관계 통계
    def count_relations(items):
        count = {'synonyms': 0, 'related': 0, 'standard_refs': 0}
        for item in items:
            if 'synonyms' in item:
                count['synonyms'] += len(item['synonyms'])
            if 'related_terms' in item:
                count['related'] += len(item['related_terms'])
            if 'standard_refs' in item:
                count['standard_refs'] += len(item['standard_refs'])
            child_counts = count_relations(item.get('children', []))
            count['synonyms'] += child_counts['synonyms']
            count['related'] += child_counts['related']
            count['standard_refs'] += child_counts['standard_refs']
        return count

    synonym_count = 0
    related_count = 0
    std_ref_count = 0
    for domain in data['domains']:
        term_counts = count_relations(domain['terms'])
        clsf_counts = count_relations(domain['classifications'])
        synonym_count += term_counts['synonyms']
        related_count += term_counts['related']
        std_ref_count += term_counts['standard_refs'] + clsf_counts['standard_refs']

    # 표준 레지스트리 통계
    std_count = data['standards']['count']

    print(f"\n✓ Generated {output_file}")
    print(f"  - {len(data['domains'])} domains")
    print(f"  - {total_clsf} classifications")
    print(f"  - {total_terms} terms")
    print(f"  - {synonym_count} synonyms")
    print(f"  - {related_count} related term links")
    print(f"  - {std_count} standards registered")
    print(f"  - {std_ref_count} standard references mapped")
