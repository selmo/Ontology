#!/usr/bin/env python3
"""
Migrate ontology.json to v3.12 with categorized synonyms
Based on synonym_categories.json analysis results
"""

import json
from datetime import datetime
from collections import defaultdict

def load_categories(filepath='synonym_categories.json'):
    """Load categorized synonyms"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_synonym_lookup(categories):
    """Build lookup: (term_id, synonym) -> category"""
    lookup = {}

    for category, items in categories.items():
        for item in items:
            key = (item['term_id'], item['synonym'])
            lookup[key] = category

    return lookup

def migrate_synonyms_v312(data, lookup):
    """Migrate synonyms to v3.12 structure"""

    stats = {
        'total_terms': 0,
        'migrated_terms': 0,
        'exact': 0,
        'close': 0,
        'related': 0,
        'broader': 0,
        'narrower': 0,
        'term_to_term': 0
    }

    for domain in data['domains']:
        for term in domain.get('terms', []):
            stats['total_terms'] += 1

            old_synonyms = term.get('synonyms', {})

            if not old_synonyms:
                continue

            # Initialize new structure
            new_synonyms = {
                'terms': [],
                'exact': [],
                'close': [],
                'related': [],
                'broader': [],
                'narrower': []
            }

            # Handle structured synonyms (v3.11)
            if isinstance(old_synonyms, dict):
                # Preserve term-to-term synonyms
                term_refs = old_synonyms.get('terms', [])
                if term_refs:
                    new_synonyms['terms'] = term_refs
                    stats['term_to_term'] += len(term_refs)

                # Categorize string synonyms
                string_syns = old_synonyms.get('strings', [])
                for syn in string_syns:
                    category = lookup.get((term['id'], syn), 'related')
                    # Map 'derived' to 'related'
                    if category == 'derived':
                        category = 'related'
                    new_synonyms[category].append(syn)
                    stats[category] += 1

            # Handle legacy flat list
            elif isinstance(old_synonyms, list):
                for syn in old_synonyms:
                    category = lookup.get((term['id'], syn), 'related')
                    # Map 'derived' to 'related'
                    if category == 'derived':
                        category = 'related'
                    new_synonyms[category].append(syn)
                    stats[category] += 1

            # Update term
            term['synonyms'] = new_synonyms
            stats['migrated_terms'] += 1

    return stats

def main():
    print("Loading files...")

    # Load categorization results
    categories = load_categories()
    lookup = build_synonym_lookup(categories)

    print(f"Loaded {len(lookup)} categorized synonyms")

    # Load ontology
    with open('ontology.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("Migrating synonyms to v3.12 structure...")
    stats = migrate_synonyms_v312(data, lookup)

    # Update metadata
    data['metadata']['version'] = '3.12.0'
    data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    data['metadata']['description'] = 'MC 분류·용어 통합 체계 (SYNONYM 타입 세분화: SKOS 기반)'

    # Save
    print("Saving ontology.json...")
    with open('ontology.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "=" * 80)
    print("v3.12 마이그레이션 완료")
    print("=" * 80)

    print(f"\n전체 통계:")
    print(f"  - 전체 용어: {stats['total_terms']}")
    print(f"  - 마이그레이션된 용어: {stats['migrated_terms']}")

    print(f"\n동의어 유형별 분포:")
    print(f"  - Term → Term: {stats['term_to_term']}개")
    print(f"  - Exact (완전 동의어): {stats['exact']}개")
    print(f"  - Close (유사어): {stats['close']}개")
    print(f"  - Related (관련어): {stats['related']}개")
    print(f"  - Broader (상위 개념): {stats['broader']}개")
    print(f"  - Narrower (하위 개념): {stats['narrower']}개")

    total = stats['exact'] + stats['close'] + stats['related'] + stats['broader'] + stats['narrower']
    print(f"\n총 문자열 동의어: {total}개")

    print(f"\n새로운 스키마:")
    print("""  {
    "synonyms": {
      "terms": [...],      // Term → Term
      "exact": [...],      // 완전 동의어
      "close": [...],      // 유사어 (수동 검토 필요)
      "related": [...],    // 관련어
      "broader": [...],    // 상위 개념
      "narrower": [...]    // 하위 개념
    }
  }""")

    print(f"\n⚠️  다음 단계: Close Match 수동 검토")
    print(f"   - Related {stats['related']}개 중 일부를 Close로 재분류")
    print(f"   - 예상: 30~50개")

    print(f"\n✅ 완료: ontology.json → v3.12")

if __name__ == '__main__':
    main()
