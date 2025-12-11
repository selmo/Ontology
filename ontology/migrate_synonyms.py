#!/usr/bin/env python3
"""
Migrate ontology.json to structured synonym format
- synonyms.terms: List of Term IDs
- synonyms.strings: List of synonym strings
"""

import json
from datetime import datetime

def migrate_synonyms(input_file='ontology.json', output_file='ontology.json'):
    """Migrate synonyms to structured format"""

    print(f"Loading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Build term name → ID mapping
    term_name_to_id = {}
    for domain in data['domains']:
        for term in domain.get('terms', []):
            term_name_to_id[term['name_ko']] = term['id']

    # Migrate synonyms
    stats = {
        'total_terms': 0,
        'migrated_terms': 0,
        'synonym_to_terms': 0,
        'synonym_to_strings': 0,
        'self_references_removed': 0,
        'invalid_references_removed': 0
    }

    for domain in data['domains']:
        for term in domain.get('terms', []):
            stats['total_terms'] += 1

            old_synonyms = term.get('synonyms', [])

            if not old_synonyms:
                # Remove empty synonyms field
                if 'synonyms' in term:
                    del term['synonyms']
                continue

            # Categorize synonyms
            synonym_terms = []
            synonym_strings = []

            for syn in old_synonyms:
                if syn in term_name_to_id:
                    # This is a Term reference
                    syn_id = term_name_to_id[syn]

                    # Skip self-references
                    if syn_id == term['id']:
                        stats['self_references_removed'] += 1
                        print(f"  ! Self-reference removed: {term['id']} → {syn}")
                        continue

                    synonym_terms.append(syn_id)
                    stats['synonym_to_terms'] += 1
                else:
                    # This is a string
                    synonym_strings.append(syn)
                    stats['synonym_to_strings'] += 1

            # Update term with new structure
            if synonym_terms or synonym_strings:
                term['synonyms'] = {}
                if synonym_terms:
                    term['synonyms']['terms'] = synonym_terms
                if synonym_strings:
                    term['synonyms']['strings'] = synonym_strings
                stats['migrated_terms'] += 1
            else:
                # All synonyms were self-references
                if 'synonyms' in term:
                    del term['synonyms']

    # Update metadata
    data['metadata']['version'] = '3.11.0'
    data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    data['metadata']['description'] = 'MC 분류·용어 통합 체계 (SYNONYM 하이브리드 구조, RELATED_TO 복원 준비)'

    # Save
    print(f"\nSaving to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "=" * 80)
    print("SYNONYM 마이그레이션 완료")
    print("=" * 80)

    print(f"\n전체 통계:")
    print(f"  - 전체 용어: {stats['total_terms']}")
    print(f"  - 마이그레이션된 용어: {stats['migrated_terms']}")

    print(f"\n동의어 분류:")
    print(f"  - Term 참조 (synonyms.terms): {stats['synonym_to_terms']}")
    print(f"  - 문자열 (synonyms.strings): {stats['synonym_to_strings']}")

    print(f"\n제거된 항목:")
    print(f"  - 자기 참조 제거: {stats['self_references_removed']}")

    print(f"\n새로운 구조:")
    print("  {")
    print('    "synonyms": {')
    print('      "terms": ["T01010005"],     // Term ID 참조 → Term → Term')
    print('      "strings": ["공공단체"]      // 문자열 → Term → Synonym node')
    print("    }")
    print("  }")

    return stats


if __name__ == '__main__':
    stats = migrate_synonyms()
    print(f"\n✅ 완료: {stats['synonym_to_terms']}개 Term 참조, {stats['synonym_to_strings']}개 문자열")
