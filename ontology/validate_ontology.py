#!/usr/bin/env python3
"""
ontology.json과 ontology.sql 간의 구조적 정합성 검증
표준 레퍼런스 검증 포함
"""

import json
import re
from typing import List, Dict, Set, Tuple

ROOT_CLSF_ID = '03facd74b2d24f7cab807b8980391649'
ROOT_TERM_ID = '4147179070a84d3887b97eb57085d850'

# 유효한 표준 ID 목록 (ontology.json에서 동적으로 로드됨)
VALID_STANDARD_IDS = set()  # Will be populated from ontology.json

# 유효한 매치 타입
VALID_MATCH_TYPES = {
    'EXACT_MATCH', 'CLOSE_MATCH', 'BROAD_MATCH', 'NARROW_MATCH',
    'RELATED_MATCH', 'DERIVED_FROM'
}

class ValidationResult:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []

    def add_error(self, msg: str):
        self.errors.append(f"❌ ERROR: {msg}")

    def add_warning(self, msg: str):
        self.warnings.append(f"⚠️  WARNING: {msg}")

    def add_info(self, msg: str):
        self.info.append(f"ℹ️  INFO: {msg}")

    def print_results(self):
        print("\n" + "="*60)
        print("구조적 정합성 검증 결과")
        print("="*60)

        if self.info:
            print("\n[정보]")
            for msg in self.info:
                print(msg)

        if self.warnings:
            print("\n[경고]")
            for msg in self.warnings:
                print(msg)

        if self.errors:
            print("\n[오류]")
            for msg in self.errors:
                print(msg)
        else:
            print("\n✅ 모든 검증 통과!")

        print("\n" + "="*60)
        print(f"총계: {len(self.errors)} 오류, {len(self.warnings)} 경고, {len(self.info)} 정보")
        print("="*60 + "\n")

def load_json(filepath: str) -> Dict:
    """Load ontology.json and populate VALID_STANDARD_IDS"""
    global VALID_STANDARD_IDS
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Populate VALID_STANDARD_IDS from standards registry
    if 'standards' in data and 'registry' in data['standards']:
        VALID_STANDARD_IDS = {std['id'] for std in data['standards']['registry']}

    return data

def parse_sql(filepath: str) -> Tuple[List[Dict], List[Dict]]:
    """Parse ontology.sql and extract classifications and terms"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    classifications = []
    terms = []

    # Parse MC_CLSF INSERT statements
    # Pattern handles escaped quotes ('') in text fields
    clsf_pattern = r"INSERT INTO MC_CLSF \(CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README\) VALUES \('([^']+)', '((?:[^']|'')+)', '((?:[^']|'')*)', '([^']+)', '([YN])', '((?:[^']|'')*)'\);"

    for match in re.finditer(clsf_pattern, content):
        classifications.append({
            'id': match.group(1),
            'name': match.group(2),
            'description': match.group(3),
            'parent_id': match.group(4),
            'group_yn': match.group(5),
            'readme': match.group(6)
        })

    # Parse MC_TERM INSERT statements (with DIC_ID instead of PRT_TERM_ID)
    # Pattern handles escaped quotes ('') in text fields
    term_pattern = r"INSERT INTO MC_TERM \(TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, DIC_ID, README\) VALUES \('([^']+)', '((?:[^']|'')+)', '((?:[^']|'')*)', '((?:[^']|'')*)', '((?:[^']|'')*)', '([^']+)', '([^']+)'\);"

    for match in re.finditer(term_pattern, content):
        terms.append({
            'id': match.group(1),
            'name_ko': match.group(2),
            'name_en': match.group(3),
            'acronym': match.group(4),
            'description': match.group(5),
            'dic_id': match.group(6),  # DIC_ID instead of parent_id
            'linked_clsf_id': match.group(7)
        })

    return classifications, terms

def parse_txt(filepath: str) -> Tuple[List[Dict], List[Dict]]:
    """Parse context_generated.txt and extract classifications and terms"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    classifications = []
    terms = []

    # Parse classifications (tree structure)
    clsf_pattern = r'([C]\d{8})\s+(.+?)(?=\n|$)'
    for match in re.finditer(clsf_pattern, content):
        classifications.append({
            'id': match.group(1),
            'name': match.group(2).strip()
        })

    # Parse terms (list structure)
    # Format: - T01010001 지방시대 | Local Era
    # Format: - T01010001 지방시대 | Local Era [acronym]
    term_pattern = r'^-\s+([T]\d{8})\s+([^|]+)\|\s+([^\[\n]+)(?:\[([^\]]+)\])?'
    for match in re.finditer(term_pattern, content, re.MULTILINE):
        terms.append({
            'id': match.group(1),
            'name_ko': match.group(2).strip(),
            'name_en': match.group(3).strip(),
            'acronym': match.group(4).strip() if match.group(4) else None
        })

    return classifications, terms

def flatten_json_classifications(data: Dict) -> List[Dict]:
    """Flatten JSON classifications"""
    result = []

    def recurse(items):
        for item in items:
            result.append(item)
            if item.get('children'):
                recurse(item['children'])

    for domain in data['domains']:
        recurse(domain['classifications'])

    return result

def flatten_json_terms(data: Dict) -> List[Dict]:
    """Flatten JSON terms"""
    result = []

    def recurse(items):
        for item in items:
            result.append(item)
            if item.get('children'):
                recurse(item['children'])

    for domain in data['domains']:
        recurse(domain['terms'])

    return result

def validate_structure(result: ValidationResult):
    """Validate overall structure"""
    print("검증 중: ontology.json, generated/ontology.sql, generated/ontology.txt 로딩...")

    # Load data
    json_data = load_json('ontology.json')
    sql_clsf, sql_terms = parse_sql('generated/ontology.sql')
    txt_clsf, txt_terms = parse_txt('generated/ontology.txt')

    json_clsf = flatten_json_classifications(json_data)
    json_terms = flatten_json_terms(json_data)

    result.add_info(f"JSON 분류: {len(json_clsf)}개")
    result.add_info(f"SQL 분류: {len(sql_clsf)}개")
    result.add_info(f"TXT 분류: {len(txt_clsf)}개")
    result.add_info(f"JSON 용어: {len(json_terms)}개")
    result.add_info(f"SQL 용어: {len(sql_terms)}개")
    result.add_info(f"TXT 용어: {len(txt_terms)}개")

    # 1. Count validation
    print("검증 중: 개수 일치...")
    if len(json_clsf) != len(sql_clsf):
        result.add_error(f"분류 개수 불일치: JSON={len(json_clsf)}, SQL={len(sql_clsf)}")

    if len(json_clsf) != len(txt_clsf):
        result.add_error(f"분류 개수 불일치: JSON={len(json_clsf)}, TXT={len(txt_clsf)}")

    if len(json_terms) != len(sql_terms):
        result.add_error(f"용어 개수 불일치: JSON={len(json_terms)}, SQL={len(sql_terms)}")

    if len(json_terms) != len(txt_terms):
        result.add_error(f"용어 개수 불일치: JSON={len(json_terms)}, TXT={len(txt_terms)}")

    # 2. ID uniqueness
    print("검증 중: ID 유일성...")
    json_clsf_ids = set(c['id'] for c in json_clsf)
    sql_clsf_ids = set(c['id'] for c in sql_clsf)
    txt_clsf_ids = set(c['id'] for c in txt_clsf)

    if len(json_clsf_ids) != len(json_clsf):
        result.add_error(f"JSON 분류 ID 중복 발견")

    if len(sql_clsf_ids) != len(sql_clsf):
        result.add_error(f"SQL 분류 ID 중복 발견")

    if len(txt_clsf_ids) != len(txt_clsf):
        result.add_error(f"TXT 분류 ID 중복 발견")

    json_term_ids = set(t['id'] for t in json_terms)
    sql_term_ids = set(t['id'] for t in sql_terms)
    txt_term_ids = set(t['id'] for t in txt_terms)

    if len(json_term_ids) != len(json_terms):
        result.add_error(f"JSON 용어 ID 중복 발견")

    if len(sql_term_ids) != len(sql_terms):
        result.add_error(f"SQL 용어 ID 중복 발견")

    if len(txt_term_ids) != len(txt_terms):
        result.add_error(f"TXT 용어 ID 중복 발견")

    # 3. ID consistency between JSON, SQL, and TXT
    print("검증 중: ID 일치 (JSON-SQL-TXT)...")
    missing_in_sql_clsf = json_clsf_ids - sql_clsf_ids
    missing_in_json_clsf = sql_clsf_ids - json_clsf_ids
    missing_in_txt_clsf = json_clsf_ids - txt_clsf_ids
    extra_in_txt_clsf = txt_clsf_ids - json_clsf_ids

    if missing_in_sql_clsf:
        result.add_error(f"SQL에 누락된 분류 ID: {missing_in_sql_clsf}")

    if missing_in_json_clsf:
        result.add_error(f"JSON에 누락된 분류 ID: {missing_in_json_clsf}")

    if missing_in_txt_clsf:
        result.add_error(f"TXT에 누락된 분류 ID: {missing_in_txt_clsf}")

    if extra_in_txt_clsf:
        result.add_error(f"TXT에만 있는 분류 ID: {extra_in_txt_clsf}")

    missing_in_sql_term = json_term_ids - sql_term_ids
    missing_in_json_term = sql_term_ids - json_term_ids
    missing_in_txt_term = json_term_ids - txt_term_ids
    extra_in_txt_term = txt_term_ids - json_term_ids

    if missing_in_sql_term:
        result.add_error(f"SQL에 누락된 용어 ID: {missing_in_sql_term}")

    if missing_in_json_term:
        result.add_error(f"JSON에 누락된 용어 ID: {missing_in_json_term}")

    if missing_in_txt_term:
        result.add_error(f"TXT에 누락된 용어 ID: {missing_in_txt_term}")

    if extra_in_txt_term:
        result.add_error(f"TXT에만 있는 용어 ID: {extra_in_txt_term}")

    # 4. Parent ID validation
    print("검증 중: 부모 ID 유효성...")
    all_clsf_ids = json_clsf_ids | {ROOT_CLSF_ID}
    all_term_ids = json_term_ids | {ROOT_TERM_ID}

    for clsf in json_clsf:
        parent_id = clsf.get('parent_id')
        if parent_id and parent_id not in all_clsf_ids:
            result.add_error(f"JSON 분류 {clsf['id']}: 잘못된 parent_id={parent_id}")

    for clsf in sql_clsf:
        parent_id = clsf['parent_id']
        if parent_id != ROOT_CLSF_ID and parent_id not in sql_clsf_ids:
            result.add_error(f"SQL 분류 {clsf['id']}: 잘못된 parent_id={parent_id}")

    for term in json_terms:
        parent_id = term.get('parent_id')
        if parent_id and parent_id not in all_term_ids:
            result.add_error(f"JSON 용어 {term['id']}: 잘못된 parent_id={parent_id}")

    # SQL terms now use DIC_ID (always ROOT_TERM_ID) instead of hierarchy
    for term in sql_terms:
        dic_id = term['dic_id']
        if dic_id != ROOT_TERM_ID:
            result.add_error(f"SQL 용어 {term['id']}: DIC_ID should be ROOT_TERM_ID, got {dic_id}")

    # 5. Field consistency (name, description, etc.)
    print("검증 중: 필드 값 일치 (JSON-SQL-TXT)...")
    json_clsf_map = {c['id']: c for c in json_clsf}
    sql_clsf_map = {c['id']: c for c in sql_clsf}
    txt_clsf_map = {c['id']: c for c in txt_clsf}

    for clsf_id in json_clsf_ids & sql_clsf_ids & txt_clsf_ids:
        json_c = json_clsf_map[clsf_id]
        sql_c = sql_clsf_map[clsf_id]
        txt_c = txt_clsf_map[clsf_id]

        if json_c['name'] != sql_c['name']:
            result.add_error(f"분류 {clsf_id}: 이름 불일치 JSON='{json_c['name']}' vs SQL='{sql_c['name']}'")

        if json_c['name'] != txt_c['name']:
            result.add_error(f"분류 {clsf_id}: 이름 불일치 JSON='{json_c['name']}' vs TXT='{txt_c['name']}'")

        if json_c['description'] != sql_c['description']:
            result.add_error(f"분류 {clsf_id}: 설명 불일치")

        # Parent ID mapping
        json_parent = json_c.get('parent_id') or ROOT_CLSF_ID
        sql_parent = sql_c['parent_id']

        if json_parent != sql_parent:
            result.add_error(f"분류 {clsf_id}: parent_id 불일치 JSON={json_parent} vs SQL={sql_parent}")

    json_term_map = {t['id']: t for t in json_terms}
    sql_term_map = {t['id']: t for t in sql_terms}
    txt_term_map = {t['id']: t for t in txt_terms}

    for term_id in json_term_ids & sql_term_ids & txt_term_ids:
        json_t = json_term_map[term_id]
        sql_t = sql_term_map[term_id]
        txt_t = txt_term_map[term_id]

        if json_t['name_ko'] != sql_t['name_ko']:
            result.add_error(f"용어 {term_id}: 한글명 불일치 JSON='{json_t['name_ko']}' vs SQL='{sql_t['name_ko']}'")

        if json_t['name_ko'] != txt_t['name_ko']:
            result.add_error(f"용어 {term_id}: 한글명 불일치 JSON='{json_t['name_ko']}' vs TXT='{txt_t['name_ko']}'")

        if json_t['name_en'] != sql_t['name_en']:
            result.add_error(f"용어 {term_id}: 영문명 불일치 JSON='{json_t['name_en']}' vs SQL='{sql_t['name_en']}'")

        if json_t['name_en'] != txt_t['name_en']:
            result.add_error(f"용어 {term_id}: 영문명 불일치 JSON='{json_t['name_en']}' vs TXT='{txt_t['name_en']}'")

        json_acronym = json_t.get('acronym') or ''
        sql_acronym = sql_t['acronym']
        txt_acronym = txt_t.get('acronym') or ''

        if json_acronym != sql_acronym:
            result.add_error(f"용어 {term_id}: 약어 불일치 JSON='{json_acronym}' vs SQL='{sql_acronym}'")

        if json_acronym != txt_acronym:
            result.add_error(f"용어 {term_id}: 약어 불일치 JSON='{json_acronym}' vs TXT='{txt_acronym}'")

        # Note: SQL terms no longer have hierarchy (parent_id), only DIC_ID
        # Hierarchy is now managed in MC_TERM_REL table

        if json_t['linked_clsf_id'] != sql_t['linked_clsf_id']:
            result.add_error(f"용어 {term_id}: linked_clsf_id 불일치 JSON={json_t['linked_clsf_id']} vs SQL={sql_t['linked_clsf_id']}")

    # 6. ID format validation
    print("검증 중: ID 형식...")
    clsf_pattern = re.compile(r'^C\d{8}$')
    term_pattern = re.compile(r'^T\d{8}$')

    for clsf in json_clsf:
        if not clsf_pattern.match(clsf['id']):
            result.add_error(f"잘못된 분류 ID 형식: {clsf['id']}")

    for term in json_terms:
        if not term_pattern.match(term['id']):
            result.add_error(f"잘못된 용어 ID 형식: {term['id']}")

    # 7. Linked classification validation
    print("검증 중: 용어-분류 연결...")
    for term in json_terms:
        linked_clsf_id = term['linked_clsf_id']
        if linked_clsf_id not in json_clsf_ids:
            result.add_error(f"용어 {term['id']}: 잘못된 linked_clsf_id={linked_clsf_id}")

    # 8. Circular reference check
    print("검증 중: 순환 참조...")
    def has_circular_ref(items, id_field='id', parent_field='parent_id'):
        item_map = {item[id_field]: item for item in items}

        for item in items:
            visited = set()
            current = item

            while current:
                current_id = current[id_field]
                if current_id in visited:
                    return current_id
                visited.add(current_id)

                parent_id = current.get(parent_field)
                if not parent_id or parent_id in [ROOT_CLSF_ID, ROOT_TERM_ID]:
                    break

                current = item_map.get(parent_id)

        return None

    circular_clsf = has_circular_ref(json_clsf)
    if circular_clsf:
        result.add_error(f"분류에서 순환 참조 발견: {circular_clsf}")

    circular_term = has_circular_ref(json_terms)
    if circular_term:
        result.add_error(f"용어에서 순환 참조 발견: {circular_term}")

    # 9. Empty field validation
    print("검증 중: 필수 필드 값...")
    for clsf in json_clsf:
        if not clsf.get('name'):
            result.add_error(f"분류 {clsf['id']}: 이름이 비어있음")
        if not clsf.get('description'):
            result.add_warning(f"분류 {clsf['id']}: 설명이 비어있음")

    for term in json_terms:
        if not term.get('name_ko'):
            result.add_error(f"용어 {term['id']}: 한글명이 비어있음")
        if not term.get('name_en'):
            result.add_error(f"용어 {term['id']}: 영문명이 비어있음")
        if not term.get('description'):
            result.add_warning(f"용어 {term['id']}: 설명이 비어있음")

    # 10. Standard references validation
    print("검증 중: 표준 레퍼런스...")
    validate_standard_refs(json_data, result)

def validate_standard_refs(json_data: Dict, result: ValidationResult):
    """Validate standard references in classifications and terms"""

    # Check standards registry
    if 'standards' not in json_data:
        result.add_warning("표준 레지스트리가 없음 (standards 필드)")
    else:
        std_registry = json_data['standards'].get('registry', [])
        registered_std_ids = {s['id'] for s in std_registry}
        result.add_info(f"등록된 표준 수: {len(registered_std_ids)}")

        # Validate registry standards
        for std in std_registry:
            if std['id'] not in VALID_STANDARD_IDS:
                result.add_warning(f"알 수 없는 표준 ID: {std['id']}")

    # Count standard refs
    clsf_with_refs = 0
    term_with_refs = 0
    total_clsf_refs = 0
    total_term_refs = 0

    for domain in json_data['domains']:
        # Check classifications
        for clsf in flatten_json_items(domain['classifications']):
            std_refs = clsf.get('standard_refs', [])
            if std_refs:
                clsf_with_refs += 1
                total_clsf_refs += len(std_refs)

                for ref in std_refs:
                    # Validate standard_id
                    std_id = ref.get('standard_id')
                    if std_id and std_id not in VALID_STANDARD_IDS:
                        result.add_error(f"분류 {clsf['id']}: 잘못된 표준 ID '{std_id}'")

                    # Validate match_type
                    match_type = ref.get('match_type')
                    if match_type and match_type not in VALID_MATCH_TYPES:
                        result.add_error(f"분류 {clsf['id']}: 잘못된 매치 타입 '{match_type}'")

                    # Validate confidence
                    confidence = ref.get('confidence', 0)
                    if not (0 <= confidence <= 1):
                        result.add_error(f"분류 {clsf['id']}: confidence 값 범위 오류 ({confidence})")

        # Check terms
        for term in flatten_json_items(domain['terms']):
            std_refs = term.get('standard_refs', [])
            if std_refs:
                term_with_refs += 1
                total_term_refs += len(std_refs)

                for ref in std_refs:
                    # Validate standard_id
                    std_id = ref.get('standard_id')
                    if std_id and std_id not in VALID_STANDARD_IDS:
                        result.add_error(f"용어 {term['id']}: 잘못된 표준 ID '{std_id}'")

                    # Validate match_type
                    match_type = ref.get('match_type')
                    if match_type and match_type not in VALID_MATCH_TYPES:
                        result.add_error(f"용어 {term['id']}: 잘못된 매치 타입 '{match_type}'")

                    # Validate confidence
                    confidence = ref.get('confidence', 0)
                    if not (0 <= confidence <= 1):
                        result.add_error(f"용어 {term['id']}: confidence 값 범위 오류 ({confidence})")

    result.add_info(f"표준 레퍼런스가 있는 분류: {clsf_with_refs}개 (총 {total_clsf_refs}개 매핑)")
    result.add_info(f"표준 레퍼런스가 있는 용어: {term_with_refs}개 (총 {total_term_refs}개 매핑)")

def flatten_json_items(items: List[Dict]) -> List[Dict]:
    """Flatten hierarchical items to flat list"""
    result = []
    for item in items:
        result.append(item)
        if item.get('children'):
            result.extend(flatten_json_items(item['children']))
    return result

if __name__ == '__main__':
    result = ValidationResult()

    try:
        validate_structure(result)
    except Exception as e:
        result.add_error(f"검증 중 예외 발생: {str(e)}")
        import traceback
        traceback.print_exc()

    result.print_results()

    # Exit code
    exit(1 if result.errors else 0)
