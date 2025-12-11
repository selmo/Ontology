#!/usr/bin/env python3
"""
Analyze synonyms in ontology.json to identify which ones are actual Terms
"""

import json
from collections import defaultdict

def analyze_synonyms(json_file='ontology.json'):
    """Analyze synonym strings and check if they match existing terms"""

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Build term name → ID mapping
    term_name_to_id = {}
    all_terms = []

    for domain in data['domains']:
        for term in domain.get('terms', []):
            term_name_to_id[term['name_ko']] = term['id']
            all_terms.append(term)

    # Analyze synonyms
    synonym_analysis = {
        'term_references': [],      # Synonyms that are Terms
        'string_only': [],          # Synonyms that are just strings
        'statistics': {
            'total_terms': len(all_terms),
            'terms_with_synonyms': 0,
            'total_synonym_entries': 0,
            'synonym_as_term': 0,
            'synonym_as_string': 0
        }
    }

    for domain in data['domains']:
        for term in domain.get('terms', []):
            synonyms = term.get('synonyms', [])

            if not synonyms:
                continue

            synonym_analysis['statistics']['terms_with_synonyms'] += 1
            synonym_analysis['statistics']['total_synonym_entries'] += len(synonyms)

            for syn in synonyms:
                if syn in term_name_to_id:
                    # This synonym is actually another Term
                    synonym_analysis['term_references'].append({
                        'term_id': term['id'],
                        'term_name': term['name_ko'],
                        'synonym_name': syn,
                        'synonym_term_id': term_name_to_id[syn],
                        'domain': domain['code']
                    })
                    synonym_analysis['statistics']['synonym_as_term'] += 1
                else:
                    # This synonym is just a string
                    synonym_analysis['string_only'].append({
                        'term_id': term['id'],
                        'term_name': term['name_ko'],
                        'synonym_name': syn,
                        'domain': domain['code']
                    })
                    synonym_analysis['statistics']['synonym_as_string'] += 1

    return synonym_analysis


def print_report(analysis):
    """Print analysis report"""

    stats = analysis['statistics']

    print("=" * 80)
    print("SYNONYM 분석 보고서")
    print("=" * 80)

    print(f"\n## 통계")
    print(f"전체 용어 수: {stats['total_terms']}")
    print(f"동의어 보유 용어: {stats['terms_with_synonyms']}")
    print(f"전체 동의어 항목: {stats['total_synonym_entries']}")
    print(f"\n동의어 분류:")
    print(f"  - Term 참조: {stats['synonym_as_term']}")
    print(f"  - 문자열만: {stats['synonym_as_string']}")

    # Term references
    if analysis['term_references']:
        print(f"\n## 1. TERM 참조 동의어 ({len(analysis['term_references'])}개)")
        print("-" * 80)
        print(f"{'Term ID':<12} {'Term Name':<20} {'→':<3} {'Synonym':<20} {'Synonym ID':<12}")
        print("-" * 80)

        for ref in analysis['term_references']:
            print(f"{ref['term_id']:<12} {ref['term_name']:<20} {'→':<3} "
                  f"{ref['synonym_name']:<20} {ref['synonym_term_id']:<12}")

    # String-only samples
    print(f"\n## 2. 문자열 전용 동의어 (샘플 20개)")
    print("-" * 80)
    print(f"{'Term ID':<12} {'Term Name':<30} {'Synonym':<30}")
    print("-" * 80)

    for item in analysis['string_only'][:20]:
        print(f"{item['term_id']:<12} {item['term_name']:<30} {item['synonym_name']:<30}")

    if len(analysis['string_only']) > 20:
        print(f"\n... 외 {len(analysis['string_only']) - 20}개")

    # Recommendations
    print("\n" + "=" * 80)
    print("권장 사항")
    print("=" * 80)

    if stats['synonym_as_term'] > 0:
        print(f"\n✓ {stats['synonym_as_term']}개 동의어를 Term → Term 관계로 변경")
        print("  - synonyms.terms 필드로 이동")
        print("  - 양방향 SYNONYM_OF 관계 생성")

    if stats['synonym_as_string'] > 0:
        print(f"\n✓ {stats['synonym_as_string']}개 동의어를 문자열로 유지")
        print("  - synonyms.strings 필드로 이동")
        print("  - Term → Synonym 노드 관계 유지")


def export_mapping(analysis, output_file='synonym_mapping.json'):
    """Export mapping for migration script"""

    mapping = {
        'term_to_term': {},
        'term_to_string': {}
    }

    # Build term_to_term mapping
    for ref in analysis['term_references']:
        term_id = ref['term_id']
        if term_id not in mapping['term_to_term']:
            mapping['term_to_term'][term_id] = []
        mapping['term_to_term'][term_id].append(ref['synonym_term_id'])

    # Build term_to_string mapping
    for item in analysis['string_only']:
        term_id = item['term_id']
        if term_id not in mapping['term_to_string']:
            mapping['term_to_string'][term_id] = []
        mapping['term_to_string'][term_id].append(item['synonym_name'])

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 매핑 데이터 저장: {output_file}")


if __name__ == '__main__':
    analysis = analyze_synonyms()
    print_report(analysis)
    export_mapping(analysis)
