#!/usr/bin/env python3
"""
기존 ID를 새로운 data.go.kr 기반 ID로 매핑
"""

# 도메인 코드 매핑
DOMAIN_MAPPING = {
    '01': '01',  # 공공 → 공공행정
    '02': '06',  # 금융 → 재정금융
    '03': '07',  # 커머스 → 산업경제
    '04': '07',  # 산업 → 산업경제
    '05': '04',  # 사회 → 사회복지
    '06': '05',  # 법률 → 법률
    '07': '03',  # 의료 → 보건의료
}

# 분류 ID 매핑 함수
def map_classification_id(old_id: str) -> str:
    """
    분류 ID를 새 체계로 매핑
    예: C02010001 → C06010001 (금융 → 재정금융)
    """
    if len(old_id) != 9 or old_id[0] != 'C':
        return old_id

    old_domain = old_id[1:3]
    rest = old_id[3:]

    new_domain = DOMAIN_MAPPING.get(old_domain, old_domain)
    return f"C{new_domain}{rest}"

# 용어 ID 매핑 함수
def map_term_id(old_id: str) -> str:
    """
    용어 ID를 새 체계로 매핑
    예: T02010001 → T06010001 (금융 → 재정금융)
    """
    if len(old_id) != 9 or old_id[0] != 'T':
        return old_id

    old_domain = old_id[1:3]
    rest = old_id[3:]

    new_domain = DOMAIN_MAPPING.get(old_domain, old_domain)
    return f"T{new_domain}{rest}"

# 중분류 코드 재매핑 (산업경제 통합)
# 커머스(03) + 산업(04) → 산업경제(07)
INDUSTRY_CATEGORY_MAPPING = {
    # 커머스 (03xx) → 산업경제 (07xx)
    '01': '01',  # 이커머스 시장·플랫폼
    '02': '02',  # 온라인 유통모델·D2C
    '03': '03',  # 라이브커머스·콘텐츠커머스
    '04': '04',  # 소비자 행동·패턴
    '05': '05',  # 이커머스 물류
    '06': '06',  # 이커머스 솔루션

    # 산업 (04xx) → 산업경제 (07xx)
    # 기존 산업 중분류를 07번대로 이동
}

# 실제 매핑 예시
if __name__ == '__main__':
    print("=== 분류 ID 매핑 예시 ===")
    test_clsf = [
        'C01000001',  # 공공 → 공공행정 (유지)
        'C02010001',  # 금융 → 재정금융
        'C03010001',  # 커머스 → 산업경제
        'C04010001',  # 산업 → 산업경제
        'C05010001',  # 사회 → 사회복지
        'C06010001',  # 법률 → 법률
        'C07010001',  # 의료 → 보건의료
    ]

    for old in test_clsf:
        new = map_classification_id(old)
        print(f"{old} → {new}")

    print("\n=== 용어 ID 매핑 예시 ===")
    test_term = [
        'T01010001',  # 공공
        'T02010001',  # 금융
        'T03010001',  # 커머스
        'T07010001',  # 의료
    ]

    for old in test_term:
        new = map_term_id(old)
        print(f"{old} → {new}")
