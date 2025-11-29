// Auto-generated from mc_clsf.sql and mc_term.sql
CREATE CONSTRAINT class_id IF NOT EXISTS FOR (c:Class) REQUIRE c.id IS UNIQUE;
CREATE CONSTRAINT term_id IF NOT EXISTS FOR (t:Term) REQUIRE t.id IS UNIQUE;

MERGE (c:Class {id:'C01000001'})
SET c.name='공공', c.display_name='공공 (Class)', c.desc='공공 부문 정책 및 행정 전반을 다루는 최상위 분류', c.readme='도메인 01. 정부 정책, 지방행정, 디지털정부, 국가안전, 지방재정 등 공공부문 전반을 포괄. public/ 디렉토리 문서와 매핑.', c.group=true;

MERGE (c:Class {id:'C01010001'})
SET c.name='지방시대·지역균형발전', c.display_name='지방시대·지역균형발전 (Class)', c.desc='지방시대 정책과 지역균형발전을 다루는 분류', c.readme='중분류 01-01. 수도권 집중 완화, 지역 주도 발전, 인구감소지역 지원 정책 포함.', c.group=true;
MATCH (child:Class {id:'C01010001'}),(parent:Class {id:'C01000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01010002'})
SET c.name='인구감소지역·지방소멸 대응', c.display_name='인구감소지역·지방소멸 대응 (Class)', c.desc='인구감소지역 지원 및 지방소멸 대응 정책을 다루는 분류', c.readme='소분류. 인구감소지역 지원 특별법, 지방소멸대응기금 등 관련 정책.', c.group=false;
MATCH (child:Class {id:'C01010002'}),(parent:Class {id:'C01010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01020001'})
SET c.name='지방자치·행정체제 개편', c.display_name='지방자치·행정체제 개편 (Class)', c.desc='지방자치제도 및 행정체제 개편을 다루는 분류', c.readme='중분류 01-02. 지방자치법, 행정구역 개편, 자치분권 정책 포함.', c.group=true;
MATCH (child:Class {id:'C01020001'}),(parent:Class {id:'C01000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01020002'})
SET c.name='특별자치시·도', c.display_name='특별자치시·도 (Class)', c.desc='특별자치시 및 특별자치도 관련 제도를 다루는 분류', c.readme='소분류. 세종특별자치시, 제주특별자치도 등 특례 지방자치단체 관련.', c.group=false;
MATCH (child:Class {id:'C01020002'}),(parent:Class {id:'C01020001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01030001'})
SET c.name='디지털플랫폼정부', c.display_name='디지털플랫폼정부 (Class)', c.desc='디지털플랫폼정부 정책 전반을 다루는 분류', c.readme='중분류 01-03. 데이터·AI·클라우드 기반 공공서비스 혁신, 전자정부 고도화 포함.', c.group=true;
MATCH (child:Class {id:'C01030001'}),(parent:Class {id:'C01000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01030002'})
SET c.name='공공마이데이터·공공데이터', c.display_name='공공마이데이터·공공데이터 (Class)', c.desc='공공마이데이터 및 공공데이터 정책을 다루는 분류', c.readme='소분류. 개인정보 자기결정권, 공공데이터 개방·활용 정책.', c.group=false;
MATCH (child:Class {id:'C01030002'}),(parent:Class {id:'C01030001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01030003'})
SET c.name='AI기반 대국민 서비스', c.display_name='AI기반 대국민 서비스 (Class)', c.desc='AI 기반 대국민 서비스 정책을 다루는 분류', c.readme='소분류. 챗봇, 보이스피싱 탐지 등 AI 활용 공공서비스.', c.group=false;
MATCH (child:Class {id:'C01030003'}),(parent:Class {id:'C01030001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01040001'})
SET c.name='국가안전시스템 개편', c.display_name='국가안전시스템 개편 (Class)', c.desc='국가안전시스템 개편 정책을 다루는 분류', c.readme='중분류 01-04. 재난안전관리체계, 위기대응 훈련, 안전관리 정책 포함.', c.group=true;
MATCH (child:Class {id:'C01040001'}),(parent:Class {id:'C01000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01040002'})
SET c.name='다중밀집·인파 안전', c.display_name='다중밀집·인파 안전 (Class)', c.desc='다중밀집 장소 및 인파 안전관리를 다루는 분류', c.readme='소분류. 대규모 행사, 다중이용시설 안전관리 정책.', c.group=false;
MATCH (child:Class {id:'C01040002'}),(parent:Class {id:'C01040001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01050001'})
SET c.name='지방재정·교부세', c.display_name='지방재정·교부세 (Class)', c.desc='지방재정 및 지방교부세 정책을 다루는 분류', c.readme='중분류 01-05. 지방재정 건전성, 교부세 배분, 지방채 관리 포함.', c.group=true;
MATCH (child:Class {id:'C01050001'}),(parent:Class {id:'C01000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C01050002'})
SET c.name='고향사랑기부제', c.display_name='고향사랑기부제 (Class)', c.desc='고향사랑기부제 관련 정책을 다루는 분류', c.readme='소분류. 지방재정 확충을 위한 기부금 제도, 답례품 정책.', c.group=false;
MATCH (child:Class {id:'C01050002'}),(parent:Class {id:'C01050001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02000001'})
SET c.name='금융', c.display_name='금융 (Class)', c.desc='금융 정책 및 제도 전반을 다루는 최상위 분류', c.readme='도메인 02. 통화정책, 금융안정, 상생금융, 핀테크, 자본시장, 연금 등 금융부문 전반을 포괄. finance/ 디렉토리 문서와 매핑.', c.group=true;

MERGE (c:Class {id:'C02010001'})
SET c.name='통화정책·통화신용정책', c.display_name='통화정책·통화신용정책 (Class)', c.desc='통화정책 및 통화신용정책 전반을 다루는 분류', c.readme='중분류 02-01. 한국은행 통화정책, 금리정책, 유동성 관리 포함.', c.group=true;
MATCH (child:Class {id:'C02010001'}),(parent:Class {id:'C02000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02010002'})
SET c.name='기준금리 운영', c.display_name='기준금리 운영 (Class)', c.desc='기준금리 결정 및 운영을 다루는 분류', c.readme='소분류. 금융통화위원회 기준금리 결정, 금리 인상/인하 정책.', c.group=false;
MATCH (child:Class {id:'C02010002'}),(parent:Class {id:'C02010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02010003'})
SET c.name='금융중개지원대출·유동성조절', c.display_name='금융중개지원대출·유동성조절 (Class)', c.desc='금융중개지원대출 및 유동성조절을 다루는 분류', c.readme='소분류. 중소기업 지원 대출, 공개시장운영 등 유동성 관리 수단.', c.group=false;
MATCH (child:Class {id:'C02010003'}),(parent:Class {id:'C02010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02010004'})
SET c.name='공개시장운영·대상기관제도', c.display_name='공개시장운영·대상기관제도 (Class)', c.desc='한국은행 공개시장운영 규정 개정, 대상기관 선정기준, 입찰 제도 개선을 다루는 분류', c.readme='소분류. finance/2. 통화신용정책 운영.pdf. 2024.1.25 공개시장운영규정 개정으로 자산운용사·비은행중앙회 편입, RP 입찰 한도·증권 배정 변경, 단기금리 안정 장치 정리.', c.group=false;
MATCH (child:Class {id:'C02010004'}),(parent:Class {id:'C02010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02020001'})
SET c.name='금융안정·부동산PF', c.display_name='금융안정·부동산PF (Class)', c.desc='금융안정 및 부동산 PF 관련 정책을 다루는 분류', c.readme='중분류 02-02. 금융시스템 안정성, 부동산 프로젝트 파이낸싱 리스크 관리.', c.group=true;
MATCH (child:Class {id:'C02020001'}),(parent:Class {id:'C02000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02020002'})
SET c.name='가계부채·취약차주', c.display_name='가계부채·취약차주 (Class)', c.desc='가계부채 및 취약차주 관리 정책을 다루는 분류', c.readme='소분류. DSR 규제, 취약차주 보호, 가계부채 관리 정책.', c.group=false;
MATCH (child:Class {id:'C02020002'}),(parent:Class {id:'C02020001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02030001'})
SET c.name='상생금융·포용금융', c.display_name='상생금융·포용금융 (Class)', c.desc='상생금융 및 포용금융 정책을 다루는 분류', c.readme='중분류 02-03. 금융소외계층 지원, 금융기관 사회적 책임, 서민금융.', c.group=false;
MATCH (child:Class {id:'C02030001'}),(parent:Class {id:'C02000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02040001'})
SET c.name='핀테크·혁신금융', c.display_name='핀테크·혁신금융 (Class)', c.desc='핀테크 및 혁신금융 정책을 다루는 분류', c.readme='중분류 02-04. 디지털금융 혁신, 규제샌드박스, 오픈뱅킹 포함.', c.group=true;
MATCH (child:Class {id:'C02040001'}),(parent:Class {id:'C02000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02040002'})
SET c.name='핀테크 투자 생태계', c.display_name='핀테크 투자 생태계 (Class)', c.desc='핀테크 투자 및 생태계 조성을 다루는 분류', c.readme='소분류. 핀테크 스타트업 투자, 혁신펀드, 액셀러레이터.', c.group=false;
MATCH (child:Class {id:'C02040002'}),(parent:Class {id:'C02040001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02050001'})
SET c.name='자본시장·증시', c.display_name='자본시장·증시 (Class)', c.desc='자본시장 및 증시 관련 정책을 다루는 분류', c.readme='중분류 02-05. 주식시장, 채권시장, 투자자 보호, 기업공시 정책.', c.group=false;
MATCH (child:Class {id:'C02050001'}),(parent:Class {id:'C02000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02050002'})
SET c.name='투자자 커뮤니케이션·시장전망', c.display_name='투자자 커뮤니케이션·시장전망 (Class)', c.desc='투자자 대상 콘퍼런스, 리서치센터 전망 공유, 증시 콘서트 등 시장소통 행사를 다루는 분류', c.readme='소분류. finance/★2019 제1회 증시콘서트 자료집_최종★.pdf. 금융투자협회 주관 콘서트 구성, 리서치센터장 발표, 자산운용사 토론 체계 기록.', c.group=false;
MATCH (child:Class {id:'C02050002'}),(parent:Class {id:'C02050001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02060001'})
SET c.name='연금·노후자산', c.display_name='연금·노후자산 (Class)', c.desc='연금 및 노후자산 관리 정책을 다루는 분류', c.readme='중분류 02-06. 퇴직연금, 개인연금, 노후자산 운용 정책.', c.group=false;
MATCH (child:Class {id:'C02060001'}),(parent:Class {id:'C02000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02060002'})
SET c.name='기금형 퇴직연금 도입', c.display_name='기금형 퇴직연금 도입 (Class)', c.desc='기금형 퇴직연금 제도 설계, 국제 포럼 협력, 디폴트옵션 논의를 다루는 분류', c.readme='소분류. finance/한-호주 퇴직연금 포럼_책자(최종).pdf. 한-호주 공동포럼 아젠다, 기금형 거버넌스·운용 사례·규제 비교 포함.', c.group=false;
MATCH (child:Class {id:'C02060002'}),(parent:Class {id:'C02060001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02070001'})
SET c.name='은행산업 경쟁·인가제도', c.display_name='은행산업 경쟁·인가제도 (Class)', c.desc='은행 인가제도와 경쟁 촉진 정책을 다루는 분류', c.readme='중분류 02-07. 지방은행 시중은행 전환, 인가요건, 영업구역 규제 완화 등.', c.group=true;
MATCH (child:Class {id:'C02070001'}),(parent:Class {id:'C02000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02070002'})
SET c.name='지방은행 시중은행 전환', c.display_name='지방은행 시중은행 전환 (Class)', c.desc='지방은행이 전국 단위 시중은행으로 전환할 때 필요한 인가방식과 절차를 다루는 분류', c.readme='소분류. 은행법 제8조 인가내용 변경, 예비인가 생략 조건, 외부평가위원회 심사 포함.', c.group=false;
MATCH (child:Class {id:'C02070002'}),(parent:Class {id:'C02070001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02070003'})
SET c.name='은행 인가 심사·외부평가', c.display_name='은행 인가 심사·외부평가 (Class)', c.desc='은행업 인가 세부심사요건, 외부평가위원회 운영, 심사중단 요건을 다루는 분류', c.readme='소분류. finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf. 대주주·사업계획·내부통제 심사, 금융사고 대응 기준, 심사기한 명문화.', c.group=false;
MATCH (child:Class {id:'C02070003'}),(parent:Class {id:'C02070001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02080001'})
SET c.name='지속가능·녹색금융', c.display_name='지속가능·녹색금융 (Class)', c.desc='기후위기 대응을 위한 녹색금융 정책, 공시, 국제 협력 전반을 다루는 분류', c.readme='중분류 02-08. finance/WP22-05.pdf. 녹색금융 추진 배경, TCFD·BIS 움직임, 정책·민간 역할 포함.', c.group=true;
MATCH (child:Class {id:'C02080001'}),(parent:Class {id:'C02000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C02080002'})
SET c.name='녹색분류체계·TCFD 공시', c.display_name='녹색분류체계·TCFD 공시 (Class)', c.desc='한국형 녹색분류체계 기준, TCFD 권고안 기반 공시, 녹색금융 핸드북 등을 다루는 분류', c.readme='소분류. finance/WP22-05.pdf. 6대 환경목표와 DNSH 요건, 금융위·금감원·금융협회 추진 현황, 공시 로드맵 정리.', c.group=false;
MATCH (child:Class {id:'C02080002'}),(parent:Class {id:'C02080001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03000001'})
SET c.name='커머스', c.display_name='커머스 (Class)', c.desc='전자상거래 및 커머스 전반을 다루는 최상위 분류', c.readme='도메인 03. 이커머스 시장, 유통모델, 라이브커머스, 소비자행동, 물류, 솔루션 등 커머스 전반을 포괄. commerce/ 디렉토리 문서와 매핑.', c.group=true;

MERGE (c:Class {id:'C03010001'})
SET c.name='이커머스 시장·플랫폼', c.display_name='이커머스 시장·플랫폼 (Class)', c.desc='이커머스 시장 및 플랫폼 동향을 다루는 분류', c.readme='중분류 03-01. 온라인 쇼핑 시장 규모, 주요 플랫폼 경쟁구도 분석.', c.group=true;
MATCH (child:Class {id:'C03010001'}),(parent:Class {id:'C03000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03010002'})
SET c.name='글로벌 이커머스 시장', c.display_name='글로벌 이커머스 시장 (Class)', c.desc='글로벌 이커머스 시장 동향을 다루는 분류', c.readme='소분류. 아마존, 알리바바 등 글로벌 플랫폼, 크로스보더 이커머스.', c.group=false;
MATCH (child:Class {id:'C03010002'}),(parent:Class {id:'C03010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03010003'})
SET c.name='국내 이커머스 경쟁구도', c.display_name='국내 이커머스 경쟁구도 (Class)', c.desc='국내 이커머스 시장 경쟁구도를 다루는 분류', c.readme='소분류. 쿠팡, 네이버, SSG 등 국내 플랫폼 경쟁 분석.', c.group=false;
MATCH (child:Class {id:'C03010003'}),(parent:Class {id:'C03010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03020001'})
SET c.name='온라인 유통모델·D2C', c.display_name='온라인 유통모델·D2C (Class)', c.desc='온라인 유통모델 및 D2C를 다루는 분류', c.readme='중분류 03-02. 직접판매, 중개모델, 구독경제 등 유통 비즈니스 모델.', c.group=true;
MATCH (child:Class {id:'C03020001'}),(parent:Class {id:'C03000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03020002'})
SET c.name='D2C·구독경제', c.display_name='D2C·구독경제 (Class)', c.desc='D2C 및 구독경제 모델을 다루는 분류', c.readme='소분류. 브랜드 직접판매, 정기구독 서비스 비즈니스 모델.', c.group=false;
MATCH (child:Class {id:'C03020002'}),(parent:Class {id:'C03020001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03030001'})
SET c.name='라이브커머스·콘텐츠 커머스', c.display_name='라이브커머스·콘텐츠 커머스 (Class)', c.desc='라이브커머스 및 콘텐츠 커머스를 다루는 분류', c.readme='중분류 03-03. 실시간 방송 판매, 숏폼 콘텐츠 연계 커머스.', c.group=true;
MATCH (child:Class {id:'C03030001'}),(parent:Class {id:'C03000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03030002'})
SET c.name='라이브커머스 플랫폼', c.display_name='라이브커머스 플랫폼 (Class)', c.desc='라이브커머스 플랫폼 동향을 다루는 분류', c.readme='소분류. 네이버 쇼핑라이브, 카카오 쇼핑라이브, 그립 등 플랫폼.', c.group=false;
MATCH (child:Class {id:'C03030002'}),(parent:Class {id:'C03030001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03040001'})
SET c.name='소비자 행동·패턴 변화', c.display_name='소비자 행동·패턴 변화 (Class)', c.desc='소비자 행동 및 패턴 변화를 다루는 분류', c.readme='중분류 03-04. 온라인 소비 트렌드, 소비자 구매 여정 분석.', c.group=true;
MATCH (child:Class {id:'C03040001'}),(parent:Class {id:'C03000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03040002'})
SET c.name='중고거래 플랫폼', c.display_name='중고거래 플랫폼 (Class)', c.desc='중고거래 플랫폼 동향을 다루는 분류', c.readme='소분류. 당근마켓, 번개장터 등 C2C 중고거래 시장.', c.group=false;
MATCH (child:Class {id:'C03040002'}),(parent:Class {id:'C03040001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03040003'})
SET c.name='배달 플랫폼·라스트마일', c.display_name='배달 플랫폼·라스트마일 (Class)', c.desc='배달 플랫폼 및 라스트마일 배송을 다루는 분류', c.readme='소분류. 배달의민족, 쿠팡이츠 등 배달앱, 퀵커머스.', c.group=false;
MATCH (child:Class {id:'C03040003'}),(parent:Class {id:'C03040001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03050001'})
SET c.name='이커머스 물류·풀필먼트', c.display_name='이커머스 물류·풀필먼트 (Class)', c.desc='이커머스 물류 및 풀필먼트를 다루는 분류', c.readme='중분류 03-05. 물류센터, 당일배송, 새벽배송, 3PL/풀필먼트 서비스.', c.group=false;
MATCH (child:Class {id:'C03050001'}),(parent:Class {id:'C03000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03060001'})
SET c.name='이커머스 솔루션·SaaS', c.display_name='이커머스 솔루션·SaaS (Class)', c.desc='이커머스 솔루션 및 SaaS를 다루는 분류', c.readme='중분류 03-06. 쇼핑몰 구축, 주문관리, 결제 솔루션.', c.group=true;
MATCH (child:Class {id:'C03060001'}),(parent:Class {id:'C03000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C03060002'})
SET c.name='마케팅·리뷰·고객경험', c.display_name='마케팅·리뷰·고객경험 (Class)', c.desc='마케팅, 리뷰, 고객경험 솔루션을 다루는 분류', c.readme='소분류. CRM, 마케팅자동화, 리뷰관리, 개인화 솔루션.', c.group=false;
MATCH (child:Class {id:'C03060002'}),(parent:Class {id:'C03060001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C04000001'})
SET c.name='산업', c.display_name='산업 (Class)', c.desc='산업 정책 및 트렌드 전반을 다루는 최상위 분류', c.readme='도메인 04. 디지털경제, 스타트업, 소비트렌드, 미디어 등 산업 전반을 포괄.', c.group=true;

MERGE (c:Class {id:'C04010001'})
SET c.name='디지털 경제·플랫폼 경제', c.display_name='디지털 경제·플랫폼 경제 (Class)', c.desc='디지털 경제 및 플랫폼 경제를 다루는 분류', c.readme='중분류 04-01. 데이터 경제, 플랫폼 비즈니스, 디지털 전환.', c.group=true;
MATCH (child:Class {id:'C04010001'}),(parent:Class {id:'C04000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C04010002'})
SET c.name='딥테크·기저기술', c.display_name='딥테크·기저기술 (Class)', c.desc='딥테크 및 기저기술을 다루는 분류', c.readme='소분류. AI, 양자컴퓨팅, 바이오테크 등 핵심 기반기술.', c.group=false;
MATCH (child:Class {id:'C04010002'}),(parent:Class {id:'C04010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C04020001'})
SET c.name='신산업·스타트업 생태계', c.display_name='신산업·스타트업 생태계 (Class)', c.desc='신산업 및 스타트업 생태계를 다루는 분류', c.readme='중분류 04-02. 창업생태계, 벤처투자, 유니콘 기업.', c.group=true;
MATCH (child:Class {id:'C04020001'}),(parent:Class {id:'C04000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C04020002'})
SET c.name='벤처투자·모태펀드', c.display_name='벤처투자·모태펀드 (Class)', c.desc='벤처투자 및 모태펀드를 다루는 분류', c.readme='소분류. 정책금융, 벤처캐피탈, 액셀러레이터 투자.', c.group=false;
MATCH (child:Class {id:'C04020002'}),(parent:Class {id:'C04020001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C04030001'})
SET c.name='소비·라이프스타일 트렌드', c.display_name='소비·라이프스타일 트렌드 (Class)', c.desc='소비 및 라이프스타일 트렌드를 다루는 분류', c.readme='중분류 04-03. 소비자 가치관 변화, 라이프스타일 트렌드 분석.', c.group=true;
MATCH (child:Class {id:'C04030001'}),(parent:Class {id:'C04000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C04030002'})
SET c.name='뉴 럭셔리 비즈니스', c.display_name='뉴 럭셔리 비즈니스 (Class)', c.desc='뉴 럭셔리 비즈니스 트렌드를 다루는 분류', c.readme='소분류. MZ세대 럭셔리 소비, 경험 중심 프리미엄.', c.group=false;
MATCH (child:Class {id:'C04030002'}),(parent:Class {id:'C04030001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C04040001'})
SET c.name='미디어·콘텐츠·플랫폼', c.display_name='미디어·콘텐츠·플랫폼 (Class)', c.desc='미디어, 콘텐츠, 플랫폼 산업을 다루는 분류', c.readme='중분류 04-04. OTT, 숏폼, 크리에이터 이코노미, 미디어 플랫폼.', c.group=false;
MATCH (child:Class {id:'C04040001'}),(parent:Class {id:'C04000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C05000001'})
SET c.name='사회', c.display_name='사회 (Class)', c.desc='사회 구조 및 복지 전반을 다루는 최상위 분류', c.readme='도메인 05. 고령화, 인구구조, 사회보장, 노동·고용 등 사회부문 전반을 포괄.', c.group=true;

MERGE (c:Class {id:'C05010001'})
SET c.name='고령화·인구구조', c.display_name='고령화·인구구조 (Class)', c.desc='고령화 및 인구구조 변화를 다루는 분류', c.readme='중분류 05-01. 저출산·고령화, 인구감소, 인구구조 변화 분석.', c.group=true;
MATCH (child:Class {id:'C05010001'}),(parent:Class {id:'C05000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C05010002'})
SET c.name='고령자 세분화·초고령사회', c.display_name='고령자 세분화·초고령사회 (Class)', c.desc='고령자 세분화 및 초고령사회를 다루는 분류', c.readme='소분류. 전기고령자/후기고령자, 액티브시니어, 초고령사회 대응.', c.group=false;
MATCH (child:Class {id:'C05010002'}),(parent:Class {id:'C05010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C05010003'})
SET c.name='초고령사회 소비·돌봄', c.display_name='초고령사회 소비·돌봄 (Class)', c.desc='초고령사회에서의 소비패턴, 노노케어, 새로운 가족형태, 유니버설 디자인 정책을 다루는 분류', c.readme='소분류. finance/KIFVIP2013-10.pdf. 일본 초고령사회 사례, 노노케어 확산, Invisible Family, 유니버설 디자인 산업 육성 분석.', c.group=false;
MATCH (child:Class {id:'C05010003'}),(parent:Class {id:'C05010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C05020001'})
SET c.name='사회보장·연금', c.display_name='사회보장·연금 (Class)', c.desc='사회보장 및 연금 제도를 다루는 분류', c.readme='중분류 05-02. 국민연금, 건강보험, 기초연금 등 사회보장제도.', c.group=true;
MATCH (child:Class {id:'C05020001'}),(parent:Class {id:'C05000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C05020002'})
SET c.name='공적연금 의존도·연금라이프', c.display_name='공적연금 의존도·연금라이프 (Class)', c.desc='공적연금 의존도 및 연금라이프를 다루는 분류', c.readme='소분류. 노후소득원, 연금 의존도, 은퇴 후 생활패턴.', c.group=false;
MATCH (child:Class {id:'C05020002'}),(parent:Class {id:'C05020001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C05030001'})
SET c.name='노동·고용·고령자 일자리', c.display_name='노동·고용·고령자 일자리 (Class)', c.desc='노동, 고용, 고령자 일자리를 다루는 분류', c.readme='중분류 05-03. 고용정책, 고령자 재취업, 정년연장.', c.group=false;
MATCH (child:Class {id:'C05030001'}),(parent:Class {id:'C05000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C06000001'})
SET c.name='법률', c.display_name='법률 (Class)', c.desc='법률 및 판례 전반을 다루는 최상위 분류', c.readme='도메인 06. 판례, 세법, 행정법 등 법률부문 전반을 포괄. law/ 디렉토리 문서와 매핑.', c.group=true;

MERGE (c:Class {id:'C06010001'})
SET c.name='판례·판결', c.display_name='판례·판결 (Class)', c.desc='판례 및 판결 전반을 다루는 분류', c.readme='중분류 06-01. 대법원, 헌법재판소, 하급심 판례 분석.', c.group=true;
MATCH (child:Class {id:'C06010001'}),(parent:Class {id:'C06000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C06010002'})
SET c.name='민사 판례', c.display_name='민사 판례 (Class)', c.desc='민사 관련 판례를 다루는 분류', c.readme='소분류. 계약, 손해배상, 부동산, 가족법 관련 민사 판결.', c.group=false;
MATCH (child:Class {id:'C06010002'}),(parent:Class {id:'C06010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C06010003'})
SET c.name='행정 판례', c.display_name='행정 판례 (Class)', c.desc='행정 관련 판례를 다루는 분류', c.readme='소분류. 행정처분 취소, 과세처분 취소 등 행정소송 판결.', c.group=false;
MATCH (child:Class {id:'C06010003'}),(parent:Class {id:'C06010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C06010004'})
SET c.name='형사 판례', c.display_name='형사 판례 (Class)', c.desc='형사 관련 판례를 다루는 분류', c.readme='소분류. 형사범죄, 특별법 위반 관련 판결.', c.group=false;
MATCH (child:Class {id:'C06010004'}),(parent:Class {id:'C06010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C06020001'})
SET c.name='세법·조세', c.display_name='세법·조세 (Class)', c.desc='세법 및 조세 제도를 다루는 분류', c.readme='중분류 06-02. 소득세, 법인세, 부가가치세, 상속세 등 조세법.', c.group=true;
MATCH (child:Class {id:'C06020001'}),(parent:Class {id:'C06000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C06020002'})
SET c.name='세금제도 변경', c.display_name='세금제도 변경 (Class)', c.desc='세금제도 변경 및 개정을 다루는 분류', c.readme='소분류. 세법 개정, 세제 혜택, 조세특례.', c.group=false;
MATCH (child:Class {id:'C06020002'}),(parent:Class {id:'C06020001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C06030001'})
SET c.name='공무원법·행정법', c.display_name='공무원법·행정법 (Class)', c.desc='공무원법 및 행정법을 다루는 분류', c.readme='중분류 06-03. 국가공무원법, 지방공무원법, 행정절차법.', c.group=false;
MATCH (child:Class {id:'C06030001'}),(parent:Class {id:'C06000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07000001'})
SET c.name='의료', c.display_name='의료 (Class)', c.desc='의료 및 건강 전반을 다루는 최상위 분류', c.readme='도메인 07. 암, 안과, 소화기, 건강관리 등 의료부문 전반을 포괄. medical/ 디렉토리 문서와 매핑.', c.group=true;

MERGE (c:Class {id:'C07010001'})
SET c.name='암·종양', c.display_name='암·종양 (Class)', c.desc='암 및 종양 관련 질환을 다루는 분류', c.readme='중분류 07-01. 암 진단, 치료, 예방, 연구 전반.', c.group=true;
MATCH (child:Class {id:'C07010001'}),(parent:Class {id:'C07000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07010002'})
SET c.name='대장암', c.display_name='대장암 (Class)', c.desc='대장암 관련 의학을 다루는 분류', c.readme='소분류. 대장암 진단, 수술, 항암치료, 예후.', c.group=false;
MATCH (child:Class {id:'C07010002'}),(parent:Class {id:'C07010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07010003'})
SET c.name='다발성골수종', c.display_name='다발성골수종 (Class)', c.desc='다발성골수종 관련 의학을 다루는 분류', c.readme='소분류. 혈액암의 일종, 진단/치료/관리.', c.group=false;
MATCH (child:Class {id:'C07010003'}),(parent:Class {id:'C07010001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07020001'})
SET c.name='안과', c.display_name='안과 (Class)', c.desc='안과 질환 전반을 다루는 분류', c.readme='중분류 07-02. 눈 관련 질환, 시력교정, 안과수술.', c.group=true;
MATCH (child:Class {id:'C07020001'}),(parent:Class {id:'C07000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07020002'})
SET c.name='안구건조증', c.display_name='안구건조증 (Class)', c.desc='안구건조증 관련 의학을 다루는 분류', c.readme='소분류. 건성안 진단, 치료, 관리.', c.group=false;
MATCH (child:Class {id:'C07020002'}),(parent:Class {id:'C07020001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07020003'})
SET c.name='안과질환', c.display_name='안과질환 (Class)', c.desc='기타 안과질환을 다루는 분류', c.readme='소분류. 백내장, 녹내장, 망막질환 등.', c.group=false;
MATCH (child:Class {id:'C07020003'}),(parent:Class {id:'C07020001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07030001'})
SET c.name='소화기', c.display_name='소화기 (Class)', c.desc='소화기 질환 전반을 다루는 분류', c.readme='중분류 07-03. 위장관, 간, 담도, 췌장 질환.', c.group=true;
MATCH (child:Class {id:'C07030001'}),(parent:Class {id:'C07000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07030002'})
SET c.name='위식도역류질환', c.display_name='위식도역류질환 (Class)', c.desc='위식도역류질환 관련 의학을 다루는 분류', c.readme='소분류. GERD 진단, 치료, 생활관리.', c.group=false;
MATCH (child:Class {id:'C07030002'}),(parent:Class {id:'C07030001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (c:Class {id:'C07040001'})
SET c.name='건강관리·예방', c.display_name='건강관리·예방 (Class)', c.desc='건강관리 및 예방의학을 다루는 분류', c.readme='중분류 07-04. 건강검진, 예방접종, 생활습관 개선.', c.group=false;
MATCH (child:Class {id:'C07040001'}),(parent:Class {id:'C07000001'}) MERGE (child)-[:CHILD_OF]->(parent);

MERGE (t:Term {id:'T01010001'})
SET t.name='지방시대', t.display_name='지방시대 (Term)', t.desc='지역 주도의 균형발전을 통해 수도권 집중을 완화하고 지방이 자생력을 갖춘 시대를 지향하는 정책 기조', t.readme='C01010001', t.type='T', t.en='Local Era';
MATCH (term:Term {id:'T01010001'}),(clsf:Class {id:'C01010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01010002'})
SET t.name='지방시대위원회', t.display_name='지방시대위원회 (Term)', t.desc='지방시대 정책을 총괄 조정하는 대통령 소속 위원회', t.readme='C01010001', t.type='T', t.en='Presidential Committee for Local Era';
MATCH (term:Term {id:'T01010002'}),(clsf:Class {id:'C01010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01010003'})
SET t.name='인구감소지역 지원 특별법', t.display_name='인구감소지역 지원 특별법 (Term)', t.desc='인구감소로 인한 지방소멸 위험에 대응하기 위해 인구감소지역을 지정하고 재정·행정지원을 규정한 법률', t.readme='C01010002', t.type='T', t.en='Special Act on Support for Depopulation Areas';
MATCH (term:Term {id:'T01010003'}),(clsf:Class {id:'C01010002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01010004'})
SET t.name='지방소멸대응기금', t.display_name='지방소멸대응기금 (Term)', t.desc='인구감소와 고령화로 소멸위기에 처한 지역의 정주여건 개선과 일자리 창출을 위해 지원하는 재정지원 기금', t.readme='C01010002', t.type='T', t.en='Local Extinction Response Fund';
MATCH (term:Term {id:'T01010004'}),(clsf:Class {id:'C01010002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01020001'})
SET t.name='디지털플랫폼정부', t.display_name='디지털플랫폼정부 (Term)', t.desc='데이터·AI·클라우드를 기반으로 공공서비스를 통합·연계하여 국민이 맞춤형 서비스를 이용할 수 있도록 하는 정부 운영 패러다임', t.readme='C01030001', t.type='T', t.en='Digital Platform Government';
MATCH (term:Term {id:'T01020001'}),(clsf:Class {id:'C01030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01020002'})
SET t.name='공공마이데이터', t.display_name='공공마이데이터 (Term)', t.desc='개인이 공공기관에 분산된 본인 정보를 통합 조회·제공받고 민간서비스와 연계해 활용할 수 있도록 하는 공공 데이터 서비스 체계', t.readme='C01030002', t.type='T', t.en='Public MyData';
MATCH (term:Term {id:'T01020002'}),(clsf:Class {id:'C01030002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01020003'})
SET t.name='보이스피싱 음성분석 모델', t.display_name='보이스피싱 음성분석 모델 (Term)', t.desc='AI 기반으로 보이스피싱 통화를 실시간 탐지하는 음성분석 모델', t.readme='C01030003', t.type='T', t.en='Voice Phishing Detection Model';
MATCH (term:Term {id:'T01020003'}),(clsf:Class {id:'C01030003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01030001'})
SET t.name='국가안전시스템 개편 종합대책', t.display_name='국가안전시스템 개편 종합대책 (Term)', t.desc='재난·사고에 대비하고 대응하기 위한 국가 차원의 통합 재난안전관리체계 개편 종합대책', t.readme='C01040001', t.type='T', t.en='Comprehensive Plan for National Safety System Reform';
MATCH (term:Term {id:'T01030001'}),(clsf:Class {id:'C01040001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01030002'})
SET t.name='READY Korea 훈련', t.display_name='READY Korea 훈련 (Term)', t.desc='국가 재난대응역량 강화를 위한 범정부 합동 재난대응 훈련', t.readme='C01040001', t.type='T', t.en='READY Korea Drill';
MATCH (term:Term {id:'T01030002'}),(clsf:Class {id:'C01040001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01040001'})
SET t.name='고향사랑기부제', t.display_name='고향사랑기부제 (Term)', t.desc='개인이 자신의 주소지 외 지방자치단체에 기부하면 세액공제와 답례품을 받을 수 있는 제도', t.readme='C01050002', t.type='T', t.en='Hometown Love Donation Program';
MATCH (term:Term {id:'T01040001'}),(clsf:Class {id:'C01050002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T01040002'})
SET t.name='지방교부세', t.display_name='지방교부세 (Term)', t.desc='국세 수입의 일정 비율을 지방자치단체에 배분하여 지방재정의 균형을 도모하는 재원', t.readme='C01050001', t.type='T', t.en='Local Allocation Tax';
MATCH (term:Term {id:'T01040002'}),(clsf:Class {id:'C01050001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010001'})
SET t.name='기준금리', t.display_name='기준금리 (Term)', t.desc='중앙은행이 금융기관과의 거래에서 기준이 되는 정책금리로, 통화정책의 기조를 나타냄', t.readme='C02010002', t.type='T', t.en='Base Rate';
MATCH (term:Term {id:'T02010001'}),(clsf:Class {id:'C02010002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010002'})
SET t.name='금융중개지원대출', t.display_name='금융중개지원대출 (Term)', t.desc='중앙은행이 금융기관에 저리로 자금을 공급하여 중소기업 등에 대한 대출을 지원하는 제도', t.readme='C02010003', t.type='T', t.en='Bank Intermediated Lending Support Facility';
MATCH (term:Term {id:'T02010002'}),(clsf:Class {id:'C02010003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010003'})
SET t.name='공개시장운영', t.display_name='공개시장운영 (Term)', t.desc='중앙은행이 금융시장에서 유가증권을 매매하여 통화량과 금리를 조절하는 정책수단', t.readme='C02010001', t.type='T', t.en='Open Market Operations', t.acronym='OMO';
MATCH (term:Term {id:'T02010003'}),(clsf:Class {id:'C02010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010004'})
SET t.name='물가안정기 재진입', t.display_name='물가안정기 재진입 (Term)', t.desc='소비자물가와 근원물가가 목표 수준(2%) 부근으로 되돌아오는 과정에서 나타나는 정책 국면으로, 물가 둔화 추세와 리스크를 지속 점검하는 단계', t.readme='C02010001 | finance/3. 향후 통화신용정책 방향.pdf. 물가안정기 복귀 리스크·조건 설명.', t.type='T', t.en='Re-entry into Price Stability Phase';
MATCH (term:Term {id:'T02010004'}),(clsf:Class {id:'C02010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010005'})
SET t.name='근원물가', t.display_name='근원물가 (Term)', t.desc='에너지·농산물 등 변동성이 큰 품목을 제외해 기조적 물가 흐름을 측정하는 지표로 통화신용정책 판단의 핵심 참고지표', t.readme='C02010001 | 동일 문건에서 근원물가 상승률 전망(2.2%) 및 둔화 흐름 강조.', t.type='T', t.en='Core Inflation';
MATCH (child:Term {id:'T02010005'}),(parent:Term {id:'T02010004'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02010005'}),(clsf:Class {id:'C02010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010006'})
SET t.name='공개시장운영 대상기관 확대', t.display_name='공개시장운영 대상기관 확대 (Term)', t.desc='2024년 1월 25일 개정된 한국은행 공개시장운영규정으로 자산운용사, 농·수·산림·신협·새마을금고 중앙회, 상호저축은행 등이 대상기관에 편입되어 초단기금리 변동성을 직접 완화할 수 있게 된 제도', t.readme='C02010004 | finance/2. 통화신용정책 운영.pdf. MMF 수신 규모, 콜론 비중 반영한 평가항목과 재무건전성 요건을 명시.', t.type='T', t.en='Expanded OMO Counterparty Scope';
MATCH (term:Term {id:'T02010006'}),(clsf:Class {id:'C02010004'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010007'})
SET t.name='통화안정증권 발행', t.display_name='통화안정증권 발행 (Term)', t.desc='콜금리를 기준금리 수준에 묶어두기 위해 통화안정증권 발행잔액을 조절하는 한국은행의 대표적 흡수수단으로, 2023년 4분기에는 잔액을 3.4조원 줄여 지준공급 축소에 대응', t.readme='C02010004 | finance/2. 통화신용정책 운영.pdf. 통안증권 발행·대상기관 재선정 조건을 동시에 정비.', t.type='T', t.en='Monetary Stabilization Bond Issuance';
MATCH (term:Term {id:'T02010007'}),(clsf:Class {id:'C02010004'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010008'})
SET t.name='환매조건부증권 매입', t.display_name='환매조건부증권 매입 (Term)', t.desc='연말 자금 수급 불일치나 지준공급 축소 시 한국은행이 RP를 매입해 단기자금시장에 유동성을 공급하는 조치로, 2024년 1~2월 네 차례 집행되어 콜금리 상승을 억제', t.readme='C02010004 | finance/2. 통화신용정책 운영.pdf. 연말 MMF 환매, 화폐발행 증가에 맞춘 4차례 매입 사례 명시.', t.type='T', t.en='Repurchase Agreement Purchases', t.acronym='RP';
MATCH (term:Term {id:'T02010008'}),(clsf:Class {id:'C02010004'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02010009'})
SET t.name='통화안정계정 예치', t.display_name='통화안정계정 예치 (Term)', t.desc='시중 은행이 초과지준을 중앙은행에 예치해 유동성을 흡수하도록 하는 통화신용정책 수단으로, 통화안정증권·RP와 병행해 콜금리 상단을 관리', t.readme='C02010004 | finance/2. 통화신용정책 운영.pdf. 통안계정 예치 규모를 Q4에 5.4조원 줄였다가 2024년 1월 다시 0.5조원 늘린 경로 설명.', t.type='T', t.en='Monetary Stabilization Account Deposit';
MATCH (term:Term {id:'T02010009'}),(clsf:Class {id:'C02010004'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02020001'})
SET t.name='부동산 PF 대출', t.display_name='부동산 PF 대출 (Term)', t.desc='부동산 개발사업의 미래 수익을 담보로 사업비를 조달하는 금융기법', t.readme='C02020001', t.type='T', t.en='Real Estate Project Financing Loan', t.acronym='PF';
MATCH (term:Term {id:'T02020001'}),(clsf:Class {id:'C02020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02020002'})
SET t.name='금융안정', t.display_name='금융안정 (Term)', t.desc='금융시스템이 충격에도 불구하고 금융중개 기능을 안정적으로 수행할 수 있는 상태', t.readme='C02020001', t.type='T', t.en='Financial Stability';
MATCH (term:Term {id:'T02020002'}),(clsf:Class {id:'C02020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02030001'})
SET t.name='상생금융', t.display_name='상생금융 (Term)', t.desc='금융기관이 취약계층·중소기업 지원 등을 통해 사회적 책임을 이행하는 금융', t.readme='C02030001', t.type='T', t.en='Mutual Growth Finance';
MATCH (term:Term {id:'T02030001'}),(clsf:Class {id:'C02030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02030002'})
SET t.name='포용금융', t.display_name='포용금융 (Term)', t.desc='금융 소외계층도 적정 비용으로 금융서비스를 이용할 수 있도록 하는 금융정책', t.readme='C02030001', t.type='T', t.en='Inclusive Finance';
MATCH (term:Term {id:'T02030002'}),(clsf:Class {id:'C02030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02030003'})
SET t.name='소상공인 금리부담경감 3종 세트', t.display_name='소상공인 금리부담경감 3종 세트 (Term)', t.desc='은행·중소금융권 이자환급, 저금리 대환 프로그램 등 소상공인 금리 부담을 낮추기 위한 3단계 패키지 지원방안', t.readme='C02030001 | 2024.3 금융위·금융권 발표 보도자료(상생금융 추진현황). 총 2.4조원 규모 환급·대환 중심.', t.type='T', t.en='Small Business Interest Relief Package';
MATCH (term:Term {id:'T02030003'}),(clsf:Class {id:'C02030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02030004'})
SET t.name='저금리 대환 프로그램', t.display_name='저금리 대환 프로그램 (Term)', t.desc='신용보증기금 보증을 통해 고금리 대출을 저금리로 갈아탈 수 있도록 지원 범위를 확대한 대환 프로그램', t.readme='C02030001 | 소상공인 금리부담경감 3종 세트 구성요소. 2023.5.31 취급분까지 대상 확대, 금리상한·보증료 인하 포함.', t.type='T', t.en='Low-interest Refinancing Program';
MATCH (term:Term {id:'T02030004'}),(clsf:Class {id:'C02030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02040001'})
SET t.name='핀테크', t.display_name='핀테크 (Term)', t.desc='금융(Finance)과 기술(Technology)의 합성어로, 디지털 기술을 활용한 혁신적 금융서비스', t.readme='C02040001', t.type='T', t.en='Fintech';
MATCH (term:Term {id:'T02040001'}),(clsf:Class {id:'C02040001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02040002'})
SET t.name='핀테크 혁신펀드', t.display_name='핀테크 혁신펀드 (Term)', t.desc='핀테크 스타트업 육성을 위한 정책금융 투자펀드', t.readme='C02040002', t.type='T', t.en='Fintech Innovation Fund';
MATCH (term:Term {id:'T02040002'}),(clsf:Class {id:'C02040002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02040003'})
SET t.name='핀테크 혁신펀드 1호', t.display_name='핀테크 혁신펀드 1호 (Term)', t.desc='2020~2023년 조성된 1호 펀드로 총 5,133억원을 모아 85개 핀테크 스타트업에 2,824억원을 공급한 모펀드', t.readme='C02040002 | 금융위 2024.4.9 핀테크 투자생태계 간담회 보도자료. 은행권·성장사다리 자금이 참여.', t.type='T', t.en='Fintech Innovation Fund I';
MATCH (child:Term {id:'T02040003'}),(parent:Term {id:'T02040002'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02040003'}),(clsf:Class {id:'C02040002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02040004'})
SET t.name='핀테크 혁신펀드 2호', t.display_name='핀테크 혁신펀드 2호 (Term)', t.desc='2024~2027년 추가로 5,000억원을 조성해 총 1조원 규모로 확대하는 후속 모펀드. 성장단계별 맞춤 투자를 추진', t.readme='C02040002 | 빅테크(네이버파이낸셜·카카오페이) 출자, 초기·사업화·해외진출 단계별 투자계획.', t.type='T', t.en='Fintech Innovation Fund II';
MATCH (child:Term {id:'T02040004'}),(parent:Term {id:'T02040002'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02040004'}),(clsf:Class {id:'C02040002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02040005'})
SET t.name='핀테크 투자생태계 활성화', t.display_name='핀테크 투자생태계 활성화 (Term)', t.desc='핀테크 기업 투자 위축에 대응해 혁신펀드 확대, 규제샌드박스 내실화, 해외진출·정책금융 지원 등을 추진하는 정책 방향', t.readme='C02040001 | 금융위 김소영 부위원장 2024.4.9 발언 요지. 투자기관·핀테크 기업 간 협업과 후속투자 연계 강조.', t.type='T', t.en='Fintech Investment Ecosystem Activation';
MATCH (term:Term {id:'T02040005'}),(clsf:Class {id:'C02040001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02050004'})
SET t.name='증시 콘서트', t.display_name='증시 콘서트 (Term)', t.desc='2019년 7월 2일 금융투자협회 불스홀에서 열린 제1회 증시 콘서트로, 증권사 리서치센터장 4인과 자산운용사 경영진이 하반기 시장전망을 공유한 투자자 커뮤니케이션 행사', t.readme='C02050002 | finance/★2019 제1회 증시콘서트 자료집_최종★.pdf. 진행순서·발표자 명단·토론 패널 구성 기술.', t.type='T', t.en='Capital Market Concert';
MATCH (term:Term {id:'T02050004'}),(clsf:Class {id:'C02050002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02050005'})
SET t.name='하반기 증시 대전망 세션', t.display_name='하반기 증시 대전망 세션 (Term)', t.desc='증시 콘서트 1부(14:40~15:40)에서 삼성·하나·SK·NH 리서치센터장이 국내외 경제·업종별 전망과 투자전략을 발표하는 세션', t.readme='C02050002 | finance/★2019 제1회 증시콘서트 자료집_최종★.pdf. 세션 시간표와 발언자 역할을 그대로 옮겨 투자자 설명자료로 사용.', t.type='T', t.en='H2 Market Outlook Session';
MATCH (child:Term {id:'T02050005'}),(parent:Term {id:'T02050004'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02050005'}),(clsf:Class {id:'C02050002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02050001'})
SET t.name='퇴직연금', t.display_name='퇴직연금 (Term)', t.desc='근로자의 노후소득 보장을 위해 사용자가 급여나 부담금을 적립하고, 퇴직 시 연금 또는 일시금으로 수령하는 제도', t.readme='C02060001', t.type='T', t.en='Retirement Pension';
MATCH (term:Term {id:'T02050001'}),(clsf:Class {id:'C02060001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02050002'})
SET t.name='기금형 퇴직연금', t.display_name='기금형 퇴직연금 (Term)', t.desc='퇴직연금 적립금을 별도의 기금으로 운용하여 전문성과 수익률을 높이는 퇴직연금 운용방식', t.readme='C02060001', t.type='T', t.en='Fund-type Retirement Pension';
MATCH (term:Term {id:'T02050002'}),(clsf:Class {id:'C02060001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02050003'})
SET t.name='고령화와 금융자산 운용', t.display_name='고령화와 금융자산 운용 (Term)', t.desc='고령화 사회에서 노후자산의 효율적 운용과 관련된 금융정책 및 연구', t.readme='C02060001', t.type='T', t.en='Ageing and Financial Asset Management';
MATCH (term:Term {id:'T02050003'}),(clsf:Class {id:'C02060001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02060001'})
SET t.name='한-호주 퇴직연금 포럼', t.display_name='한-호주 퇴직연금 포럼 (Term)', t.desc='2019년 금융투자협회·주한호주대사관이 공동 개최해 기금형 퇴직연금 도입, 디폴트옵션, 감독체계 등을 논의한 양국 포럼으로 기조발표-국가별 세션-패널토론으로 구성', t.readme='C02060002 | finance/한-호주 퇴직연금 포럼_책자(최종).pdf. 시간표, 발표자, 축사 등 운영 절차를 README에 요약.', t.type='T', t.en='Korea-Australia Retirement Pension Forum';
MATCH (term:Term {id:'T02060001'}),(clsf:Class {id:'C02060002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02060002'})
SET t.name='호주 Superannuation 제도', t.display_name='호주 Superannuation 제도 (Term)', t.desc='호주의 의무적 직역연금을 뜻하며 고용주·근로자·정부가 적립하고 자산운용사가 투자, 세계 4위 수준의 연기금 자산과 높은 GDP 대비 비중을 갖춘 제도', t.readme='C02060002 | 동일 포럼 문건. 대사 환영사와 Garry Weaven 발표에서 1.9조 달러 규모, 고용주 강제부담금 구조, 글로벌 펀드 순위를 소개.', t.type='T', t.en='Australian Superannuation System';
MATCH (child:Term {id:'T02060002'}),(parent:Term {id:'T02060001'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02060002'}),(clsf:Class {id:'C02060002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02060003'})
SET t.name='AIST 대표제 거버넌스', t.display_name='AIST 대표제 거버넌스 (Term)', t.desc='호주 퇴직연금 수탁자협회(AIST)가 비영리 산업·기업·공적 기금의 대표제 거버넌스 모델과 교육·CMSF 컨퍼런스를 통해 수탁자 역량을 지원하는 운영 체계', t.readme='C02060002 | finance/한-호주 퇴직연금 포럼_책자(최종).pdf. AIST CEO 발표가 소개한 대표제 모델, 회원 구성, CMSF 행사 정보를 기술.', t.type='T', t.en='AIST Representative Governance';
MATCH (child:Term {id:'T02060003'}),(parent:Term {id:'T02060001'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02060003'}),(clsf:Class {id:'C02060002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02070001'})
SET t.name='지방은행 시중은행 전환', t.display_name='지방은행 시중은행 전환 (Term)', t.desc='지방은행이 영업구역 제한을 해제하고 전국 단위 시중은행으로 전환하기 위한 절차와 조건', t.readme='C02070002 | 금융위 2024.1.31 보도자료. 은행권 경쟁 촉진·영업구역 확대 맥락.', t.type='T', t.en='Regional Bank Conversion to Nationwide Bank';
MATCH (term:Term {id:'T02070001'}),(clsf:Class {id:'C02070002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02070002'})
SET t.name='인가내용 변경 방식', t.display_name='인가내용 변경 방식 (Term)', t.desc='은행법 제8조상 인가내용 변경 절차를 통해 기존 지방은행 인가를 유지한 채 시중은행으로 전환하는 방식', t.readme='C02070002 | 신규인가 대비 폐업인가 불요, 법적 불확실성 완화. 대주주/사업계획 등 모든 세부요건 재심사.', t.type='T', t.en='Authorization Change Method';
MATCH (child:Term {id:'T02070002'}),(parent:Term {id:'T02070001'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02070002'}),(clsf:Class {id:'C02070002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02070003'})
SET t.name='예비인가 제도', t.display_name='예비인가 제도 (Term)', t.desc='본인가 전 사업타당성을 점검해 불필요한 투자를 방지하는 제도로, 기존 지방은행 전환 시 신청인이 요청할 때만 적용', t.readme='C02070002 | 인적·물적설비 이미 갖춘 지방은행은 생략 가능하나 희망 시 진행. 2024.1.31 보도자료 근거.', t.type='T', t.en='Preliminary Authorization Regime';
MATCH (child:Term {id:'T02070003'}),(parent:Term {id:'T02070001'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02070003'}),(clsf:Class {id:'C02070002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02070004'})
SET t.name='은행업 인가 세부심사요건', t.display_name='은행업 인가 세부심사요건 (Term)', t.desc='지방은행이 시중은행으로 전환할 때도 자본금·대주주·사업계획·임원·영업시설 등 모든 인가 세부요건을 신규인가 수준으로 다시 심사한다는 원칙', t.readme='C02070003 | finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf. 자본금 1천억, 대주주 출자능력, 내부통제 강화 항목을 표로 정리.', t.type='T', t.en='Detailed Bank Authorization Requirements';
MATCH (child:Term {id:'T02070004'}),(parent:Term {id:'T02070001'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02070004'}),(clsf:Class {id:'C02070003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02070005'})
SET t.name='외부평가위원회 심사절차', t.display_name='외부평가위원회 심사절차 (Term)', t.desc='사업계획 타당성, 이해관계자 의견을 확인하기 위해 은행업감독규정 제7조에 따라 외부평가위원회를 구성·운영하고 심사결과를 인가에 반영하는 절차', t.readme='C02070003 | finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf. 영업범위 확대에 맞춰 평가위 생략 없이 진행하도록 명시.', t.type='T', t.en='External Evaluation Committee Review';
MATCH (child:Term {id:'T02070005'}),(parent:Term {id:'T02070004'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02070005'}),(clsf:Class {id:'C02070003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02070006'})
SET t.name='인가 심사중단사유 관리', t.display_name='인가 심사중단사유 관리 (Term)', t.desc='인가신청 이후 주주 관련 형사절차가 진행될 때만 심사중단사유가 적용되며, 금융사고가 임직원 위법행위에 한정되면 제재확정 전이라도 심사를 지속할 수 있도록 계획을 요구하는 절차', t.readme='C02070003 | finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf. 심사중단·임원 결격 사례 및 제재 대비 조치계획 제출 요구를 설명.', t.type='T', t.en='Authorization Review Suspension Triggers';
MATCH (child:Term {id:'T02070006'}),(parent:Term {id:'T02070004'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02070006'}),(clsf:Class {id:'C02070003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02080001'})
SET t.name='녹색금융', t.display_name='녹색금융 (Term)', t.desc='기후변화 대응을 위해 자원·에너지 효율을 높이는 경제활동에 민관 자금을 공급하고 탄소중립 전환을 촉진하는 금융정책·시장 관행', t.readme='C02080001 | finance/WP22-05.pdf. FSB·BIS·IMF 등 국제기구 제도화, 국내 정책당국과 민간의 확대 필요성을 서술.', t.type='T', t.en='Green Finance';
MATCH (term:Term {id:'T02080001'}),(clsf:Class {id:'C02080001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02080002'})
SET t.name='TCFD 권고안', t.display_name='TCFD 권고안 (Term)', t.desc='금융안정위원회가 제시한 기후관련 재무정보공시 권고안으로, 글로벌 금융회사들이 투자대상 기업에 TCFD 기준 공시를 요구하며 녹색금융을 의무화하는 핵심 프레임', t.readme='C02080002 | finance/WP22-05.pdf. 2022년 1월 기준 2,990개 기관 지지, 미이행 기업 투자 철회 등 주주행동주의 사례 포함.', t.type='T', t.en='TCFD Recommendations';
MATCH (child:Term {id:'T02080002'}),(parent:Term {id:'T02080001'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02080002'}),(clsf:Class {id:'C02080002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02080003'})
SET t.name='한국형 녹색분류체계', t.display_name='한국형 녹색분류체계 (Term)', t.desc='환경부가 제시한 6대 환경목표와 DNSH, 최소 사회적 안전장치 기준을 충족하는 녹색경제활동을 정의한 분류체계로 녹색투자 평가 기준을 제공', t.readme='C02080002 | finance/WP22-05.pdf. 탄소중립·기후적응·물·사전오염예방·순환경제·생물다양성 기여 요건과 포함 기준을 상세화.', t.type='T', t.en='Korean Green Taxonomy';
MATCH (child:Term {id:'T02080003'}),(parent:Term {id:'T02080001'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02080003'}),(clsf:Class {id:'C02080002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T02080004'})
SET t.name='녹색금융 핸드북', t.display_name='녹색금융 핸드북 (Term)', t.desc='은행연합회 등 5대 금융협회가 2021년 12월 공동 발간한 실무 지침서로 녹색금융 주요 개념, 가이드라인, 운영사례, 질의응답을 담아 금융사 실무를 지원', t.readme='C02080002 | finance/WP22-05.pdf. 2022년 3월 최종 발간 계획과 정보공개 표준(SASB 번역, ESG 플랫폼) 연계를 설명.', t.type='T', t.en='Green Finance Handbook';
MATCH (child:Term {id:'T02080004'}),(parent:Term {id:'T02080001'}) MERGE (child)-[:TERM_CHILD_OF]->(parent);
MATCH (term:Term {id:'T02080004'}),(clsf:Class {id:'C02080002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03010001'})
SET t.name='이커머스', t.display_name='이커머스 (Term)', t.desc='온라인 디지털 네트워크를 통해 상품과 서비스를 거래하는 전자상거래 방식', t.readme='C03010001', t.type='T', t.en='E-commerce';
MATCH (term:Term {id:'T03010001'}),(clsf:Class {id:'C03010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03010002'})
SET t.name='온라인 마켓플레이스', t.display_name='온라인 마켓플레이스 (Term)', t.desc='다수의 판매자와 구매자가 거래하는 온라인 중개 플랫폼', t.readme='C03010001', t.type='T', t.en='Online Marketplace';
MATCH (term:Term {id:'T03010002'}),(clsf:Class {id:'C03010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03010003'})
SET t.name='D2C', t.display_name='D2C (Term)', t.desc='제조업체가 중간 유통단계 없이 소비자에게 직접 판매하는 비즈니스 모델', t.readme='C03020001', t.type='T', t.en='Direct to Consumer', t.acronym='D2C';
MATCH (term:Term {id:'T03010003'}),(clsf:Class {id:'C03020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03010004'})
SET t.name='구독경제', t.display_name='구독경제 (Term)', t.desc='일정 금액을 정기 결제하고 상품이나 서비스를 지속적으로 이용하는 경제 모델', t.readme='C03020002', t.type='T', t.en='Subscription Economy';
MATCH (term:Term {id:'T03010004'}),(clsf:Class {id:'C03020002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03020001'})
SET t.name='라이브커머스', t.display_name='라이브커머스 (Term)', t.desc='실시간 동영상 스트리밍을 통해 상품을 소개하고 판매하는 온라인 쇼핑 방식', t.readme='C03030001', t.type='T', t.en='Live Commerce';
MATCH (term:Term {id:'T03020001'}),(clsf:Class {id:'C03030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03020002'})
SET t.name='라이브커머스 플랫폼', t.display_name='라이브커머스 플랫폼 (Term)', t.desc='라이브커머스 서비스를 제공하는 온라인 플랫폼', t.readme='C03030002', t.type='T', t.en='Live Commerce Platform';
MATCH (term:Term {id:'T03020002'}),(clsf:Class {id:'C03030002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03030001'})
SET t.name='중고거래 플랫폼', t.display_name='중고거래 플랫폼 (Term)', t.desc='개인 간 중고물품 거래를 중개하는 온라인 플랫폼', t.readme='C03040002', t.type='T', t.en='Used-goods Marketplace';
MATCH (term:Term {id:'T03030001'}),(clsf:Class {id:'C03040002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03030002'})
SET t.name='라스트마일 배송', t.display_name='라스트마일 배송 (Term)', t.desc='물류센터에서 최종 소비자까지 상품을 배송하는 마지막 구간의 배송 서비스', t.readme='C03040003', t.type='T', t.en='Last-mile Delivery';
MATCH (term:Term {id:'T03030002'}),(clsf:Class {id:'C03040003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03040001'})
SET t.name='커머스 SaaS', t.display_name='커머스 SaaS (Term)', t.desc='이커머스 사업자에게 쇼핑몰 구축·운영 기능을 클라우드 기반으로 제공하는 서비스형 소프트웨어', t.readme='C03060001', t.type='T', t.en='Commerce SaaS', t.acronym='SaaS';
MATCH (term:Term {id:'T03040001'}),(clsf:Class {id:'C03060001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03040002'})
SET t.name='마케팅 자동화', t.display_name='마케팅 자동화 (Term)', t.desc='고객 데이터를 기반으로 마케팅 활동을 자동화하는 기술 및 솔루션', t.readme='C03060002', t.type='T', t.en='Marketing Automation';
MATCH (term:Term {id:'T03040002'}),(clsf:Class {id:'C03060002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03040003'})
SET t.name='리뷰 솔루션', t.display_name='리뷰 솔루션 (Term)', t.desc='이커머스 상품 리뷰 수집·관리·분석을 지원하는 솔루션', t.readme='C03060002', t.type='T', t.en='Review Solution';
MATCH (term:Term {id:'T03040003'}),(clsf:Class {id:'C03060002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03040004'})
SET t.name='체리슈머', t.display_name='체리슈머 (Term)', t.desc='여러 이커머스 플랫폼에서 쿠폰·할인 등 혜택을 선별해 소비하는 가격 민감형 소비자 유형', t.readme='C03040001 | 코로나19·고물가 시기 등장한 혜택 선별형 소비 트렌드. 소비자 후생·플랫폼 경쟁 맥락에서 등장하며 체리피커와 유사.', t.type='T', t.en='Cherry-sumer';
MATCH (term:Term {id:'T03040004'}),(clsf:Class {id:'C03040001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T03040005'})
SET t.name='소비자 후생', t.display_name='소비자 후생 (Term)', t.desc='소비자가 시장에서 얻는 효용·편익 수준을 나타내는 개념으로 가격, 선택권, 품질, 편의성 등을 포괄', t.readme='C03040001 | 이커머스 진화가 소비자 편익에 미치는 영향 분석 맥락에서 사용. 체리슈머·플랫폼 경쟁 논의와 함께 등장.', t.type='T', t.en='Consumer Welfare';
MATCH (term:Term {id:'T03040005'}),(clsf:Class {id:'C03040001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T04010001'})
SET t.name='디지털 경제', t.display_name='디지털 경제 (Term)', t.desc='디지털 기술과 데이터를 기반으로 가치가 창출되는 경제 구조', t.readme='C04010001', t.type='T', t.en='Digital Economy';
MATCH (term:Term {id:'T04010001'}),(clsf:Class {id:'C04010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T04010002'})
SET t.name='딥테크', t.display_name='딥테크 (Term)', t.desc='인공지능, 양자컴퓨팅, 바이오 등 과학적 발견이나 공학적 혁신에 기반한 기저기술', t.readme='C04010002', t.type='T', t.en='Deep Tech';
MATCH (term:Term {id:'T04010002'}),(clsf:Class {id:'C04010002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T04020001'})
SET t.name='스타트업 생태계', t.display_name='스타트업 생태계 (Term)', t.desc='창업기업, 투자자, 액셀러레이터, 정부 등이 상호작용하는 창업 환경 전체', t.readme='C04020001', t.type='T', t.en='Startup Ecosystem';
MATCH (term:Term {id:'T04020001'}),(clsf:Class {id:'C04020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T04020002'})
SET t.name='모태펀드', t.display_name='모태펀드 (Term)', t.desc='정부가 출자하여 민간 벤처캐피탈에 재출자하는 정책금융 펀드', t.readme='C04020002', t.type='T', t.en='Fund of Funds', t.acronym='FoF';
MATCH (term:Term {id:'T04020002'}),(clsf:Class {id:'C04020002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T04030001'})
SET t.name='뉴 럭셔리', t.display_name='뉴 럭셔리 (Term)', t.desc='전통적 명품 개념을 넘어 개인의 가치와 경험을 중시하는 새로운 럭셔리 소비 트렌드', t.readme='C04030002', t.type='T', t.en='New Luxury';
MATCH (term:Term {id:'T04030001'}),(clsf:Class {id:'C04030002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T05010001'})
SET t.name='고령화사회·고령사회·초고령사회', t.display_name='고령화사회·고령사회·초고령사회 (Term)', t.desc='65세 이상 인구 비율에 따른 사회 분류 (7% 이상: 고령화사회, 14% 이상: 고령사회, 20% 이상: 초고령사회)', t.readme='C05010001', t.type='T', t.en='Ageing Society / Aged Society / Super-aged Society';
MATCH (term:Term {id:'T05010001'}),(clsf:Class {id:'C05010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T05010002'})
SET t.name='전기고령자·후기고령자', t.display_name='전기고령자·후기고령자 (Term)', t.desc='고령자를 연령대별로 세분화한 분류 (전기고령자: 65-74세, 후기고령자: 75세 이상)', t.readme='C05010002', t.type='T', t.en='Young-old / Old-old';
MATCH (term:Term {id:'T05010002'}),(clsf:Class {id:'C05010002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T05010003'})
SET t.name='노노케어', t.display_name='노노케어 (Term)', t.desc='돌봄이 필요한 노인을 또 다른 고령자가 돌보는 방식으로, 일본 초고령사회에서 NPO와 결합해 고령자의 사회참여와 소비를 동시에 확대하는 모델', t.readme='C05010003 | finance/KIFVIP2013-10.pdf. NPO법 이후 보건·복지 분야 NPO의 60%가 노노케어 등 돌봄 서비스를 제공한다고 서술.', t.type='T', t.en='Old-to-old Care';
MATCH (term:Term {id:'T05010003'}),(clsf:Class {id:'C05010003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T05010004'})
SET t.name='보이지 않는 가족', t.display_name='보이지 않는 가족 (Term)', t.desc='고령 부모와 기혼 자녀가 근거리에서 살며 경제적·정서적으로 상호 지원하는 가족형태로, 다세대 여행·군락형 아파트 등 새로운 소비수요를 만든다', t.readme='C05010003 | finance/KIFVIP2013-10.pdf. 수도권 부모가 집을 매각하고 자녀 근처로 이주하는 사례와 Invisible Family 정의를 소개.', t.type='T', t.en='Invisible Family';
MATCH (term:Term {id:'T05010004'}),(clsf:Class {id:'C05010003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T05010005'})
SET t.name='유니버설 디자인 정책', t.display_name='유니버설 디자인 정책 (Term)', t.desc='연령·장애와 무관하게 누구나 이용하기 쉬운 도시·생활환경을 설계하는 정책으로, 고령친화 건축·설계 산업을 촉진하는 초고령사회 대응 전략', t.readme='C05010003 | finance/KIFVIP2013-10.pdf. 일본 정부가 유니버설 디자인 정책을 추진하며 관련 산업 성장을 견인한 사례를 설명.', t.type='T', t.en='Universal Design Policy';
MATCH (term:Term {id:'T05010005'}),(clsf:Class {id:'C05010003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T05020001'})
SET t.name='공적연금', t.display_name='공적연금 (Term)', t.desc='국가가 운영하는 국민연금, 공무원연금 등 법정 연금제도', t.readme='C05020001', t.type='T', t.en='Public Pension';
MATCH (term:Term {id:'T05020001'}),(clsf:Class {id:'C05020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T05020002'})
SET t.name='연금라이프', t.display_name='연금라이프 (Term)', t.desc='연금 수입을 주요 소득원으로 하는 은퇴 후 생활 방식', t.readme='C05020002', t.type='T', t.en='Pension-based Life';
MATCH (term:Term {id:'T05020002'}),(clsf:Class {id:'C05020002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T05030001'})
SET t.name='고령자 가계의 소득·지출 구조', t.display_name='고령자 가계의 소득·지출 구조 (Term)', t.desc='고령자 가구의 소득원 구성과 지출 패턴을 분석하는 사회경제적 지표', t.readme='C05030001', t.type='T', t.en='Income and Expenditure Structure of Elderly Households';
MATCH (term:Term {id:'T05030001'}),(clsf:Class {id:'C05030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06010001'})
SET t.name='판례', t.display_name='판례 (Term)', t.desc='법원이 구체적 사건에 대해 내린 판결로서 이후 유사 사건의 재판에 기준이 되는 선례', t.readme='C06010001', t.type='T', t.en='Precedent';
MATCH (term:Term {id:'T06010001'}),(clsf:Class {id:'C06010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06010002'})
SET t.name='대법원 판결', t.display_name='대법원 판결 (Term)', t.desc='대법원이 상고심에서 내린 최종 판결로서 법령 해석의 통일적 기준 제시', t.readme='C06010001', t.type='T', t.en='Supreme Court Decision';
MATCH (term:Term {id:'T06010002'}),(clsf:Class {id:'C06010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06010003'})
SET t.name='헌법재판소 결정', t.display_name='헌법재판소 결정 (Term)', t.desc='헌법재판소가 위헌법률심판, 헌법소원 등에서 내린 결정', t.readme='C06010001', t.type='T', t.en='Constitutional Court Decision';
MATCH (term:Term {id:'T06010003'}),(clsf:Class {id:'C06010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06020001'})
SET t.name='소득세', t.display_name='소득세 (Term)', t.desc='개인의 소득에 대해 부과되는 조세로 종합소득세, 양도소득세 등 포함', t.readme='C06020001', t.type='T', t.en='Income Tax';
MATCH (term:Term {id:'T06020001'}),(clsf:Class {id:'C06020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06020002'})
SET t.name='법인세', t.display_name='법인세 (Term)', t.desc='법인의 소득에 대해 부과되는 조세', t.readme='C06020001', t.type='T', t.en='Corporate Tax';
MATCH (term:Term {id:'T06020002'}),(clsf:Class {id:'C06020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06020003'})
SET t.name='부가가치세', t.display_name='부가가치세 (Term)', t.desc='재화나 용역의 공급 시 창출된 부가가치에 부과되는 간접세', t.readme='C06020001', t.type='T', t.en='Value Added Tax', t.acronym='VAT';
MATCH (term:Term {id:'T06020003'}),(clsf:Class {id:'C06020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06020004'})
SET t.name='상속세·증여세', t.display_name='상속세·증여세 (Term)', t.desc='상속이나 증여로 재산을 취득한 경우 부과되는 조세', t.readme='C06020001', t.type='T', t.en='Inheritance Tax / Gift Tax';
MATCH (term:Term {id:'T06020004'}),(clsf:Class {id:'C06020001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06030001'})
SET t.name='국가공무원법', t.display_name='국가공무원법 (Term)', t.desc='국가공무원의 임용, 복무, 신분보장 등을 규정한 법률', t.readme='C06030001', t.type='T', t.en='State Public Officials Act';
MATCH (term:Term {id:'T06030001'}),(clsf:Class {id:'C06030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T06030002'})
SET t.name='행정절차법', t.display_name='행정절차법 (Term)', t.desc='행정청의 처분, 신고, 입법예고 등 행정절차에 관한 공통사항을 규정한 법률', t.readme='C06030001', t.type='T', t.en='Administrative Procedure Act';
MATCH (term:Term {id:'T06030002'}),(clsf:Class {id:'C06030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07010001'})
SET t.name='암', t.display_name='암 (Term)', t.desc='세포가 비정상적으로 증식하여 주변 조직을 침범하거나 전이하는 악성 종양', t.readme='C07010001', t.type='T', t.en='Cancer';
MATCH (term:Term {id:'T07010001'}),(clsf:Class {id:'C07010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07010002'})
SET t.name='대장암', t.display_name='대장암 (Term)', t.desc='대장(결장과 직장)에 발생하는 악성 종양으로 한국인에게 흔한 암 중 하나', t.readme='C07010002', t.type='T', t.en='Colorectal Cancer', t.acronym='CRC';
MATCH (term:Term {id:'T07010002'}),(clsf:Class {id:'C07010002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07010003'})
SET t.name='다발성골수종', t.display_name='다발성골수종 (Term)', t.desc='골수 내 형질세포가 비정상적으로 증식하는 혈액암의 일종', t.readme='C07010003', t.type='T', t.en='Multiple Myeloma', t.acronym='MM';
MATCH (term:Term {id:'T07010003'}),(clsf:Class {id:'C07010003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07010004'})
SET t.name='항암화학요법', t.display_name='항암화학요법 (Term)', t.desc='항암제를 사용하여 암세포를 파괴하거나 성장을 억제하는 치료법', t.readme='C07010001', t.type='T', t.en='Chemotherapy';
MATCH (term:Term {id:'T07010004'}),(clsf:Class {id:'C07010001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07020001'})
SET t.name='안구건조증', t.display_name='안구건조증 (Term)', t.desc='눈물 분비 감소 또는 과도한 증발로 눈 표면이 손상되어 불편감을 유발하는 질환', t.readme='C07020002', t.type='T', t.en='Dry Eye Syndrome', t.acronym='DES';
MATCH (term:Term {id:'T07020001'}),(clsf:Class {id:'C07020002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07020002'})
SET t.name='백내장', t.display_name='백내장 (Term)', t.desc='수정체가 혼탁해져 시력이 저하되는 안과 질환', t.readme='C07020003', t.type='T', t.en='Cataract';
MATCH (term:Term {id:'T07020002'}),(clsf:Class {id:'C07020003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07020003'})
SET t.name='녹내장', t.display_name='녹내장 (Term)', t.desc='안압 상승 등으로 시신경이 손상되어 시야가 좁아지는 질환', t.readme='C07020003', t.type='T', t.en='Glaucoma';
MATCH (term:Term {id:'T07020003'}),(clsf:Class {id:'C07020003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07020004'})
SET t.name='황반변성', t.display_name='황반변성 (Term)', t.desc='망막 중심부인 황반이 변성되어 중심 시력이 저하되는 질환', t.readme='C07020003', t.type='T', t.en='Macular Degeneration', t.acronym='AMD';
MATCH (term:Term {id:'T07020004'}),(clsf:Class {id:'C07020003'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07030001'})
SET t.name='위식도역류질환', t.display_name='위식도역류질환 (Term)', t.desc='위 내용물이 식도로 역류하여 속쓰림, 역류 등 증상을 유발하는 질환', t.readme='C07030002', t.type='T', t.en='Gastroesophageal Reflux Disease', t.acronym='GERD';
MATCH (term:Term {id:'T07030001'}),(clsf:Class {id:'C07030002'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07030002'})
SET t.name='내시경', t.display_name='내시경 (Term)', t.desc='내시경 기구를 삽입하여 소화기관 내부를 관찰하고 진단·치료하는 시술', t.readme='C07030001', t.type='T', t.en='Endoscopy';
MATCH (term:Term {id:'T07030002'}),(clsf:Class {id:'C07030001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07040001'})
SET t.name='건강검진', t.display_name='건강검진 (Term)', t.desc='질병의 조기 발견과 예방을 위해 정기적으로 실시하는 종합적인 건강 검사', t.readme='C07040001', t.type='T', t.en='Health Screening';
MATCH (term:Term {id:'T07040001'}),(clsf:Class {id:'C07040001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MERGE (t:Term {id:'T07040002'})
SET t.name='예방의학', t.display_name='예방의학 (Term)', t.desc='질병 예방, 건강증진, 수명연장을 목적으로 하는 의학 분야', t.readme='C07040001', t.type='T', t.en='Preventive Medicine';
MATCH (term:Term {id:'T07040002'}),(clsf:Class {id:'C07040001'}) MERGE (term)-[:BELONGS_TO]->(clsf);

MATCH (s:Term {id:'T02030003'}),(d:Term {id:'T02030004'}) MERGE (s)-[r:HAS_COMPONENT]->(d) SET r.source_file='finance/240320(보도자료) 금융권의 상생금융 추진현황.pdf', r.note='"소상공인 금리부담경감 3종 세트는 저금리 대환 프로그램을 구성요소로 포함"';

MATCH (s:Term {id:'T02070001'}),(d:Term {id:'T02070002'}) MERGE (s)-[r:USES_METHOD]->(d) SET r.source_file='finance/240130(보도자료) 지방은행의 시중은행 전환시 인가방식 및 절차.pdf', r.note='"지방은행 전환은 신규인가가 아닌 인가내용 변경 방식을 따른다고 명시"';

MATCH (s:Term {id:'T02070001'}),(d:Term {id:'T02070003'}) MERGE (s)-[r:OPTIONAL_STEP]->(d) SET r.source_file='finance/240130(보도자료) 지방은행의 시중은행 전환시 인가방식 및 절차.pdf', r.note='"예비인가는 신청 시 생략 가능하지만 필요시 진행 가능하다고 안내"';

MATCH (s:Term {id:'T02010004'}),(d:Term {id:'T02010005'}) MERGE (s)-[r:MONITORED_BY]->(d) SET r.source_file='finance/3. 향후 통화신용정책 방향.pdf', r.note='"물가안정기 재진입 여부는 근원물가 둔화 흐름과 인플레이션 분포를 점검하며 판단"';

MATCH (s:Term {id:'T02070001'}),(d:Term {id:'T02070004'}) MERGE (s)-[r:MUST_PASS]->(d) SET r.source_file='finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf', r.note='"지방은행 시중은행 전환은 자본금·대주주·내부통제 등 모든 세부심사요건을 다시 충족해야 한다고 정리"';

MATCH (s:Term {id:'T02070004'}),(d:Term {id:'T02070005'}) MERGE (s)-[r:ASSESSED_BY]->(d) SET r.source_file='finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf', r.note='"사업계획 타당성은 외부평가위원회를 통해 확인하라고 은행업감독규정 제7조가 요구"';

MATCH (s:Term {id:'T02070001'}),(d:Term {id:'T02070006'}) MERGE (s)-[r:GOVERNED_BY]->(d) SET r.source_file='finance/[별첨] 지방은행의 시중은행 전환시 인가방식 및 절차.pdf', r.note='"주주 관련 형사절차만 심사중단사유로 인정하고 금융사고 시 조치계획 제출로 심사를 이어갈 수 있다고 안내"';

MATCH (s:Term {id:'T02080001'}),(d:Term {id:'T02080002'}) MERGE (s)-[r:MANDATED_BY]->(d) SET r.source_file='finance/WP22-05.pdf', r.note='"TCFD 권고안 지지가 2,990개 기관으로 확대되며 녹색금융 공시 의무화 근거가 된다고 보고"';

MATCH (s:Term {id:'T02080001'}),(d:Term {id:'T02080003'}) MERGE (s)-[r:ENABLED_BY]->(d) SET r.source_file='finance/WP22-05.pdf', r.note='"한국형 녹색분류체계의 6대 환경목표·DNSH 기준이 녹색투자 대상을 식별해 녹색금융을 가능하게 함"';

MATCH (s:Term {id:'T02080001'}),(d:Term {id:'T02080004'}) MERGE (s)-[r:GUIDED_BY]->(d) SET r.source_file='finance/WP22-05.pdf', r.note='"금융권 녹색금융 핸드북이 실무 가이드·운영사례·Q&A를 제공해 금융사의 녹색금융 집행을 안내"';

