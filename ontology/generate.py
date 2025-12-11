#!/usr/bin/env python3
"""
ontology.json으로부터 다음 파일 생성:
- ontology.txt (minimal - IDs and names only)
- mc_clsf.sql (분류 테이블)
- mc_term.sql (용어 테이블, DIC_ID 사용)
- mc_term_rel.sql (용어 관계 테이블, 동의어/연관용어/계층)
- mc_std_ref.sql (표준 레퍼런스 테이블)
- ontology.sql (통합 SQL: MC_CLSF + MC_TERM + MC_TERM_REL + MC_STD_REF)
- ontology.cypher (Memgraph 그래프 DB 쿼리)
- standards_registry.json (표준 레지스트리 독립 파일)
"""

import json
from typing import List, Dict

ROOT_CLSF_ID = '03facd74b2d24f7cab807b8980391649'
ROOT_TERM_ID = '4147179070a84d3887b97eb57085d850'

def load_ontology_json(filepath: str) -> Dict:
    """Load ontology.json"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def flatten_classifications(items: List[Dict], result: List[Dict] = None) -> List[Dict]:
    """Flatten hierarchical classifications to flat list"""
    if result is None:
        result = []

    for item in items:
        result.append(item)
        if item.get('children'):
            flatten_classifications(item['children'], result)

    return result

def flatten_terms(items: List[Dict], result: List[Dict] = None) -> List[Dict]:
    """Flatten hierarchical terms to flat list"""
    if result is None:
        result = []

    for item in items:
        result.append(item)
        if item.get('children'):
            flatten_terms(item['children'], result)

    return result

# ==================== ontology.txt 생성 ====================

def generate_ontology_txt(data: Dict) -> str:
    """Generate minimal ontology.txt with IDs and names only"""
    lines = []
    lines.append("# MC 분류·용어 통합 체계")
    lines.append("")
    lines.append(f"**버전:** {data['metadata']['version']}")
    lines.append(f"**최종 업데이트:** {data['metadata']['last_updated']}")
    lines.append("")
    lines.append("## ID 체계")
    lines.append("")
    lines.append(f"- **분류 ID**: {data['id_schema']['classification']}")
    lines.append(f"- **용어 ID**: {data['id_schema']['term']}")
    lines.append("")
    lines.append("## 도메인 구조")
    lines.append("")

    for domain in data['domains']:
        lines.append("---")
        lines.append(f"## {domain['code']}. {domain['name_ko']} | {domain['name_en']}")
        lines.append("")

        # 분류
        lines.append("### [분류 체계]")
        lines.append("")
        lines.extend(render_clsf_tree(domain['classifications']))
        lines.append("")

        # 용어
        lines.append("### [핵심 용어]")
        lines.append("")
        lines.extend(render_term_list(domain['terms']))
        lines.append("")

    return '\n'.join(lines)

def render_clsf_tree(items: List[Dict], prefix: str = '', is_last: bool = True) -> List[str]:
    """Render classification tree with minimal info"""
    lines = []

    for i, item in enumerate(items):
        is_last_item = (i == len(items) - 1)

        if item.get('level', 0) == 0:
            # Domain level
            lines.append(f"- {item['id']} {item['name']}")
        else:
            # Child items
            connector = '└' if is_last_item else '├'
            lines.append(f"{prefix}{connector} {item['id']} {item['name']}")

        if item.get('children'):
            new_prefix = prefix + ('  ' if is_last_item else '│ ')
            lines.extend(render_clsf_tree(item['children'], new_prefix, is_last_item))

    return lines

def render_term_list(items: List[Dict]) -> List[str]:
    """Render term list with minimal info"""
    lines = []

    for item in items:
        if item.get('acronym'):
            lines.append(f"- {item['id']} {item['name_ko']} | {item['name_en']} [{item['acronym']}]")
        else:
            lines.append(f"- {item['id']} {item['name_ko']} | {item['name_en']}")

        if item.get('children'):
            lines.extend(render_term_list(item['children']))

    return lines

# ==================== mc_clsf.sql 생성 ====================

def generate_mc_clsf_sql(data: Dict) -> str:
    """Generate mc_clsf.sql with detailed README"""
    lines = []
    lines.append("-- MC_CLSF 분류 테이블 INSERT 문")
    lines.append(f"-- Generated: {data['metadata']['last_updated']}")
    lines.append("")

    for domain in data['domains']:
        lines.append(f"-- {domain['name_ko']} ({domain['name_en']})")

        flat_clsf = flatten_classifications(domain['classifications'])

        for clsf in flat_clsf:
            parent_id = clsf.get('parent_id') or ROOT_CLSF_ID
            group_yn = 'Y' if clsf.get('group') else 'N'

            # README escape
            readme = clsf.get('readme', '').replace("'", "''")

            lines.append(
                f"INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README) "
                f"VALUES ('{clsf['id']}', '{clsf['name']}', '{clsf['description']}', '{parent_id}', '{group_yn}', '{readme}');"
            )

        lines.append("")

    return '\n'.join(lines)

# ==================== mc_term.sql 생성 ====================

def generate_mc_term_sql(data: Dict) -> str:
    """Generate mc_term.sql with detailed TERM_DESC and DIC_ID"""
    lines = []
    lines.append("-- MC_TERM 용어 테이블 INSERT 문")
    lines.append(f"-- Generated: {data['metadata']['last_updated']}")
    lines.append("")

    for domain in data['domains']:
        lines.append(f"-- {domain['name_ko']} ({domain['name_en']})")

        flat_terms = flatten_terms(domain['terms'])

        for term in flat_terms:
            # DIC_ID는 ROOT_TERM_ID 사용 (기존 PRT_TERM_ID 역할)
            dic_id = ROOT_TERM_ID
            acronym = term.get('acronym') or ''

            # Escape single quotes
            term_desc = term.get('description', '').replace("'", "''")

            lines.append(
                f"INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, DIC_ID, README) "
                f"VALUES ('{term['id']}', '{term['name_ko']}', '{term['name_en']}', '{acronym}', '{term_desc}', '{dic_id}', '{term['linked_clsf_id']}');"
            )

        lines.append("")

    return '\n'.join(lines)

# ==================== mc_term_rel.sql 생성 ====================

def generate_mc_term_rel_sql(data: Dict) -> str:
    """Generate mc_term_rel.sql with synonyms and related terms"""
    lines = []
    lines.append("-- MC_TERM_REL 용어 관계 테이블 INSERT 문")
    lines.append(f"-- Generated: {data['metadata']['last_updated']}")
    lines.append("-- REL_TYPE: 'S' (Synonym), 'T' (Related Term)")
    lines.append("")

    for domain in data['domains']:
        flat_terms = flatten_terms(domain['terms'])

        has_relations = any(term.get('synonyms') or term.get('parent_id') or term.get('related_terms')
                           for term in flat_terms)

        if has_relations:
            lines.append(f"-- {domain['name_ko']} ({domain['name_en']})")
            lines.append("")

        # 계층 구조 관계 (부모-자식)
        hierarchy_found = False
        for term in flat_terms:
            if term.get('parent_id'):
                if not hierarchy_found:
                    lines.append("-- 계층 구조 (Term Hierarchy)")
                    hierarchy_found = True
                lines.append(
                    f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                    f"VALUES ('{term['id']}', 'T', '{term['parent_id']}');"
                )

        if hierarchy_found:
            lines.append("")

        # 동의어 관계 (타입별 구분, v3.12+)
        # REL_TYPE: 'S' (Term→Term), 'SE' (Exact), 'SC' (Close), 'SR' (Related), 'SB' (Broader), 'SN' (Narrower)
        synonym_found = False
        for term in flat_terms:
            if term.get('synonyms'):
                if not synonym_found:
                    lines.append("-- 동의어 (Synonyms - Typed)")
                    synonym_found = True

                synonyms = term['synonyms']

                # Handle structured synonyms (v3.12+)
                if isinstance(synonyms, dict):
                    # Term → Term synonyms
                    for synonym_term_id in synonyms.get('terms', []):
                        lines.append(
                            f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                            f"VALUES ('{term['id']}', 'S', '{synonym_term_id}');"
                        )

                    # Exact synonyms
                    for synonym_str in synonyms.get('exact', []):
                        synonym_escaped = synonym_str.replace("'", "''")
                        lines.append(
                            f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                            f"VALUES ('{term['id']}', 'SE', '{synonym_escaped}');"
                        )

                    # Close synonyms
                    for synonym_str in synonyms.get('close', []):
                        synonym_escaped = synonym_str.replace("'", "''")
                        lines.append(
                            f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                            f"VALUES ('{term['id']}', 'SC', '{synonym_escaped}');"
                        )

                    # Related synonyms
                    for synonym_str in synonyms.get('related', []):
                        synonym_escaped = synonym_str.replace("'", "''")
                        lines.append(
                            f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                            f"VALUES ('{term['id']}', 'SR', '{synonym_escaped}');"
                        )

                    # Broader
                    for synonym_str in synonyms.get('broader', []):
                        synonym_escaped = synonym_str.replace("'", "''")
                        lines.append(
                            f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                            f"VALUES ('{term['id']}', 'SB', '{synonym_escaped}');"
                        )

                    # Narrower
                    for synonym_str in synonyms.get('narrower', []):
                        synonym_escaped = synonym_str.replace("'", "''")
                        lines.append(
                            f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                            f"VALUES ('{term['id']}', 'SN', '{synonym_escaped}');"
                        )

                    # Legacy 'strings' field (backward compatibility)
                    for synonym_str in synonyms.get('strings', []):
                        synonym_escaped = synonym_str.replace("'", "''")
                        lines.append(
                            f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                            f"VALUES ('{term['id']}', 'S', '{synonym_escaped}');"
                        )

                # Handle legacy flat list (backward compatibility)
                elif isinstance(synonyms, list):
                    for synonym in synonyms:
                        synonym_escaped = synonym.replace("'", "''")
                        lines.append(
                            f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                            f"VALUES ('{term['id']}', 'S', '{synonym_escaped}');"
                        )

        if synonym_found:
            lines.append("")

        # 연관 용어 관계 (RELATED_TO)
        related_found = False
        for term in flat_terms:
            if term.get('related_terms'):
                if not related_found:
                    lines.append("-- 연관 용어 (Related Terms)")
                    related_found = True
                for related_id in term['related_terms']:
                    lines.append(
                        f"INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID) "
                        f"VALUES ('{term['id']}', 'T', '{related_id}');"
                    )

        if related_found:
            lines.append("")

    return '\n'.join(lines)

# ==================== mc_std_ref.sql 생성 ====================

def generate_mc_std_ref_sql(data: Dict) -> str:
    """Generate mc_std_ref.sql for standard references"""
    lines = []
    lines.append("-- MC_STD_REF 표준 레퍼런스 테이블 INSERT 문")
    lines.append(f"-- Generated: {data['metadata']['last_updated']}")
    lines.append("")

    # 표준 레지스트리 INSERT
    lines.append("-- 표준 레지스트리 (MC_STANDARD)")
    if 'standards' in data and 'registry' in data['standards']:
        for std in data['standards']['registry']:
            std_desc = std.get('description', '').replace("'", "''")
            lines.append(
                f"INSERT INTO MC_STANDARD (STD_ID, STD_CODE, STD_NAME_KO, STD_NAME_EN, STD_TYPE, STD_SCOPE, ORGANIZATION, VERSION, URI, STD_DESC) "
                f"VALUES ('{std['id']}', '{std['code']}', '{std['name_ko']}', '{std['name_en']}', "
                f"'{std['type']}', '{std['scope']}', '{std['organization']}', '{std['version']}', "
                f"'{std['uri']}', '{std_desc}');"
            )
    lines.append("")

    # 분류별 표준 레퍼런스 INSERT
    lines.append("-- 분류 표준 레퍼런스 (MC_CLSF_STD_REF)")
    for domain in data['domains']:
        flat_clsf = flatten_classifications(domain['classifications'])
        domain_has_refs = False

        for clsf in flat_clsf:
            if clsf.get('standard_refs'):
                if not domain_has_refs:
                    lines.append(f"-- {domain['name_ko']}")
                    domain_has_refs = True

                for ref in clsf['standard_refs']:
                    ext_name = ref.get('external_name', '').replace("'", "''")
                    note = ref.get('note', '').replace("'", "''")
                    confidence = ref.get('confidence', 0.0)
                    lines.append(
                        f"INSERT INTO MC_CLSF_STD_REF (CLSF_ID, STD_ID, EXTERNAL_ID, EXTERNAL_NAME, MATCH_TYPE, CONFIDENCE, NOTE) "
                        f"VALUES ('{clsf['id']}', '{ref['standard_id']}', '{ref.get('external_id', '')}', "
                        f"'{ext_name}', '{ref['match_type']}', {confidence}, '{note}');"
                    )

    lines.append("")

    # 용어별 표준 레퍼런스 INSERT
    lines.append("-- 용어 표준 레퍼런스 (MC_TERM_STD_REF)")
    for domain in data['domains']:
        flat_terms = flatten_terms(domain['terms'])
        domain_has_refs = False

        for term in flat_terms:
            if term.get('standard_refs'):
                if not domain_has_refs:
                    lines.append(f"-- {domain['name_ko']}")
                    domain_has_refs = True

                for ref in term['standard_refs']:
                    ext_name = ref.get('external_name', '').replace("'", "''")
                    note = ref.get('note', '').replace("'", "''")
                    confidence = ref.get('confidence', 0.0)
                    lines.append(
                        f"INSERT INTO MC_TERM_STD_REF (TERM_ID, STD_ID, EXTERNAL_ID, EXTERNAL_NAME, MATCH_TYPE, CONFIDENCE, NOTE) "
                        f"VALUES ('{term['id']}', '{ref['standard_id']}', '{ref.get('external_id', '')}', "
                        f"'{ext_name}', '{ref['match_type']}', {confidence}, '{note}');"
                    )

    lines.append("")
    return '\n'.join(lines)

def generate_standards_json(data: Dict) -> str:
    """Generate standalone standards registry JSON"""
    if 'standards' in data:
        return json.dumps(data['standards'], ensure_ascii=False, indent=2)
    return '{}'

# ==================== ontology.cypher 생성 ====================

def generate_ontology_cypher(data: Dict) -> str:
    """Generate ontology.cypher with all relations"""
    lines = []
    lines.append("// MC 분류·용어 Memgraph Cypher")
    lines.append(f"// Generated: {data['metadata']['last_updated']}")
    lines.append("")

    # Root nodes
    lines.append("// Root Nodes")
    lines.append(f"CREATE (:Classification {{id: '{ROOT_CLSF_ID}', name: 'ROOT', display_name: 'ROOT (:Classification)'}});")
    lines.append(f"CREATE (:Term {{id: '{ROOT_TERM_ID}', name_ko: 'ROOT', name_en: 'ROOT', display_name: 'ROOT (:Term)'}});")
    lines.append("")

    for domain in data['domains']:
        lines.append(f"// {domain['name_ko']} ({domain['name_en']})")
        lines.append("")

        # Classifications
        lines.append("// Classifications")
        flat_clsf = flatten_classifications(domain['classifications'])

        for clsf in flat_clsf:
            display_name = f"{clsf['name']} (:Classification)"
            readme = clsf.get('readme', '').replace("'", "\\'")

            lines.append(
                f"CREATE (:Classification {{id: '{clsf['id']}', name: '{clsf['name']}', "
                f"description: '{clsf['description']}', display_name: '{display_name}', "
                f"readme: '{readme}', group: {str(clsf.get('group', False)).lower()}}});"
            )

        lines.append("")

        # Classification relationships (PARENT_OF)
        lines.append("// Classification Hierarchy")
        for clsf in flat_clsf:
            parent_id = clsf.get('parent_id') or ROOT_CLSF_ID
            lines.append(
                f"MATCH (p:Classification {{id: '{parent_id}'}}), "
                f"(c:Classification {{id: '{clsf['id']}'}}) "
                f"CREATE (p)-[:PARENT_OF]->(c);"
            )

        lines.append("")

        # Terms
        lines.append("// Terms")
        flat_terms = flatten_terms(domain['terms'])

        for term in flat_terms:
            display_name = f"{term['name_ko']} (:Term)"
            acronym = term.get('acronym', '')
            term_desc = term.get('description', '').replace("'", "\\'")

            lines.append(
                f"CREATE (:Term {{id: '{term['id']}', name_ko: '{term['name_ko']}', "
                f"name_en: '{term['name_en']}', acronym: '{acronym}', "
                f"description: '{term_desc}', display_name: '{display_name}'}});"
            )

        lines.append("")

        # Term hierarchy (PARENT_OF)
        lines.append("// Term Hierarchy")
        for term in flat_terms:
            parent_id = term.get('parent_id') or ROOT_TERM_ID
            lines.append(
                f"MATCH (p:Term {{id: '{parent_id}'}}), "
                f"(t:Term {{id: '{term['id']}'}}) "
                f"CREATE (p)-[:PARENT_OF]->(t);"
            )

        lines.append("")

        # Term-Classification relationship (BELONGS_TO)
        lines.append("// Term-Classification Relations")
        for term in flat_terms:
            lines.append(
                f"MATCH (t:Term {{id: '{term['id']}'}}), "
                f"(c:Classification {{id: '{term['linked_clsf_id']}'}}) "
                f"CREATE (t)-[:BELONGS_TO]->(c);"
            )

        lines.append("")

        # Synonyms - Typed relationships (v3.12+)
        lines.append("// Synonym Relations (Typed)")

        # Track processed bidirectional relationships
        processed_pairs = set()

        for term in flat_terms:
            if term.get('synonyms'):
                synonyms = term['synonyms']

                # Handle structured synonyms (v3.12+)
                if isinstance(synonyms, dict):
                    # Term → Term SYNONYM_OF (bidirectional)
                    for synonym_term_id in synonyms.get('terms', []):
                        # Create bidirectional relationship
                        pair = tuple(sorted([term['id'], synonym_term_id]))
                        if pair not in processed_pairs:
                            lines.append(
                                f"MATCH (t1:Term {{id: '{term['id']}'}}), "
                                f"(t2:Term {{id: '{synonym_term_id}'}}) "
                                f"CREATE (t1)-[:SYNONYM_OF]->(t2), (t2)-[:SYNONYM_OF]->(t1);"
                            )
                            processed_pairs.add(pair)

                    # Exact synonyms
                    for synonym_str in synonyms.get('exact', []):
                        synonym_escaped = synonym_str.replace("'", "\\'")
                        display_name = f"{synonym_str} (:Synonym)"
                        lines.append(
                            f"MATCH (t:Term {{id: '{term['id']}'}}) "
                            f"CREATE (t)-[:EXACT_SYNONYM]->(:Synonym {{value: '{synonym_escaped}', display_name: '{display_name}'}});"
                        )

                    # Close synonyms
                    for synonym_str in synonyms.get('close', []):
                        synonym_escaped = synonym_str.replace("'", "\\'")
                        display_name = f"{synonym_str} (:Synonym)"
                        lines.append(
                            f"MATCH (t:Term {{id: '{term['id']}'}}) "
                            f"CREATE (t)-[:CLOSE_SYNONYM]->(:Synonym {{value: '{synonym_escaped}', display_name: '{display_name}'}});"
                        )

                    # Related synonyms
                    for synonym_str in synonyms.get('related', []):
                        synonym_escaped = synonym_str.replace("'", "\\'")
                        display_name = f"{synonym_str} (:Synonym)"
                        lines.append(
                            f"MATCH (t:Term {{id: '{term['id']}'}}) "
                            f"CREATE (t)-[:RELATED_SYNONYM]->(:Synonym {{value: '{synonym_escaped}', display_name: '{display_name}'}});"
                        )

                    # Broader than (상위 개념)
                    for synonym_str in synonyms.get('broader', []):
                        synonym_escaped = synonym_str.replace("'", "\\'")
                        display_name = f"{synonym_str} (:Synonym)"
                        lines.append(
                            f"MATCH (t:Term {{id: '{term['id']}'}}) "
                            f"CREATE (t)-[:BROADER_THAN]->(:Synonym {{value: '{synonym_escaped}', display_name: '{display_name}'}});"
                        )

                    # Narrower than (하위 개념)
                    for synonym_str in synonyms.get('narrower', []):
                        synonym_escaped = synonym_str.replace("'", "\\'")
                        display_name = f"{synonym_str} (:Synonym)"
                        lines.append(
                            f"MATCH (t:Term {{id: '{term['id']}'}}) "
                            f"CREATE (t)-[:NARROWER_THAN]->(:Synonym {{value: '{synonym_escaped}', display_name: '{display_name}'}});"
                        )

                    # Legacy 'strings' field (backward compatibility)
                    for synonym_str in synonyms.get('strings', []):
                        synonym_escaped = synonym_str.replace("'", "\\'")
                        display_name = f"{synonym_str} (:Synonym)"
                        lines.append(
                            f"MATCH (t:Term {{id: '{term['id']}'}}) "
                            f"CREATE (t)-[:SYNONYM_OF]->(:Synonym {{value: '{synonym_escaped}', display_name: '{display_name}'}});"
                        )

                # Handle legacy flat list (backward compatibility)
                elif isinstance(synonyms, list):
                    for synonym in synonyms:
                        synonym_escaped = synonym.replace("'", "\\'")
                        display_name = f"{synonym} (:Synonym)"
                        lines.append(
                            f"MATCH (t:Term {{id: '{term['id']}'}}) "
                            f"CREATE (t)-[:SYNONYM_OF]->(:Synonym {{value: '{synonym_escaped}', display_name: '{display_name}'}});"
                        )

        lines.append("")

        # Similar classifications (SIMILAR_TO)
        lines.append("// Similar Classification Relations")
        for clsf in flat_clsf:
            if clsf.get('similar_to'):
                for similar_id in clsf['similar_to']:
                    lines.append(
                        f"MATCH (c1:Classification {{id: '{clsf['id']}'}}), "
                        f"(c2:Classification {{id: '{similar_id}'}}) "
                        f"CREATE (c1)-[:SIMILAR_TO]->(c2);"
                    )

        lines.append("")

        # Related terms (RELATED_TO)
        lines.append("// Related Term Relations")
        processed_related_pairs = set()

        for term in flat_terms:
            if term.get('related_terms'):
                for related_id in term['related_terms']:
                    # Create bidirectional relationship
                    pair = tuple(sorted([term['id'], related_id]))
                    if pair not in processed_related_pairs:
                        lines.append(
                            f"MATCH (t1:Term {{id: '{term['id']}'}}), "
                            f"(t2:Term {{id: '{related_id}'}}) "
                            f"CREATE (t1)-[:RELATED_TO]->(t2), (t2)-[:RELATED_TO]->(t1);"
                        )
                        processed_related_pairs.add(pair)

        lines.append("")

    return '\n'.join(lines)

# ==================== Main ====================

if __name__ == '__main__':
    import os

    input_file = 'ontology.json'
    output_dir = 'generated'

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print(f"Loading {input_file}...")
    data = load_ontology_json(input_file)

    # Generate ontology.txt
    print("Generating ontology.txt...")
    txt_content = generate_ontology_txt(data)
    with open(f'{output_dir}/ontology.txt', 'w', encoding='utf-8') as f:
        f.write(txt_content)
    print("✓ generated/ontology.txt")

    # Generate mc_clsf.sql
    print("Generating mc_clsf.sql...")
    clsf_sql = generate_mc_clsf_sql(data)
    with open(f'{output_dir}/mc_clsf_generated.sql', 'w', encoding='utf-8') as f:
        f.write(clsf_sql)
    print("✓ generated/mc_clsf_generated.sql")

    # Generate mc_term.sql
    print("Generating mc_term.sql...")
    term_sql = generate_mc_term_sql(data)
    with open(f'{output_dir}/mc_term_generated.sql', 'w', encoding='utf-8') as f:
        f.write(term_sql)
    print("✓ generated/mc_term_generated.sql")

    # Generate mc_term_rel.sql
    print("Generating mc_term_rel.sql...")
    term_rel_sql = generate_mc_term_rel_sql(data)
    with open(f'{output_dir}/mc_term_rel_generated.sql', 'w', encoding='utf-8') as f:
        f.write(term_rel_sql)
    print("✓ generated/mc_term_rel_generated.sql")

    # Generate mc_std_ref.sql
    print("Generating mc_std_ref.sql...")
    std_ref_sql = generate_mc_std_ref_sql(data)
    with open(f'{output_dir}/mc_std_ref_generated.sql', 'w', encoding='utf-8') as f:
        f.write(std_ref_sql)
    print("✓ generated/mc_std_ref_generated.sql")

    # Generate combined SQL file
    print("Generating ontology.sql (combined)...")
    combined_sql = []
    combined_sql.append("-- MC 분류·용어 통합 SQL")
    combined_sql.append(f"-- Generated: {data['metadata']['last_updated']}")
    combined_sql.append("")
    combined_sql.append("-- ==================== MC_CLSF (분류) ====================")
    combined_sql.append("")
    combined_sql.append(clsf_sql)
    combined_sql.append("")
    combined_sql.append("-- ==================== MC_TERM (용어) ====================")
    combined_sql.append("")
    combined_sql.append(term_sql)
    combined_sql.append("")
    combined_sql.append("-- ==================== MC_TERM_REL (용어 관계) ====================")
    combined_sql.append("")
    combined_sql.append(term_rel_sql)
    combined_sql.append("")
    combined_sql.append("-- ==================== MC_STD_REF (표준 레퍼런스) ====================")
    combined_sql.append("")
    combined_sql.append(std_ref_sql)

    with open(f'{output_dir}/ontology.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_sql))
    print("✓ generated/ontology.sql")

    # Generate ontology.cypher
    print("Generating ontology.cypher...")
    cypher = generate_ontology_cypher(data)
    with open(f'{output_dir}/ontology.cypher', 'w', encoding='utf-8') as f:
        f.write(cypher)
    print("✓ generated/ontology.cypher")

    # Generate standalone standards_registry.json
    print("Generating standards_registry.json...")
    std_json = generate_standards_json(data)
    with open(f'{output_dir}/standards_registry.json', 'w', encoding='utf-8') as f:
        f.write(std_json)
    print("✓ generated/standards_registry.json")

    print("\n✓ All files generated successfully in 'generated/' directory!")
