------------------------------------------------------------
-- MC_TERM : 용어 체계
-- context.txt 기준 ID 체계 적용
--
-- ID 체계: T + DD(도메인) + LL(중분류) + SSSS(일련번호)
-- 예: T01010001 = 도메인01 + 중분류01 + 일련번호0001
--
-- 간소화 INSERT (DELETE_YN, CREATE_ID, CREATE_DT 제외 - 기본값 사용)
-- TERM_NAME_EN: 영문명, ACRONYM: 약어, TERM_DESC: 설명, README: 관련 분류 ID
-- 최상위 PRT_TERM_ID : '4147179070a84d3887b97eb57085d850'
------------------------------------------------------------


------------------------------------------------------------
-- 01. 공공 | Public Sector
------------------------------------------------------------

-- 01-01. 지방시대·지역균형발전 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01010001', '지방시대', 'Local Era', NULL,
'지역 주도의 균형발전을 통해 수도권 집중을 완화하고 지방이 자생력을 갖춘 시대를 지향하는 정책 기조',
'4147179070a84d3887b97eb57085d850', 'T', 'C01010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01010002', '지방시대위원회', 'Presidential Committee for Local Era', NULL,
'지방시대 정책을 총괄 조정하는 대통령 소속 위원회',
'4147179070a84d3887b97eb57085d850', 'T', 'C01010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01010003', '인구감소지역 지원 특별법', 'Special Act on Support for Depopulation Areas', NULL,
'인구감소로 인한 지방소멸 위험에 대응하기 위해 인구감소지역을 지정하고 재정·행정지원을 규정한 법률',
'4147179070a84d3887b97eb57085d850', 'T', 'C01010002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01010004', '지방소멸대응기금', 'Local Extinction Response Fund', NULL,
'인구감소와 고령화로 소멸위기에 처한 지역의 정주여건 개선과 일자리 창출을 위해 지원하는 재정지원 기금',
'4147179070a84d3887b97eb57085d850', 'T', 'C01010002');

-- 01-02. 디지털플랫폼정부 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01020001', '디지털플랫폼정부', 'Digital Platform Government', NULL,
'데이터·AI·클라우드를 기반으로 공공서비스를 통합·연계하여 국민이 맞춤형 서비스를 이용할 수 있도록 하는 정부 운영 패러다임',
'4147179070a84d3887b97eb57085d850', 'T', 'C01030001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01020002', '공공마이데이터', 'Public MyData', NULL,
'개인이 공공기관에 분산된 본인 정보를 통합 조회·제공받고 민간서비스와 연계해 활용할 수 있도록 하는 공공 데이터 서비스 체계',
'4147179070a84d3887b97eb57085d850', 'T', 'C01030002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01020003', '보이스피싱 음성분석 모델', 'Voice Phishing Detection Model', NULL,
'AI 기반으로 보이스피싱 통화를 실시간 탐지하는 음성분석 모델',
'4147179070a84d3887b97eb57085d850', 'T', 'C01030003');

-- 01-03. 국가안전시스템 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01030001', '국가안전시스템 개편 종합대책', 'Comprehensive Plan for National Safety System Reform', NULL,
'재난·사고에 대비하고 대응하기 위한 국가 차원의 통합 재난안전관리체계 개편 종합대책',
'4147179070a84d3887b97eb57085d850', 'T', 'C01040001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01030002', 'READY Korea 훈련', 'READY Korea Drill', NULL,
'국가 재난대응역량 강화를 위한 범정부 합동 재난대응 훈련',
'4147179070a84d3887b97eb57085d850', 'T', 'C01040001');

-- 01-04. 지방재정 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01040001', '고향사랑기부제', 'Hometown Love Donation Program', NULL,
'개인이 자신의 주소지 외 지방자치단체에 기부하면 세액공제와 답례품을 받을 수 있는 제도',
'4147179070a84d3887b97eb57085d850', 'T', 'C01050002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T01040002', '지방교부세', 'Local Allocation Tax', NULL,
'국세 수입의 일정 비율을 지방자치단체에 배분하여 지방재정의 균형을 도모하는 재원',
'4147179070a84d3887b97eb57085d850', 'T', 'C01050001');


------------------------------------------------------------
-- 02. 금융 | Finance
------------------------------------------------------------

-- 02-01. 통화정책 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010001', '기준금리', 'Base Rate', NULL,
'중앙은행이 금융기관과의 거래에서 기준이 되는 정책금리로, 통화정책의 기조를 나타냄',
'4147179070a84d3887b97eb57085d850', 'T', 'C02010002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010002', '금융중개지원대출', 'Bank Intermediated Lending Support Facility', NULL,
'중앙은행이 금융기관에 저리로 자금을 공급하여 중소기업 등에 대한 대출을 지원하는 제도',
'4147179070a84d3887b97eb57085d850', 'T', 'C02010003');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010003', '공개시장운영', 'Open Market Operations', 'OMO',
'중앙은행이 금융시장에서 유가증권을 매매하여 통화량과 금리를 조절하는 정책수단',
'4147179070a84d3887b97eb57085d850', 'T', 'C02010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010004', '물가안정기 재진입', 'Re-entry into Price Stability Phase', NULL,
'소비자물가와 근원물가가 목표 수준(2%) 부근으로 되돌아오는 과정에서 나타나는 정책 국면으로, 물가 둔화 추세와 리스크를 지속 점검하는 단계',
'4147179070a84d3887b97eb57085d850', 'T', 'C02010001 | finance/3. 향후 통화신용정책 방향.pdf. 물가안정기 복귀 리스크·조건 설명.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010005', '근원물가', 'Core Inflation', NULL,
'에너지·농산물 등 변동성이 큰 품목을 제외해 기조적 물가 흐름을 측정하는 지표로 통화신용정책 판단의 핵심 참고지표',
'T02010004', 'T', 'C02010001 | 동일 문건에서 근원물가 상승률 전망(2.2%) 및 둔화 흐름 강조.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010006', '공개시장운영 대상기관 확대', 'Expanded OMO Counterparty Scope', NULL,
'2024년 1월 25일 개정된 한국은행 공개시장운영규정으로 자산운용사, 농·수·산림·신협·새마을금고 중앙회, 상호저축은행 등이 대상기관에 편입되어 초단기금리 변동성을 직접 완화할 수 있게 된 제도',
'4147179070a84d3887b97eb57085d850', 'T', 'C02010004 | finance/2. 통화신용정책 운영.pdf. MMF 수신 규모, 콜론 비중 반영한 평가항목과 재무건전성 요건을 명시.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010007', '통화안정증권 발행', 'Monetary Stabilization Bond Issuance', NULL,
'콜금리를 기준금리 수준에 묶어두기 위해 통화안정증권 발행잔액을 조절하는 한국은행의 대표적 흡수수단으로, 2023년 4분기에는 잔액을 3.4조원 줄여 지준공급 축소에 대응',
'4147179070a84d3887b97eb57085d850', 'T', 'C02010004 | finance/2. 통화신용정책 운영.pdf. 통안증권 발행·대상기관 재선정 조건을 동시에 정비.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010008', '환매조건부증권 매입', 'Repurchase Agreement Purchases', 'RP',
'연말 자금 수급 불일치나 지준공급 축소 시 한국은행이 RP를 매입해 단기자금시장에 유동성을 공급하는 조치로, 2024년 1~2월 네 차례 집행되어 콜금리 상승을 억제',
'4147179070a84d3887b97eb57085d850', 'T', 'C02010004 | finance/2. 통화신용정책 운영.pdf. 연말 MMF 환매, 화폐발행 증가에 맞춘 4차례 매입 사례 명시.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02010009', '통화안정계정 예치', 'Monetary Stabilization Account Deposit', NULL,
'시중 은행이 초과지준을 중앙은행에 예치해 유동성을 흡수하도록 하는 통화신용정책 수단으로, 통화안정증권·RP와 병행해 콜금리 상단을 관리',
'4147179070a84d3887b97eb57085d850', 'T', 'C02010004 | finance/2. 통화신용정책 운영.pdf. 통안계정 예치 규모를 Q4에 5.4조원 줄였다가 2024년 1월 다시 0.5조원 늘린 경로 설명.');

-- 02-02. 금융안정 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02020001', '부동산 PF 대출', 'Real Estate Project Financing Loan', 'PF',
'부동산 개발사업의 미래 수익을 담보로 사업비를 조달하는 금융기법',
'4147179070a84d3887b97eb57085d850', 'T', 'C02020001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02020002', '금융안정', 'Financial Stability', NULL,
'금융시스템이 충격에도 불구하고 금융중개 기능을 안정적으로 수행할 수 있는 상태',
'4147179070a84d3887b97eb57085d850', 'T', 'C02020001');

-- 02-03. 상생금융·포용금융 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02030001', '상생금융', 'Mutual Growth Finance', NULL,
'금융기관이 취약계층·중소기업 지원 등을 통해 사회적 책임을 이행하는 금융',
'4147179070a84d3887b97eb57085d850', 'T', 'C02030001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02030002', '포용금융', 'Inclusive Finance', NULL,
'금융 소외계층도 적정 비용으로 금융서비스를 이용할 수 있도록 하는 금융정책',
'4147179070a84d3887b97eb57085d850', 'T', 'C02030001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02030003', '소상공인 금리부담경감 3종 세트', 'Small Business Interest Relief Package', NULL,
'은행·중소금융권 이자환급, 저금리 대환 프로그램 등 소상공인 금리 부담을 낮추기 위한 3단계 패키지 지원방안',
'4147179070a84d3887b97eb57085d850', 'T', 'C02030001 | 2024.3 금융위·금융권 발표 보도자료(상생금융 추진현황). 총 2.4조원 규모 환급·대환 중심.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02030004', '저금리 대환 프로그램', 'Low-interest Refinancing Program', NULL,
'신용보증기금 보증을 통해 고금리 대출을 저금리로 갈아탈 수 있도록 지원 범위를 확대한 대환 프로그램',
'4147179070a84d3887b97eb57085d850', 'T', 'C02030001 | 소상공인 금리부담경감 3종 세트 구성요소. 2023.5.31 취급분까지 대상 확대, 금리상한·보증료 인하 포함.');

-- 02-04. 핀테크 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02040001', '핀테크', 'Fintech', NULL,
'금융(Finance)과 기술(Technology)의 합성어로, 디지털 기술을 활용한 혁신적 금융서비스',
'4147179070a84d3887b97eb57085d850', 'T', 'C02040001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02040002', '핀테크 혁신펀드', 'Fintech Innovation Fund', NULL,
'핀테크 스타트업 육성을 위한 정책금융 투자펀드',
'4147179070a84d3887b97eb57085d850', 'T', 'C02040002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02040003', '핀테크 혁신펀드 1호', 'Fintech Innovation Fund I', NULL,
'2020~2023년 조성된 1호 펀드로 총 5,133억원을 모아 85개 핀테크 스타트업에 2,824억원을 공급한 모펀드',
'T02040002', 'T', 'C02040002 | 금융위 2024.4.9 핀테크 투자생태계 간담회 보도자료. 은행권·성장사다리 자금이 참여.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02040004', '핀테크 혁신펀드 2호', 'Fintech Innovation Fund II', NULL,
'2024~2027년 추가로 5,000억원을 조성해 총 1조원 규모로 확대하는 후속 모펀드. 성장단계별 맞춤 투자를 추진',
'T02040002', 'T', 'C02040002 | 빅테크(네이버파이낸셜·카카오페이) 출자, 초기·사업화·해외진출 단계별 투자계획.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02040005', '핀테크 투자생태계 활성화', 'Fintech Investment Ecosystem Activation', NULL,
'핀테크 기업 투자 위축에 대응해 혁신펀드 확대, 규제샌드박스 내실화, 해외진출·정책금융 지원 등을 추진하는 정책 방향',
'4147179070a84d3887b97eb57085d850', 'T', 'C02040001 | 금융위 김소영 부위원장 2024.4.9 발언 요지. 투자기관·핀테크 기업 간 협업과 후속투자 연계 강조.');

-- 02-05. 자본시장·증시 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02050004', '증시 콘서트', 'Capital Market Concert', NULL,
'2019년 7월 2일 금융투자협회 불스홀에서 열린 제1회 증시 콘서트로, 증권사 리서치센터장 4인과 자산운용사 경영진이 하반기 시장전망을 공유한 투자자 커뮤니케이션 행사',
'4147179070a84d3887b97eb57085d850', 'T', 'C02050002 | finance/★2019 제1회 증시콘서트 자료집_최종★.pdf. 진행순서·발표자 명단·토론 패널 구성 기술.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02050005', '하반기 증시 대전망 세션', 'H2 Market Outlook Session', NULL,
'증시 콘서트 1부(14:40~15:40)에서 삼성·하나·SK·NH 리서치센터장이 국내외 경제·업종별 전망과 투자전략을 발표하는 세션',
'T02050004', 'T', 'C02050002 | finance/★2019 제1회 증시콘서트 자료집_최종★.pdf. 세션 시간표와 발언자 역할을 그대로 옮겨 투자자 설명자료로 사용.');

-- 02-06. 연금 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02050001', '퇴직연금', 'Retirement Pension', NULL,
'근로자의 노후소득 보장을 위해 사용자가 급여나 부담금을 적립하고, 퇴직 시 연금 또는 일시금으로 수령하는 제도',
'4147179070a84d3887b97eb57085d850', 'T', 'C02060001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02050002', '기금형 퇴직연금', 'Fund-type Retirement Pension', NULL,
'퇴직연금 적립금을 별도의 기금으로 운용하여 전문성과 수익률을 높이는 퇴직연금 운용방식',
'4147179070a84d3887b97eb57085d850', 'T', 'C02060001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02050003', '고령화와 금융자산 운용', 'Ageing and Financial Asset Management', NULL,
'고령화 사회에서 노후자산의 효율적 운용과 관련된 금융정책 및 연구',
'4147179070a84d3887b97eb57085d850', 'T', 'C02060001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02060001', '한-호주 퇴직연금 포럼', 'Korea-Australia Retirement Pension Forum', NULL,
'2019년 금융투자협회·주한호주대사관이 공동 개최해 기금형 퇴직연금 도입, 디폴트옵션, 감독체계 등을 논의한 양국 포럼으로 기조발표-국가별 세션-패널토론으로 구성',
'4147179070a84d3887b97eb57085d850', 'T', 'C02060002 | finance/한-호주 퇴직연금 포럼_책자(최종).pdf. 시간표, 발표자, 축사 등 운영 절차를 README에 요약.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02060002', '호주 Superannuation 제도', 'Australian Superannuation System', NULL,
'호주의 의무적 직역연금을 뜻하며 고용주·근로자·정부가 적립하고 자산운용사가 투자, 세계 4위 수준의 연기금 자산과 높은 GDP 대비 비중을 갖춘 제도',
'T02060001', 'T', 'C02060002 | 동일 포럼 문건. 대사 환영사와 Garry Weaven 발표에서 1.9조 달러 규모, 고용주 강제부담금 구조, 글로벌 펀드 순위를 소개.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02060003', 'AIST 대표제 거버넌스', 'AIST Representative Governance', NULL,
'호주 퇴직연금 수탁자협회(AIST)가 비영리 산업·기업·공적 기금의 대표제 거버넌스 모델과 교육·CMSF 컨퍼런스를 통해 수탁자 역량을 지원하는 운영 체계',
'T02060001', 'T', 'C02060002 | finance/한-호주 퇴직연금 포럼_책자(최종).pdf. AIST CEO 발표가 소개한 대표제 모델, 회원 구성, CMSF 행사 정보를 기술.');

-- 02-07. 은행산업 경쟁·인가제도 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02070001', '지방은행 시중은행 전환', 'Regional Bank Conversion to Nationwide Bank', NULL,
'지방은행이 영업구역 제한을 해제하고 전국 단위 시중은행으로 전환하기 위한 절차와 조건',
'4147179070a84d3887b97eb57085d850', 'T', 'C02070002 | 금융위 2024.1.31 보도자료. 은행권 경쟁 촉진·영업구역 확대 맥락.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02070002', '인가내용 변경 방식', 'Authorization Change Method', NULL,
'은행법 제8조상 인가내용 변경 절차를 통해 기존 지방은행 인가를 유지한 채 시중은행으로 전환하는 방식',
'T02070001', 'T', 'C02070002 | 신규인가 대비 폐업인가 불요, 법적 불확실성 완화. 대주주/사업계획 등 모든 세부요건 재심사.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02070003', '예비인가 제도', 'Preliminary Authorization Regime', NULL,
'본인가 전 사업타당성을 점검해 불필요한 투자를 방지하는 제도로, 기존 지방은행 전환 시 신청인이 요청할 때만 적용',
'T02070001', 'T', 'C02070002 | 인적·물적설비 이미 갖춘 지방은행은 생략 가능하나 희망 시 진행. 2024.1.31 보도자료 근거.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02070004', '은행업 인가 세부심사요건', 'Detailed Bank Authorization Requirements', NULL,
'지방은행이 시중은행으로 전환할 때도 자본금·대주주·사업계획·임원·영업시설 등 모든 인가 세부요건을 신규인가 수준으로 다시 심사한다는 원칙',
'T02070001', 'T', 'C02070003 | finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf. 자본금 1천억, 대주주 출자능력, 내부통제 강화 항목을 표로 정리.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02070005', '외부평가위원회 심사절차', 'External Evaluation Committee Review', NULL,
'사업계획 타당성, 이해관계자 의견을 확인하기 위해 은행업감독규정 제7조에 따라 외부평가위원회를 구성·운영하고 심사결과를 인가에 반영하는 절차',
'T02070004', 'T', 'C02070003 | finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf. 영업범위 확대에 맞춰 평가위 생략 없이 진행하도록 명시.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02070006', '인가 심사중단사유 관리', 'Authorization Review Suspension Triggers', NULL,
'인가신청 이후 주주 관련 형사절차가 진행될 때만 심사중단사유가 적용되며, 금융사고가 임직원 위법행위에 한정되면 제재확정 전이라도 심사를 지속할 수 있도록 계획을 요구하는 절차',
'T02070004', 'T', 'C02070003 | finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf. 심사중단·임원 결격 사례 및 제재 대비 조치계획 제출 요구를 설명.');

-- 02-08. 지속가능·녹색금융 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02080001', '녹색금융', 'Green Finance', NULL,
'기후변화 대응을 위해 자원·에너지 효율을 높이는 경제활동에 민관 자금을 공급하고 탄소중립 전환을 촉진하는 금융정책·시장 관행',
'4147179070a84d3887b97eb57085d850', 'T', 'C02080001 | finance/WP22-05.pdf. FSB·BIS·IMF 등 국제기구 제도화, 국내 정책당국과 민간의 확대 필요성을 서술.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02080002', 'TCFD 권고안', 'TCFD Recommendations', NULL,
'금융안정위원회가 제시한 기후관련 재무정보공시 권고안으로, 글로벌 금융회사들이 투자대상 기업에 TCFD 기준 공시를 요구하며 녹색금융을 의무화하는 핵심 프레임',
'T02080001', 'T', 'C02080002 | finance/WP22-05.pdf. 2022년 1월 기준 2,990개 기관 지지, 미이행 기업 투자 철회 등 주주행동주의 사례 포함.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02080003', '한국형 녹색분류체계', 'Korean Green Taxonomy', NULL,
'환경부가 제시한 6대 환경목표와 DNSH, 최소 사회적 안전장치 기준을 충족하는 녹색경제활동을 정의한 분류체계로 녹색투자 평가 기준을 제공',
'T02080001', 'T', 'C02080002 | finance/WP22-05.pdf. 탄소중립·기후적응·물·사전오염예방·순환경제·생물다양성 기여 요건과 포함 기준을 상세화.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T02080004', '녹색금융 핸드북', 'Green Finance Handbook', NULL,
'은행연합회 등 5대 금융협회가 2021년 12월 공동 발간한 실무 지침서로 녹색금융 주요 개념, 가이드라인, 운영사례, 질의응답을 담아 금융사 실무를 지원',
'T02080001', 'T', 'C02080002 | finance/WP22-05.pdf. 2022년 3월 최종 발간 계획과 정보공개 표준(SASB 번역, ESG 플랫폼) 연계를 설명.');


------------------------------------------------------------
-- 03. 커머스 | Commerce
------------------------------------------------------------

-- 03-01. 이커머스 시장 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03010001', '이커머스', 'E-commerce', NULL,
'온라인 디지털 네트워크를 통해 상품과 서비스를 거래하는 전자상거래 방식',
'4147179070a84d3887b97eb57085d850', 'T', 'C03010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03010002', '온라인 마켓플레이스', 'Online Marketplace', NULL,
'다수의 판매자와 구매자가 거래하는 온라인 중개 플랫폼',
'4147179070a84d3887b97eb57085d850', 'T', 'C03010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03010003', 'D2C', 'Direct to Consumer', 'D2C',
'제조업체가 중간 유통단계 없이 소비자에게 직접 판매하는 비즈니스 모델',
'4147179070a84d3887b97eb57085d850', 'T', 'C03020001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03010004', '구독경제', 'Subscription Economy', NULL,
'일정 금액을 정기 결제하고 상품이나 서비스를 지속적으로 이용하는 경제 모델',
'4147179070a84d3887b97eb57085d850', 'T', 'C03020002');

-- 03-02. 라이브커머스 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03020001', '라이브커머스', 'Live Commerce', NULL,
'실시간 동영상 스트리밍을 통해 상품을 소개하고 판매하는 온라인 쇼핑 방식',
'4147179070a84d3887b97eb57085d850', 'T', 'C03030001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03020002', '라이브커머스 플랫폼', 'Live Commerce Platform', NULL,
'라이브커머스 서비스를 제공하는 온라인 플랫폼',
'4147179070a84d3887b97eb57085d850', 'T', 'C03030002');

-- 03-03. 소비자 행동 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03030001', '중고거래 플랫폼', 'Used-goods Marketplace', NULL,
'개인 간 중고물품 거래를 중개하는 온라인 플랫폼',
'4147179070a84d3887b97eb57085d850', 'T', 'C03040002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03030002', '라스트마일 배송', 'Last-mile Delivery', NULL,
'물류센터에서 최종 소비자까지 상품을 배송하는 마지막 구간의 배송 서비스',
'4147179070a84d3887b97eb57085d850', 'T', 'C03040003');

-- 03-04. 이커머스 솔루션 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03040001', '커머스 SaaS', 'Commerce SaaS', 'SaaS',
'이커머스 사업자에게 쇼핑몰 구축·운영 기능을 클라우드 기반으로 제공하는 서비스형 소프트웨어',
'4147179070a84d3887b97eb57085d850', 'T', 'C03060001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03040002', '마케팅 자동화', 'Marketing Automation', NULL,
'고객 데이터를 기반으로 마케팅 활동을 자동화하는 기술 및 솔루션',
'4147179070a84d3887b97eb57085d850', 'T', 'C03060002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03040003', '리뷰 솔루션', 'Review Solution', NULL,
'이커머스 상품 리뷰 수집·관리·분석을 지원하는 솔루션',
'4147179070a84d3887b97eb57085d850', 'T', 'C03060002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03040004', '체리슈머', 'Cherry-sumer', NULL,
'여러 이커머스 플랫폼에서 쿠폰·할인 등 혜택을 선별해 소비하는 가격 민감형 소비자 유형',
'4147179070a84d3887b97eb57085d850', 'T', 'C03040001 | 코로나19·고물가 시기 등장한 혜택 선별형 소비 트렌드. 소비자 후생·플랫폼 경쟁 맥락에서 등장하며 체리피커와 유사.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T03040005', '소비자 후생', 'Consumer Welfare', NULL,
'소비자가 시장에서 얻는 효용·편익 수준을 나타내는 개념으로 가격, 선택권, 품질, 편의성 등을 포괄',
'4147179070a84d3887b97eb57085d850', 'T', 'C03040001 | 이커머스 진화가 소비자 편익에 미치는 영향 분석 맥락에서 사용. 체리슈머·플랫폼 경쟁 논의와 함께 등장.');


------------------------------------------------------------
-- 04. 산업 | Industry
------------------------------------------------------------

-- 04-01. 디지털 경제 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T04010001', '디지털 경제', 'Digital Economy', NULL,
'디지털 기술과 데이터를 기반으로 가치가 창출되는 경제 구조',
'4147179070a84d3887b97eb57085d850', 'T', 'C04010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T04010002', '딥테크', 'Deep Tech', NULL,
'인공지능, 양자컴퓨팅, 바이오 등 과학적 발견이나 공학적 혁신에 기반한 기저기술',
'4147179070a84d3887b97eb57085d850', 'T', 'C04010002');

-- 04-02. 스타트업 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T04020001', '스타트업 생태계', 'Startup Ecosystem', NULL,
'창업기업, 투자자, 액셀러레이터, 정부 등이 상호작용하는 창업 환경 전체',
'4147179070a84d3887b97eb57085d850', 'T', 'C04020001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T04020002', '모태펀드', 'Fund of Funds', 'FoF',
'정부가 출자하여 민간 벤처캐피탈에 재출자하는 정책금융 펀드',
'4147179070a84d3887b97eb57085d850', 'T', 'C04020002');

-- 04-03. 소비 트렌드 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T04030001', '뉴 럭셔리', 'New Luxury', NULL,
'전통적 명품 개념을 넘어 개인의 가치와 경험을 중시하는 새로운 럭셔리 소비 트렌드',
'4147179070a84d3887b97eb57085d850', 'T', 'C04030002');


------------------------------------------------------------
-- 05. 사회 | Society
------------------------------------------------------------

-- 05-01. 고령화 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T05010001', '고령화사회·고령사회·초고령사회', 'Ageing Society / Aged Society / Super-aged Society', NULL,
'65세 이상 인구 비율에 따른 사회 분류 (7% 이상: 고령화사회, 14% 이상: 고령사회, 20% 이상: 초고령사회)',
'4147179070a84d3887b97eb57085d850', 'T', 'C05010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T05010002', '전기고령자·후기고령자', 'Young-old / Old-old', NULL,
'고령자를 연령대별로 세분화한 분류 (전기고령자: 65-74세, 후기고령자: 75세 이상)',
'4147179070a84d3887b97eb57085d850', 'T', 'C05010002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T05010003', '노노케어', 'Old-to-old Care', NULL,
'돌봄이 필요한 노인을 또 다른 고령자가 돌보는 방식으로, 일본 초고령사회에서 NPO와 결합해 고령자의 사회참여와 소비를 동시에 확대하는 모델',
'4147179070a84d3887b97eb57085d850', 'T', 'C05010003 | finance/KIFVIP2013-10.pdf. NPO법 이후 보건·복지 분야 NPO의 60%가 노노케어 등 돌봄 서비스를 제공한다고 서술.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T05010004', '보이지 않는 가족', 'Invisible Family', NULL,
'고령 부모와 기혼 자녀가 근거리에서 살며 경제적·정서적으로 상호 지원하는 가족형태로, 다세대 여행·군락형 아파트 등 새로운 소비수요를 만든다',
'4147179070a84d3887b97eb57085d850', 'T', 'C05010003 | finance/KIFVIP2013-10.pdf. 수도권 부모가 집을 매각하고 자녀 근처로 이주하는 사례와 Invisible Family 정의를 소개.');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T05010005', '유니버설 디자인 정책', 'Universal Design Policy', NULL,
'연령·장애와 무관하게 누구나 이용하기 쉬운 도시·생활환경을 설계하는 정책으로, 고령친화 건축·설계 산업을 촉진하는 초고령사회 대응 전략',
'4147179070a84d3887b97eb57085d850', 'T', 'C05010003 | finance/KIFVIP2013-10.pdf. 일본 정부가 유니버설 디자인 정책을 추진하며 관련 산업 성장을 견인한 사례를 설명.');

-- 05-02. 연금 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T05020001', '공적연금', 'Public Pension', NULL,
'국가가 운영하는 국민연금, 공무원연금 등 법정 연금제도',
'4147179070a84d3887b97eb57085d850', 'T', 'C05020001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T05020002', '연금라이프', 'Pension-based Life', NULL,
'연금 수입을 주요 소득원으로 하는 은퇴 후 생활 방식',
'4147179070a84d3887b97eb57085d850', 'T', 'C05020002');

-- 05-03. 노동·고용 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T05030001', '고령자 가계의 소득·지출 구조', 'Income and Expenditure Structure of Elderly Households', NULL,
'고령자 가구의 소득원 구성과 지출 패턴을 분석하는 사회경제적 지표',
'4147179070a84d3887b97eb57085d850', 'T', 'C05030001');


------------------------------------------------------------
-- 06. 법률 | Law
------------------------------------------------------------

-- 06-01. 판례·판결 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06010001', '판례', 'Precedent', NULL,
'법원이 구체적 사건에 대해 내린 판결로서 이후 유사 사건의 재판에 기준이 되는 선례',
'4147179070a84d3887b97eb57085d850', 'T', 'C06010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06010002', '대법원 판결', 'Supreme Court Decision', NULL,
'대법원이 상고심에서 내린 최종 판결로서 법령 해석의 통일적 기준 제시',
'4147179070a84d3887b97eb57085d850', 'T', 'C06010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06010003', '헌법재판소 결정', 'Constitutional Court Decision', NULL,
'헌법재판소가 위헌법률심판, 헌법소원 등에서 내린 결정',
'4147179070a84d3887b97eb57085d850', 'T', 'C06010001');

-- 06-02. 세법·조세 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06020001', '소득세', 'Income Tax', NULL,
'개인의 소득에 대해 부과되는 조세로 종합소득세, 양도소득세 등 포함',
'4147179070a84d3887b97eb57085d850', 'T', 'C06020001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06020002', '법인세', 'Corporate Tax', NULL,
'법인의 소득에 대해 부과되는 조세',
'4147179070a84d3887b97eb57085d850', 'T', 'C06020001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06020003', '부가가치세', 'Value Added Tax', 'VAT',
'재화나 용역의 공급 시 창출된 부가가치에 부과되는 간접세',
'4147179070a84d3887b97eb57085d850', 'T', 'C06020001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06020004', '상속세·증여세', 'Inheritance Tax / Gift Tax', NULL,
'상속이나 증여로 재산을 취득한 경우 부과되는 조세',
'4147179070a84d3887b97eb57085d850', 'T', 'C06020001');

-- 06-03. 공무원법·행정법 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06030001', '국가공무원법', 'State Public Officials Act', NULL,
'국가공무원의 임용, 복무, 신분보장 등을 규정한 법률',
'4147179070a84d3887b97eb57085d850', 'T', 'C06030001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T06030002', '행정절차법', 'Administrative Procedure Act', NULL,
'행정청의 처분, 신고, 입법예고 등 행정절차에 관한 공통사항을 규정한 법률',
'4147179070a84d3887b97eb57085d850', 'T', 'C06030001');


------------------------------------------------------------
-- 07. 의료 | Medical
------------------------------------------------------------

-- 07-01. 암·종양 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07010001', '암', 'Cancer', NULL,
'세포가 비정상적으로 증식하여 주변 조직을 침범하거나 전이하는 악성 종양',
'4147179070a84d3887b97eb57085d850', 'T', 'C07010001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07010002', '대장암', 'Colorectal Cancer', 'CRC',
'대장(결장과 직장)에 발생하는 악성 종양으로 한국인에게 흔한 암 중 하나',
'4147179070a84d3887b97eb57085d850', 'T', 'C07010002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07010003', '다발성골수종', 'Multiple Myeloma', 'MM',
'골수 내 형질세포가 비정상적으로 증식하는 혈액암의 일종',
'4147179070a84d3887b97eb57085d850', 'T', 'C07010003');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07010004', '항암화학요법', 'Chemotherapy', NULL,
'항암제를 사용하여 암세포를 파괴하거나 성장을 억제하는 치료법',
'4147179070a84d3887b97eb57085d850', 'T', 'C07010001');

-- 07-02. 안과 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07020001', '안구건조증', 'Dry Eye Syndrome', 'DES',
'눈물 분비 감소 또는 과도한 증발로 눈 표면이 손상되어 불편감을 유발하는 질환',
'4147179070a84d3887b97eb57085d850', 'T', 'C07020002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07020002', '백내장', 'Cataract', NULL,
'수정체가 혼탁해져 시력이 저하되는 안과 질환',
'4147179070a84d3887b97eb57085d850', 'T', 'C07020003');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07020003', '녹내장', 'Glaucoma', NULL,
'안압 상승 등으로 시신경이 손상되어 시야가 좁아지는 질환',
'4147179070a84d3887b97eb57085d850', 'T', 'C07020003');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07020004', '황반변성', 'Macular Degeneration', 'AMD',
'망막 중심부인 황반이 변성되어 중심 시력이 저하되는 질환',
'4147179070a84d3887b97eb57085d850', 'T', 'C07020003');

-- 07-03. 소화기 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07030001', '위식도역류질환', 'Gastroesophageal Reflux Disease', 'GERD',
'위 내용물이 식도로 역류하여 속쓰림, 역류 등 증상을 유발하는 질환',
'4147179070a84d3887b97eb57085d850', 'T', 'C07030002');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07030002', '내시경', 'Endoscopy', NULL,
'내시경 기구를 삽입하여 소화기관 내부를 관찰하고 진단·치료하는 시술',
'4147179070a84d3887b97eb57085d850', 'T', 'C07030001');

-- 07-04. 건강관리·예방 관련 용어
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07040001', '건강검진', 'Health Screening', NULL,
'질병의 조기 발견과 예방을 위해 정기적으로 실시하는 종합적인 건강 검사',
'4147179070a84d3887b97eb57085d850', 'T', 'C07040001');

INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, PRT_TERM_ID, TERM_TYPE, README)
VALUES ('T07040002', '예방의학', 'Preventive Medicine', NULL,
'질병 예방, 건강증진, 수명연장을 목적으로 하는 의학 분야',
'4147179070a84d3887b97eb57085d850', 'T', 'C07040001');
