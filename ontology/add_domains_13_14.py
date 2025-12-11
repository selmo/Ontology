#!/usr/bin/env python3
"""
13번 데이터 거버넌스, 14번 학술연구 도메인 추가
v3.14.0: 12개 → 14개 도메인 확장
"""

import json


def load_json(filepath):
    """JSON 파일 로드"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(filepath, data):
    """JSON 파일 저장"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 저장 완료: {filepath}")


def add_domains():
    """13번, 14번 도메인 추가"""

    # Load files
    print("파일 로딩 중...")
    ontology = load_json('ontology.json')
    domain_13 = load_json('domain_13_data_governance_design.json')
    domain_14 = load_json('domain_14_academic_research_design.json')

    # Current stats
    print()
    print(f"현재 도메인 수: {len(ontology['domains'])}개")
    print(f"현재 용어 수: {sum(len(d['terms']) for d in ontology['domains'])}개")
    print()

    # Add domain 13
    print("=" * 80)
    print("13번 데이터 거버넌스 도메인 추가")
    print("=" * 80)

    domain_13_data = {
        "code": domain_13["domain"]["code"],
        "name_ko": domain_13["domain"]["name_ko"],
        "name_en": domain_13["domain"]["name_en"],
        "description": domain_13["domain"]["description"],
        "primary_standards": domain_13["domain"]["primary_standards"],
        "classifications": domain_13["classifications"],
        "terms": domain_13["terms"]
    }

    ontology['domains'].append(domain_13_data)

    print(f"✅ 도메인 13 추가 완료")
    print(f"   - 분류: {len(domain_13['classifications'])}개")
    print(f"   - 용어: {len(domain_13['terms'])}개")
    print(f"   - 표준: {len(domain_13['domain']['primary_standards'])}개")
    print()

    # Add domain 14
    print("=" * 80)
    print("14번 학술연구 도메인 추가")
    print("=" * 80)

    domain_14_data = {
        "code": domain_14["domain"]["code"],
        "name_ko": domain_14["domain"]["name_ko"],
        "name_en": domain_14["domain"]["name_en"],
        "description": domain_14["domain"]["description"],
        "primary_standards": domain_14["domain"]["primary_standards"],
        "classifications": domain_14["classifications"],
        "terms": domain_14["terms"]
    }

    ontology['domains'].append(domain_14_data)

    print(f"✅ 도메인 14 추가 완료")
    print(f"   - 분류: {len(domain_14['classifications'])}개")
    print(f"   - 용어: {len(domain_14['terms'])}개")
    print(f"   - 표준: {len(domain_14['domain']['primary_standards'])}개")
    print()

    # Update metadata
    ontology['metadata']['version'] = '3.14.0'
    ontology['metadata']['last_updated'] = '2025-12-11'
    ontology['metadata']['description'] = (
        "MC 분류·용어 통합 체계 (Option C: 14개 도메인 확장 - 데이터 거버넌스 + 학술연구 신설)"
    )

    # New stats
    print("=" * 80)
    print("통계 업데이트")
    print("=" * 80)

    total_clsf = sum(len(d['classifications']) for d in ontology['domains'])
    total_terms = sum(len(d['terms']) for d in ontology['domains'])

    print(f"도메인: 12개 → 14개 (+2)")
    print(f"분류: 12개 → {total_clsf}개 (+{total_clsf - 12})")
    print(f"용어: 401개 → {total_terms}개 (+{total_terms - 401})")
    print()

    # Save
    save_json('ontology.json', ontology)

    print()
    print("=" * 80)
    print("✅ v3.14.0 도메인 추가 완료")
    print("=" * 80)


if __name__ == '__main__':
    add_domains()
