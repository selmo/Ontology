# 용어 체계 개선안

## 문제점 요약

현재 context.txt의 용어 중 **문서 제목**, **판례명**, **가이드명** 등이 포함되어 있음.
이는 온톨로지 관점에서 **개념(Concept)**이 아닌 **인스턴스(Instance)**에 해당.

### 전체 통계
- 총 용어: 148개
- 문제가 있는 용어: 약 40개
  - 공공: 13개 (문서 제목)
  - 법률: 10개 (판례명 + 문서)
  - 의료: 17개 (가이드/연구 제목)

---

## 도메인별 개선안

### 01. 공공 (Public Sector)

#### 삭제 대상 (중복 문서 제목)

```
삭제:
- T01060003 2020년 중소벤처기업부 업무계획
- T01060004 2021년도 중소벤처기업부 업무계획
- T01060005 2023년 주요업무 추진계획
- T01060006 2024년 주요업무 추진계획
- T01060007 2025년 주요업무 추진계획
- T01060008 2024년 행정안전부 업무계획
- T01060009 2024년 교육부 주요정책 추진계획

→ 통합: T01060001 부처 업무계획 | Government Work Plan
```

#### 일반화 필요

```
변경 전: T01060001 2023~2027 국가재정운용계획 | 2023-2027 Medium-term Fiscal Plan
변경 후: T01060001 국가재정운용계획 | National Fiscal Plan

변경 전: T01060002 재정동향 2024년 4월호 | April 2024 Fiscal Trends Report
변경 후: T01060002 재정동향 | Fiscal Trends Report

변경 전: T01060010 2024년 국립대학육성사업 기본계획 | 2024 National University Fostering Plan
변경 후: T01060003 국립대학육성사업 | National University Fostering Program

변경 전: T01060011 제4차 학교도서관 진흥 기본계획 | 4th School Library Promotion Plan
변경 후: T01060004 학교도서관 진흥계획 | School Library Promotion Plan

변경 전: T01060014 2024 앙골라 개황 | 2024 Angola Country Report
변경 후: T01060005 국가 개황 | Country Profile Report
```

#### 삭제 검토

```
- T01060013 도로터널 결로대책 가이드라인 | Road Tunnel Condensation Guideline
  → 너무 구체적, 삭제 권장
```

#### 유지 (제도명)

```
✅ T01060012 청년농업인 신용보증 | Young Farmer Credit Guarantee
✅ T01060015 항공 전문교육기관 지정제도 | Aviation Training Institute Designation System
✅ T01060016 항공훈련기관 안전감독 | Aviation Training Safety Oversight
```

---

### 06. 법률 (Law)

#### 개념 용어 유지

```
✅ T06010001 판례 | Precedent
✅ T06010002 대법원 판결 | Supreme Court Decision
✅ T06010003 헌법재판소 결정 | Constitutional Court Decision
✅ T06020001 소득세 | Income Tax
✅ T06020002 법인세 | Corporate Tax
✅ T06020003 부가가치세 | Value Added Tax [VAT]
✅ T06020004 상속세·증여세 | Inheritance Tax / Gift Tax
✅ T06030001 국가공무원법 | State Public Officials Act
✅ T06030002 행정절차법 | Administrative Procedure Act
```

#### 삭제 대상 (특정 판례명)

```
삭제:
- T06010004 분양점포 기둥 미고지 판결
- T06010005 미용 필러 의료과실 판결
- T06010006 아이폰 성능저하 집단소송 판결
- T06010007 특허권 침해금지청구권 부존재 확인 판결
- T06010008 유도가열식 미세입자발생장치 거절결정 판결
- T06010009 통신비밀보호법 위반 판결
- T06010010 상호출자제한기업집단 의결권 시정명령 취소 판결
- T06010011 관세 로열티 과세판결
- T06010012 공무원연금 환수처분 판결

→ 이유: 특정 사건, 재사용 불가능한 인스턴스
```

#### 일반화 필요

```
변경 전: T06020007 2024 달라지는 세금제도 | 2024 Tax Changes Guide
변경 후: T06020005 세제 개편 | Tax Reform

추가:
- T06020006 가상자산 과세 | Crypto Asset Taxation
```

#### 유지 (개념)

```
✅ T06020005 비거주자 가상자산 국내원천소득 | Crypto-source Income for Non-residents
  → 변경: T06020007 비거주자 가상자산 과세 | Non-resident Crypto Taxation

✅ T06020006 가상자산 거래소 원천징수 의무 | Withholding Duty for Crypto Exchanges
  → 변경: T06020008 가상자산 원천징수 | Crypto Withholding Tax
```

---

### 07. 의료 (Medical)

#### 개념 용어 유지

```
✅ T07010001 암 | Cancer
✅ T07010002 대장암 | Colorectal Cancer [CRC]
✅ T07010003 다발성골수종 | Multiple Myeloma [MM]
✅ T07010004 항암화학요법 | Chemotherapy
✅ T07020001 안구건조증 | Dry Eye Syndrome [DES]
✅ T07020002 백내장 | Cataract
✅ T07020003 녹내장 | Glaucoma
✅ T07020004 황반변성 | Macular Degeneration [AMD]
✅ T07030001 위식도역류질환 | Gastroesophageal Reflux Disease [GERD]
✅ T07030002 내시경 | Endoscopy
✅ T07040001 건강검진 | Health Screening
✅ T07040002 예방의학 | Preventive Medicine
```

#### 삭제 대상 (문서/가이드 제목)

```
삭제:
- T07010005 NCCN 대장암 검진 가이드 2024
- T07010006 알기 쉬운 대장암 가이드
- T07010007 조기발병 대장암 리뷰
- T07010008 대장암 위험요인 역학보고
- T07010009 제2형 당뇨병과 대장암 연관 연구
- T07010010 대장암 초기증상·검사 분석
- T07010011 암환자 생활세계 경험 연구
- T07010013 암환자 뇌혈관질환 임상 분석
- T07010014 다발성골수종 환자 가이드 2022
- T07020005 바이러스 결막염 관리지침
- T07020006 겨울철 위험 안과질환 예방 가이드
- T07020007 눈건강 9대 생활수칙
- T07020008 안구건조증 약물요법 가이드
- T07030003 위암 스크리닝·진단 가이드
- T07030004 위식도역류 환자 안내서
- T07040003 어린이 안질환 안내

→ 이유: 특정 문서/가이드 제목, 일회성
```

#### 추가 권장 (개념 용어)

```
추가:
- T07010005 암 검진 | Cancer Screening
- T07010006 암 치료 | Cancer Treatment
- T07010007 환자 네비게이션 | Patient Navigation
- T07020005 안과 질환 예방 | Eye Disease Prevention
- T07030003 위암 검진 | Gastric Cancer Screening
```

---

## 금융/커머스/산업/사회 도메인

### 02. 금융 - 현재 상태 양호 ✅
대부분 개념적 용어로 구성됨. 수정 불필요.

### 03. 커머스 - 일부 수정 필요

```
변경 전: T03010006 2022 메조미디어 이커머스 리포트
삭제 권장

변경 전: T03010007 국내 이커머스 재편 분석
삭제 권장

변경 전: T03030008 2021 중국 라이브커머스 산업 보고
삭제 권장
```

### 04. 산업 - 현재 상태 양호 ✅

### 05. 사회 - 현재 상태 양호 ✅

---

## 최종 통계

### 변경 전
- 총 용어: 148개
- 개념 용어: ~108개
- 문서/인스턴스: ~40개

### 변경 후 (예상)
- 총 용어: ~75개
- 개념 용어: 75개 (100%)
- 문서/인스턴스: 0개

---

## 권장 사항

1. **문서 제목 완전 삭제**: 연도별 계획서, 보고서 등
2. **판례명 삭제**: 특정 사건
3. **가이드 제목 삭제**: 특정 버전/연도의 가이드
4. **개념으로 일반화**: 시간 독립적인 용어만 유지
5. **중복 제거**: 같은 개념의 연도별 용어 통합

이렇게 하면 **재사용 가능한 온톨로지**가 구축됩니다.
