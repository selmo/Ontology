# -*- coding: utf-8 -*-
"""
표준 레지스트리 (Standards Registry)
- 20개 표준 정의 (국제 8개, 국내 6개, 한국형 응용 6개)
- 분류/용어와 표준 간 매핑 정보
"""

# 표준 유형
STANDARD_TYPES = {
    'INTERNATIONAL': '국제 표준',
    'NATIONAL': '국내 표준',
    'APPLICATION': '한국형 응용 표준',
}

# 표준 범위
STANDARD_SCOPES = {
    'ONTOLOGY': '온톨로지/시소러스 표준',
    'CLASSIFICATION': '분류체계 표준',
    'TERMINOLOGY': '용어체계 표준',
    'METADATA': '메타데이터 표준',
}

# 매핑 유형 (SKOS 기반)
MATCH_TYPES = {
    'EXACT_MATCH': '정확히 일치 (skos:exactMatch)',
    'CLOSE_MATCH': '근접 일치 (skos:closeMatch)',
    'BROAD_MATCH': '상위 개념 (skos:broadMatch)',
    'NARROW_MATCH': '하위 개념 (skos:narrowMatch)',
    'RELATED_MATCH': '연관 개념 (skos:relatedMatch)',
    'DERIVED_FROM': '파생됨 (계보 추적용)',
}

# =============================================================================
# 표준 레지스트리 (20개)
# =============================================================================
STANDARDS_REGISTRY = {
    # -------------------------------------------------------------------------
    # 국제 표준 (8개)
    # -------------------------------------------------------------------------
    'STD-SKOS': {
        'code': 'W3C-SKOS',
        'name_ko': 'SKOS',
        'name_en': 'Simple Knowledge Organization System',
        'type': 'INTERNATIONAL',
        'scope': 'ONTOLOGY',
        'organization': 'W3C',
        'version': '2009-08-18',
        'uri': 'https://www.w3.org/2004/02/skos/',
        'description': 'RDF 기반 지식조직체계 표준. 시소러스, 분류체계, 택소노미 표현.',
        'domains': ['ALL'],
    },
    'STD-ISO25964': {
        'code': 'ISO-25964',
        'name_ko': 'ISO 25964',
        'name_en': 'ISO 25964 Thesauri and Interoperability',
        'type': 'INTERNATIONAL',
        'scope': 'ONTOLOGY',
        'organization': 'ISO',
        'version': '2011/2013',
        'uri': 'https://www.iso.org/standard/53657.html',
        'description': '시소러스 개발(Part 1) 및 상호운용성(Part 2) 국제 표준.',
        'domains': ['ALL'],
    },
    'STD-DC': {
        'code': 'ISO-15836',
        'name_ko': '더블린 코어',
        'name_en': 'Dublin Core',
        'type': 'INTERNATIONAL',
        'scope': 'METADATA',
        'organization': 'DCMI',
        'version': '1.1',
        'uri': 'https://www.dublincore.org/',
        'description': '15개 핵심 메타데이터 요소 표준. Title, Creator, Subject 등.',
        'domains': ['ALL'],
    },
    'STD-UNESCO': {
        'code': 'UNESCO-THESAURUS',
        'name_ko': 'UNESCO 시소러스',
        'name_en': 'UNESCO Thesaurus',
        'type': 'INTERNATIONAL',
        'scope': 'TERMINOLOGY',
        'organization': 'UNESCO',
        'version': '2023',
        'uri': 'http://vocabularies.unesco.org/thesaurus',
        'description': '7개 도메인, SKOS/ISO 25964 준수, 5개 언어 지원.',
        'domains': ['02', '09'],  # 교육, 문화관광
    },
    'STD-OECD-FOS': {
        'code': 'OECD-FOS',
        'name_ko': 'OECD 학문분류',
        'name_en': 'OECD Fields of Science Classification',
        'type': 'INTERNATIONAL',
        'scope': 'CLASSIFICATION',
        'organization': 'OECD',
        'version': '2015',
        'uri': 'https://www.oecd.org/science/inno/38235147.pdf',
        'description': '6개 대분류, 42개 소분류. R&D 조사 국제표준.',
        'domains': ['11'],  # 과학기술
    },
    'STD-FIBO': {
        'code': 'FIBO',
        'name_ko': 'FIBO',
        'name_en': 'Financial Industry Business Ontology',
        'type': 'INTERNATIONAL',
        'scope': 'TERMINOLOGY',
        'organization': 'EDM Council / OMG',
        'version': '2025Q3',
        'uri': 'https://spec.edmcouncil.org/fibo/',
        'description': 'OWL 기반 금융 온톨로지. 10개 도메인, 2,457개 클래스.',
        'domains': ['06'],  # 재정금융
    },
    'STD-MESH': {
        'code': 'NLM-MESH',
        'name_ko': 'MeSH',
        'name_en': 'Medical Subject Headings',
        'type': 'INTERNATIONAL',
        'scope': 'TERMINOLOGY',
        'organization': 'NLM (NIH)',
        'version': '2025',
        'uri': 'https://www.nlm.nih.gov/mesh/',
        'description': '약 30,000개 의학 주제어. MEDLINE/PubMed 색인 표준.',
        'domains': ['03'],  # 보건의료
    },
    'STD-ICD11': {
        'code': 'WHO-ICD11',
        'name_ko': 'ICD-11',
        'name_en': 'International Classification of Diseases 11th Revision',
        'type': 'INTERNATIONAL',
        'scope': 'CLASSIFICATION',
        'organization': 'WHO',
        'version': '2022',
        'uri': 'https://icd.who.int/browse11',
        'description': '국제질병분류 11차 개정. 디지털 최적화, URL 기반 코드.',
        'domains': ['03'],  # 보건의료
    },

    # -------------------------------------------------------------------------
    # 국내 표준 (6개)
    # -------------------------------------------------------------------------
    'STD-BRM': {
        'code': 'MOIS-BRM',
        'name_ko': '정부기능분류체계',
        'name_en': 'Business Reference Model',
        'type': 'NATIONAL',
        'scope': 'CLASSIFICATION',
        'organization': '행정안전부',
        'version': '2024',
        'uri': 'https://www.archives.go.kr/',
        'description': '6단계 정부기능분류. 17개 정책분야, 76개 정책영역.',
        'domains': ['01'],  # 공공행정
    },
    'STD-KSIC': {
        'code': 'KOSTAT-KSIC',
        'name_ko': '한국표준산업분류',
        'name_en': 'Korean Standard Industrial Classification',
        'type': 'NATIONAL',
        'scope': 'CLASSIFICATION',
        'organization': '통계청',
        'version': '11차 (2024)',
        'uri': 'https://kssc.kostat.go.kr/',
        'description': '5단계 산업분류. 대분류(알파벳)~세세분류(5자리).',
        'domains': ['07', '08'],  # 산업경제, 디지털커머스
    },
    'STD-KCD': {
        'code': 'KOSTAT-KCD',
        'name_ko': '한국표준질병사인분류',
        'name_en': 'Korean Standard Classification of Diseases',
        'type': 'NATIONAL',
        'scope': 'CLASSIFICATION',
        'organization': '통계청',
        'version': '8차 (2021)',
        'uri': 'https://www.koicd.kr/',
        'description': 'ICD-11 기반 한국형 질병분류. 22장 구조.',
        'domains': ['03'],  # 보건의료
    },
    'STD-MOLEG': {
        'code': 'MOLEG',
        'name_ko': '국가법령정보',
        'name_en': 'National Law Information',
        'type': 'NATIONAL',
        'scope': 'CLASSIFICATION',
        'organization': '법제처',
        'version': '2024',
        'uri': 'https://www.law.go.kr/',
        'description': '법령 계층구조. 헌법→법률→시행령→조례.',
        'domains': ['05'],  # 법률
    },
    'STD-DATAGOkr': {
        'code': 'DATA-GO-KR',
        'name_ko': '공공데이터포털 분류',
        'name_en': 'Data.go.kr Classification',
        'type': 'NATIONAL',
        'scope': 'CLASSIFICATION',
        'organization': '행정안전부',
        'version': '2024',
        'uri': 'https://www.data.go.kr/',
        'description': '16개 분야 카테고리. 공공데이터 분류체계.',
        'domains': ['ALL'],
    },
    'STD-STDTERM': {
        'code': 'MOIS-STDTERM',
        'name_ko': '공공데이터 공통표준용어',
        'name_en': 'Public Data Standard Terms',
        'type': 'NATIONAL',
        'scope': 'TERMINOLOGY',
        'organization': '행정안전부',
        'version': '7차 (2024.11)',
        'uri': 'https://www.data.go.kr/information/PDS_0000000000000464/recsroom.do',
        'description': '9,027개 표준용어, 2,396개 표준단어.',
        'domains': ['ALL'],
    },

    # -------------------------------------------------------------------------
    # 한국형 응용 표준 (6개)
    # -------------------------------------------------------------------------
    'STD-DCAT-AP-KR': {
        'code': 'DCAT-AP-KR',
        'name_ko': 'DCAT-AP-KR',
        'name_en': 'DCAT Application Profile for Korea',
        'type': 'APPLICATION',
        'scope': 'METADATA',
        'organization': 'NIA',
        'version': '1.0 (2023)',
        'uri': 'http://vocab.datahub.kr/spec/dcat-ap-kr/',
        'description': '한국 공공데이터 메타데이터 표준. DCAT-AP 2.1 기반.',
        'domains': ['ALL'],
    },
    'STD-KOOR': {
        'code': 'KOOR',
        'name_ko': '한국 기관 온톨로지',
        'name_en': 'Korean Organization Ontology',
        'type': 'APPLICATION',
        'scope': 'TERMINOLOGY',
        'organization': 'NIA',
        'version': '1.0',
        'uri': 'http://vocab.datahub.kr/def/organization/',
        'description': '공공기관 표현 온톨로지. DCAT-AP-KR 연계.',
        'domains': ['01'],  # 공공행정
    },
    'STD-ADMCODE': {
        'code': 'ADMCODE',
        'name_ko': '행정표준코드',
        'name_en': 'Administrative Standard Code',
        'type': 'APPLICATION',
        'scope': 'CLASSIFICATION',
        'organization': '행정안전부',
        'version': '2024',
        'uri': 'https://code.go.kr/',
        'description': '법정동/행정동 코드. 10자리 체계.',
        'domains': ['01'],  # 공공행정
    },
    'STD-KS-ISO11179': {
        'code': 'KS-X-ISO11179',
        'name_ko': '메타데이터 레지스트리',
        'name_en': 'Metadata Registry Standard',
        'type': 'APPLICATION',
        'scope': 'METADATA',
        'organization': '국가기술표준원',
        'version': '2021',
        'uri': 'https://standard.go.kr/',
        'description': 'KS X ISO/IEC 11179 시리즈. 메타데이터 레지스트리 표준.',
        'domains': ['ALL'],
    },
    'STD-DBSTD': {
        'code': 'MOIS-DBSTD',
        'name_ko': 'DB 표준화 지침',
        'name_en': 'Database Standardization Guidelines',
        'type': 'APPLICATION',
        'scope': 'METADATA',
        'organization': '행정안전부',
        'version': '2023-18호',
        'uri': 'https://www.mois.go.kr/',
        'description': '공공기관 데이터베이스 표준화 지침. 38개 메타데이터 관리항목.',
        'domains': ['ALL'],
    },
    'STD-DATAQUALITY': {
        'code': 'MOIS-DQ',
        'name_ko': '데이터 품질관리',
        'name_en': 'Data Quality Management',
        'type': 'APPLICATION',
        'scope': 'METADATA',
        'organization': '행정안전부',
        'version': '2024',
        'uri': 'https://www.data.go.kr/',
        'description': '공공데이터 품질관리 수준평가. 공공데이터법 제22조.',
        'domains': ['ALL'],
    },
}

# =============================================================================
# 도메인별 주요 표준 매핑
# =============================================================================
DOMAIN_PRIMARY_STANDARDS = {
    '01': ['STD-BRM', 'STD-ADMCODE', 'STD-KOOR'],           # 공공행정
    '02': ['STD-UNESCO'],                                    # 교육
    '03': ['STD-KCD', 'STD-MESH', 'STD-ICD11'],             # 보건의료
    '04': [],                                                # 사회복지
    '05': ['STD-MOLEG'],                                     # 법률
    '06': ['STD-FIBO'],                                      # 재정금융
    '07': ['STD-KSIC'],                                      # 산업경제
    '08': ['STD-KSIC'],                                      # 디지털커머스
    '09': ['STD-UNESCO'],                                    # 문화관광
    '10': [],                                                # 환경기상
    '11': ['STD-OECD-FOS'],                                  # 과학기술
    '12': ['STD-DATAGOkr'],                                  # 재난안전
}

# =============================================================================
# 분류 표준 레퍼런스 매핑 (주요 분류에 대한 표준 연결)
# =============================================================================
CLASSIFICATION_STANDARD_REFS = {
    # 01 공공행정 - BRM 기반
    'C01000001': [
        {'standard_id': 'STD-BRM', 'external_id': '일반공공행정', 'match_type': 'BROAD_MATCH', 'confidence': 0.9},
        {'standard_id': 'STD-DATAGOkr', 'external_id': '공공행정', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C01010001': [
        {'standard_id': 'STD-BRM', 'external_id': '정부자원관리', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],
    'C01020001': [
        {'standard_id': 'STD-BRM', 'external_id': '지방행정·재정지원', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
        {'standard_id': 'STD-ADMCODE', 'external_id': '행정동코드', 'match_type': 'RELATED_MATCH', 'confidence': 0.7},
    ],
    'C01030001': [
        {'standard_id': 'STD-BRM', 'external_id': '정보화', 'match_type': 'CLOSE_MATCH', 'confidence': 0.8},
    ],
    'C01040001': [
        {'standard_id': 'STD-BRM', 'external_id': '국정운영', 'match_type': 'CLOSE_MATCH', 'confidence': 0.8},
    ],
    'C01050001': [
        {'standard_id': 'STD-BRM', 'external_id': '민원·행정서비스', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],
    'C01060001': [
        {'standard_id': 'STD-BRM', 'external_id': '통계·조사', 'match_type': 'CLOSE_MATCH', 'confidence': 0.8},
    ],

    # 02 교육 - UNESCO 기반
    'C02000001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept2954', 'external_name': 'Education', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
        {'standard_id': 'STD-DATAGOkr', 'external_id': '교육', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C02010001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept3143', 'external_name': 'Educational statistics', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C02020001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept5645', 'external_name': 'Lifelong learning', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C02030001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept2776', 'external_name': 'School education', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'C02040001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept4598', 'external_name': 'Higher education', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C02050001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept6504', 'external_name': 'Early childhood education', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'C02060001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept7484', 'external_name': 'Special education', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],

    # 03 보건의료 - KCD/MeSH 기반
    'C03000001': [
        {'standard_id': 'STD-MESH', 'external_id': 'D006296', 'external_name': 'Health Services', 'match_type': 'BROAD_MATCH', 'confidence': 0.9},
        {'standard_id': 'STD-DATAGOkr', 'external_id': '보건', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C03010001': [
        {'standard_id': 'STD-MESH', 'external_id': 'D006268', 'external_name': 'Health Facilities', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C03020001': [
        {'standard_id': 'STD-MESH', 'external_id': 'D006296', 'external_name': 'Health Services', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
    ],
    'C03030001': [
        {'standard_id': 'STD-MESH', 'external_id': 'D006282', 'external_name': 'Health Personnel', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C03040001': [
        {'standard_id': 'STD-MESH', 'external_id': 'D007348', 'external_name': 'Insurance, Health', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'C03050001': [
        {'standard_id': 'STD-MESH', 'external_id': 'D004194', 'external_name': 'Disease', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
        {'standard_id': 'STD-KCD', 'external_id': 'A00-Z99', 'external_name': '질병분류 전체', 'match_type': 'BROAD_MATCH', 'confidence': 0.8},
    ],
    'C03050002': [
        {'standard_id': 'STD-MESH', 'external_id': 'D009369', 'external_name': 'Neoplasms', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
        {'standard_id': 'STD-KCD', 'external_id': 'C00-D48', 'external_name': '신생물', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
        {'standard_id': 'STD-ICD11', 'external_id': '2', 'external_name': 'Neoplasms', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C03050003': [
        {'standard_id': 'STD-MESH', 'external_id': 'D005128', 'external_name': 'Eye Diseases', 'match_type': 'BROAD_MATCH', 'confidence': 0.9},
        {'standard_id': 'STD-KCD', 'external_id': 'H00-H59', 'external_name': '눈 및 눈부속기의 질환', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C03050004': [
        {'standard_id': 'STD-MESH', 'external_id': 'D004066', 'external_name': 'Digestive System Diseases', 'match_type': 'BROAD_MATCH', 'confidence': 0.9},
        {'standard_id': 'STD-KCD', 'external_id': 'K00-K93', 'external_name': '소화계통의 질환', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C03060001': [
        {'standard_id': 'STD-MESH', 'external_id': 'D064886', 'external_name': 'Dataset', 'match_type': 'RELATED_MATCH', 'confidence': 0.7},
    ],

    # 04 사회복지 - DATA-GO-KR 기반
    'C04000001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C04010001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C04020001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C04030001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C04040001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C04050001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C04060001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],

    # 05 법률 - 법제처 기반
    'C05000001': [
        {'standard_id': 'STD-MOLEG', 'external_id': 'LAW', 'external_name': '법령', 'match_type': 'BROAD_MATCH', 'confidence': 0.9},
        {'standard_id': 'STD-DATAGOkr', 'external_id': '법률', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C05010001': [
        {'standard_id': 'STD-MOLEG', 'external_id': 'STATUTE', 'external_name': '법령·법규', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C05020001': [
        {'standard_id': 'STD-MOLEG', 'external_id': 'PREC', 'external_name': '판례', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C05030001': [
        {'standard_id': 'STD-MOLEG', 'external_id': 'SERVICE', 'external_name': '법률서비스', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'C05040001': [
        {'standard_id': 'STD-MOLEG', 'external_id': 'LAW', 'external_name': '법령', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'C05050001': [
        {'standard_id': 'STD-MOLEG', 'external_id': 'LAW', 'external_name': '법령', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'C05060001': [
        {'standard_id': 'STD-MOLEG', 'external_id': 'LAW', 'external_name': '법령', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],

    # 06 재정금융 - FIBO 기반
    'C06000001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fnd', 'external_name': 'Foundations', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재정금융', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C06010001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-ind-ir', 'external_name': 'Interest Rates', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],
    'C06020001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fbc-fi', 'external_name': 'Financial Instruments', 'match_type': 'CLOSE_MATCH', 'confidence': 0.8},
    ],
    'C06030001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-be-corp', 'external_name': 'Corporations', 'match_type': 'BROAD_MATCH', 'confidence': 0.8},
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fbc-fct-fse', 'external_name': 'Financial Services Entities', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],
    'C06040001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-sec', 'external_name': 'Securities', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C06050001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-loan', 'external_name': 'Loan', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C06060001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-ind', 'external_name': 'Indices and Indicators', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C06070001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fbc-pas', 'external_name': 'Products and Services', 'match_type': 'CLOSE_MATCH', 'confidence': 0.8},
    ],
    'C06080001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-sec-fund', 'external_name': 'Funds', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
    ],
    'C06090001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-be-ge', 'external_name': 'Government Entities', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],
    'C06100001': [
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fnd-acc', 'external_name': 'Accounting', 'match_type': 'CLOSE_MATCH', 'confidence': 0.8},
    ],

    # 07 산업경제 - KSIC 기반
    'C07000001': [
        {'standard_id': 'STD-KSIC', 'external_id': 'A-U', 'external_name': '전체 산업분류', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
        {'standard_id': 'STD-DATAGOkr', 'external_id': '산업고용', 'match_type': 'CLOSE_MATCH', 'confidence': 0.8},
    ],
    'C07010001': [
        {'standard_id': 'STD-KSIC', 'external_id': 'C', 'external_name': '제조업', 'match_type': 'BROAD_MATCH', 'confidence': 0.8},
    ],
    'C07020001': [
        {'standard_id': 'STD-KSIC', 'external_id': 'C', 'external_name': '제조업', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
    ],
    'C07030001': [
        {'standard_id': 'STD-KSIC', 'external_id': 'G-N', 'external_name': '서비스업', 'match_type': 'BROAD_MATCH', 'confidence': 0.75},
    ],
    'C07040001': [
        {'standard_id': 'STD-KSIC', 'external_id': 'P', 'external_name': '교육 서비스업', 'match_type': 'NARROW_MATCH', 'confidence': 0.7},
    ],
    'C07050001': [
        {'standard_id': 'STD-KSIC', 'external_id': 'M', 'external_name': '전문, 과학 및 기술 서비스업', 'match_type': 'BROAD_MATCH', 'confidence': 0.75},
    ],
    'C07060001': [
        {'standard_id': 'STD-KSIC', 'external_id': 'C', 'external_name': '제조업', 'match_type': 'BROAD_MATCH', 'confidence': 0.8},
    ],
    'C07070001': [
        {'standard_id': 'STD-KSIC', 'external_id': 'G', 'external_name': '도매 및 소매업', 'match_type': 'RELATED_MATCH', 'confidence': 0.7},
    ],

    # 08 디지털커머스 - KSIC 기반
    'C08000001': [
        {'standard_id': 'STD-KSIC', 'external_id': '47', 'external_name': '소매업; 자동차 제외', 'match_type': 'CLOSE_MATCH', 'confidence': 0.75},
    ],
    'C08010001': [
        {'standard_id': 'STD-KSIC', 'external_id': '4791', 'external_name': '전자상거래 소매업', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C08020001': [
        {'standard_id': 'STD-KSIC', 'external_id': '47', 'external_name': '소매업; 자동차 제외', 'match_type': 'BROAD_MATCH', 'confidence': 0.8},
    ],
    'C08030001': [
        {'standard_id': 'STD-KSIC', 'external_id': '64', 'external_name': '금융업', 'match_type': 'NARROW_MATCH', 'confidence': 0.7},
    ],
    'C08040001': [
        {'standard_id': 'STD-KSIC', 'external_id': '49-52', 'external_name': '운수 및 창고업', 'match_type': 'NARROW_MATCH', 'confidence': 0.75},
    ],
    'C08050001': [
        {'standard_id': 'STD-KSIC', 'external_id': '47', 'external_name': '소매업; 자동차 제외', 'match_type': 'RELATED_MATCH', 'confidence': 0.7},
    ],

    # 09 문화관광 - UNESCO 기반
    'C09000001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept1560', 'external_name': 'Culture', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
        {'standard_id': 'STD-DATAGOkr', 'external_id': '문화관광', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C09010001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept1567', 'external_name': 'Cultural heritage', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C09020001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept8340', 'external_name': 'Tourism', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C09030001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept478', 'external_name': 'Arts', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'C09040001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept1560', 'external_name': 'Culture', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'C09050001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept7538', 'external_name': 'Sport', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'C09060001': [
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept5350', 'external_name': 'Mass media', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],

    # 10 환경기상 - DATA-GO-KR 기반
    'C10000001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경기상', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C10010001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'C10020001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'C10030001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '기상', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C10040001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'C10050001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'C10060001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],

    # 11 과학기술 - OECD FOS 기반
    'C11000001': [
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1-6', 'external_name': 'All Fields of Science', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
        {'standard_id': 'STD-DATAGOkr', 'external_id': '과학기술', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C11010001': [
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1-6', 'external_name': 'Research and Development', 'match_type': 'RELATED_MATCH', 'confidence': 0.7},
    ],
    'C11020001': [
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1', 'external_name': 'Natural sciences', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C11030001': [
        {'standard_id': 'STD-OECD-FOS', 'external_id': '2', 'external_name': 'Engineering and technology', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C11040001': [
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1.2', 'external_name': 'Computer and information sciences', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'C11050001': [
        {'standard_id': 'STD-OECD-FOS', 'external_id': '2', 'external_name': 'Engineering and technology', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C11060001': [
        {'standard_id': 'STD-OECD-FOS', 'external_id': '2.10', 'external_name': 'Nano-technology', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],

    # 12 재난안전 - DATA-GO-KR 기반
    'C12000001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'C12010001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C12020001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C12030001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C12040001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'C12050001': [
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
}

# =============================================================================
# 용어 표준 레퍼런스 매핑 (주요 용어에 대한 표준 연결)
# =============================================================================
TERM_STANDARD_REFS = {
    # 01 공공행정 용어
    'T01010001': [  # 공공기관
        {'standard_id': 'STD-KOOR', 'external_id': 'koor:PublicInstitution', 'external_name': 'Public Institution', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
        {'standard_id': 'STD-BRM', 'external_id': '정부자원관리', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],
    'T01010002': [  # 정부조직도
        {'standard_id': 'STD-KOOR', 'external_id': 'koor:Organization', 'external_name': 'Organization', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],
    'T01020001': [  # 행정구역
        {'standard_id': 'STD-ADMCODE', 'external_id': '법정동코드', 'match_type': 'RELATED_MATCH', 'confidence': 0.9},
    ],
    'T01020002': [  # 지방자치단체
        {'standard_id': 'STD-BRM', 'external_id': '지방행정·재정지원', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
        {'standard_id': 'STD-ADMCODE', 'external_id': '행정동코드', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],
    'T01030001': [  # 공공데이터
        {'standard_id': 'STD-DCAT-AP-KR', 'external_id': 'dcat:Dataset', 'external_name': 'Dataset', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
        {'standard_id': 'STD-STDTERM', 'external_id': '데이터', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
    ],
    'T01030002': [  # 정보시스템
        {'standard_id': 'STD-DBSTD', 'external_id': '정보시스템', 'match_type': 'EXACT_MATCH', 'confidence': 0.9},
    ],

    # 02 교육 용어
    'T02010002': [  # 학교 통계
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept3143', 'external_name': 'Educational statistics', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T02020003': [  # 평생학습강좌
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept5645', 'external_name': 'Lifelong learning', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T02030001': [  # 초중고 교육
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept2776', 'external_name': 'School education', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T02030002': [  # 교육과정
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept1605', 'external_name': 'Curriculum', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T02040002': [  # 대학정보
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept4598', 'external_name': 'Higher education', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
    ],

    # 03 보건의료 용어
    'T03010001': [  # 의료기관
        {'standard_id': 'STD-MESH', 'external_id': 'D006268', 'external_name': 'Health Facilities', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T03010002': [  # 병원
        {'standard_id': 'STD-MESH', 'external_id': 'D006761', 'external_name': 'Hospitals', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'T03010003': [  # 의원
        {'standard_id': 'STD-MESH', 'external_id': 'D011320', 'external_name': 'Primary Health Care', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],
    'T03010004': [  # 약국
        {'standard_id': 'STD-MESH', 'external_id': 'D010607', 'external_name': 'Pharmacies', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T03020002': [  # 백내장
        {'standard_id': 'STD-MESH', 'external_id': 'D002386', 'external_name': 'Cataract', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
        {'standard_id': 'STD-KCD', 'external_id': 'H25-H26', 'external_name': '수정체의 장애', 'match_type': 'NARROW_MATCH', 'confidence': 0.95},
    ],
    'T03020003': [  # 녹내장
        {'standard_id': 'STD-MESH', 'external_id': 'D005901', 'external_name': 'Glaucoma', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
        {'standard_id': 'STD-KCD', 'external_id': 'H40-H42', 'external_name': '녹내장', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'T03030001': [  # 의사
        {'standard_id': 'STD-MESH', 'external_id': 'D010820', 'external_name': 'Physicians', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'T03030002': [  # 간호사
        {'standard_id': 'STD-MESH', 'external_id': 'D009741', 'external_name': 'Nursing Staff', 'match_type': 'CLOSE_MATCH', 'confidence': 0.95},
    ],
    'T03040001': [  # 건강보험
        {'standard_id': 'STD-MESH', 'external_id': 'D007348', 'external_name': 'Insurance, Health', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T03050001': [  # 암
        {'standard_id': 'STD-MESH', 'external_id': 'D009369', 'external_name': 'Neoplasms', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
        {'standard_id': 'STD-ICD11', 'external_id': '2', 'external_name': 'Neoplasms', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
        {'standard_id': 'STD-KCD', 'external_id': 'C00-D48', 'external_name': '신생물', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'T03050002': [  # 대장암
        {'standard_id': 'STD-MESH', 'external_id': 'D015179', 'external_name': 'Colorectal Neoplasms', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
        {'standard_id': 'STD-KCD', 'external_id': 'C18-C20', 'external_name': '결장·직장 악성신생물', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'T03050003': [  # 안구건조증
        {'standard_id': 'STD-MESH', 'external_id': 'D015352', 'external_name': 'Dry Eye Syndromes', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],
    'T03050004': [  # 위식도역류질환
        {'standard_id': 'STD-MESH', 'external_id': 'D005764', 'external_name': 'Gastroesophageal Reflux', 'match_type': 'EXACT_MATCH', 'confidence': 1.0},
    ],

    # 06 재정금융 용어
    'T06010001': [  # 기준금리
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-ind-ir-ir/BaseRate', 'external_name': 'Base Rate', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T06020001': [  # 프로젝트파이낸싱
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-loan-ln-ln/Loan', 'external_name': 'Loan', 'match_type': 'BROAD_MATCH', 'confidence': 0.8},
    ],
    'T06040001': [  # 핀테크
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fbc-fct-fse/FinancialTechnologyCompany', 'external_name': 'FinTech Company', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
        {'standard_id': 'STD-KSIC', 'external_id': '64', 'external_name': '금융업', 'match_type': 'BROAD_MATCH', 'confidence': 0.7},
    ],
    'T06050001': [  # 퇴직연금
         {'standard_id': 'STD-FIBO', 'external_id': 'fibo-sec-fund/PensionFund', 'external_name': 'Pension Fund', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],

    # 07 산업경제 용어
    'T07020001': [  # 반도체산업
        {'standard_id': 'STD-KSIC', 'external_id': '261', 'external_name': '반도체 제조업', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T07020002': [  # 자동차산업
        {'standard_id': 'STD-KSIC', 'external_id': '30', 'external_name': '자동차 및 트레일러 제조업', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],

    # 04 사회복지 용어
    'T04010001': [  # 사회보험
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T04030001': [  # 복지시설
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],

    # 05 법률 용어
    'T05010001': [  # 법령
        {'standard_id': 'STD-MOLEG', 'external_id': '법령', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T05010002': [  # 법률
        {'standard_id': 'STD-MOLEG', 'external_id': '법률', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T05010003': [  # 시행령
        {'standard_id': 'STD-MOLEG', 'external_id': '대통령령', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T05020001': [  # 판례
        {'standard_id': 'STD-MOLEG', 'external_id': '판례', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T05020002': [  # 대법원 판례
        {'standard_id': 'STD-MOLEG', 'external_id': '판례', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],

    # 06 재정금융 용어 (추가)
    'T06010002': [  # 통화량
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fnd-acc-cur/MonetaryAmount', 'external_name': 'Monetary Amount', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
    ],
    'T06030001': [  # 은행
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fbc-fct-fse/Bank', 'external_name': 'Bank', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
        {'standard_id': 'STD-KSIC', 'external_id': '641', 'external_name': '은행 및 저축기관', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T06040002': [  # 주식
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-sec-eq-eq/Equity', 'external_name': 'Equity', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T06040003': [  # 채권
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-sec-dbt-dbti/Bond', 'external_name': 'Bond', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T06040004': [  # 파생상품
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-der-drc-bsc/Derivative', 'external_name': 'Derivative', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T06050002': [  # 국민연금
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-sec-fund/PensionFund', 'external_name': 'Pension Fund', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],

    # 07 산업경제 용어 (추가)
    'T07010001': [  # 산업생산지수
        {'standard_id': 'STD-KSIC', 'external_id': 'C', 'external_name': '제조업', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],
    'T07020003': [  # 바이오산업
        {'standard_id': 'STD-KSIC', 'external_id': '21', 'external_name': '의료용 물질 및 의약품 제조업', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],
    'T07030002': [  # 일자리
        {'standard_id': 'STD-KSIC', 'external_id': 'ALL', 'match_type': 'BROAD_MATCH', 'confidence': 0.7},
    ],
    'T07050001': [  # 중소기업
        {'standard_id': 'STD-KSIC', 'external_id': 'ALL', 'match_type': 'BROAD_MATCH', 'confidence': 0.75},
    ],

    # 08 디지털커머스 용어
    'T08010001': [  # 이커머스 플랫폼
        {'standard_id': 'STD-KSIC', 'external_id': '525', 'external_name': '전자상거래 소매중개업', 'match_type': 'EXACT_MATCH', 'confidence': 0.9},
    ],
    'T08010002': [  # 온라인쇼핑몰
        {'standard_id': 'STD-KSIC', 'external_id': '525', 'external_name': '전자상거래 소매중개업', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'T08020001': [  # 오픈마켓
        {'standard_id': 'STD-KSIC', 'external_id': '525', 'external_name': '전자상거래 소매중개업', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T08030001': [  # 전자결제
        {'standard_id': 'STD-KSIC', 'external_id': '661', 'external_name': '금융 지원 서비스업', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],
    'T08040001': [  # 물류
        {'standard_id': 'STD-KSIC', 'external_id': 'H', 'external_name': '운수 및 창고업', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
    ],

    # 09 문화관광 용어
    'T09010001': [  # 문화재
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept7541', 'external_name': 'Cultural heritage', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T09010002': [  # 유형문화재
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept7541', 'external_name': 'Cultural heritage', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T09010003': [  # 무형문화재
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept451', 'external_name': 'Intangible cultural heritage', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T09020001': [  # 공연예술
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept1756', 'external_name': 'Performing arts', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T09030001': [  # 영화
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept2513', 'external_name': 'Cinema', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T09030002': [  # 방송
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept923', 'external_name': 'Broadcasting', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T09040001': [  # 관광지
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept6974', 'external_name': 'Tourism', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],

    # 10 환경기상 용어
    'T10010001': [  # 대기환경
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경기상', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T10010002': [  # 수질환경
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경기상', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T10010004': [  # 미세먼지
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경기상', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T10020001': [  # 기후변화
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept1346', 'external_name': 'Climate change', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T10030001': [  # 재생에너지
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept5459', 'external_name': 'Renewable energy', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],

    # 11 과학기술 용어
    'T11010001': [  # 연구개발
        {'standard_id': 'STD-OECD-FOS', 'external_id': 'ALL', 'match_type': 'BROAD_MATCH', 'confidence': 0.8},
    ],
    'T11020001': [  # 물리학
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1.3', 'external_name': 'Physical sciences', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T11020002': [  # 화학
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1.4', 'external_name': 'Chemical sciences', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T11030001': [  # 전자공학
        {'standard_id': 'STD-OECD-FOS', 'external_id': '2.2', 'external_name': 'Electrical, electronic and information engineering', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T11030002': [  # 기계공학
        {'standard_id': 'STD-OECD-FOS', 'external_id': '2.3', 'external_name': 'Mechanical engineering', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T11040001': [  # 정보기술
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1.2', 'external_name': 'Computer and information sciences', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T11040002': [  # AI
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1.2', 'external_name': 'Computer and information sciences', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T11050001': [  # 특허
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept4822', 'external_name': 'Patents', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],

    # 12 재난안전 용어
    'T12010001': [  # 재난관리
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T12010002': [  # 재난예방
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T12020001': [  # 생활안전
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T12030001': [  # 민방위
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],

    # === 추가 매핑 (v3.5.0) - 50% 커버리지 달성 ===

    # 01 공공행정 추가 (50% → 75%+)
    'T01020003': [  # 읍면동
        {'standard_id': 'STD-ADMCODE', 'external_id': '법정동코드', 'match_type': 'RELATED_MATCH', 'confidence': 0.9},
    ],
    'T01020004': [  # 행정복지센터
        {'standard_id': 'STD-BRM', 'external_id': '지방행정·재정지원', 'match_type': 'NARROW_MATCH', 'confidence': 0.8},
    ],
    'T01040001': [  # 국가정책
        {'standard_id': 'STD-BRM', 'external_id': '정책분야', 'match_type': 'BROAD_MATCH', 'confidence': 0.85},
    ],

    # 02 교육 추가 (23% → 40%+)
    'T02010001': [  # 교육통계연보
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept3143', 'external_name': 'Educational statistics', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T02010003': [  # 교원 통계
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept6763', 'external_name': 'Teachers', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
    ],
    'T02010004': [  # 학생 통계
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept6556', 'external_name': 'Students', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
    ],
    'T02020001': [  # 평생교육
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept5645', 'external_name': 'Lifelong learning', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T02020004': [  # 성인문해교육
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept4559', 'external_name': 'Literacy', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
    ],
    'T02020005': [  # 직업능력개발
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept7373', 'external_name': 'Vocational education', 'match_type': 'CLOSE_MATCH', 'confidence': 0.9},
    ],
    'T02030004': [  # 학교시설
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept5872', 'external_name': 'School buildings', 'match_type': 'EXACT_MATCH', 'confidence': 0.9},
    ],
    'T02040004': [  # 대학재정
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept3210', 'external_name': 'Educational finance', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T02050002': [  # 특수교육
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept6337', 'external_name': 'Special education', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],

    # 03 보건의료 추가 (63% → 80%+)
    'T03010005': [  # 의료시설
        {'standard_id': 'STD-MESH', 'external_id': 'D006268', 'external_name': 'Health Facilities', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T03010006': [  # 의료장비
        {'standard_id': 'STD-MESH', 'external_id': 'D004864', 'external_name': 'Equipment and Supplies', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],
    'T03020001': [  # 의료이용 통계
        {'standard_id': 'STD-MESH', 'external_id': 'D006296', 'external_name': 'Health Services', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],
    'T03040002': [  # 의료급여
        {'standard_id': 'STD-MESH', 'external_id': 'D008484', 'external_name': 'Medicaid', 'match_type': 'CLOSE_MATCH', 'confidence': 0.85},
    ],

    # 04 사회복지 추가 (20% → 50%+)
    'T04010002': [  # 사회보험
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T04010003': [  # 공적부조
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T04020001': [  # 복지시설
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T04020002': [  # 노인복지시설
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T04040001': [  # 고령사회
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],
    'T04040002': [  # 초고령사회
        {'standard_id': 'STD-DATAGOkr', 'external_id': '사회복지', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],

    # 05 법률 추가 (23% → 40%+)
    'T05010004': [  # 자치법규
        {'standard_id': 'STD-MOLEG', 'external_id': '자치법규', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T05010005': [  # 행정규칙
        {'standard_id': 'STD-MOLEG', 'external_id': '행정규칙', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T05020003': [  # 헌법재판소 결정
        {'standard_id': 'STD-MOLEG', 'external_id': '헌법재판소결정', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T05030001': [  # 법률서비스
        {'standard_id': 'STD-MOLEG', 'external_id': '법령', 'match_type': 'RELATED_MATCH', 'confidence': 0.75},
    ],
    'T05040001': [  # 조세
        {'standard_id': 'STD-MOLEG', 'external_id': '국세기본법', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
    ],
    'T05040002': [  # 종합부동산세
        {'standard_id': 'STD-MOLEG', 'external_id': '종합부동산세법', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T05040003': [  # 양도소득세
        {'standard_id': 'STD-MOLEG', 'external_id': '소득세법', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],

    # 06 재정금융 추가 (47% → 65%+)
    'T06010003': [  # 부처별 예산
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fnd-acc-cur/Budget', 'external_name': 'Budget', 'match_type': 'NARROW_MATCH', 'confidence': 0.8},
    ],
    'T06020002': [  # 재정상태표
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-be-corp-corp/BalanceSheet', 'external_name': 'Balance Sheet', 'match_type': 'EXACT_MATCH', 'confidence': 0.9},
    ],
    'T06030002': [  # 지방교부세
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fnd-acc-cur/Tax', 'external_name': 'Tax', 'match_type': 'RELATED_MATCH', 'confidence': 0.75},
    ],
    'T06060001': [  # 통화정책
        {'standard_id': 'STD-FIBO', 'external_id': 'fibo-fbc-fct-mkt/MonetaryPolicy', 'external_name': 'Monetary Policy', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],

    # 07 산업경제 추가 (26% → 45%+)
    'T07010002': [  # 산업동향
        {'standard_id': 'STD-KSIC', 'external_id': 'ALL', 'match_type': 'BROAD_MATCH', 'confidence': 0.7},
    ],
    'T07030001': [  # 서비스업
        {'standard_id': 'STD-KSIC', 'external_id': 'I-U', 'external_name': '서비스업', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T07040001': [  # 고용통계
        {'standard_id': 'STD-KSIC', 'external_id': 'ALL', 'match_type': 'BROAD_MATCH', 'confidence': 0.7},
    ],
    'T07040003': [  # 실업률
        {'standard_id': 'STD-KSIC', 'external_id': 'ALL', 'match_type': 'BROAD_MATCH', 'confidence': 0.7},
    ],
    'T07050002': [  # 벤처투자
        {'standard_id': 'STD-KSIC', 'external_id': '641', 'external_name': '금융업', 'match_type': 'RELATED_MATCH', 'confidence': 0.75},
    ],
    'T07050003': [  # 창업지원
        {'standard_id': 'STD-KSIC', 'external_id': 'ALL', 'match_type': 'BROAD_MATCH', 'confidence': 0.7},
    ],
    'T07060001': [  # 무역
        {'standard_id': 'STD-KSIC', 'external_id': '46', 'external_name': '도매 및 상품중개업', 'match_type': 'RELATED_MATCH', 'confidence': 0.75},
    ],

    # 08 디지털커머스 추가 (45% → 70%+)
    'T08020002': [  # 크로스보더
        {'standard_id': 'STD-KSIC', 'external_id': '525', 'external_name': '전자상거래 소매중개업', 'match_type': 'RELATED_MATCH', 'confidence': 0.8},
    ],
    'T08030002': [  # BNPL
        {'standard_id': 'STD-KSIC', 'external_id': '661', 'external_name': '금융 지원 서비스업', 'match_type': 'NARROW_MATCH', 'confidence': 0.8},
    ],
    'T08050001': [  # 라이브커머스
        {'standard_id': 'STD-KSIC', 'external_id': '525', 'external_name': '전자상거래 소매중개업', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],

    # 09 문화관광 추가 (29% → 50%+)
    'T09010004': [  # 국보
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept7541', 'external_name': 'Cultural heritage', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T09010005': [  # 세계유산
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept7832', 'external_name': 'World heritage', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T09020002': [  # 관광통계
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept6974', 'external_name': 'Tourism', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T09030003': [  # 미술관
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept5049', 'external_name': 'Museums', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T09030005': [  # 도서관
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept4554', 'external_name': 'Libraries', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T09040002': [  # 전시
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept3381', 'external_name': 'Exhibitions', 'match_type': 'EXACT_MATCH', 'confidence': 0.9},
    ],
    'T09040003': [  # 축제
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept2551', 'external_name': 'Festivals', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T09050001': [  # 체육
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept6372', 'external_name': 'Sport', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],

    # 10 환경기상 추가 (19% → 40%+)
    'T10010003': [  # 수질환경
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경기상', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T10010005': [  # 미세먼지
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경기상', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept264', 'external_name': 'Air pollution', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T10020002': [  # 온실가스
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept1346', 'external_name': 'Climate change', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
    ],
    'T10020003': [  # 탄소중립
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept1346', 'external_name': 'Climate change', 'match_type': 'RELATED_MATCH', 'confidence': 0.85},
    ],
    'T10030002': [  # 기상
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경기상', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T10030003': [  # 기상예보
        {'standard_id': 'STD-DATAGOkr', 'external_id': '환경기상', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T10040001': [  # 생태계
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept2265', 'external_name': 'Ecosystems', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],
    'T10050001': [  # 환경보호
        {'standard_id': 'STD-UNESCO', 'external_id': 'concept2812', 'external_name': 'Environmental protection', 'match_type': 'EXACT_MATCH', 'confidence': 0.95},
    ],

    # 11 과학기술 추가 (67% → 80%+)
    'T11010002': [  # 국가R&D
        {'standard_id': 'STD-OECD-FOS', 'external_id': 'ALL', 'match_type': 'BROAD_MATCH', 'confidence': 0.8},
    ],
    'T11040003': [  # 빅데이터
        {'standard_id': 'STD-OECD-FOS', 'external_id': '1.2', 'external_name': 'Computer and information sciences', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],

    # 12 재난안전 추가 (19% → 40%+)
    'T12010003': [  # 재난대응
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T12020002': [  # 시설물안전
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T12030002': [  # 민방위
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T12040001': [  # 자연재해
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
    'T12040002': [  # 태풍
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.85},
    ],
    'T12050001': [  # 사회재난
        {'standard_id': 'STD-DATAGOkr', 'external_id': '재난안전', 'match_type': 'NARROW_MATCH', 'confidence': 0.9},
    ],
}

# =============================================================================
# 헬퍼 함수
# =============================================================================
def get_standard(standard_id: str) -> dict:
    """표준 ID로 표준 정보 조회"""
    return STANDARDS_REGISTRY.get(standard_id)

def get_classification_refs(clsf_id: str) -> list:
    """분류 ID로 표준 레퍼런스 조회"""
    return CLASSIFICATION_STANDARD_REFS.get(clsf_id, [])

def get_term_refs(term_id: str) -> list:
    """용어 ID로 표준 레퍼런스 조회"""
    return TERM_STANDARD_REFS.get(term_id, [])

def get_domain_standards(domain_code: str) -> list:
    """도메인 코드로 주요 표준 목록 조회"""
    return DOMAIN_PRIMARY_STANDARDS.get(domain_code, [])

def get_standards_by_scope(scope: str) -> list:
    """범위별 표준 목록 조회"""
    return [sid for sid, std in STANDARDS_REGISTRY.items() if std['scope'] == scope]

def get_standards_by_type(std_type: str) -> list:
    """유형별 표준 목록 조회"""
    return [sid for sid, std in STANDARDS_REGISTRY.items() if std['type'] == std_type]
