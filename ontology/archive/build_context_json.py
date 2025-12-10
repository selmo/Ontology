#!/usr/bin/env python3
"""
현재 context.txt를 파싱하여 context.json 생성
용어 계층구조와 상세 설명 추가
"""

import json
import re
from typing import List, Dict, Optional
from datetime import datetime

# 상수
ROOT_CLSF_ID = '03facd74b2d24f7cab807b8980391649'
ROOT_TERM_ID = '4147179070a84d3887b97eb57085d850'

# 용어 설명 데이터 (실제 도메인 지식 기반)
TERM_DESCRIPTIONS = {
    # 01. 공공
    'T01010001': '지역 주도의 균형발전을 통해 수도권 집중을 완화하고 지방이 자생력을 갖춘 시대를 지향하는 정책 기조',
    'T01010002': '지방시대 정책을 총괄 조정하는 대통령 소속 위원회',
    'T01010003': '인구감소지역에 대한 국가의 특별한 지원을 규정한 법률',
    'T01010004': '인구감소지역의 지역 소멸 위기 대응을 위한 재정 지원 기금',
    'T01020001': '데이터·AI·클라우드 기반으로 공공서비스를 혁신하는 정부 운영 방식',
    'T01020002': '공공기관이 보유한 개인정보를 본인이 직접 관리·활용할 수 있도록 하는 제도',
    'T01020003': '보이스피싱 범죄를 탐지하고 예방하기 위한 AI 기반 음성 분석 기술',
    'T01030001': '재난·안전 관리 체계를 효율적으로 개선하기 위한 국가 차원의 시스템',
    'T01030002': '국가 차원의 재난 대응 능력을 점검하고 훈련하는 통합 재난안전 훈련',
    'T01040001': '개인이 고향이나 관심 있는 지방자치단체에 기부하면 세액공제와 답례품을 제공하는 제도',
    'T01040002': '지방재정 조정을 위해 국세의 일부를 지방자치단체에 교부하는 재원',
    'T01060001': '중기적 재정운용 방향과 분야별 지출계획을 담은 국가 재정 계획',
    'T01060002': '재정 현황과 동향을 정리한 정기 보고서',
    'T01060003': '정부 부처의 연간 업무 추진 방향과 주요 과제를 담은 계획',
    'T01060004': '국립대학의 경쟁력 강화와 발전을 위한 정부 지원 사업',
    'T01060005': '학교도서관의 진흥과 발전을 위한 중장기 기본 계획',
    'T01060006': '청년농업인의 안정적 영농 정착을 위한 신용보증 지원 제도',
    'T01060007': '특정 국가의 정치·경제·사회·문화 전반을 소개하는 공식 보고서',
    'T01060008': '항공훈련기관의 안전한 운영을 위한 정부의 감독 및 관리 체계',

    # 02. 금융
    'T02010001': '중앙은행이 금융기관과 거래할 때 적용하는 정책금리',
    'T02010002': '중앙은행이 금융기관에 유동성을 지원하여 금융중개 기능을 활성화하는 대출제도',
    'T02010003': '중앙은행이 유가증권을 매매하여 시중 통화량을 조절하는 정책 수단',
    'T02010004': '물가가 목표 범위로 돌아와 안정화되는 시기',
    'T02010005': '식료품·에너지 등 변동성이 큰 품목을 제외한 물가지수',
    'T02010006': '공개시장운영에 참여할 수 있는 금융기관의 범위를 확대하는 정책',
    'T02010007': '중앙은행이 시중 유동성을 흡수하기 위해 발행하는 단기 증권',
    'T02010008': '중앙은행이 금융기관으로부터 증권을 매입하고 일정 기간 후 되파는 거래',
    'T02020001': '부동산 개발사업에 필요한 자금을 금융기관이 대출해주는 금융 상품',
    'T02020002': '금융시스템의 안정성 유지와 시스템 리스크 관리',
    'T02030001': '대기업과 중소기업, 금융기관과 서민이 함께 성장하는 금융 생태계',
    'T02030002': '금융 소외계층도 적절한 금융서비스를 이용할 수 있도록 하는 정책',
    'T02030003': '소상공인의 금리 부담을 경감하기 위한 3가지 정책 패키지',
    'T02030004': '고금리 대출을 저금리 대출로 갈아타는 프로그램',
    'T02040001': '금융(Finance)과 기술(Technology)의 결합으로 혁신적인 금융서비스를 제공하는 산업',
    'T02040002': '핀테크 기업의 성장을 지원하기 위한 정부 및 민간의 투자 펀드',
    'T02040003': '핀테크 혁신펀드 1호',
    'T02040004': '핀테크 혁신펀드 2호',
    'T02040005': '핀테크 산업의 투자 생태계를 활성화하기 위한 정책',
    'T02050004': '증권시장 투자자를 대상으로 시장 전망을 공유하는 행사',
    'T02050005': '하반기 증권시장 전망을 다루는 세션',
    'T02050001': '근로자가 퇴직 후 생활안정을 위해 적립하는 연금',
    'T02050002': '퇴직연금을 여러 사용자가 공동으로 적립·운용하는 기금 형태',
    'T02050003': '고령화 사회에서 금융자산을 효율적으로 운용하는 방법',
    'T02060001': '한국과 호주 간 퇴직연금 제도를 논의하는 포럼',
    'T02060002': '호주의 의무적 퇴직연금 제도',
    'T02060003': '호주 산업 슈퍼펀드의 대표 거버넌스 모델',
    'T02070001': '지방은행이 영업 범위를 전국으로 확대하여 시중은행으로 전환하는 것',
    'T02070002': '은행 인가 내용을 변경하는 방식',
    'T02070003': '은행 설립 전 사전에 인가를 받는 제도',
    'T02070004': '은행업 인가 신청 시 세부 심사 요건',
    'T02070005': '외부 전문가로 구성된 평가위원회의 심사 절차',
    'T02070006': '인가 심사를 중단할 수 있는 사유를 관리하는 제도',
    'T02080001': '환경 보호와 지속가능성을 목표로 하는 금융 활동',
    'T02080002': '기후변화 관련 재무정보 공개를 권고하는 국제 기준',
    'T02080003': '한국형 녹색 경제활동 분류 체계',
    'T02080004': '녹색금융 실무 안내서',

    # 03. 커머스
    'T03010001': '인터넷을 통한 상품 및 서비스의 거래',
    'T03010002': '다수의 판매자와 구매자가 모여 거래하는 온라인 플랫폼',
    'T03010003': '제조사가 유통 중간 단계를 거치지 않고 소비자에게 직접 판매하는 방식',
    'T03010004': '정기적으로 상품이나 서비스를 제공받고 비용을 지불하는 경제 모델',
    'T03020001': '실시간 동영상 스트리밍을 통해 상품을 판매하는 커머스',
    'T03020002': '라이브커머스 서비스를 제공하는 플랫폼',
    'T03020003': '기업 간(B2B) 디지털 커머스 거래',
    'T03030001': '중고 물품을 거래하는 온라인 플랫폼',
    'T03030002': '상품을 최종 목적지까지 배송하는 마지막 단계',
    'T03030003': '콘텐츠(Content), 커머스(Commerce), 커뮤니티(Community)가 통합된 소비 트렌드',
    'T03030004': '농식품을 라이브커머스로 판매하는 방식',
    'T03040001': '커머스 운영을 위한 클라우드 기반 소프트웨어 서비스',
    'T03040002': '마케팅 업무를 자동화하는 소프트웨어',
    'T03040003': '고객 리뷰를 관리하는 솔루션',
    'T03040004': '가격과 혜택을 중시하는 소비자',
    'T03040005': '소비자가 얻는 경제적·심리적 만족도',
    'T03060001': '이커머스 운영에 필요한 기술 솔루션',
    'T03060002': '주문부터 배송까지 물류 전 과정을 처리하는 서비스',

    # 04. 산업
    'T04010001': '디지털 기술을 기반으로 한 경제 활동',
    'T04010002': '과학적 발견이나 공학적 혁신을 기반으로 한 첨단 기술',
    'T04020001': '스타트업이 성장할 수 있는 창업·투자·지원 생태계',
    'T04020002': '벤처캐피탈에 투자하는 정부 출자 펀드',
    'T04030001': '새로운 형태의 럭셔리 소비 트렌드',

    # 05. 사회
    'T05010001': '고령 인구 비율에 따른 사회 단계 구분 (7%, 14%, 20% 기준)',
    'T05010002': '65-74세 전기고령자와 75세 이상 후기고령자의 구분',
    'T05010003': '고령자가 고령자를 돌보는 돌봄 형태',
    'T05010004': '사회적으로 인지되지 않는 가족 형태나 관계',
    'T05010005': '연령·장애 등에 관계없이 모든 사람이 이용 가능한 디자인 정책',
    'T05020001': '국가가 운영하는 공적 연금 제도',
    'T05020002': '연금 소득에 의존하여 생활하는 삶의 방식',
    'T05030001': '고령자 가구의 소득원과 지출 항목 구조',

    # 06. 법률
    'T06010001': '법원의 재판 선례',
    'T06010002': '대법원의 판결',
    'T06010003': '헌법재판소의 결정',
    'T06020001': '개인의 소득에 부과하는 세금',
    'T06020002': '법인의 소득에 부과하는 세금',
    'T06020003': '재화와 용역의 공급에 부과하는 세금',
    'T06020004': '상속 또는 증여받은 재산에 부과하는 세금',
    'T06020005': '세금 제도를 개편하는 정책',
    'T06020006': '비거주자의 가상자산 소득에 대한 과세',
    'T06020007': '가상자산 거래소가 거래자의 소득세를 원천징수하는 의무',
    'T06030001': '국가공무원의 복무·권리·의무 등을 규정한 법률',
    'T06030002': '행정절차의 공정성·투명성·신뢰성 확보를 위한 법률',

    # 07. 의료
    'T07010001': '악성 종양으로, 비정상적인 세포의 무제한적 성장과 전이를 특징으로 하는 질환',
    'T07010002': '대장(결장 및 직장)에 발생하는 악성 종양',
    'T07010003': '골수의 형질세포에서 발생하는 혈액암',
    'T07010004': '암세포를 죽이거나 성장을 억제하는 약물 치료',
    'T07010005': '암을 조기에 발견하기 위한 검진',
    'T07010006': '암을 치료하기 위한 의학적 처치',
    'T07010007': '암 환자가 진료 과정을 원활히 받을 수 있도록 안내하고 지원하는 체계',
    'T07020001': '눈물이 부족하거나 과도하게 증발하여 안구 표면이 손상되는 질환',
    'T07020002': '수정체가 혼탁해져 시력이 저하되는 질환',
    'T07020003': '시신경이 손상되어 시야가 좁아지는 질환',
    'T07020004': '망막 중심부(황반)가 손상되어 시력이 저하되는 질환',
    'T07020005': '안과 질환을 예방하기 위한 활동',
    'T07030001': '위산이 식도로 역류하여 불편감이나 합병증을 유발하는 질환',
    'T07030002': '내부 장기를 관찰하기 위해 내시경을 삽입하는 검사',
    'T07030003': '위암을 조기에 발견하기 위한 검진',
    'T07040001': '질병의 조기 발견과 예방을 위한 정기 검진',
    'T07040002': '질병을 예방하고 건강을 증진하는 의학 분야',
}

# 용어 계층구조 정의 (parent_term_id 매핑)
TERM_HIERARCHY = {
    # 의료: 암 계층
    'T07010002': 'T07010001',  # 대장암 → 암
    'T07010003': 'T07010001',  # 다발성골수종 → 암

    # 의료: 안과 질환은 동등 레벨 (계층 없음)

    # 금융: 공개시장운영 계층
    'T02010007': 'T02010003',  # 통화안정증권 발행 → 공개시장운영
    'T02010008': 'T02010003',  # 환매조건부증권 매입 → 공개시장운영

    # 금융: 핀테크 혁신펀드 계층
    'T02040003': 'T02040002',  # 핀테크 혁신펀드 1호 → 핀테크 혁신펀드
    'T02040004': 'T02040002',  # 핀테크 혁신펀드 2호 → 핀테크 혁신펀드

    # 커머스: 이커머스 하위
    'T03010003': 'T03010001',  # D2C → 이커머스
    'T03020001': 'T03010001',  # 라이브커머스 → 이커머스
    'T03010004': 'T03010001',  # 구독경제 → 이커머스
}

def parse_context_txt(filepath: str):
    """context.txt 파싱"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        "metadata": {
            "version": "1.0.0",
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "description": "MC 분류·용어 통합 체계"
        },
        "id_schema": {
            "classification": "C + DD(도메인) + LL(중분류) + SSSS(일련번호)",
            "term": "T + DD(도메인) + LL(중분류) + SSSS(일련번호)"
        },
        "constants": {
            "root_clsf_id": ROOT_CLSF_ID,
            "root_term_id": ROOT_TERM_ID
        },
        "domains": []
    }

    sections = re.split(r'^---$', content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        domain_match = re.search(r'^## (\d+)\. (.+?) \| (.+?)$', section, re.MULTILINE)
        if not domain_match:
            continue

        domain = {
            "code": domain_match.group(1),
            "name_ko": domain_match.group(2),
            "name_en": domain_match.group(3),
            "description": f"{domain_match.group(2)} 부문 정책 및 제도 전반",
            "classifications": [],
            "terms": []
        }

        # 분류 파싱
        clsf_section = re.search(r'### \[분류 체계\](.*?)### \[핵심 용어\]', section, re.DOTALL)
        if clsf_section:
            parse_classifications(clsf_section.group(1), domain)

        # 용어 파싱
        term_section = re.search(r'### \[핵심 용어\](.*?)$', section, re.DOTALL)
        if term_section:
            parse_terms(term_section.group(1), domain)

        data["domains"].append(domain)

    return data

def parse_classifications(text: str, domain: Dict):
    """분류 파싱 및 계층 구조 생성"""
    lines = text.strip().split('\n')
    parent_stack = []
    flat_list = []

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue

        match = re.search(r'([C]\d{8})\s+(.+)$', line)
        if not match:
            continue

        clsf_id = match.group(1)
        clsf_name = match.group(2).strip()

        tree_symbols = line.split(clsf_id)[0]
        indent = len(tree_symbols) - len(tree_symbols.lstrip(' '))
        pipe_count = tree_symbols.count('│')

        if line.strip().startswith('-'):
            level = 0
            parent_id = None
        elif pipe_count > 0:
            level = pipe_count + 1
            while parent_stack and parent_stack[-1]['level'] >= level:
                parent_stack.pop()
            parent_id = parent_stack[-1]['id'] if parent_stack else None
        else:
            level = indent // 2
            while parent_stack and parent_stack[-1]['level'] >= level:
                parent_stack.pop()
            parent_id = parent_stack[-1]['id'] if parent_stack else None

        id_suffix = clsf_id[-4:]
        mid_code = clsf_id[3:7]
        group = mid_code == '0000' or id_suffix == '0001'

        clsf_obj = {
            "id": clsf_id,
            "name": clsf_name,
            "description": generate_clsf_desc(clsf_name, level),
            "readme": generate_clsf_readme(clsf_name, level, domain['code']),
            "group": group,
            "level": level,
            "parent_id": parent_id,
            "children": []
        }

        flat_list.append(clsf_obj)
        parent_stack.append(clsf_obj)

    # 계층 구조 생성
    domain['classifications'] = build_hierarchy(flat_list)

def parse_terms(text: str, domain: Dict):
    """용어 파싱 및 계층 구조 생성"""
    lines = text.strip().split('\n')
    flat_list = []

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue

        term_match = re.match(r'^-\s+([T]\d{8})\s+([^|]+)\|\s+([^\[]+)(?:\[([^\]]+)\])?', line)
        if not term_match:
            continue

        term_id = term_match.group(1)
        term_name_ko = term_match.group(2).strip()
        term_name_en = term_match.group(3).strip()
        acronym = term_match.group(4).strip() if term_match.group(4) else None

        linked_clsf_id = 'C' + term_id[1:5] + '0001'
        parent_id = TERM_HIERARCHY.get(term_id, None)
        description = TERM_DESCRIPTIONS.get(term_id, f"{term_name_ko} ({term_name_en})")

        term_obj = {
            "id": term_id,
            "name_ko": term_name_ko,
            "name_en": term_name_en,
            "acronym": acronym,
            "description": description,
            "linked_clsf_id": linked_clsf_id,
            "parent_id": parent_id,
            "children": []
        }

        flat_list.append(term_obj)

    # 계층 구조 생성
    domain['terms'] = build_hierarchy(flat_list)

def build_hierarchy(flat_list: List[Dict]) -> List[Dict]:
    """평면 리스트를 계층 구조로 변환"""
    id_map = {item['id']: item for item in flat_list}
    root_items = []

    for item in flat_list:
        parent_id = item.get('parent_id')
        if parent_id and parent_id in id_map:
            id_map[parent_id]['children'].append(item)
        else:
            root_items.append(item)

    return root_items

def generate_clsf_desc(name: str, level: int) -> str:
    """분류 설명 생성"""
    if level == 0:
        return f"{name} 부문 정책 및 제도 전반을 다루는 최상위 분류"
    elif level == 1:
        return f"{name}을(를) 다루는 분류"
    else:
        return f"{name} 관련 분류"

def generate_clsf_readme(name: str, level: int, domain_code: str) -> str:
    """분류 README 생성"""
    if level == 0:
        return f"도메인 {domain_code}. {name} 부문 전반을 포괄."
    elif level == 1:
        return f"중분류. {name} 관련 정책 및 제도 포함."
    else:
        return f"소분류. {name} 관련."

def count_items(items: List[Dict]) -> int:
    """재귀적으로 아이템 개수 세기"""
    count = len(items)
    for item in items:
        count += count_items(item.get('children', []))
    return count

if __name__ == '__main__':
    input_file = 'context.txt'
    output_file = 'context.json'

    print(f"Parsing {input_file}...")
    data = parse_context_txt(input_file)

    print(f"Writing {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 통계 출력
    total_clsf = sum(count_items(d['classifications']) for d in data['domains'])
    total_terms = sum(count_items(d['terms']) for d in data['domains'])

    print(f"\n✓ Generated {output_file}")
    print(f"  - {len(data['domains'])} domains")
    print(f"  - {total_clsf} classifications")
    print(f"  - {total_terms} terms")
