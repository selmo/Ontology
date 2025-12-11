#!/usr/bin/env python3
"""
Analyze synonym types to identify different relationship patterns
- Exact synonyms (완전 동의어)
- Close matches (유사어)
- Derived terms (파생어)
- Broader/Narrower terms (상하위 개념)
"""

import json
from collections import defaultdict

def analyze_synonym_types(filepath='ontology.json'):
    """Analyze and categorize synonym relationships"""

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Categories based on patterns
    categories = {
        'exact': [],      # 완전 동의어 (약어, 영문명 등)
        'close': [],      # 유사어 (비슷한 개념)
        'derived': [],    # 파생어 (접미사/접두사 추가)
        'broader': [],    # 상위 개념
        'narrower': [],   # 하위 개념
        'related': []     # 관련어
    }

    examples = {
        'exact': [],
        'close': [],
        'derived': [],
        'broader': [],
        'narrower': [],
        'related': []
    }

    for domain in data['domains']:
        for term in domain.get('terms', []):
            term_name = term['name_ko']
            synonyms_data = term.get('synonyms', {})

            if not synonyms_data:
                continue

            # Handle structured synonyms
            if isinstance(synonyms_data, dict):
                syn_strings = synonyms_data.get('strings', [])
            elif isinstance(synonyms_data, list):
                syn_strings = synonyms_data
            else:
                continue

            for syn in syn_strings:
                # Categorize based on patterns
                category = categorize_synonym(term_name, syn, term.get('acronym'))

                categories[category].append({
                    'term_id': term['id'],
                    'term': term_name,
                    'synonym': syn,
                    'domain': domain['name_ko']
                })

                # Collect examples (max 5 per category)
                if len(examples[category]) < 5:
                    examples[category].append({
                        'term': term_name,
                        'synonym': syn,
                        'reason': get_categorization_reason(term_name, syn, term.get('acronym'), category)
                    })

    return categories, examples


def categorize_synonym(term, synonym, acronym=None):
    """Categorize synonym relationship based on patterns"""

    term_lower = term.lower()
    syn_lower = synonym.lower()

    # 1. Exact match patterns
    # - Acronyms
    if acronym and synonym == acronym:
        return 'exact'

    # - English equivalents (all caps or mixed case English words)
    if synonym.isupper() or (synonym.isascii() and any(c.isupper() for c in synonym)):
        return 'exact'

    # - Simple character substitution
    if term_lower.replace(' ', '') == syn_lower.replace(' ', ''):
        return 'exact'

    # 2. Derived patterns
    # - Adding suffixes/prefixes
    suffixes = ['시설', '기관', '제도', '정책', '사업', '서비스', '통계', '정보', '현황', '관리']
    prefixes = ['국가', '공공', '정부', '지역', '전국']

    for suffix in suffixes:
        if (term.endswith(suffix) and synonym == term.replace(suffix, '')) or \
           (synonym.endswith(suffix) and term == synonym.replace(suffix, '')):
            return 'derived'

    for prefix in prefixes:
        if (term.startswith(prefix) and synonym == term.replace(prefix, '')) or \
           (synonym.startswith(prefix) and term == synonym.replace(prefix, '')):
            return 'derived'

    # 3. Broader/Narrower patterns
    # - Synonym is shorter and contained in term
    if len(synonym) < len(term) and synonym in term:
        return 'broader'

    # - Term is shorter and contained in synonym
    if len(term) < len(synonym) and term in synonym:
        return 'narrower'

    # 4. Close match patterns
    # - Similar structure or wording
    term_words = set(term_lower.split())
    syn_words = set(syn_lower.split())

    if term_words & syn_words:  # Has common words
        overlap_ratio = len(term_words & syn_words) / max(len(term_words), len(syn_words))
        if overlap_ratio > 0.5:
            return 'close'

    # 5. Default to related
    return 'related'


def get_categorization_reason(term, synonym, acronym, category):
    """Get human-readable reason for categorization"""

    if category == 'exact':
        if acronym and synonym == acronym:
            return '약어'
        if synonym.isupper() or (synonym.isascii() and any(c.isupper() for c in synonym)):
            return '영문명'
        return '완전 동일'

    elif category == 'derived':
        if any(term.endswith(s) and synonym == term.replace(s, '') for s in ['시설', '기관', '제도']):
            return '접미사 제거'
        if any(synonym.endswith(s) and term == synonym.replace(s, '') for s in ['시설', '기관', '제도']):
            return '접미사 추가'
        return '파생어'

    elif category == 'broader':
        return '상위 개념 (더 일반적)'

    elif category == 'narrower':
        return '하위 개념 (더 구체적)'

    elif category == 'close':
        return '유사어 (공통 단어 포함)'

    else:
        return '관련어'


def print_report(categories, examples):
    """Print analysis report"""

    print("=" * 80)
    print("동의어 관계 유형 분석")
    print("=" * 80)

    total = sum(len(items) for items in categories.values())

    print(f"\n전체 동의어: {total}개")
    print("\n유형별 분포:")
    print("-" * 80)

    for cat_name, cat_label in [
        ('exact', '완전 동의어'),
        ('close', '유사어'),
        ('derived', '파생어'),
        ('broader', '상위 개념'),
        ('narrower', '하위 개념'),
        ('related', '관련어')
    ]:
        count = len(categories[cat_name])
        pct = (count / total * 100) if total > 0 else 0
        print(f"  {cat_label:12s}: {count:3d}개 ({pct:5.1f}%)")

    print("\n" + "=" * 80)
    print("유형별 예시")
    print("=" * 80)

    for cat_name, cat_label in [
        ('exact', '완전 동의어'),
        ('close', '유사어'),
        ('derived', '파생어'),
        ('broader', '상위 개념'),
        ('narrower', '하위 개념'),
        ('related', '관련어')
    ]:
        print(f"\n## {cat_label} ({len(categories[cat_name])}개)")
        print("-" * 80)

        if examples[cat_name]:
            for ex in examples[cat_name]:
                print(f"  {ex['term']:30s} → {ex['synonym']:30s} [{ex['reason']}]")
        else:
            print("  (해당 없음)")

    print("\n" + "=" * 80)
    print("권장 사항")
    print("=" * 80)

    print("""
1. SKOS 기반 매치 타입 도입:
   - exactMatch: 완전 동의어 (약어, 영문명 포함)
   - closeMatch: 유사어 (의미가 매우 유사)
   - relatedMatch: 관련어 (관련성만 있음)
   - broadMatch: 상위 개념
   - narrowMatch: 하위 개념

2. ontology.json 스키마 변경:
   {
     "synonyms": {
       "exact": ["약어", "영문명"],
       "close": ["유사한용어"],
       "related": ["관련용어"],
       "broader": ["상위개념"],
       "narrower": ["하위개념"]
     }
   }

3. Cypher 관계 타입:
   - :EXACT_SYNONYM
   - :CLOSE_SYNONYM
   - :BROADER_THAN / :NARROWER_THAN
   - :RELATED (기존 RELATED_TO와 통합 가능)

4. SQL REL_TYPE 확장:
   - 'SE': Exact Synonym
   - 'SC': Close Synonym
   - 'SR': Related
   - 'SB': Broader
   - 'SN': Narrower
""")


def export_categorized(categories, output_file='synonym_categories.json'):
    """Export categorized synonyms"""

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(categories, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 분류 결과 저장: {output_file}")


if __name__ == '__main__':
    print("Analyzing synonym types...")
    categories, examples = analyze_synonym_types()
    print_report(categories, examples)
    export_categorized(categories)
