------------------------------------------------------------
-- MC_CLSF : 분류 체계
-- context.txt 기준 ID 체계 적용
--
-- ID 체계: C + DD(도메인) + LL(중분류) + SSSS(일련번호)
-- 예: C01010001 = 도메인01 + 중분류01 + 일련번호0001
--
-- 간소화 INSERT (DELETE_YN, CREATE_ID, CREATE_DT 제외 - 기본값 사용)
-- 최상위 PRT_CLSF_ID : '03facd74b2d24f7cab807b8980391649'
------------------------------------------------------------


------------------------------------------------------------
-- 01. 공공 | Public Sector
------------------------------------------------------------

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01000001', '공공', '공공 부문 정책 및 행정 전반을 다루는 최상위 분류', '03facd74b2d24f7cab807b8980391649', 'Y',
'도메인 01. 정부 정책, 지방행정, 디지털정부, 국가안전, 지방재정 등 공공부문 전반을 포괄. public/ 디렉토리 문서와 매핑.');

-- 01-01. 지방시대·지역균형발전
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01010001', '지방시대·지역균형발전', '지방시대 정책과 지역균형발전을 다루는 분류', 'C01000001', 'Y',
'중분류 01-01. 수도권 집중 완화, 지역 주도 발전, 인구감소지역 지원 정책 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01010002', '인구감소지역·지방소멸 대응', '인구감소지역 지원 및 지방소멸 대응 정책을 다루는 분류', 'C01010001', 'N',
'소분류. 인구감소지역 지원 특별법, 지방소멸대응기금 등 관련 정책.');

-- 01-02. 지방자치·행정체제 개편
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01020001', '지방자치·행정체제 개편', '지방자치제도 및 행정체제 개편을 다루는 분류', 'C01000001', 'Y',
'중분류 01-02. 지방자치법, 행정구역 개편, 자치분권 정책 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01020002', '특별자치시·도', '특별자치시 및 특별자치도 관련 제도를 다루는 분류', 'C01020001', 'N',
'소분류. 세종특별자치시, 제주특별자치도 등 특례 지방자치단체 관련.');

-- 01-03. 디지털플랫폼정부
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01030001', '디지털플랫폼정부', '디지털플랫폼정부 정책 전반을 다루는 분류', 'C01000001', 'Y',
'중분류 01-03. 데이터·AI·클라우드 기반 공공서비스 혁신, 전자정부 고도화 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01030002', '공공마이데이터·공공데이터', '공공마이데이터 및 공공데이터 정책을 다루는 분류', 'C01030001', 'N',
'소분류. 개인정보 자기결정권, 공공데이터 개방·활용 정책.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01030003', 'AI기반 대국민 서비스', 'AI 기반 대국민 서비스 정책을 다루는 분류', 'C01030001', 'N',
'소분류. 챗봇, 보이스피싱 탐지 등 AI 활용 공공서비스.');

-- 01-04. 국가안전시스템 개편
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01040001', '국가안전시스템 개편', '국가안전시스템 개편 정책을 다루는 분류', 'C01000001', 'Y',
'중분류 01-04. 재난안전관리체계, 위기대응 훈련, 안전관리 정책 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01040002', '다중밀집·인파 안전', '다중밀집 장소 및 인파 안전관리를 다루는 분류', 'C01040001', 'N',
'소분류. 대규모 행사, 다중이용시설 안전관리 정책.');

-- 01-05. 지방재정·교부세
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01050001', '지방재정·교부세', '지방재정 및 지방교부세 정책을 다루는 분류', 'C01000001', 'Y',
'중분류 01-05. 지방재정 건전성, 교부세 배분, 지방채 관리 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C01050002', '고향사랑기부제', '고향사랑기부제 관련 정책을 다루는 분류', 'C01050001', 'N',
'소분류. 지방재정 확충을 위한 기부금 제도, 답례품 정책.');


------------------------------------------------------------
-- 02. 금융 | Finance
------------------------------------------------------------

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02000001', '금융', '금융 정책 및 제도 전반을 다루는 최상위 분류', '03facd74b2d24f7cab807b8980391649', 'Y',
'도메인 02. 통화정책, 금융안정, 상생금융, 핀테크, 자본시장, 연금 등 금융부문 전반을 포괄. finance/ 디렉토리 문서와 매핑.');

-- 02-01. 통화정책·통화신용정책
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02010001', '통화정책·통화신용정책', '통화정책 및 통화신용정책 전반을 다루는 분류', 'C02000001', 'Y',
'중분류 02-01. 한국은행 통화정책, 금리정책, 유동성 관리 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02010002', '기준금리 운영', '기준금리 결정 및 운영을 다루는 분류', 'C02010001', 'N',
'소분류. 금융통화위원회 기준금리 결정, 금리 인상/인하 정책.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02010003', '금융중개지원대출·유동성조절', '금융중개지원대출 및 유동성조절을 다루는 분류', 'C02010001', 'N',
'소분류. 중소기업 지원 대출, 공개시장운영 등 유동성 관리 수단.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02010004', '공개시장운영·대상기관제도', '한국은행 공개시장운영 규정 개정, 대상기관 선정기준, 입찰 제도 개선을 다루는 분류', 'C02010001', 'N',
'소분류. finance/2. 통화신용정책 운영.pdf. 2024.1.25 공개시장운영규정 개정으로 자산운용사·비은행중앙회 편입, RP 입찰 한도·증권 배정 변경, 단기금리 안정 장치 정리.');

-- 02-02. 금융안정·부동산PF
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02020001', '금융안정·부동산PF', '금융안정 및 부동산 PF 관련 정책을 다루는 분류', 'C02000001', 'Y',
'중분류 02-02. 금융시스템 안정성, 부동산 프로젝트 파이낸싱 리스크 관리.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02020002', '가계부채·취약차주', '가계부채 및 취약차주 관리 정책을 다루는 분류', 'C02020001', 'N',
'소분류. DSR 규제, 취약차주 보호, 가계부채 관리 정책.');

-- 02-03. 상생금융·포용금융
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02030001', '상생금융·포용금융', '상생금융 및 포용금융 정책을 다루는 분류', 'C02000001', 'N',
'중분류 02-03. 금융소외계층 지원, 금융기관 사회적 책임, 서민금융.');

-- 02-04. 핀테크·혁신금융
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02040001', '핀테크·혁신금융', '핀테크 및 혁신금융 정책을 다루는 분류', 'C02000001', 'Y',
'중분류 02-04. 디지털금융 혁신, 규제샌드박스, 오픈뱅킹 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02040002', '핀테크 투자 생태계', '핀테크 투자 및 생태계 조성을 다루는 분류', 'C02040001', 'N',
'소분류. 핀테크 스타트업 투자, 혁신펀드, 액셀러레이터.');

-- 02-05. 자본시장·증시
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02050001', '자본시장·증시', '자본시장 및 증시 관련 정책을 다루는 분류', 'C02000001', 'N',
'중분류 02-05. 주식시장, 채권시장, 투자자 보호, 기업공시 정책.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02050002', '투자자 커뮤니케이션·시장전망', '투자자 대상 콘퍼런스, 리서치센터 전망 공유, 증시 콘서트 등 시장소통 행사를 다루는 분류', 'C02050001', 'N',
'소분류. finance/★2019 제1회 증시콘서트 자료집_최종★.pdf. 금융투자협회 주관 콘서트 구성, 리서치센터장 발표, 자산운용사 토론 체계 기록.');

-- 02-06. 연금·노후자산
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02060001', '연금·노후자산', '연금 및 노후자산 관리 정책을 다루는 분류', 'C02000001', 'N',
'중분류 02-06. 퇴직연금, 개인연금, 노후자산 운용 정책.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02060002', '기금형 퇴직연금 도입', '기금형 퇴직연금 제도 설계, 국제 포럼 협력, 디폴트옵션 논의를 다루는 분류', 'C02060001', 'N',
'소분류. finance/한-호주 퇴직연금 포럼_책자(최종).pdf. 한-호주 공동포럼 아젠다, 기금형 거버넌스·운용 사례·규제 비교 포함.');

-- 02-07. 은행산업 경쟁·인가제도
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02070001', '은행산업 경쟁·인가제도', '은행 인가제도와 경쟁 촉진 정책을 다루는 분류', 'C02000001', 'Y',
'중분류 02-07. 지방은행 시중은행 전환, 인가요건, 영업구역 규제 완화 등.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02070002', '지방은행 시중은행 전환', '지방은행이 전국 단위 시중은행으로 전환할 때 필요한 인가방식과 절차를 다루는 분류', 'C02070001', 'N',
'소분류. 은행법 제8조 인가내용 변경, 예비인가 생략 조건, 외부평가위원회 심사 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02070003', '은행 인가 심사·외부평가', '은행업 인가 세부심사요건, 외부평가위원회 운영, 심사중단 요건을 다루는 분류', 'C02070001', 'N',
'소분류. finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf. 대주주·사업계획·내부통제 심사, 금융사고 대응 기준, 심사기한 명문화.');

-- 02-08. 지속가능·녹색금융
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02080001', '지속가능·녹색금융', '기후위기 대응을 위한 녹색금융 정책, 공시, 국제 협력 전반을 다루는 분류', 'C02000001', 'Y',
'중분류 02-08. finance/WP22-05.pdf. 녹색금융 추진 배경, TCFD·BIS 움직임, 정책·민간 역할 포함.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C02080002', '녹색분류체계·TCFD 공시', '한국형 녹색분류체계 기준, TCFD 권고안 기반 공시, 녹색금융 핸드북 등을 다루는 분류', 'C02080001', 'N',
'소분류. finance/WP22-05.pdf. 6대 환경목표와 DNSH 요건, 금융위·금감원·금융협회 추진 현황, 공시 로드맵 정리.');


------------------------------------------------------------
-- 03. 커머스 | Commerce
------------------------------------------------------------

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03000001', '커머스', '전자상거래 및 커머스 전반을 다루는 최상위 분류', '03facd74b2d24f7cab807b8980391649', 'Y',
'도메인 03. 이커머스 시장, 유통모델, 라이브커머스, 소비자행동, 물류, 솔루션 등 커머스 전반을 포괄. commerce/ 디렉토리 문서와 매핑.');

-- 03-01. 이커머스 시장·플랫폼
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03010001', '이커머스 시장·플랫폼', '이커머스 시장 및 플랫폼 동향을 다루는 분류', 'C03000001', 'Y',
'중분류 03-01. 온라인 쇼핑 시장 규모, 주요 플랫폼 경쟁구도 분석.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03010002', '글로벌 이커머스 시장', '글로벌 이커머스 시장 동향을 다루는 분류', 'C03010001', 'N',
'소분류. 아마존, 알리바바 등 글로벌 플랫폼, 크로스보더 이커머스.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03010003', '국내 이커머스 경쟁구도', '국내 이커머스 시장 경쟁구도를 다루는 분류', 'C03010001', 'N',
'소분류. 쿠팡, 네이버, SSG 등 국내 플랫폼 경쟁 분석.');

-- 03-02. 온라인 유통모델·D2C
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03020001', '온라인 유통모델·D2C', '온라인 유통모델 및 D2C를 다루는 분류', 'C03000001', 'Y',
'중분류 03-02. 직접판매, 중개모델, 구독경제 등 유통 비즈니스 모델.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03020002', 'D2C·구독경제', 'D2C 및 구독경제 모델을 다루는 분류', 'C03020001', 'N',
'소분류. 브랜드 직접판매, 정기구독 서비스 비즈니스 모델.');

-- 03-03. 라이브커머스·콘텐츠 커머스
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03030001', '라이브커머스·콘텐츠 커머스', '라이브커머스 및 콘텐츠 커머스를 다루는 분류', 'C03000001', 'Y',
'중분류 03-03. 실시간 방송 판매, 숏폼 콘텐츠 연계 커머스.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03030002', '라이브커머스 플랫폼', '라이브커머스 플랫폼 동향을 다루는 분류', 'C03030001', 'N',
'소분류. 네이버 쇼핑라이브, 카카오 쇼핑라이브, 그립 등 플랫폼.');

-- 03-04. 소비자 행동·패턴 변화
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03040001', '소비자 행동·패턴 변화', '소비자 행동 및 패턴 변화를 다루는 분류', 'C03000001', 'Y',
'중분류 03-04. 온라인 소비 트렌드, 소비자 구매 여정 분석.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03040002', '중고거래 플랫폼', '중고거래 플랫폼 동향을 다루는 분류', 'C03040001', 'N',
'소분류. 당근마켓, 번개장터 등 C2C 중고거래 시장.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03040003', '배달 플랫폼·라스트마일', '배달 플랫폼 및 라스트마일 배송을 다루는 분류', 'C03040001', 'N',
'소분류. 배달의민족, 쿠팡이츠 등 배달앱, 퀵커머스.');

-- 03-05. 이커머스 물류·풀필먼트
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03050001', '이커머스 물류·풀필먼트', '이커머스 물류 및 풀필먼트를 다루는 분류', 'C03000001', 'N',
'중분류 03-05. 물류센터, 당일배송, 새벽배송, 3PL/풀필먼트 서비스.');

-- 03-06. 이커머스 솔루션·SaaS
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03060001', '이커머스 솔루션·SaaS', '이커머스 솔루션 및 SaaS를 다루는 분류', 'C03000001', 'Y',
'중분류 03-06. 쇼핑몰 구축, 주문관리, 결제 솔루션.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C03060002', '마케팅·리뷰·고객경험', '마케팅, 리뷰, 고객경험 솔루션을 다루는 분류', 'C03060001', 'N',
'소분류. CRM, 마케팅자동화, 리뷰관리, 개인화 솔루션.');


------------------------------------------------------------
-- 04. 산업 | Industry
------------------------------------------------------------

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C04000001', '산업', '산업 정책 및 트렌드 전반을 다루는 최상위 분류', '03facd74b2d24f7cab807b8980391649', 'Y',
'도메인 04. 디지털경제, 스타트업, 소비트렌드, 미디어 등 산업 전반을 포괄.');

-- 04-01. 디지털 경제·플랫폼 경제
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C04010001', '디지털 경제·플랫폼 경제', '디지털 경제 및 플랫폼 경제를 다루는 분류', 'C04000001', 'Y',
'중분류 04-01. 데이터 경제, 플랫폼 비즈니스, 디지털 전환.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C04010002', '딥테크·기저기술', '딥테크 및 기저기술을 다루는 분류', 'C04010001', 'N',
'소분류. AI, 양자컴퓨팅, 바이오테크 등 핵심 기반기술.');

-- 04-02. 신산업·스타트업 생태계
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C04020001', '신산업·스타트업 생태계', '신산업 및 스타트업 생태계를 다루는 분류', 'C04000001', 'Y',
'중분류 04-02. 창업생태계, 벤처투자, 유니콘 기업.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C04020002', '벤처투자·모태펀드', '벤처투자 및 모태펀드를 다루는 분류', 'C04020001', 'N',
'소분류. 정책금융, 벤처캐피탈, 액셀러레이터 투자.');

-- 04-03. 소비·라이프스타일 트렌드
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C04030001', '소비·라이프스타일 트렌드', '소비 및 라이프스타일 트렌드를 다루는 분류', 'C04000001', 'Y',
'중분류 04-03. 소비자 가치관 변화, 라이프스타일 트렌드 분석.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C04030002', '뉴 럭셔리 비즈니스', '뉴 럭셔리 비즈니스 트렌드를 다루는 분류', 'C04030001', 'N',
'소분류. MZ세대 럭셔리 소비, 경험 중심 프리미엄.');

-- 04-04. 미디어·콘텐츠·플랫폼
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C04040001', '미디어·콘텐츠·플랫폼', '미디어, 콘텐츠, 플랫폼 산업을 다루는 분류', 'C04000001', 'N',
'중분류 04-04. OTT, 숏폼, 크리에이터 이코노미, 미디어 플랫폼.');


------------------------------------------------------------
-- 05. 사회 | Society
------------------------------------------------------------

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C05000001', '사회', '사회 구조 및 복지 전반을 다루는 최상위 분류', '03facd74b2d24f7cab807b8980391649', 'Y',
'도메인 05. 고령화, 인구구조, 사회보장, 노동·고용 등 사회부문 전반을 포괄.');

-- 05-01. 고령화·인구구조
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C05010001', '고령화·인구구조', '고령화 및 인구구조 변화를 다루는 분류', 'C05000001', 'Y',
'중분류 05-01. 저출산·고령화, 인구감소, 인구구조 변화 분석.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C05010002', '고령자 세분화·초고령사회', '고령자 세분화 및 초고령사회를 다루는 분류', 'C05010001', 'N',
'소분류. 전기고령자/후기고령자, 액티브시니어, 초고령사회 대응.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C05010003', '초고령사회 소비·돌봄', '초고령사회에서의 소비패턴, 노노케어, 새로운 가족형태, 유니버설 디자인 정책을 다루는 분류', 'C05010001', 'N',
'소분류. finance/KIFVIP2013-10.pdf. 일본 초고령사회 사례, 노노케어 확산, Invisible Family, 유니버설 디자인 산업 육성 분석.');

-- 05-02. 사회보장·연금
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C05020001', '사회보장·연금', '사회보장 및 연금 제도를 다루는 분류', 'C05000001', 'Y',
'중분류 05-02. 국민연금, 건강보험, 기초연금 등 사회보장제도.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C05020002', '공적연금 의존도·연금라이프', '공적연금 의존도 및 연금라이프를 다루는 분류', 'C05020001', 'N',
'소분류. 노후소득원, 연금 의존도, 은퇴 후 생활패턴.');

-- 05-03. 노동·고용·고령자 일자리
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C05030001', '노동·고용·고령자 일자리', '노동, 고용, 고령자 일자리를 다루는 분류', 'C05000001', 'N',
'중분류 05-03. 고용정책, 고령자 재취업, 정년연장.');


------------------------------------------------------------
-- 06. 법률 | Law
------------------------------------------------------------

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06000001', '법률', '법률 및 판례 전반을 다루는 최상위 분류', '03facd74b2d24f7cab807b8980391649', 'Y',
'도메인 06. 판례, 세법, 행정법 등 법률부문 전반을 포괄. law/ 디렉토리 문서와 매핑.');

-- 06-01. 판례·판결
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06010001', '판례·판결', '판례 및 판결 전반을 다루는 분류', 'C06000001', 'Y',
'중분류 06-01. 대법원, 헌법재판소, 하급심 판례 분석.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06010002', '민사 판례', '민사 관련 판례를 다루는 분류', 'C06010001', 'N',
'소분류. 계약, 손해배상, 부동산, 가족법 관련 민사 판결.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06010003', '행정 판례', '행정 관련 판례를 다루는 분류', 'C06010001', 'N',
'소분류. 행정처분 취소, 과세처분 취소 등 행정소송 판결.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06010004', '형사 판례', '형사 관련 판례를 다루는 분류', 'C06010001', 'N',
'소분류. 형사범죄, 특별법 위반 관련 판결.');

-- 06-02. 세법·조세
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06020001', '세법·조세', '세법 및 조세 제도를 다루는 분류', 'C06000001', 'Y',
'중분류 06-02. 소득세, 법인세, 부가가치세, 상속세 등 조세법.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06020002', '세금제도 변경', '세금제도 변경 및 개정을 다루는 분류', 'C06020001', 'N',
'소분류. 세법 개정, 세제 혜택, 조세특례.');

-- 06-03. 공무원법·행정법
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06030001', '공무원법·행정법', '공무원법 및 행정법을 다루는 분류', 'C06000001', 'N',
'중분류 06-03. 국가공무원법, 지방공무원법, 행정절차법.');


------------------------------------------------------------
-- 07. 의료 | Medical
------------------------------------------------------------

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07000001', '의료', '의료 및 건강 전반을 다루는 최상위 분류', '03facd74b2d24f7cab807b8980391649', 'Y',
'도메인 07. 암, 안과, 소화기, 건강관리 등 의료부문 전반을 포괄. medical/ 디렉토리 문서와 매핑.');

-- 07-01. 암·종양
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07010001', '암·종양', '암 및 종양 관련 질환을 다루는 분류', 'C07000001', 'Y',
'중분류 07-01. 암 진단, 치료, 예방, 연구 전반.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07010002', '대장암', '대장암 관련 의학을 다루는 분류', 'C07010001', 'N',
'소분류. 대장암 진단, 수술, 항암치료, 예후.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07010003', '다발성골수종', '다발성골수종 관련 의학을 다루는 분류', 'C07010001', 'N',
'소분류. 혈액암의 일종, 진단/치료/관리.');

-- 07-02. 안과
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07020001', '안과', '안과 질환 전반을 다루는 분류', 'C07000001', 'Y',
'중분류 07-02. 눈 관련 질환, 시력교정, 안과수술.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07020002', '안구건조증', '안구건조증 관련 의학을 다루는 분류', 'C07020001', 'N',
'소분류. 건성안 진단, 치료, 관리.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07020003', '안과질환', '기타 안과질환을 다루는 분류', 'C07020001', 'N',
'소분류. 백내장, 녹내장, 망막질환 등.');

-- 07-03. 소화기
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07030001', '소화기', '소화기 질환 전반을 다루는 분류', 'C07000001', 'Y',
'중분류 07-03. 위장관, 간, 담도, 췌장 질환.');

INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07030002', '위식도역류질환', '위식도역류질환 관련 의학을 다루는 분류', 'C07030001', 'N',
'소분류. GERD 진단, 치료, 생활관리.');

-- 07-04. 건강관리·예방
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C07040001', '건강관리·예방', '건강관리 및 예방의학을 다루는 분류', 'C07000001', 'N',
'중분류 07-04. 건강검진, 예방접종, 생활습관 개선.');
