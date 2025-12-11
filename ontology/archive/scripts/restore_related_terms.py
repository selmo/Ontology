#!/usr/bin/env python3
"""
Restore RELATED_TO relationships from v3.9 backup
Apply according to user's policy:
- Keep RELATED_TO when it's the only relationship
- Remove RELATED_TO when PARENT_OF or SYNONYM_OF already exists
"""

import json
from datetime import datetime

def restore_related_terms(
    current_file='ontology.json',
    backup_file='backup_20251211/ontology_v3.9.json',
    output_file='ontology.json'
):
    """Restore and filter RELATED_TO relationships"""

    print(f"Loading current file: {current_file}...")
    with open(current_file, 'r', encoding='utf-8') as f:
        current_data = json.load(f)

    print(f"Loading v3.9 backup: {backup_file}...")
    with open(backup_file, 'r', encoding='utf-8') as f:
        backup_data = json.load(f)

    # Build term lookup for current data
    current_terms = {}
    for domain in current_data['domains']:
        for term in domain.get('terms', []):
            current_terms[term['id']] = term

    # Extract related_terms from backup
    backup_related = {}
    for domain in backup_data['domains']:
        for term in domain.get('terms', []):
            if 'related_terms' in term and term['related_terms']:
                backup_related[term['id']] = term['related_terms']

    print(f"\nFound {len(backup_related)} terms with related_terms in v3.9")

    # Restore with filtering
    stats = {
        'total_restored': 0,
        'total_relationships': 0,
        'filtered_parent_of': 0,
        'filtered_synonym_of': 0,
        'kept_relationships': 0
    }

    for term_id, related_list in backup_related.items():
        if term_id not in current_terms:
            print(f"  ! Term {term_id} not found in current data")
            continue

        current_term = current_terms[term_id]
        filtered_related = []

        for related_id in related_list:
            stats['total_relationships'] += 1

            # Check PARENT_OF relationship
            if current_term.get('parent_id') == related_id:
                stats['filtered_parent_of'] += 1
                print(f"  - Filtered (PARENT_OF): {term_id} → {related_id}")
                continue

            # Check SYNONYM_OF relationship (Term → Term)
            if 'synonyms' in current_term:
                synonym_terms = current_term['synonyms'].get('terms', [])
                if related_id in synonym_terms:
                    stats['filtered_synonym_of'] += 1
                    print(f"  - Filtered (SYNONYM_OF): {term_id} → {related_id}")
                    continue

            # Keep this RELATED_TO relationship
            filtered_related.append(related_id)
            stats['kept_relationships'] += 1

        # Update current term
        if filtered_related:
            current_term['related_terms'] = filtered_related
            stats['total_restored'] += 1

    # Update metadata
    current_data['metadata']['version'] = '3.11.0'
    current_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    current_data['metadata']['description'] = 'MC 분류·용어 통합 체계 (SYNONYM 하이브리드, RELATED_TO 조건부 복원)'

    # Save
    print(f"\nSaving to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(current_data, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "=" * 80)
    print("RELATED_TO 복원 완료")
    print("=" * 80)

    print(f"\n복원 통계:")
    print(f"  - v3.9 관계 총계: {stats['total_relationships']}")
    print(f"  - 필터링 (PARENT_OF): {stats['filtered_parent_of']}")
    print(f"  - 필터링 (SYNONYM_OF): {stats['filtered_synonym_of']}")
    print(f"  - 유지된 관계: {stats['kept_relationships']}")
    print(f"  - RELATED_TO 보유 용어: {stats['total_restored']}")

    print(f"\n필터링 정책:")
    print("  ✓ PARENT_OF 존재 → RELATED_TO 제거")
    print("  ✓ SYNONYM_OF 존재 → RELATED_TO 제거")
    print("  ✓ 다른 관계 없음 → RELATED_TO 유지")

    return stats


if __name__ == '__main__':
    stats = restore_related_terms()
    print(f"\n✅ 완료: {stats['kept_relationships']}개 RELATED_TO 관계 복원")
