#!/usr/bin/env python3
"""
도메인-표준 매핑 분석 및 도메인 세분화 검토

현재 12개 도메인과 24개 표준의 매핑 관계를 분석하고,
표준 기반 도메인 추가/세분화 필요성을 검토합니다.
"""

import json
from collections import defaultdict
from typing import Dict, List, Set


def load_data():
    """데이터 로드"""
    with open('ontology.json', 'r', encoding='utf-8') as f:
        ontology = json.load(f)

    with open('generated/standards_registry.json', 'r', encoding='utf-8') as f:
        standards = json.load(f)

    return ontology, standards


def analyze_domain_standard_mapping(ontology, standards):
    """도메인별 표준 매핑 분석"""

    print("=" * 80)
    print("도메인-표준 매핑 분석")
    print("=" * 80)
    print()

    # 도메인별 표준 수집
    domain_standards = {}
    domain_stats = {}

    for domain in ontology['domains']:
        code = domain['code']
        name = domain['name_ko']

        # Primary standards
        primary_stds = set(domain.get('primary_standards', []))

        # 분류에서 참조된 표준
        clsf_stds = set()
        for clsf in domain.get('classifications', []):
            for ref in clsf.get('standard_refs', []):
                clsf_stds.add(ref['standard_id'])

        # 용어에서 참조된 표준
        term_stds = set()
        for term in domain.get('terms', []):
            for ref in term.get('standard_refs', []):
                term_stds.add(ref['standard_id'])

        # 전체 표준 (primary + 실제 사용)
        all_stds = primary_stds | clsf_stds | term_stds

        domain_standards[code] = {
            'name': name,
            'primary': primary_stds,
            'classification': clsf_stds,
            'term': term_stds,
            'all': all_stds
        }

        # 통계
        num_clsf = len(domain.get('classifications', []))
        num_terms = len(domain.get('terms', []))
        clsf_with_std = sum(1 for c in domain.get('classifications', [])
                           if c.get('standard_refs'))
        terms_with_std = sum(1 for t in domain.get('terms', [])
                            if t.get('standard_refs'))

        domain_stats[code] = {
            'name': name,
            'num_clsf': num_clsf,
            'num_terms': num_terms,
            'clsf_with_std': clsf_with_std,
            'terms_with_std': terms_with_std,
            'clsf_coverage': clsf_with_std / num_clsf * 100 if num_clsf > 0 else 0,
            'term_coverage': terms_with_std / num_terms * 100 if num_terms > 0 else 0,
            'num_standards': len(all_stds)
        }

    # 도메인별 출력
    print(f"{'도메인':<20} {'분류':<8} {'용어':<8} {'표준 수':<8} {'분류 커버리지':<12} {'용어 커버리지':<12}")
    print("-" * 80)

    for code in sorted(domain_stats.keys()):
        stats = domain_stats[code]
        print(f"{stats['name']:<20} "
              f"{stats['num_clsf']:<8} "
              f"{stats['num_terms']:<8} "
              f"{stats['num_standards']:<8} "
              f"{stats['clsf_coverage']:.1f}%{'':<7} "
              f"{stats['term_coverage']:.1f}%")

    print()
    print(f"평균 분류 커버리지: {sum(s['clsf_coverage'] for s in domain_stats.values()) / len(domain_stats):.1f}%")
    print(f"평균 용어 커버리지: {sum(s['term_coverage'] for s in domain_stats.values()) / len(domain_stats):.1f}%")
    print()

    return domain_standards, domain_stats


def analyze_standard_usage(ontology, standards, domain_standards):
    """표준별 사용 현황 분석"""

    print("=" * 80)
    print("표준별 사용 현황 분석")
    print("=" * 80)
    print()

    # 표준별 도메인 매핑
    standard_domains = defaultdict(set)

    for code, data in domain_standards.items():
        for std_id in data['all']:
            standard_domains[std_id].add(code)

    # 표준 정보 조회
    std_registry = {std['id']: std for std in standards['registry']}

    # 유형별 그룹핑
    by_type = defaultdict(list)
    by_scope = defaultdict(list)

    for std in standards['registry']:
        std_id = std['id']
        std_type = std['type']
        std_scope = std['scope']

        domains = standard_domains.get(std_id, set())
        num_domains = len(domains)

        by_type[std_type].append((std_id, std['name_ko'], num_domains, domains))
        by_scope[std_scope].append((std_id, std['name_ko'], num_domains, domains))

    # 유형별 출력
    print("### 표준 유형별 분류")
    print()

    for std_type in ['INTERNATIONAL', 'NATIONAL', 'APPLICATION']:
        print(f"**{std_type}** ({len(by_type[std_type])}개)")
        print()

        for std_id, name, num_domains, domains in sorted(by_type[std_type],
                                                          key=lambda x: x[2],
                                                          reverse=True):
            domain_names = ', '.join(domain_standards[d]['name'] for d in sorted(domains))
            status = "✅" if num_domains > 0 else "❌"
            print(f"{status} {name} ({num_domains}개 도메인): {domain_names if domain_names else '미사용'}")

        print()

    # Scope별 출력
    print("### 표준 범위별 분류")
    print()

    for scope in ['ONTOLOGY', 'CLASSIFICATION', 'TERMINOLOGY', 'METADATA']:
        if scope in by_scope:
            print(f"**{scope}** ({len(by_scope[scope])}개)")
            print()

            for std_id, name, num_domains, domains in sorted(by_scope[scope],
                                                              key=lambda x: x[2],
                                                              reverse=True):
                domain_names = ', '.join(domain_standards[d]['name'] for d in sorted(domains))
                status = "✅" if num_domains > 0 else "❌"
                print(f"{status} {name} ({num_domains}개 도메인): {domain_names if domain_names else '미사용'}")

            print()

    # 미사용 표준
    unused_standards = []
    for std in standards['registry']:
        if std['id'] not in standard_domains:
            unused_standards.append(std)

    if unused_standards:
        print("=" * 80)
        print(f"⚠️  미사용 표준 ({len(unused_standards)}개)")
        print("=" * 80)
        print()

        for std in unused_standards:
            print(f"- {std['name_ko']} ({std['code']})")
            print(f"  유형: {std['type']}, 범위: {std['scope']}")
            print(f"  설명: {std['description']}")
            print()

    return standard_domains, unused_standards


def identify_domain_gaps(ontology, standards, domain_standards, standard_domains):
    """도메인 갭 분석 및 세분화 제안"""

    print("=" * 80)
    print("도메인 갭 분석 및 세분화 제안")
    print("=" * 80)
    print()

    # 표준 분석
    std_registry = {std['id']: std for std in standards['registry']}

    # 1. 표준 기반 도메인 커버리지 분석
    print("### 1. 표준 기반 도메인 커버리지")
    print()

    # 미사용 표준으로 가능한 도메인 파악
    potential_domains = []

    for std in standards['registry']:
        std_id = std['id']
        if std_id not in standard_domains:
            # 표준의 scope와 description으로 도메인 제안
            name = std['name_ko']
            scope = std['scope']
            desc = std['description']

            # 키워드 기반 도메인 추론
            if 'GS1' in std['code'] or 'eCommerce' in std['name_en']:
                potential_domains.append({
                    'standard': std,
                    'suggested_domain': '디지털커머스',
                    'reason': 'GS1 전자상거래 표준'
                })
            elif 'Schema.org' in std['name_ko']:
                potential_domains.append({
                    'standard': std,
                    'suggested_domain': '디지털커머스/과학기술',
                    'reason': '웹 구조화 데이터 (Product, Offer 등)'
                })
            elif 'arXiv' in std['code'] or 'ACM' in std['code']:
                potential_domains.append({
                    'standard': std,
                    'suggested_domain': '과학기술',
                    'reason': '과학 논문/컴퓨터과학 분류'
                })

    if potential_domains:
        for item in potential_domains:
            std = item['standard']
            print(f"- {std['name_ko']} → **{item['suggested_domain']}**")
            print(f"  이유: {item['reason']}")
            print()
    else:
        print("- 모든 주요 표준이 도메인에 매핑되어 있습니다.")
        print()

    # 2. 도메인 세분화 제안
    print("### 2. 도메인 세분화 제안")
    print()

    # 표준이 많은 도메인 (2개 이상)
    large_domains = []
    for code, data in domain_standards.items():
        if len(data['all']) >= 3:
            large_domains.append((code, data['name'], len(data['all']), data['all']))

    large_domains.sort(key=lambda x: x[2], reverse=True)

    print("#### 표준이 많은 도메인 (세분화 고려)")
    print()

    for code, name, num_stds, stds in large_domains:
        print(f"**{name}** ({num_stds}개 표준)")
        std_names = [std_registry[s]['name_ko'] for s in stds if s in std_registry]
        for std_name in std_names:
            print(f"  - {std_name}")
        print()

    # 3. 새 도메인 제안
    print("### 3. 새 도메인 제안")
    print()

    # 현재 도메인 구조 분석
    existing_domains = {d['code']: d['name_ko'] for d in ontology['domains']}

    # 제안 1: 데이터 거버넌스 (메타데이터 표준 통합)
    metadata_standards = [s for s in standards['registry'] if s['scope'] == 'METADATA']
    if len(metadata_standards) >= 2:
        print("#### 제안 1: 데이터 거버넌스 (Data Governance)")
        print()
        print("**근거:** 메타데이터 관련 표준 4개 존재")
        for std in metadata_standards:
            print(f"  - {std['name_ko']}: {std['description']}")
        print()
        print("**포함 내용:**")
        print("  - 메타데이터 관리")
        print("  - 데이터 품질 관리")
        print("  - 데이터베이스 표준화")
        print("  - 공공데이터 개방")
        print()

    # 제안 2: 학술연구 (arXiv, ACM CCS 등)
    research_standards = [s for s in standards['registry']
                         if 'arXiv' in s['code'] or 'ACM' in s['code'] or 'OECD-FOS' in s['code']]
    if research_standards:
        print("#### 제안 2: 학술연구 세분화")
        print()
        print("**현재:** 과학기술 도메인에 통합")
        print("**제안:** 학술연구 분야별 세분화 또는 독립 도메인")
        for std in research_standards:
            print(f"  - {std['name_ko']}: {std['description']}")
        print()

    return potential_domains


def generate_recommendations(domain_stats, unused_standards, potential_domains):
    """종합 권장사항 생성"""

    print("=" * 80)
    print("종합 권장사항")
    print("=" * 80)
    print()

    # 우선순위 1: 커버리지가 낮은 도메인 보강
    low_coverage = [(code, stats) for code, stats in domain_stats.items()
                    if stats['term_coverage'] < 50]

    if low_coverage:
        print("### 우선순위 1: 표준 레퍼런스 보강이 필요한 도메인")
        print()
        low_coverage.sort(key=lambda x: x[1]['term_coverage'])

        for code, stats in low_coverage[:5]:
            print(f"**{stats['name']}** (용어 커버리지: {stats['term_coverage']:.1f}%)")
            print(f"  - 현재: {stats['terms_with_std']}/{stats['num_terms']}개 용어에 표준 매핑")
            print(f"  - 목표: 50% 이상 ({int(stats['num_terms'] * 0.5)}개 이상)")
            print()

    # 우선순위 2: 미사용 표준 활용
    if unused_standards:
        print("### 우선순위 2: 미사용 표준 활용")
        print()
        for std in unused_standards[:3]:
            print(f"**{std['name_ko']}**")
            print(f"  - 범위: {std['scope']}")
            print(f"  - 활용 방안: 관련 도메인에 매핑 또는 새 도메인 생성")
            print()

    # 우선순위 3: 도메인 세분화
    print("### 우선순위 3: 도메인 세분화 또는 추가")
    print()
    print("**Option A: 데이터 거버넌스 도메인 신설** (권장)")
    print("  - 13번 도메인으로 추가")
    print("  - 메타데이터 표준 4개 통합")
    print("  - 공공행정 도메인의 정보화 분류 이관")
    print()

    print("**Option B: 현재 구조 유지 + 표준 매핑 강화** (보수적)")
    print("  - 미사용 표준을 기존 도메인에 매핑")
    print("  - 디지털커머스에 GS1, Schema.org 추가")
    print("  - 과학기술에 arXiv, ACM CCS 추가")
    print()

    print("**Option C: 대규모 재구조화** (적극적)")
    print("  - 데이터 거버넌스 도메인 신설")
    print("  - 학술연구 도메인 신설")
    print("  - 디지털경제 도메인 세분화 (커머스/핀테크)")
    print()


def main():
    """메인 실행"""
    print()
    print("=" * 80)
    print("도메인-표준 매핑 분석 및 도메인 세분화 검토")
    print("=" * 80)
    print()

    # 데이터 로드
    ontology, standards = load_data()

    print(f"현재 도메인 수: {len(ontology['domains'])}개")
    print(f"등록된 표준 수: {standards['count']}개")
    print()

    # 분석 수행
    domain_standards, domain_stats = analyze_domain_standard_mapping(ontology, standards)
    standard_domains, unused_standards = analyze_standard_usage(ontology, standards, domain_standards)
    potential_domains = identify_domain_gaps(ontology, standards, domain_standards, standard_domains)
    generate_recommendations(domain_stats, unused_standards, potential_domains)

    print()
    print("=" * 80)
    print("분석 완료")
    print("=" * 80)
    print()


if __name__ == '__main__':
    main()
