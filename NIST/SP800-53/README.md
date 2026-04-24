# NIST SP 800-53 Rev. 5: 보안 및 프라이버시 컨트롤

## 개요

| 항목 | 내용 |
|------|------|
| **정식 명칭** | Security and Privacy Controls for Information Systems and Organizations |
| **문서 번호** | SP 800-53 Revision 5, Update 1 |
| **발행일** | 2020년 9월 (Rev. 5 최초 발행), 이후 Update 1 반영 |
| **대상** | 연방 정보시스템 및 조직 (민간 부문에서도 널리 참조) |
| **원문** | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |

SP 800-53은 NIST 사이버보안 체계의 **핵심 문서**입니다. 조직이 정보시스템과 데이터를 보호하기 위해 구현해야 하는 보안 및 프라이버시 **컨트롤** (통제)의 카탈로그를 제공합니다.

---

## 53 시리즈 구성

SP 800-53은 단독으로 사용되지 않으며, 3개 문서가 함께 작동합니다:

| 문서 | 역할 | 핵심 질문 |
|------|------|----------|
| **SP 800-53** | 컨트롤 카탈로그 | "어떤 통제 항목이 존재하는가?" |
| **SP 800-53A** | 평가 절차 | "컨트롤이 제대로 구현되었는지 어떻게 검증하는가?" |
| **SP 800-53B** | 기준선 (Baselines) | "우리 시스템에 어떤 컨트롤을 적용해야 하는가?" |

---

## Rev. 5의 주요 변경점 (vs Rev. 4)

| 변경 사항 | 설명 |
|-----------|------|
| **프라이버시 컨트롤 통합** | 기존 별도 부록이었던 프라이버시 컨트롤이 본문에 통합. PT, PM 패밀리 확대 |
| **SR 패밀리 신설** | Supply Chain Risk Management — 공급망 리스크 관리 컨트롤 추가 |
| **PT 패밀리 신설** | PII Processing and Transparency — 개인정보 처리 및 투명성 컨트롤 추가 |
| **"연방" 한정 제거** | 컨트롤 문구에서 "federal"을 제거하여 모든 조직이 활용 가능하도록 범용화 |
| **성과 기반으로 전환** | 컨트롤이 "무엇을 해야 하는가"(what)에 집중하며, "어떻게"(how)는 조직이 결정 |

---

## 수치 요약

| 구분 | 수량 |
|------|------|
| 컨트롤 패밀리 | 20개 |
| Base 컨트롤 | 300개 |
| Enhancement 컨트롤 | 714개 |
| Withdrawn 컨트롤 | 182개 |
| **총 컨트롤** (base + enhancement + withdrawn) | **1,196개** |
| **활성 컨트롤** (base + enhancement) | **1,014개** |

---

## 기준선 (Baselines)

SP 800-53B는 시스템의 **영향도** (Impact Level)에 따라 적용할 컨트롤 세트를 정의합니다. 영향도는 FIPS 199에 의해 결정됩니다.

| 기준선 | 영향도 | 컨트롤 수 | 적용 상황 | 체크리스트 |
|--------|--------|----------|----------|-----------|
| **LOW** | 제한적 피해 | 149개 | 기밀성/무결성/가용성 손실 시 피해가 제한적 | [LOW 체크리스트](./low.md) |
| **MODERATE** | 심각한 피해 | 287개 | 피해가 심각한 수준 | [MODERATE 체크리스트](./moderate.md) |
| **HIGH** | 치명적 피해 | 370개 | 피해가 치명적/재앙적 | [HIGH 체크리스트](./high.md) |
| **PRIVACY** | 개인정보 | 별도 | PII를 처리하는 시스템에 적용 | — |

> 컨트롤 수는 NIST OSCAL 공식 프로파일 기준입니다.  
> PM(Program Management)과 PT(PII Processing and Transparency) 패밀리는 기준선에 포함되지 않으며, 조직 수준에서 별도 적용됩니다.

---

## 컨트롤 구조 이해

### 컨트롤의 구성 요소

각 컨트롤은 다음 요소로 구성됩니다:

| 요소 | 설명 | 예시 (AC-02) |
|------|------|-------------|
| **ID** | 패밀리 코드 + 번호 | AC-02 |
| **Title** | 컨트롤 명칭 | Account Management |
| **Statement** | 컨트롤이 요구하는 성과 | "시스템 계정을 정의·생성·활성화·수정·비활성화·제거한다" |
| **Guidance** | 구현 지침 | 계정 유형, 조건, 자동화 방법 등 |
| **Enhancement** | 강화 항목 (하위 컨트롤) | AC-02(01): 자동화된 계정 관리 |
| **Related Controls** | 관련 컨트롤 참조 | IA-01, IA-04, IA-05... |
| **Baselines** | 적용 기준선 | L/M/H |

### Base 컨트롤과 Enhancement의 관계

SP 800-53의 컨트롤은 **Base 컨트롤**과 **Enhancement(강화 항목)** 두 계층으로 구성됩니다.

- **Base 컨트롤**: 독립적으로 존재하는 기본 통제 항목 (예: AC-02)
- **Enhancement**: Base에 종속되는 강화 요구사항. 독립적으로 존재할 수 없음 (예: AC-02(01))

Enhancement은 `AC-02(01)`처럼 **괄호 번호**로 표기됩니다. 시스템의 영향도가 높아질수록(LOW → MODERATE → HIGH) 더 많은 Enhancement이 필수로 적용됩니다.

**예시: AC-02 (Account Management)의 계층 구조**

```
AC-02 (Base) — 계정 관리                              [LOW / MODERATE / HIGH]
│  "시스템 계정을 정의·생성·활성화·수정·비활성화·제거한다"
│
├── AC-02(01) — 자동화된 계정 관리                      [MODERATE / HIGH]
├── AC-02(02) — 임시/긴급 계정 자동 관리                 [MODERATE / HIGH]
├── AC-02(03) — 비활성 계정 비활성화                     [MODERATE / HIGH]
├── AC-02(04) — 자동 감사 조치                          [MODERATE / HIGH]
├── AC-02(05) — 비활성 로그아웃                          [MODERATE / HIGH]
├── AC-02(06) — 동적 권한 관리                          [—]
├── AC-02(07) — 특권 사용자 계정                        [—]
├── AC-02(08) — 동적 계정 관리                          [—]
├── AC-02(09) — 공유/그룹 계정 사용 제한                 [—]
├── AC-02(11) — 사용 조건                              [HIGH]
├── AC-02(12) — 비정형 사용 모니터링                     [HIGH]
└── AC-02(13) — 고위험 개인 계정 비활성화                 [MODERATE / HIGH]
```

위 예시에서:
- **LOW** 시스템: AC-02(Base)만 구현
- **MODERATE** 시스템: AC-02 + AC-02(01)~(05), (13) 구현
- **HIGH** 시스템: AC-02 + AC-02(01)~(05), (11), (12), (13) 구현
- `—` 표시 항목: 기준선에 미포함. 조직이 필요에 따라 선택적으로 적용

---

## 20개 컨트롤 패밀리 — 전체 Base 컨트롤 목록

### 한눈에 보기

| 코드 | 패밀리 | Base | Enhancement | 활성 합계 |
|------|--------|------|-------------|----------|
| AC | Access Control | 23 | 108 | 131 |
| AT | Awareness and Training | 5 | 10 | 15 |
| AU | Audit and Accountability | 15 | 41 | 56 |
| CA | Assessment, Authorization, and Monitoring | 8 | 17 | 25 |
| CM | Configuration Management | 14 | 42 | 56 |
| CP | Contingency Planning | 12 | 37 | 49 |
| IA | Identification and Authentication | 13 | 46 | 59 |
| IR | Incident Response | 9 | 31 | 40 |
| MA | Maintenance | 7 | 21 | 28 |
| MP | Media Protection | 8 | 12 | 20 |
| PE | Physical and Environmental Protection | 22 | 29 | 51 |
| PL | Planning | 8 | 3 | 11 |
| PM | Program Management | 32 | 5 | 37 |
| PS | Personnel Security | 9 | 8 | 17 |
| PT | PII Processing and Transparency | 8 | 13 | 21 |
| RA | Risk Assessment | 9 | 13 | 22 |
| SA | System and Services Acquisition | 17 | 91 | 108 |
| SC | System and Communications Protection | 47 | 92 | 139 |
| SI | System and Information Integrity | 22 | 80 | 102 |
| SR | Supply Chain Risk Management | 12 | 15 | 27 |
| | **합계** | **300** | **714** | **1,014** |

> 아래 각 패밀리를 클릭하면 Base 컨트롤 전체 목록을 확인할 수 있습니다.  
> 기준선 컬럼: L=LOW, M=MODERATE, H=HIGH, —=기준선 미포함  
> 컨트롤 번호에 갭이 있는 경우(예: AT-04 다음에 AT-06)가 있습니다. 이는 해당 번호의 컨트롤이 Withdrawn(폐지)된 결과이며, 누락이 아닙니다.

---

<details>
<summary><b>AC — Access Control (23 base / 108 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| AC-01 | Policy and Procedures | L/M/H | — |
| AC-02 | Account Management | L/M/H | 12개 |
| AC-03 | Access Enforcement | L/M/H | 13개 |
| AC-04 | Information Flow Enforcement | M/H | 30개 |
| AC-05 | Separation of Duties | M/H | — |
| AC-06 | Least Privilege | M/H | 10개 |
| AC-07 | Unsuccessful Logon Attempts | L/M/H | 3개 |
| AC-08 | System Use Notification | L/M/H | — |
| AC-09 | Previous Logon Notification | — | 4개 |
| AC-10 | Concurrent Session Control | H | — |
| AC-11 | Device Lock | M/H | 1개 |
| AC-12 | Session Termination | M/H | 3개 |
| AC-14 | Permitted Actions Without Identification or Authentication | L/M/H | — |
| AC-16 | Security and Privacy Attributes | — | 10개 |
| AC-17 | Remote Access | L/M/H | 7개 |
| AC-18 | Wireless Access | L/M/H | 4개 |
| AC-19 | Access Control for Mobile Devices | L/M/H | 2개 |
| AC-20 | Use of External Systems | L/M/H | 5개 |
| AC-21 | Information Sharing | M/H | 2개 |
| AC-22 | Publicly Accessible Content | L/M/H | — |
| AC-23 | Data Mining Protection | — | — |
| AC-24 | Access Control Decisions | — | 2개 |
| AC-25 | Reference Monitor | — | — |

</details>

<details>
<summary><b>AT — Awareness and Training (5 base / 10 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| AT-01 | Policy and Procedures | L/M/H | — |
| AT-02 | Literacy Training and Awareness | L/M/H | 6개 |
| AT-03 | Role-based Training | L/M/H | 4개 |
| AT-04 | Training Records | L/M/H | — |
| AT-06 | Training Feedback | — | — |

</details>

<details>
<summary><b>AU — Audit and Accountability (15 base / 41 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| AU-01 | Policy and Procedures | L/M/H | — |
| AU-02 | Event Logging | L/M/H | — |
| AU-03 | Content of Audit Records | L/M/H | 2개 |
| AU-04 | Audit Log Storage Capacity | L/M/H | 1개 |
| AU-05 | Response to Audit Logging Process Failures | L/M/H | 5개 |
| AU-06 | Audit Record Review, Analysis, and Reporting | L/M/H | 8개 |
| AU-07 | Audit Record Reduction and Report Generation | M/H | 1개 |
| AU-08 | Time Stamps | L/M/H | — |
| AU-09 | Protection of Audit Information | L/M/H | 7개 |
| AU-10 | Non-repudiation | H | 4개 |
| AU-11 | Audit Record Retention | L/M/H | 1개 |
| AU-12 | Audit Record Generation | L/M/H | 4개 |
| AU-13 | Monitoring for Information Disclosure | — | 3개 |
| AU-14 | Session Audit | — | 2개 |
| AU-16 | Cross-organizational Audit Logging | — | 3개 |

</details>

<details>
<summary><b>CA — Assessment, Authorization, and Monitoring (8 base / 17 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| CA-01 | Policy and Procedures | L/M/H | — |
| CA-02 | Control Assessments | L/M/H | 3개 |
| CA-03 | Information Exchange | L/M/H | 2개 |
| CA-05 | Plan of Action and Milestones | L/M/H | 1개 |
| CA-06 | Authorization | L/M/H | 2개 |
| CA-07 | Continuous Monitoring | L/M/H | 5개 |
| CA-08 | Penetration Testing | H | 3개 |
| CA-09 | Internal System Connections | L/M/H | 1개 |

</details>

<details>
<summary><b>CM — Configuration Management (14 base / 42 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| CM-01 | Policy and Procedures | L/M/H | — |
| CM-02 | Baseline Configuration | L/M/H | 4개 |
| CM-03 | Configuration Change Control | M/H | 8개 |
| CM-04 | Impact Analyses | L/M/H | 2개 |
| CM-05 | Access Restrictions for Change | L/M/H | 4개 |
| CM-06 | Configuration Settings | L/M/H | 2개 |
| CM-07 | Least Functionality | L/M/H | 9개 |
| CM-08 | System Component Inventory | L/M/H | 8개 |
| CM-09 | Configuration Management Plan | M/H | 1개 |
| CM-10 | Software Usage Restrictions | L/M/H | 1개 |
| CM-11 | User-installed Software | L/M/H | 2개 |
| CM-12 | Information Location | M/H | 1개 |
| CM-13 | Data Action Mapping | — | — |
| CM-14 | Signed Components | — | — |

</details>

<details>
<summary><b>CP — Contingency Planning (12 base / 37 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| CP-01 | Policy and Procedures | L/M/H | — |
| CP-02 | Contingency Plan | L/M/H | 7개 |
| CP-03 | Contingency Training | L/M/H | 2개 |
| CP-04 | Contingency Plan Testing | L/M/H | 5개 |
| CP-06 | Alternate Storage Site | M/H | 3개 |
| CP-07 | Alternate Processing Site | M/H | 5개 |
| CP-08 | Telecommunications Services | M/H | 5개 |
| CP-09 | System Backup | L/M/H | 7개 |
| CP-10 | System Recovery and Reconstitution | L/M/H | 3개 |
| CP-11 | Alternate Communications Protocols | — | — |
| CP-12 | Safe Mode | — | — |
| CP-13 | Alternative Security Mechanisms | — | — |

</details>

<details>
<summary><b>IA — Identification and Authentication (13 base / 46 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| IA-01 | Policy and Procedures | L/M/H | — |
| IA-02 | Identification and Authentication (Organizational Users) | L/M/H | 8개 |
| IA-03 | Device Identification and Authentication | M/H | 3개 |
| IA-04 | Identifier Management | L/M/H | 6개 |
| IA-05 | Authenticator Management | L/M/H | 15개 |
| IA-06 | Authentication Feedback | L/M/H | — |
| IA-07 | Cryptographic Module Authentication | L/M/H | — |
| IA-08 | Identification and Authentication (Non-organizational Users) | L/M/H | 5개 |
| IA-09 | Service Identification and Authentication | — | — |
| IA-10 | Adaptive Authentication | — | — |
| IA-11 | Re-authentication | L/M/H | — |
| IA-12 | Identity Proofing | M/H | 6개 |
| IA-13 | Identity Providers and Authorization Servers | — | 3개 |

</details>

<details>
<summary><b>IR — Incident Response (9 base / 31 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| IR-01 | Policy and Procedures | L/M/H | — |
| IR-02 | Incident Response Training | L/M/H | 3개 |
| IR-03 | Incident Response Testing | M/H | 3개 |
| IR-04 | Incident Handling | L/M/H | 15개 |
| IR-05 | Incident Monitoring | L/M/H | 1개 |
| IR-06 | Incident Reporting | L/M/H | 3개 |
| IR-07 | Incident Response Assistance | L/M/H | 2개 |
| IR-08 | Incident Response Plan | L/M/H | 1개 |
| IR-09 | Information Spillage Response | — | 3개 |

</details>

<details>
<summary><b>MA — Maintenance (7 base / 21 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| MA-01 | Policy and Procedures | L/M/H | — |
| MA-02 | Controlled Maintenance | L/M/H | 1개 |
| MA-03 | Maintenance Tools | M/H | 6개 |
| MA-04 | Nonlocal Maintenance | L/M/H | 6개 |
| MA-05 | Maintenance Personnel | L/M/H | 5개 |
| MA-06 | Timely Maintenance | M/H | 3개 |
| MA-07 | Field Maintenance | — | — |

</details>

<details>
<summary><b>MP — Media Protection (8 base / 12 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| MP-01 | Policy and Procedures | L/M/H | — |
| MP-02 | Media Access | L/M/H | — |
| MP-03 | Media Marking | M/H | — |
| MP-04 | Media Storage | M/H | 1개 |
| MP-05 | Media Transport | M/H | 1개 |
| MP-06 | Media Sanitization | L/M/H | 5개 |
| MP-07 | Media Use | L/M/H | 1개 |
| MP-08 | Media Downgrading | — | 4개 |

</details>

<details>
<summary><b>PE — Physical and Environmental Protection (22 base / 29 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| PE-01 | Policy and Procedures | L/M/H | — |
| PE-02 | Physical Access Authorizations | L/M/H | 3개 |
| PE-03 | Physical Access Control | L/M/H | 7개 |
| PE-04 | Access Control for Transmission | M/H | — |
| PE-05 | Access Control for Output Devices | M/H | 1개 |
| PE-06 | Monitoring Physical Access | L/M/H | 4개 |
| PE-08 | Visitor Access Records | L/M/H | 2개 |
| PE-09 | Power Equipment and Cabling | M/H | 2개 |
| PE-10 | Emergency Shutoff | M/H | — |
| PE-11 | Emergency Power | M/H | 2개 |
| PE-12 | Emergency Lighting | L/M/H | 1개 |
| PE-13 | Fire Protection | L/M/H | 3개 |
| PE-14 | Environmental Controls | L/M/H | 2개 |
| PE-15 | Water Damage Protection | L/M/H | 1개 |
| PE-16 | Delivery and Removal | L/M/H | — |
| PE-17 | Alternate Work Site | M/H | — |
| PE-18 | Location of System Components | H | — |
| PE-19 | Information Leakage | — | 1개 |
| PE-20 | Asset Monitoring and Tracking | — | — |
| PE-21 | Electromagnetic Pulse Protection | — | — |
| PE-22 | Component Marking | — | — |
| PE-23 | Facility Location | — | — |

</details>

<details>
<summary><b>PL — Planning (8 base / 3 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| PL-01 | Policy and Procedures | L/M/H | — |
| PL-02 | System Security and Privacy Plans | L/M/H | — |
| PL-04 | Rules of Behavior | L/M/H | 1개 |
| PL-07 | Concept of Operations | — | — |
| PL-08 | Security and Privacy Architectures | M/H | 2개 |
| PL-09 | Central Management | — | — |
| PL-10 | Baseline Selection | L/M/H | — |
| PL-11 | Baseline Tailoring | L/M/H | — |

</details>

<details>
<summary><b>PM — Program Management (32 base / 5 enhancement)</b></summary>

| 컨트롤 | 제목 | Enhancement |
|--------|------|-------------|
| PM-01 | Information Security Program Plan | — |
| PM-02 | Information Security Program Leadership Role | — |
| PM-03 | Information Security and Privacy Resources | — |
| PM-04 | Plan of Action and Milestones Process | — |
| PM-05 | System Inventory | 1개 |
| PM-06 | Measures of Performance | — |
| PM-07 | Enterprise Architecture | 1개 |
| PM-08 | Critical Infrastructure Plan | — |
| PM-09 | Risk Management Strategy | — |
| PM-10 | Authorization Process | — |
| PM-11 | Mission and Business Process Definition | — |
| PM-12 | Insider Threat Program | — |
| PM-13 | Security and Privacy Workforce | — |
| PM-14 | Testing, Training, and Monitoring | — |
| PM-15 | Security and Privacy Groups and Associations | — |
| PM-16 | Threat Awareness Program | 1개 |
| PM-17 | Protecting Controlled Unclassified Information on External Systems | — |
| PM-18 | Privacy Program Plan | — |
| PM-19 | Privacy Program Leadership Role | — |
| PM-20 | Dissemination of Privacy Program Information | 1개 |
| PM-21 | Accounting of Disclosures | — |
| PM-22 | Personally Identifiable Information Quality Management | — |
| PM-23 | Data Governance Body | — |
| PM-24 | Data Integrity Board | — |
| PM-25 | Minimization of Personally Identifiable Information Used in Testing, Training, and Research | — |
| PM-26 | Complaint Management | — |
| PM-27 | Privacy Reporting | — |
| PM-28 | Risk Framing | — |
| PM-29 | Risk Management Program Leadership Roles | — |
| PM-30 | Supply Chain Risk Management Strategy | 1개 |
| PM-31 | Continuous Monitoring Strategy | — |
| PM-32 | Purposing | — |

</details>

<details>
<summary><b>PS — Personnel Security (9 base / 8 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| PS-01 | Policy and Procedures | L/M/H | — |
| PS-02 | Position Risk Designation | L/M/H | — |
| PS-03 | Personnel Screening | L/M/H | 4개 |
| PS-04 | Personnel Termination | L/M/H | 2개 |
| PS-05 | Personnel Transfer | L/M/H | — |
| PS-06 | Access Agreements | L/M/H | 2개 |
| PS-07 | External Personnel Security | L/M/H | — |
| PS-08 | Personnel Sanctions | L/M/H | — |
| PS-09 | Position Descriptions | L/M/H | — |

</details>

<details>
<summary><b>PT — Personally Identifiable Information Processing and Transparency (8 base / 13 enhancement)</b></summary>

| 컨트롤 | 제목 | Enhancement |
|--------|------|-------------|
| PT-01 | Policy and Procedures | — |
| PT-02 | Authority to Process Personally Identifiable Information | 2개 |
| PT-03 | Personally Identifiable Information Processing Purposes | 2개 |
| PT-04 | Consent | 3개 |
| PT-05 | Privacy Notice | 2개 |
| PT-06 | System of Records Notice | 2개 |
| PT-07 | Specific Categories of Personally Identifiable Information | 2개 |
| PT-08 | Computer Matching Requirements | — |

</details>

<details>
<summary><b>RA — Risk Assessment (9 base / 13 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| RA-01 | Policy and Procedures | L/M/H | — |
| RA-02 | Security Categorization | L/M/H | 1개 |
| RA-03 | Risk Assessment | L/M/H | 4개 |
| RA-05 | Vulnerability Monitoring and Scanning | L/M/H | 8개 |
| RA-06 | Technical Surveillance Countermeasures Survey | — | — |
| RA-07 | Risk Response | L/M/H | — |
| RA-08 | Privacy Impact Assessments | — | — |
| RA-09 | Criticality Analysis | M/H | — |
| RA-10 | Threat Hunting | — | — |

</details>

<details>
<summary><b>SA — System and Services Acquisition (17 base / 91 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| SA-01 | Policy and Procedures | L/M/H | — |
| SA-02 | Allocation of Resources | L/M/H | — |
| SA-03 | System Development Life Cycle | L/M/H | 3개 |
| SA-04 | Acquisition Process | L/M/H | 11개 |
| SA-05 | System Documentation | L/M/H | — |
| SA-08 | Security and Privacy Engineering Principles | L/M/H | 33개 |
| SA-09 | External System Services | L/M/H | 8개 |
| SA-10 | Developer Configuration Management | M/H | 7개 |
| SA-11 | Developer Testing and Evaluation | M/H | 9개 |
| SA-15 | Development Process, Standards, and Tools | M/H | 11개 |
| SA-16 | Developer-provided Training | H | — |
| SA-17 | Developer Security and Privacy Architecture and Design | H | 9개 |
| SA-20 | Customized Development of Critical Components | — | — |
| SA-21 | Developer Screening | H | — |
| SA-22 | Unsupported System Components | L/M/H | — |
| SA-23 | Specialization | — | — |
| SA-24 | Design For Cyber Resiliency | — | — |

</details>

<details>
<summary><b>SC — System and Communications Protection (47 base / 92 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| SC-01 | Policy and Procedures | L/M/H | — |
| SC-02 | Separation of System and User Functionality | M/H | 2개 |
| SC-03 | Security Function Isolation | H | 5개 |
| SC-04 | Information in Shared System Resources | M/H | 1개 |
| SC-05 | Denial-of-service Protection | L/M/H | 3개 |
| SC-06 | Resource Availability | — | — |
| SC-07 | Boundary Protection | L/M/H | 26개 |
| SC-08 | Transmission Confidentiality and Integrity | M/H | 5개 |
| SC-10 | Network Disconnect | M/H | — |
| SC-11 | Trusted Path | — | 1개 |
| SC-12 | Cryptographic Key Establishment and Management | L/M/H | 4개 |
| SC-13 | Cryptographic Protection | L/M/H | — |
| SC-15 | Collaborative Computing Devices and Applications | L/M/H | 3개 |
| SC-16 | Transmission of Security and Privacy Attributes | — | 3개 |
| SC-17 | Public Key Infrastructure Certificates | M/H | — |
| SC-18 | Mobile Code | M/H | 5개 |
| SC-20 | Secure Name/Address Resolution Service (Authoritative Source) | L/M/H | 1개 |
| SC-21 | Secure Name/Address Resolution Service (Recursive or Caching Resolver) | L/M/H | — |
| SC-22 | Architecture and Provisioning for Name/Address Resolution Service | L/M/H | — |
| SC-23 | Session Authenticity | M/H | 3개 |
| SC-24 | Fail in Known State | H | — |
| SC-25 | Thin Nodes | — | — |
| SC-26 | Decoys | — | — |
| SC-27 | Platform-independent Applications | — | — |
| SC-28 | Protection of Information at Rest | M/H | 3개 |
| SC-29 | Heterogeneity | — | 1개 |
| SC-30 | Concealment and Misdirection | — | 4개 |
| SC-31 | Covert Channel Analysis | — | 3개 |
| SC-32 | System Partitioning | — | 1개 |
| SC-34 | Non-modifiable Executable Programs | — | 2개 |
| SC-35 | External Malicious Code Identification | — | — |
| SC-36 | Distributed Processing and Storage | — | 2개 |
| SC-37 | Out-of-band Channels | — | 1개 |
| SC-38 | Operations Security | — | — |
| SC-39 | Process Isolation | L/M/H | 2개 |
| SC-40 | Wireless Link Protection | — | 4개 |
| SC-41 | Port and I/O Device Access | — | — |
| SC-42 | Sensor Capability and Data | — | 4개 |
| SC-43 | Usage Restrictions | — | — |
| SC-44 | Detonation Chambers | — | — |
| SC-45 | System Time Synchronization | — | 2개 |
| SC-46 | Cross Domain Policy Enforcement | — | — |
| SC-47 | Alternate Communications Paths | — | — |
| SC-48 | Sensor Relocation | — | 1개 |
| SC-49 | Hardware-enforced Separation and Policy Enforcement | — | — |
| SC-50 | Software-enforced Separation and Policy Enforcement | — | — |
| SC-51 | Hardware-based Protection | — | — |

</details>

<details>
<summary><b>SI — System and Information Integrity (22 base / 80 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| SI-01 | Policy and Procedures | L/M/H | — |
| SI-02 | Flaw Remediation | L/M/H | 6개 |
| SI-03 | Malicious Code Protection | L/M/H | 4개 |
| SI-04 | System Monitoring | L/M/H | 23개 |
| SI-05 | Security Alerts, Advisories, and Directives | L/M/H | 1개 |
| SI-06 | Security and Privacy Function Verification | H | 2개 |
| SI-07 | Software, Firmware, and Information Integrity | M/H | 13개 |
| SI-08 | Spam Protection | M/H | 2개 |
| SI-10 | Information Input Validation | M/H | 6개 |
| SI-11 | Error Handling | M/H | — |
| SI-12 | Information Management and Retention | L/M/H | 3개 |
| SI-13 | Predictable Failure Prevention | — | 4개 |
| SI-14 | Non-persistence | — | 3개 |
| SI-15 | Information Output Filtering | — | — |
| SI-16 | Memory Protection | M/H | — |
| SI-17 | Fail-safe Procedures | — | — |
| SI-18 | Personally Identifiable Information Quality Operations | — | 5개 |
| SI-19 | De-identification | — | 8개 |
| SI-20 | Tainting | — | — |
| SI-21 | Information Refresh | — | — |
| SI-22 | Information Diversity | — | — |
| SI-23 | Information Fragmentation | — | — |

</details>

<details>
<summary><b>SR — Supply Chain Risk Management (12 base / 15 enhancement)</b></summary>

| 컨트롤 | 제목 | 기준선 | Enhancement |
|--------|------|--------|-------------|
| SR-01 | Policy and Procedures | L/M/H | — |
| SR-02 | Supply Chain Risk Management Plan | L/M/H | 1개 |
| SR-03 | Supply Chain Controls and Processes | L/M/H | 3개 |
| SR-04 | Provenance | — | 4개 |
| SR-05 | Acquisition Strategies, Tools, and Methods | L/M/H | 2개 |
| SR-06 | Supplier Assessments and Reviews | M/H | 1개 |
| SR-07 | Supply Chain Operations Security | — | — |
| SR-08 | Notification Agreements | L/M/H | — |
| SR-09 | Tamper Resistance and Detection | H | 1개 |
| SR-10 | Inspection of Systems or Components | L/M/H | — |
| SR-11 | Component Authenticity | L/M/H | 3개 |
| SR-12 | Component Disposal | L/M/H | — |

</details>

---

## 참고 자료

| 리소스 | URL |
|--------|-----|
| SP 800-53 Rev. 5 원문 | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| SP 800-53A (평가 절차) | https://csrc.nist.gov/pubs/sp/800/53/a/r5/final |
| SP 800-53B (기준선) | https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final |
| OSCAL 컨트롤 카탈로그 (JSON) | https://github.com/usnistgov/oscal-content/tree/main/nist.gov/SP800-53/rev5 |
| CPRT (컨트롤 참조 도구) | https://csrc.nist.gov/projects/cprt |
| CSF 2.0 ↔ SP 800-53 매핑 | https://csrc.nist.gov/files/pubs/sp/800/53/r5/upd1/final/docs/csf-pf-to-sp800-53r5-mappings.xlsx |
