#!/usr/bin/env python3
"""
Suggest Close Match candidates from Related synonyms
Based on semantic similarity and common usage patterns
"""

import json
from difflib import SequenceMatcher

def similarity_ratio(a, b):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, a, b).ratio()

def suggest_close_matches(filepath='ontology.json'):
    """Suggest close match candidates"""

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    suggestions = []

    # Patterns for close matches
    close_patterns = [
        # 준말과 정식 명칭
        ('지자체', '지방자치단체'),
        ('지방정부', '지방자치단체'),

        # 혼용되는 용어
        ('공기업', '공공기관'),
        ('병원', '의료기관'),

        # 유사 개념
        ('행정조직', '정부조직'),
        ('공공단체', '공공기관'),
        ('공공조직', '공공기관'),
    ]

    for domain in data['domains']:
        for term in domain.get('terms', []):
            synonyms = term.get('synonyms', {})

            if not isinstance(synonyms, dict):
                continue

            related = synonyms.get('related', [])

            if not related:
                continue

            term_name = term['name_ko']

            # Check against patterns
            for rel_syn in related:
                # Pattern matching
                for pat1, pat2 in close_patterns:
                    if (term_name == pat1 and rel_syn == pat2) or \
                       (term_name == pat2 and rel_syn == pat1):
                        suggestions.append({
                            'term_id': term['id'],
                            'term': term_name,
                            'synonym': rel_syn,
                            'reason': '패턴 매칭: 혼용 용어',
                            'confidence': 0.9
                        })
                        continue

                # String similarity (high threshold)
                sim = similarity_ratio(term_name, rel_syn)
                if sim > 0.7:  # Very similar
                    suggestions.append({
                        'term_id': term['id'],
                        'term': term_name,
                        'synonym': rel_syn,
                        'reason': f'문자열 유사도: {sim:.2f}',
                        'confidence': sim
                    })

                # Common substring (준말 패턴)
                if len(rel_syn) >= 2 and rel_syn in term_name and len(term_name) - len(rel_syn) <= 3:
                    suggestions.append({
                        'term_id': term['id'],
                        'term': term_name,
                        'synonym': rel_syn,
                        'reason': '준말 패턴',
                        'confidence': 0.85
                    })

    # Remove duplicates
    seen = set()
    unique_suggestions = []
    for sug in suggestions:
        key = (sug['term_id'], sug['synonym'])
        if key not in seen:
            seen.add(key)
            unique_suggestions.append(sug)

    # Sort by confidence
    unique_suggestions.sort(key=lambda x: x['confidence'], reverse=True)

    return unique_suggestions

def print_suggestions(suggestions):
    """Print suggestions"""

    print("=" * 80)
    print("Close Match 후보 추천")
    print("=" * 80)

    print(f"\n총 {len(suggestions)}개 후보")

    if not suggestions:
        print("\n자동 추천 없음. 수동 검토 필요.")
        return

    print("\n추천 목록:")
    print("-" * 80)
    print(f"{'Term ID':<12} {'Term':30s} {'→':3s} {'Synonym':30s} {'Confidence':>10s} {'Reason':30s}")
    print("-" * 80)

    for sug in suggestions[:50]:  # Top 50
        print(f"{sug['term_id']:<12} {sug['term']:30s} {'→':3s} {sug['synonym']:30s} {sug['confidence']:>10.2f} {sug['reason']:30s}")

    if len(suggestions) > 50:
        print(f"\n... 외 {len(suggestions) - 50}개")

    print("\n" + "=" * 80)
    print("검토 방법")
    print("=" * 80)
    print("""
1. 위 목록을 검토하여 실제로 Close Match인지 확인
2. ontology.json에서 해당 용어 찾기
3. related → close로 이동

예시:
  "synonyms": {
    "related": ["공기업", "공공단체"],  // Before
    "close": ["공기업"],              // After (이동)
    "related": ["공공단체"]            // After (유지)
  }

추천 기준:
- Confidence 0.9+: 강력 추천
- Confidence 0.8-0.9: 검토 추천
- Confidence 0.7-0.8: 참고
""")

def export_suggestions(suggestions, output_file='close_match_suggestions.json'):
    """Export suggestions"""

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(suggestions, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 추천 결과 저장: {output_file}")

if __name__ == '__main__':
    suggestions = suggest_close_matches()
    print_suggestions(suggestions)
    export_suggestions(suggestions)
