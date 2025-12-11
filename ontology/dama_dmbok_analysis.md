# DAMA-DMBOK 분석 및 데이터 거버넌스 도메인 보강

**목적:** DAMA-DMBOK 2.0 지식체계를 반영하여 13번 데이터 거버넌스 도메인 보완
**작성일:** 2025-12-11

---

## DAMA-DMBOK 2.0 개요

**DAMA-DMBOK** (Data Management Body of Knowledge)
- **발행기관:** DAMA International
- **버전:** 2.0 (2017)
- **범위:** 데이터 관리 전문가를 위한 지식체계
- **구성:** 11개 지식 영역 (Knowledge Areas)

---

## DAMA-DMBOK 2.0 11개 지식 영역

### 1. Data Governance (데이터 거버넌스)
**정의:** 데이터 자산의 관리를 위한 권한 행사 및 통제

**주요 활동:**
- 데이터 거버넌스 전략 및 정책 수립
- 데이터 거버넌스 조직 구성 (Data Governance Council, Stewards)
- 데이터 정책 및 표준 관리
- 데이터 이슈 관리 및 에스컬레이션
- 데이터 관련 의사결정 프로세스

**핵심 역할:**
- Chief Data Officer (CDO)
- Data Governance Council
- Data Stewards (데이터 관리자)
- Data Owners (데이터 소유자)

### 2. Data Architecture (데이터 아키텍처)
**정의:** 비즈니스 요구사항을 데이터 자산으로 변환하는 청사진

**주요 활동:**
- 엔터프라이즈 데이터 모델 개발
- 데이터 흐름 설계
- 데이터 통합 설계
- 데이터 아키텍처 표준 정의

**산출물:**
- Enterprise Data Model
- Data Flow Diagrams
- Data Integration Architecture

### 3. Data Modeling & Design (데이터 모델링 및 설계)
**정의:** 데이터 요구사항을 발견, 분석, 표현하는 프로세스

**주요 활동:**
- 개념 데이터 모델링 (Conceptual)
- 논리 데이터 모델링 (Logical)
- 물리 데이터 모델링 (Physical)
- 데이터 모델 관리 및 유지보수

**표기법:**
- ERD (Entity-Relationship Diagram)
- UML (Unified Modeling Language)
- Dimensional Modeling (Star/Snowflake Schema)

### 4. Data Storage & Operations (데이터 저장 및 운영)
**정의:** 데이터 저장소의 배포, 운영, 지원

**주요 활동:**
- 데이터베이스 관리 (DBA)
- 데이터 백업 및 복구
- 데이터 보관 및 아카이빙
- 데이터베이스 성능 최적화

**기술:**
- Relational DBMS (Oracle, PostgreSQL, MySQL)
- NoSQL (MongoDB, Cassandra)
- Cloud Storage (S3, Azure Blob)

### 5. Data Security (데이터 보안)
**정의:** 데이터 프라이버시, 기밀성, 접근 권한 보장

**주요 활동:**
- 데이터 분류 (Public, Internal, Confidential, Restricted)
- 접근 제어 (Authentication, Authorization)
- 암호화 (Encryption at Rest, in Transit)
- 개인정보 보호 (Privacy, De-identification)
- 감사 및 모니터링

**규제:**
- GDPR (EU 개인정보보호규정)
- CCPA (캘리포니아 소비자 프라이버시법)
- 개인정보보호법 (한국)

### 6. Data Integration & Interoperability (데이터 통합 및 상호운용성)
**정의:** 시스템 간 데이터 이동 및 통합

**주요 활동:**
- ETL/ELT 프로세스 설계 및 구현
- 데이터 파이프라인 구축
- API 및 웹 서비스 통합
- 실시간 데이터 통합 (Streaming)

**기술:**
- ETL 도구 (Informatica, Talend, Apache NiFi)
- Message Queue (Kafka, RabbitMQ)
- API Gateway

### 7. Document & Content Management (문서 및 콘텐츠 관리)
**정의:** 비정형 데이터(문서, 이미지, 영상 등) 관리

**주요 활동:**
- 문서 분류 체계 수립
- 문서 생명주기 관리
- 콘텐츠 검색 및 검색
- 레코드 관리 (Records Management)

**기술:**
- ECM (Enterprise Content Management)
- DMS (Document Management System)
- DAM (Digital Asset Management)

### 8. Reference & Master Data (참조 및 마스터 데이터)
**정의:** 핵심 비즈니스 엔티티의 공유 데이터 관리

**주요 활동:**
- 마스터 데이터 식별 (고객, 제품, 위치 등)
- 마스터 데이터 통합 및 동기화
- 참조 데이터 관리 (코드, 분류 체계)
- 데이터 정합성 유지

**유형:**
- **Master Data:** 고객, 제품, 계정, 위치
- **Reference Data:** 국가 코드, 통화 코드, 상태 코드

**기술:**
- MDM (Master Data Management)
- Data Hub

### 9. Data Warehousing & Business Intelligence (데이터 웨어하우스 및 BI)
**정의:** 의사결정을 위한 데이터 분석 환경 구축

**주요 활동:**
- 데이터 웨어하우스 설계 및 구축
- OLAP (Online Analytical Processing)
- BI 리포트 및 대시보드 개발
- 셀프서비스 분석 환경 제공

**기술:**
- Data Warehouse (Snowflake, Redshift, BigQuery)
- BI Tools (Tableau, Power BI, Looker)
- OLAP Engines

### 10. Metadata (메타데이터)
**정의:** 데이터에 대한 데이터

**주요 활동:**
- 메타데이터 모델 정의
- 메타데이터 저장소 구축
- 메타데이터 수집 및 관리
- 데이터 리니지 (Data Lineage) 추적
- 비즈니스 용어집 (Business Glossary)

**유형:**
- **Business Metadata:** 비즈니스 정의, 용어
- **Technical Metadata:** 스키마, 데이터 타입, 제약조건
- **Operational Metadata:** 실행 시간, 데이터 볼륨, 로그

### 11. Data Quality (데이터 품질)
**정의:** 데이터가 의도된 용도에 적합한지 보장

**주요 활동:**
- 데이터 품질 차원 정의 (정확성, 완전성, 일관성, 적시성, 유효성, 유일성)
- 데이터 프로파일링
- 데이터 품질 규칙 정의 및 모니터링
- 데이터 품질 이슈 관리
- 데이터 정제 (Data Cleansing)

**품질 차원:**
- Accuracy (정확성)
- Completeness (완전성)
- Consistency (일관성)
- Timeliness (적시성)
- Validity (유효성)
- Uniqueness (유일성)

---

## 현재 13번 데이터 거버넌스 도메인 구조

```
13. 데이터 거버넌스
├─ 13.01 메타데이터 관리
│  ├─ 메타데이터 표준
│  ├─ 데이터 사전
│  └─ 데이터 카탈로그
├─ 13.02 데이터 품질관리
│  ├─ 품질 지표
│  ├─ 품질 평가
│  └─ 품질 개선
├─ 13.03 데이터 표준화
│  ├─ 표준 용어 관리
│  ├─ 표준 코드 관리
│  └─ 데이터베이스 표준
└─ 13.04 공공데이터 개방
   ├─ 오픈데이터 정책
   ├─ 데이터셋 관리
   └─ API 관리
```

---

## DAMA-DMBOK vs 현재 구조 비교

| DAMA 지식 영역 | 현재 도메인 13 커버리지 | 비고 |
|----------------|------------------------|------|
| 1. Data Governance | ⚠️ 부분적 | 거버넌스 조직, 정책 미포함 |
| 2. Data Architecture | ❌ 없음 | 데이터 아키텍처 영역 부재 |
| 3. Data Modeling & Design | ⚠️ 부분적 | DB 표준에 일부 포함 |
| 4. Data Storage & Operations | ❌ 없음 | DBA 영역 부재 |
| 5. Data Security | ❌ 없음 | 데이터 보안 영역 부재 |
| 6. Data Integration | ❌ 없음 | ETL, API 통합 부재 |
| 7. Document & Content Mgmt | ❌ 없음 | 문서 관리 부재 |
| 8. Reference & Master Data | ⚠️ 부분적 | 참조 데이터만 포함 |
| 9. DW & BI | ❌ 없음 | 별도 도메인 필요 |
| 10. Metadata | ✅ 포함 | 13.01에 완전 포함 |
| 11. Data Quality | ✅ 포함 | 13.02에 완전 포함 |

**커버리지:**
- ✅ 완전 포함: 2개 (18%)
- ⚠️ 부분 포함: 3개 (27%)
- ❌ 미포함: 6개 (55%)

---

## 보완 제안

### Option A: 데이터 거버넌스 도메인 확장 (권장)

**추가할 중분류 (5개):**

1. **13.05 데이터 거버넌스 조직**
   - 거버넌스 위원회
   - 데이터 관리자 (Data Stewards)
   - 데이터 소유자
   - CDO 역할

2. **13.06 데이터 아키텍처**
   - 엔터프라이즈 데이터 모델
   - 데이터 흐름
   - 데이터 통합 설계

3. **13.07 데이터 모델링**
   - 개념/논리/물리 모델
   - ERD, UML
   - 모델 관리

4. **13.08 데이터 보안**
   - 데이터 분류
   - 접근 제어
   - 암호화
   - 개인정보 보호

5. **13.09 마스터 데이터 관리**
   - 마스터 데이터 (고객, 제품)
   - 참조 데이터 (코드)
   - MDM 프로세스

**결과:**
- 중분류: 4개 → 9개
- DAMA 커버리지: 27% → 73%

### Option B: 새 도메인 추가

**15. 데이터 관리** (Data Management) 도메인 신설
- Data Storage & Operations
- Data Integration
- Document & Content Management

**16. 데이터 분석** (Data Analytics) 도메인 신설
- Data Warehousing & BI
- Advanced Analytics
- Data Science

**장점:** 영역별 명확한 분리
**단점:** 도메인 수 과다 증가 (14 → 16개)

### Option C: 현재 구조 유지 + DAMA 매핑만

**변경사항 최소화:**
- DAMA-DMBOK 표준만 추가
- 현재 분류에 DAMA 지식 영역 매핑
- 용어 일부 추가 (5-10개)

**장점:** 안정적, 변경 최소
**단점:** DAMA 커버리지 낮음

---

## 권장: Option A 실행

**단계:**
1. DAMA-DMBOK 표준 등록
2. 5개 중분류 추가 (13.05-13.09)
3. 관련 용어 15-20개 추가
4. DAMA 11개 지식 영역 매핑

**예상 결과:**
- 중분류: 17개 → 30개 (+13개)
- 용어: 10개 → 30개 (+20개)
- DAMA 커버리지: 27% → 73%
- 표준 레퍼런스: +30개

---

## DAMA-DMBOK 표준 정보

**표준 ID:** STD-DAMA
**코드:** DAMA-DMBOK
**명칭:** DAMA-DMBOK 2.0
**영문명:** Data Management Body of Knowledge
**유형:** INTERNATIONAL
**범위:** ONTOLOGY
**조직:** DAMA International
**버전:** 2.0 (2017)
**URI:** https://www.dama.org/cpages/body-of-knowledge
**설명:** 데이터 관리 전문가를 위한 11개 지식 영역 체계. 데이터 거버넌스, 아키텍처, 품질, 보안 등 포괄.

---

## 다음 단계

1. ✅ DAMA-DMBOK 분석 완료
2. ⏭️ 사용자 승인: Option A/B/C 선택
3. ⏭️ 표준 등록 및 도메인 구조 확장
4. ⏭️ 용어 추가 및 매핑
5. ⏭️ 검증 및 커밋 (v3.14.1)
