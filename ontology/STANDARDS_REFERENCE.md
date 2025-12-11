# 표준 레퍼런스 가이드

**버전:** 1.0.0
**작성일:** 2025-12-11
**ontology 버전:** 3.12.0

이 문서는 MC 분류·용어 통합 체계에서 사용하는 24개 표준에 대한 상세 정보를 제공합니다.

---

## 목차

1. [개요](#1-개요)
2. [국제 표준 (12개)](#2-국제-표준-12개)
3. [국내 표준 (6개)](#3-국내-표준-6개)
4. [한국 응용 표준 (6개)](#4-한국-응용-표준-6개)
5. [온톨로지 반영 현황](#5-온톨로지-반영-현황)
6. [도메인별 표준 반영도](#6-도메인별-표준-반영도)
7. [표준별 상세 프로필](#7-표준별-상세-프로필)
8. [참고 자료](#8-참고-자료)

---

## 1. 개요

### 1.1 표준 현황 요약

| 구분 | 개수 | 용도 |
|------|------|------|
| **국제 표준** | 12개 | 글로벌 상호운용성, 국제 기준 준수 |
| **국내 표준** | 6개 | 한국 공공데이터·법령·분류 기준 |
| **한국 응용 표준** | 6개 | 한국형 메타데이터·온톨로지 적용 |
| **총계** | **24개** | - |

### 1.2 표준 유형별 분류

```
표준 레지스트리 (24개)
├── INTERNATIONAL (12개)
│   ├── ONTOLOGY (3개): SKOS, ISO25964, Schema.org
│   ├── CLASSIFICATION (5개): OECD-FOS, ICD11, GS1, arXiv, ACM CCS
│   ├── TERMINOLOGY (2개): FIBO, MeSH
│   └── METADATA (2개): Dublin Core, UNESCO
│
├── NATIONAL (6개)
│   ├── CLASSIFICATION (4개): BRM, KSIC, KCD, DATAGOkr
│   ├── TERMINOLOGY (1개): STDTERM
│   └── METADATA (1개): MOLEG
│
└── APPLICATION (6개)
    ├── METADATA (4개): DCAT-AP-KR, KS-ISO11179, DBSTD, DATAQUALITY
    ├── TERMINOLOGY (1개): KOOR
    └── CLASSIFICATION (1개): ADMCODE
```

### 1.3 온톨로지 반영 통계

| 항목 | 개수 | 비율 |
|------|------|------|
| 총 분류 | 376개 | 100% |
| 표준 매핑된 분류 | 232개 | **61.7%** |
| 총 용어 | 182개 | 100% |
| 표준 매핑된 용어 | 112개 | **61.5%** |
| 총 레퍼런스 | 376개 | - |

---

## 2. 국제 표준 (12개)

### 2.1 온톨로지 표준 (3개)

#### STD-SKOS (Simple Knowledge Organization System)

| 항목 | 내용 |
|------|------|
| **관리기관** | W3C (World Wide Web Consortium) |
| **현재 버전** | W3C Recommendation (2009-08-18) |
| **규모** | 핵심 개념 ~50개, 속성 ~30개 |
| **URI** | https://www.w3.org/2004/02/skos/ |
| **용도** | 지식조직체계(시소러스, 분류표, 택소노미) 표현 |

**핵심 개념:**
- `skos:Concept` - 개념
- `skos:ConceptScheme` - 개념 체계
- `skos:prefLabel`, `skos:altLabel` - 선호/대안 레이블
- `skos:broader`, `skos:narrower` - 상위/하위 관계
- `skos:related` - 연관 관계
- `skos:exactMatch`, `skos:closeMatch` - 매핑 관계

**온톨로지 반영:**
- **노드**: Classification, Term, Synonym 구조에 SKOS 개념 적용
- **관계**: `:EXACT_SYNONYM`, `:CLOSE_SYNONYM`, `:BROADER_THAN`, `:NARROWER_THAN` (v3.12)
- **프로퍼티**: `match_type` (EXACT_MATCH, CLOSE_MATCH, BROAD_MATCH, NARROW_MATCH, RELATED_MATCH)

---

#### STD-ISO25964 (Thesauri and Interoperability)

| 항목 | 내용 |
|------|------|
| **관리기관** | ISO (International Organization for Standardization) |
| **현재 버전** | ISO 25964-1:2011, ISO 25964-2:2013 |
| **URI** | https://www.iso.org/standard/53657.html |
| **용도** | 시소러스 구축 및 상호운용성 표준 |

**핵심 개념:**
- 선호용어(Preferred Term) / 비선호용어(Non-preferred Term)
- 계층관계(Hierarchical) / 연관관계(Associative)
- 동의관계(Equivalence)

**온톨로지 반영:**
- **구조**: Term-Synonym 관계 설계 기반
- **관계**: `synonyms.exact`, `synonyms.related` 구조

---

#### STD-SCHEMA (Schema.org)

| 항목 | 내용 |
|------|------|
| **관리기관** | Schema.org (Google, Microsoft, Yahoo, Yandex) |
| **현재 버전** | 28.0 (2024) |
| **규모** | 800+ 타입, 1,500+ 속성 |
| **URI** | https://schema.org/ |
| **용도** | 웹 구조화 데이터 표현 |

**주요 타입:**
- `Product`, `Offer`, `Order` - 전자상거래
- `Organization`, `Person` - 조직/개인
- `Event`, `Place` - 이벤트/장소

**온톨로지 반영:**
- **분류**: 디지털커머스 도메인 (8개 매핑)
- **용도**: 전자상거래 관련 분류 표준화

---

### 2.2 분류 표준 (5개)

#### STD-OECD-FOS (Fields of Science Classification)

| 항목 | 내용 |
|------|------|
| **관리기관** | OECD (경제협력개발기구) |
| **현재 버전** | 2015 개정판 |
| **규모** | 6개 대분류, 42개 소분류 |
| **URI** | https://www.oecd.org/science/inno/38235147.pdf |

**대분류 체계:**
1. Natural Sciences (자연과학)
2. Engineering and Technology (공학기술)
3. Medical and Health Sciences (의료보건과학)
4. Agricultural Sciences (농업과학)
5. Social Sciences (사회과학)
6. Humanities (인문학)

**온톨로지 반영:**
- **분류**: 과학기술 도메인 (19개 매핑)
- **용어**: 과학기술 관련 용어 (9개 매핑)

---

#### STD-ICD11 (International Classification of Diseases)

| 항목 | 내용 |
|------|------|
| **관리기관** | WHO (세계보건기구) |
| **현재 버전** | ICD-11 (2022년 발효) |
| **규모** | 26개 챕터, 17,000+ 코드 |
| **URI** | https://icd.who.int/browse11 |

**주요 챕터:**
- Chapter 01: 감염성 질병
- Chapter 02: 신생물
- Chapter 05: 정신행동장애
- Chapter 09: 순환기계 질환

**온톨로지 반영:**
- **분류**: 보건의료 도메인 (1개 매핑)
- **연계**: STD-KCD와 상호 참조

---

#### STD-GS1 (eCommerce Standards)

| 항목 | 내용 |
|------|------|
| **관리기관** | GS1 (국제표준기구) |
| **현재 버전** | GS1 General Specifications 24.0 |
| **규모** | 상품분류 28,000+ 코드 |
| **URI** | https://www.gs1.org/standards/ecommerce |

**핵심 표준:**
- GPC (Global Product Classification)
- GTIN (Global Trade Item Number)
- GLN (Global Location Number)

**온톨로지 반영:**
- **분류**: 디지털커머스 도메인 (4개 매핑)
- **용도**: 상품분류 및 유통 표준화

---

#### STD-ARXIV (Subject Classification)

| 항목 | 내용 |
|------|------|
| **관리기관** | Cornell University |
| **현재 버전** | 2024 |
| **규모** | 8개 대분류, 150+ 소분류 |
| **URI** | https://arxiv.org/category_taxonomy |

**대분류:**
- Physics, Mathematics, Computer Science
- Quantitative Biology, Quantitative Finance
- Statistics, Electrical Engineering, Economics

**온톨로지 반영:**
- **분류**: 과학기술 도메인 (8개 매핑)

---

#### STD-ACMCCS (Computing Classification System)

| 항목 | 내용 |
|------|------|
| **관리기관** | ACM (Association for Computing Machinery) |
| **현재 버전** | CCS 2012 |
| **규모** | 13개 대분류, 2,000+ 항목 |
| **URI** | https://www.acm.org/publications/class-2012 |

**대분류:**
- General and reference
- Hardware, Computer systems organization
- Software and its engineering
- Theory of computation
- Information systems

**온톨로지 반영:**
- **분류**: 과학기술 도메인 (4개 매핑)

---

### 2.3 용어 표준 (2개)

#### STD-FIBO (Financial Industry Business Ontology)

| 항목 | 내용 |
|------|------|
| **관리기관** | EDM Council / OMG |
| **현재 버전** | 2024 Q1 |
| **규모** | 700+ 클래스, 10개 도메인 모듈 |
| **URI** | https://spec.edmcouncil.org/fibo/ |

**도메인 모듈:**
- FND (Foundations)
- BE (Business Entities)
- FBC (Financial Business and Commerce)
- SEC (Securities)
- DER (Derivatives)
- LOAN (Loans)
- IND (Indices and Indicators)
- CAE (Corporate Actions and Events)
- BP (Business Processes)
- MD (Market Data)

**온톨로지 반영:**
- **분류**: 재정금융 도메인 (29개 매핑)
- **용어**: 금융 관련 용어 (12개 매핑)
- **관계**: 금융상품 계층 구조

---

#### STD-MESH (Medical Subject Headings)

| 항목 | 내용 |
|------|------|
| **관리기관** | NLM (NIH) |
| **현재 버전** | 2025 |
| **규모** | 30,000+ 주제어, 318,000+ 보충개념 |
| **URI** | https://www.nlm.nih.gov/mesh/ |

**주요 카테고리:**
- A: Anatomy (해부)
- B: Organisms (생물)
- C: Diseases (질병)
- D: Chemicals and Drugs (화학/약물)
- E: Analytical, Diagnostic and Therapeutic Techniques (기술)
- F: Psychiatry and Psychology (정신의학)
- G: Phenomena and Processes (현상/과정)
- H: Disciplines and Occupations (학문/직업)

**온톨로지 반영:**
- **분류**: 72개 매핑 (최다 사용 표준)
  - 보건의료: 22개
  - 사회복지: 12개
  - 법률: 8개
  - 환경기상: 12개
  - 재난안전: 9개
- **용어**: 13개 매핑

---

### 2.4 메타데이터 표준 (2개)

#### STD-DC (Dublin Core)

| 항목 | 내용 |
|------|------|
| **관리기관** | DCMI (Dublin Core Metadata Initiative) |
| **현재 버전** | ISO 15836-1:2017 |
| **규모** | 15개 핵심 요소, 55개 용어 |
| **URI** | https://www.dublincore.org/ |

**15개 핵심 요소:**
- Title, Creator, Subject, Description, Publisher
- Contributor, Date, Type, Format, Identifier
- Source, Language, Relation, Coverage, Rights

**온톨로지 반영:**
- **구조**: ontology.json 메타데이터 설계 참조
- **프로퍼티**: description, source 등 속성명

---

#### STD-UNESCO (UNESCO Thesaurus)

| 항목 | 내용 |
|------|------|
| **관리기관** | UNESCO |
| **현재 버전** | 2019 |
| **규모** | 4,400+ 용어, 7개 도메인, 5개 언어 |
| **URI** | http://vocabularies.unesco.org/thesaurus |

**7개 도메인:**
1. Education (교육)
2. Science (과학)
3. Culture (문화)
4. Social and Human Sciences (사회인문과학)
5. Information and Communication (정보통신)
6. Politics, Law and Economics (정치법경제)
7. Countries and Country Groups (국가)

**온톨로지 반영:**
- **분류**: 28개 매핑
  - 교육: 18개
  - 문화관광: 10개
- **용어**: 24개 매핑 (두 번째 최다 사용)

---

## 3. 국내 표준 (6개)

### STD-BRM (정부기능분류체계)

| 항목 | 내용 |
|------|------|
| **관리기관** | 행정안전부 |
| **현재 버전** | 2024-12-11 |
| **규모** | 17개 정책분야, 72개 정책영역, 6계층 |
| **URI** | https://www.data.go.kr/data/15062615/fileData.do |
| **법적 근거** | 행정기관의 기능분류에 관한 규정 |

**6계층 구조:**
1. 정책분야 (17개)
2. 정책영역 (72개)
3. 대기능
4. 중기능
5. 소기능
6. 단위과제

**17개 정책분야:**
- 일반공공행정, 공공질서및안전, 통일외교
- 국방, 교육, 문화및관광, 환경, 사회복지
- 보건, 농림해양수산, 산업중소기업및에너지
- 교통및물류, 통신, 국토및지역개발
- 과학기술, 예비비, 기타

**온톨로지 반영:**
- **분류**: 공공행정 도메인 (18개 매핑)
- **용어**: 4개 매핑

---

### STD-KSIC (한국표준산업분류)

| 항목 | 내용 |
|------|------|
| **관리기관** | 통계청 |
| **현재 버전** | 제11차 개정 (2024-07-01 시행) |
| **규모** | 21개 대분류, 77개 중분류, 234개 소분류, 501개 세분류, 1,205개 세세분류 |
| **URI** | http://kssc.kostat.go.kr/ |
| **법적 근거** | 통계법 제22조 |

**5단계 분류:**
| 단계 | 자릿수 | 개수 |
|------|--------|------|
| 대분류 | 1자리 (영문) | 21개 |
| 중분류 | 2자리 | 77개 |
| 소분류 | 3자리 | 234개 |
| 세분류 | 4자리 | 501개 |
| 세세분류 | 5자리 | 1,205개 |

**21개 대분류:**
- A: 농업, 임업 및 어업
- B: 광업
- C: 제조업
- D: 전기, 가스, 증기 및 공기조절 공급업
- E: 수도, 하수 및 폐기물 처리, 원료 재생업
- F: 건설업
- G: 도매 및 소매업
- H: 운수 및 창고업
- I: 숙박 및 음식점업
- J: 정보통신업
- K: 금융 및 보험업
- ... (총 21개)

**제11차 개정 주요 변경 (2024):**
- 수소, 이차전지, 전기차, 풍력발전 등 미래산업 신설
- 가상자산, 온라인 플랫폼 서비스 세분화

**온톨로지 반영:**
- **분류**: 산업경제 도메인 (17개), 디지털커머스 도메인 (7개) - 총 24개 매핑
- **용어**: 19개 매핑

---

### STD-KCD (한국표준질병사인분류)

| 항목 | 내용 |
|------|------|
| **관리기관** | 통계청, 건강보험심사평가원 |
| **현재 버전** | KCD-8 (ICD-11 기반) |
| **규모** | 22개 장, 12,000+ 코드 |
| **URI** | https://www.koicd.kr/ |

**ICD 연계:**
- ICD-10 기반 → ICD-11 전환 진행 중
- WHO 국제표준과 호환

**온톨로지 반영:**
- **분류**: 보건의료 도메인 (4개 매핑)
- **용어**: 2개 매핑

---

### STD-MOLEG (국가법령정보)

| 항목 | 내용 |
|------|------|
| **관리기관** | 법제처 |
| **규모** | 법률 1,500+, 대통령령 2,000+, 부령 3,000+ |
| **URI** | https://www.law.go.kr/ |

**법령 체계:**
- 헌법 → 법률 → 대통령령 → 총리령/부령 → 행정규칙

**온톨로지 반영:**
- **분류**: 법률 도메인 (7개 매핑)
- **용어**: 법률 용어 (10개 매핑)

---

### STD-DATAGOkr (공공데이터포털 분류)

| 항목 | 내용 |
|------|------|
| **관리기관** | 행정안전부, NIA |
| **현재 버전** | 2024 |
| **규모** | 16개 분야 |
| **URI** | https://www.data.go.kr/ |

**16개 분야:**
1. 공공행정
2. 교육
3. 국토관리
4. 문화관광
5. 보건의료
6. 사회복지
7. 산업고용
8. 식품건강
9. 재난안전
10. 재정금융
11. 통일외교안보
12. 환경
13. 교통물류
14. 과학기술
15. 농축수산
16. 법률

**온톨로지 반영:**
- **분류**: 전체 도메인 (28개 매핑)
- **용어**: 19개 매핑

---

### STD-STDTERM (공공데이터 공통표준용어)

| 항목 | 내용 |
|------|------|
| **관리기관** | 행정안전부, NIA |
| **현재 버전** | 7차 제·개정 (2024-11-29) |
| **규모** | **9,027개** 표준용어 |
| **URI** | https://www.data.go.kr/information/PDS_0000000000000464/recsroom.do |
| **법적 근거** | 공공데이터법 제23조, 공공기관 DB 표준화 지침 |

**구성 요소:**
| 구분 | 신규 (7차) | 누적 |
|------|-----------|------|
| 공통표준용어 | 3,641개 | 9,027개 |
| 공통표준단어 | 697개 | 2,396개 |
| 공통표준도메인 | 6개 | 112개 |

**온톨로지 반영:**
- **현재**: 1개 용어 매핑
- **계획**: 선별적 Term 추가 (221개 → 400~600개)

---

## 4. 한국 응용 표준 (6개)

### STD-DCAT-AP-KR (한국형 데이터 카탈로그)

| 항목 | 내용 |
|------|------|
| **관리기관** | NIA |
| **기반 표준** | W3C DCAT, DCAT-AP (유럽) |
| **URI** | http://vocab.datahub.kr/spec/dcat-ap-kr/ |

**온톨로지 반영:**
- **용어**: 1개 매핑

---

### STD-KOOR (한국 기관 온톨로지)

| 항목 | 내용 |
|------|------|
| **관리기관** | NIA |
| **URI** | http://vocab.datahub.kr/def/organization/ |

**온톨로지 반영:**
- **용어**: 공공기관 관련 (2개 매핑)

---

### STD-ADMCODE (행정표준코드)

| 항목 | 내용 |
|------|------|
| **관리기관** | 행정안전부 |
| **URI** | https://code.go.kr/ |

**주요 코드:**
- 법정동코드, 행정동코드
- 도로명코드, 건물코드
- 기관코드

**온톨로지 반영:**
- **분류**: 공공행정 도메인 (1개 매핑)
- **용어**: 3개 매핑

---

### STD-KS-ISO11179 (메타데이터 레지스트리)

| 항목 | 내용 |
|------|------|
| **관리기관** | 국가기술표준원 |
| **기반 표준** | ISO/IEC 11179 |
| **URI** | https://standard.go.kr/ |

---

### STD-DBSTD (DB 표준화 지침)

| 항목 | 내용 |
|------|------|
| **관리기관** | 행정안전부 |
| **현재 버전** | 행안부 고시 제2023-18호 |
| **URI** | https://www.mois.go.kr/ |

**온톨로지 반영:**
- **용어**: 1개 매핑

---

### STD-DATAQUALITY (데이터 품질관리)

| 항목 | 내용 |
|------|------|
| **관리기관** | 행정안전부 |
| **URI** | https://www.data.go.kr/ |

---

## 5. 온톨로지 반영 현황

### 5.1 표준별 매핑 통계

#### 분류 레퍼런스 (총 255개)

| 순위 | 표준 | 매핑 수 | 주요 도메인 |
|------|------|---------|------------|
| 1 | **STD-MESH** | 72개 | 보건의료, 사회복지, 법률, 환경, 재난 |
| 2 | STD-FIBO | 29개 | 재정금융 |
| 3 | STD-DATAGOkr | 28개 | 전체 도메인 |
| 4 | STD-UNESCO | 28개 | 교육, 문화관광 |
| 5 | STD-KSIC | 24개 | 산업경제, 디지털커머스 |
| 6 | STD-OECD-FOS | 19개 | 과학기술 |
| 7 | STD-BRM | 18개 | 공공행정 |
| 8 | STD-SCHEMA | 8개 | 디지털커머스 |
| 9 | STD-ARXIV | 8개 | 과학기술 |
| 10 | STD-MOLEG | 7개 | 법률 |

#### 용어 레퍼런스 (총 121개)

| 순위 | 표준 | 매핑 수 | 주요 도메인 |
|------|------|---------|------------|
| 1 | **STD-UNESCO** | 24개 | 교육, 문화관광 |
| 2 | STD-DATAGOkr | 19개 | 전체 도메인 |
| 3 | STD-KSIC | 19개 | 산업경제 |
| 4 | STD-MESH | 13개 | 보건의료 |
| 5 | STD-FIBO | 12개 | 재정금융 |
| 6 | STD-MOLEG | 10개 | 법률 |
| 7 | STD-OECD-FOS | 9개 | 과학기술 |
| 8 | STD-BRM | 4개 | 공공행정 |

### 5.2 매치 타입 분포

#### 분류

| 매치 타입 | 개수 | 비율 | 설명 |
|----------|------|------|------|
| EXACT_MATCH | 82개 | 32% | 정확히 일치 |
| CLOSE_MATCH | 79개 | 31% | 밀접하게 유사 |
| RELATED_MATCH | 48개 | 19% | 연관 관계 |
| NARROW_MATCH | 24개 | 9% | 하위 개념 |
| BROAD_MATCH | 22개 | 9% | 상위 개념 |

#### 용어

| 매치 타입 | 개수 | 비율 | 설명 |
|----------|------|------|------|
| EXACT_MATCH | 51개 | 42% | 정확히 일치 |
| NARROW_MATCH | 33개 | 27% | 하위 개념 |
| RELATED_MATCH | 16개 | 13% | 연관 관계 |
| BROAD_MATCH | 13개 | 11% | 상위 개념 |
| CLOSE_MATCH | 8개 | 7% | 밀접하게 유사 |

### 5.3 온톨로지 구조 반영

#### 노드 (Node) 반영

| 노드 타입 | 표준 기반 | 설명 |
|----------|----------|------|
| `:Classification` | SKOS:Concept, ISO25964 | 분류 노드 |
| `:Term` | SKOS:Concept | 용어 노드 |
| `:Synonym` | SKOS:altLabel | 동의어 노드 |
| `:Standard` | Dublin Core | 표준 메타데이터 노드 |

#### 관계 (Relationship) 반영

| 관계 타입 | 표준 기반 | SKOS 매핑 |
|----------|----------|----------|
| `:PARENT_OF` | SKOS, ISO25964 | skos:broader/narrower |
| `:EXACT_SYNONYM` | **SKOS** (v3.12) | skos:exactMatch |
| `:CLOSE_SYNONYM` | **SKOS** (v3.12) | skos:closeMatch |
| `:RELATED_SYNONYM` | **SKOS** (v3.12) | skos:related |
| `:BROADER_THAN` | **SKOS** (v3.12) | skos:broader |
| `:NARROWER_THAN` | **SKOS** (v3.12) | skos:narrower |
| `:RELATED_TO` | SKOS | skos:related |
| `:MAPPED_TO` | SKOS | skos:*Match |

#### 프로퍼티 (Property) 반영

| 프로퍼티 | 표준 기반 | 용도 |
|----------|----------|------|
| `standard_id` | 자체 정의 | 표준 식별자 |
| `external_id` | SKOS notation | 외부 표준 코드 |
| `external_name` | SKOS prefLabel | 외부 표준 명칭 |
| `match_type` | SKOS mapping | 매핑 관계 타입 |
| `confidence` | 자체 정의 | 매핑 신뢰도 (0.0~1.0) |

---

## 6. 도메인별 표준 반영도

| 코드 | 도메인 | 분류 커버리지 | 용어 커버리지 | 주요 표준 |
|------|--------|--------------|--------------|----------|
| 01 | 공공행정 | 18/29 (62%) | 9/12 (75%) | BRM(18), DATAGOkr, ADMCODE |
| 02 | 교육 | 18/30 (60%) | 7/14 (50%) | UNESCO(18), DATAGOkr |
| 03 | 보건의료 | 22/43 (51%) | 13/16 (81%) | MESH(22), KCD(4), DATAGOkr |
| 04 | 사회복지 | 19/30 (63%) | 7/9 (78%) | MESH(12), DATAGOkr(7) |
| 05 | 법률 | 15/28 (54%) | 10/19 (53%) | MESH(8), MOLEG(7), DATAGOkr |
| 06 | 재정금융 | 28/52 (54%) | 12/16 (75%) | FIBO(29), DATAGOkr |
| 07 | 산업경제 | 20/34 (59%) | 11/18 (61%) | KSIC(17), MESH(3), DATAGOkr |
| 08 | 디지털커머스 | 18/22 **(82%)** | 6/8 (75%) | SCHEMA(8), KSIC(7), GS1(4) |
| 09 | 문화관광 | 16/29 (55%) | 11/20 (55%) | UNESCO(10), MESH(6), DATAGOkr |
| 10 | 환경기상 | 19/29 (66%) | 6/17 (35%) | MESH(12), DATAGOkr(7) |
| 11 | 과학기술 | 24/27 **(89%)** | 10/12 (83%) | OECD-FOS(19), ARXIV(8), ACMCCS(4) |
| 12 | 재난안전 | 15/23 (65%) | 10/21 (48%) | MESH(9), DATAGOkr(6) |

**최고 커버리지:**
- 분류: 과학기술 (89%), 디지털커머스 (82%)
- 용어: 과학기술 (83%), 보건의료 (81%)

---

## 7. 표준별 상세 프로필

### 7.1 활용도 매트릭스

| 표준 | 분류 매핑 | 용어 매핑 | 노드 영향 | 관계 영향 | 프로퍼티 영향 |
|------|----------|----------|----------|----------|--------------|
| SKOS | - | - | ★★★ | ★★★ | ★★★ |
| MESH | 72개 | 13개 | ★☆☆ | ★☆☆ | ★★☆ |
| FIBO | 29개 | 12개 | ★☆☆ | ★☆☆ | ★★☆ |
| UNESCO | 28개 | 24개 | ★☆☆ | ★☆☆ | ★★☆ |
| KSIC | 24개 | 19개 | ★☆☆ | ★☆☆ | ★★☆ |
| BRM | 18개 | 4개 | ★☆☆ | ★☆☆ | ★★☆ |

### 7.2 표준 간 연계

```
                    ┌─────────────┐
                    │    SKOS     │ ◄── 온톨로지 구조 기반
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│ 국제 분류 표준 │  │ 국제 용어 표준 │  │ 국내 표준     │
├───────────────┤  ├───────────────┤  ├───────────────┤
│ OECD-FOS      │  │ MESH          │  │ BRM           │
│ ICD11         │  │ FIBO          │  │ KSIC          │
│ GS1           │  │ UNESCO        │  │ KCD           │
│ arXiv         │  │               │  │ DATAGOkr      │
│ ACM CCS       │  │               │  │ STDTERM       │
└───────────────┘  └───────────────┘  └───────────────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                 ┌─────────────────┐
                 │  ontology.json  │
                 │  (MC 통합 체계)  │
                 └─────────────────┘
```

---

## 8. 참고 자료

### 8.1 공식 웹사이트

**국제 표준:**
- [W3C SKOS](https://www.w3.org/2004/02/skos/)
- [FIBO - EDM Council](https://spec.edmcouncil.org/fibo/)
- [MeSH - NLM](https://www.nlm.nih.gov/mesh/)
- [UNESCO Thesaurus](http://vocabularies.unesco.org/thesaurus)
- [Schema.org](https://schema.org/)
- [GS1 Standards](https://www.gs1.org/standards)
- [arXiv Categories](https://arxiv.org/category_taxonomy)
- [ACM CCS](https://www.acm.org/publications/class-2012)

**국내 표준:**
- [공공데이터포털](https://www.data.go.kr/)
- [통계분류포털](http://kssc.kostat.go.kr/)
- [국가법령정보센터](https://www.law.go.kr/)
- [행정표준코드관리시스템](https://code.go.kr/)

### 8.2 관련 문서

- [context_schema.md](context_schema.md) - ontology.json 스키마 상세
- [SYNONYM_REFINEMENT_PROPOSAL.md](SYNONYM_REFINEMENT_PROPOSAL.md) - v3.12 SKOS 기반 설계
- [SAMPLE_QUERIES.md](SAMPLE_QUERIES.md) - 표준 관련 쿼리 예시

### 8.3 버전 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|----------|
| 1.0.0 | 2025-12-11 | 최초 작성 (24개 표준 프로필, 온톨로지 반영 현황) |

---

*이 문서는 MC 분류·용어 통합 체계의 표준 레퍼런스 가이드입니다.*
