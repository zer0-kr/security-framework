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

| 기준선 | 영향도 | 컨트롤 수 | 적용 상황 |
|--------|--------|----------|----------|
| **LOW** | 제한적 피해 | 149개 | 기밀성/무결성/가용성 손실 시 피해가 제한적 |
| **MODERATE** | 심각한 피해 | 287개 | 피해가 심각한 수준 |
| **HIGH** | 치명적 피해 | 370개 | 피해가 치명적/재앙적 |
| **PRIVACY** | 개인정보 | 별도 | PII를 처리하는 시스템에 적용 |

> 컨트롤 수는 NIST OSCAL 공식 프로파일 기준입니다.  
> PM(Program Management)과 PT(PII Processing and Transparency) 패밀리는 기준선에 포함되지 않으며, 조직 수준에서 별도 적용됩니다.

---

## 컨트롤 구조 이해

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

> Enhancement은 "AC-02(01)"처럼 괄호 번호로 표기됩니다. Base 컨트롤의 요구사항을 더 구체화하거나 강화합니다.

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

> 아래 각 패밀리를 클릭하면 Base 컨트롤과 Enhancement의 전체 목록을 확인할 수 있습니다.  
> **굵은 글씨** = Base 컨트롤, ↳ = Enhancement (Base에 종속되는 강화 항목)  
> 기준선 컬럼: L=LOW, M=MODERATE, H=HIGH, —=기준선 미포함  
> 컨트롤 번호에 갭이 있는 경우(예: AT-04 다음에 AT-06)가 있습니다. 이는 해당 번호의 컨트롤이 Withdrawn(폐지)된 결과이며, 누락이 아닙니다.

---

<details>
<summary><b>AC — Access Control (23 base / 108 enhancement)</b></summary>

- **AC-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>AC-02</b> — Account Management [L/M/H] (12개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-02(01) | Automated System Account Management | M/H |
| AC-02(02) | Automated Temporary and Emergency Account Management | M/H |
| AC-02(03) | Disable Accounts | M/H |
| AC-02(04) | Automated Audit Actions | M/H |
| AC-02(05) | Inactivity Logout | M/H |
| AC-02(06) | Dynamic Privilege Management | — |
| AC-02(07) | Privileged User Accounts | — |
| AC-02(08) | Dynamic Account Management | — |
| AC-02(09) | Restrictions on Use of Shared and Group Accounts | — |
| AC-02(11) | Usage Conditions | H |
| AC-02(12) | Account Monitoring for Atypical Usage | H |
| AC-02(13) | Disable Accounts for High-risk Individuals | M/H |

</details>
<details>
<summary><b>AC-03</b> — Access Enforcement [L/M/H] (13개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-03(02) | Dual Authorization | — |
| AC-03(03) | Mandatory Access Control | — |
| AC-03(04) | Discretionary Access Control | — |
| AC-03(05) | Security-relevant Information | — |
| AC-03(07) | Role-based Access Control | — |
| AC-03(08) | Revocation of Access Authorizations | — |
| AC-03(09) | Controlled Release | — |
| AC-03(10) | Audited Override of Access Control Mechanisms | — |
| AC-03(11) | Restrict Access to Specific Information Types | — |
| AC-03(12) | Assert and Enforce Application Access | — |
| AC-03(13) | Attribute-based Access Control | — |
| AC-03(14) | Individual Access | — |
| AC-03(15) | Discretionary and Mandatory Access Control | — |

</details>
<details>
<summary><b>AC-04</b> — Information Flow Enforcement [M/H] (30개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-04(01) | Object Security and Privacy Attributes | — |
| AC-04(02) | Processing Domains | — |
| AC-04(03) | Dynamic Information Flow Control | — |
| AC-04(04) | Flow Control of Encrypted Information | H |
| AC-04(05) | Embedded Data Types | — |
| AC-04(06) | Metadata | — |
| AC-04(07) | One-way Flow Mechanisms | — |
| AC-04(08) | Security and Privacy Policy Filters | — |
| AC-04(09) | Human Reviews | — |
| AC-04(10) | Enable and Disable Security or Privacy Policy Filters | — |
| AC-04(11) | Configuration of Security or Privacy Policy Filters | — |
| AC-04(12) | Data Type Identifiers | — |
| AC-04(13) | Decomposition into Policy-relevant Subcomponents | — |
| AC-04(14) | Security or Privacy Policy Filter Constraints | — |
| AC-04(15) | Detection of Unsanctioned Information | — |
| AC-04(17) | Domain Authentication | — |
| AC-04(19) | Validation of Metadata | — |
| AC-04(20) | Approved Solutions | — |
| AC-04(21) | Physical or Logical Separation of Information Flows | — |
| AC-04(22) | Access Only | — |
| AC-04(23) | Modify Non-releasable Information | — |
| AC-04(24) | Internal Normalized Format | — |
| AC-04(25) | Data Sanitization | — |
| AC-04(26) | Audit Filtering Actions | — |
| AC-04(27) | Redundant/Independent Filtering Mechanisms | — |
| AC-04(28) | Linear Filter Pipelines | — |
| AC-04(29) | Filter Orchestration Engines | — |
| AC-04(30) | Filter Mechanisms Using Multiple Processes | — |
| AC-04(31) | Failed Content Transfer Prevention | — |
| AC-04(32) | Process Requirements for Information Transfer | — |

</details>
- **AC-05** — Separation of Duties [M/H]
<details>
<summary><b>AC-06</b> — Least Privilege [M/H] (10개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-06(01) | Authorize Access to Security Functions | M/H |
| AC-06(02) | Non-privileged Access for Nonsecurity Functions | M/H |
| AC-06(03) | Network Access to Privileged Commands | H |
| AC-06(04) | Separate Processing Domains | — |
| AC-06(05) | Privileged Accounts | M/H |
| AC-06(06) | Privileged Access by Non-organizational Users | — |
| AC-06(07) | Review of User Privileges | M/H |
| AC-06(08) | Privilege Levels for Code Execution | — |
| AC-06(09) | Log Use of Privileged Functions | M/H |
| AC-06(10) | Prohibit Non-privileged Users from Executing Privileged Functions | M/H |

</details>
<details>
<summary><b>AC-07</b> — Unsuccessful Logon Attempts [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-07(02) | Purge or Wipe Mobile Device | — |
| AC-07(03) | Biometric Attempt Limiting | — |
| AC-07(04) | Use of Alternate Authentication Factor | — |

</details>
- **AC-08** — System Use Notification [L/M/H]
<details>
<summary><b>AC-09</b> — Previous Logon Notification [—] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-09(01) | Unsuccessful Logons | — |
| AC-09(02) | Successful and Unsuccessful Logons | — |
| AC-09(03) | Notification of Account Changes | — |
| AC-09(04) | Additional Logon Information | — |

</details>
- **AC-10** — Concurrent Session Control [H]
<details>
<summary><b>AC-11</b> — Device Lock [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-11(01) | Pattern-hiding Displays | M/H |

</details>
<details>
<summary><b>AC-12</b> — Session Termination [M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-12(01) | User-initiated Logouts | — |
| AC-12(02) | Termination Message | — |
| AC-12(03) | Timeout Warning Message | — |

</details>
- **AC-14** — Permitted Actions Without Identification or Authentication [L/M/H]
<details>
<summary><b>AC-16</b> — Security and Privacy Attributes [—] (10개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-16(01) | Dynamic Attribute Association | — |
| AC-16(02) | Attribute Value Changes by Authorized Individuals | — |
| AC-16(03) | Maintenance of Attribute Associations by System | — |
| AC-16(04) | Association of Attributes by Authorized Individuals | — |
| AC-16(05) | Attribute Displays on Objects to Be Output | — |
| AC-16(06) | Maintenance of Attribute Association | — |
| AC-16(07) | Consistent Attribute Interpretation | — |
| AC-16(08) | Association Techniques and Technologies | — |
| AC-16(09) | Attribute Reassignment — Regrading Mechanisms | — |
| AC-16(10) | Attribute Configuration by Authorized Individuals | — |

</details>
<details>
<summary><b>AC-17</b> — Remote Access [L/M/H] (7개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-17(01) | Monitoring and Control | M/H |
| AC-17(02) | Protection of Confidentiality and Integrity Using Encryption | M/H |
| AC-17(03) | Managed Access Control Points | M/H |
| AC-17(04) | Privileged Commands and Access | M/H |
| AC-17(06) | Protection of Mechanism Information | — |
| AC-17(09) | Disconnect or Disable Access | — |
| AC-17(10) | Authenticate Remote Commands | — |

</details>
<details>
<summary><b>AC-18</b> — Wireless Access [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-18(01) | Authentication and Encryption | M/H |
| AC-18(03) | Disable Wireless Networking | M/H |
| AC-18(04) | Restrict Configurations by Users | H |
| AC-18(05) | Antennas and Transmission Power Levels | H |

</details>
<details>
<summary><b>AC-19</b> — Access Control for Mobile Devices [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-19(04) | Restrictions for Classified Information | — |
| AC-19(05) | Full Device or Container-based Encryption | M/H |

</details>
<details>
<summary><b>AC-20</b> — Use of External Systems [L/M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-20(01) | Limits on Authorized Use | M/H |
| AC-20(02) | Portable Storage Devices — Restricted Use | M/H |
| AC-20(03) | Non-organizationally Owned Systems — Restricted Use | — |
| AC-20(04) | Network Accessible Storage Devices — Prohibited Use | — |
| AC-20(05) | Portable Storage Devices — Prohibited Use | — |

</details>
<details>
<summary><b>AC-21</b> — Information Sharing [M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-21(01) | Automated Decision Support | — |
| AC-21(02) | Information Search and Retrieval | — |

</details>
- **AC-22** — Publicly Accessible Content [L/M/H]
- **AC-23** — Data Mining Protection [—]
<details>
<summary><b>AC-24</b> — Access Control Decisions [—] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AC-24(01) | Transmit Access Authorization Information | — |
| AC-24(02) | No User or Process Identity | — |

</details>
- **AC-25** — Reference Monitor [—]

</details>

<details>
<summary><b>AT — Awareness and Training (5 base / 10 enhancement)</b></summary>

- **AT-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>AT-02</b> — Literacy Training and Awareness [L/M/H] (6개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AT-02(01) | Practical Exercises | — |
| AT-02(02) | Insider Threat | L/M/H |
| AT-02(03) | Social Engineering and Mining | M/H |
| AT-02(04) | Suspicious Communications and Anomalous System Behavior | — |
| AT-02(05) | Advanced Persistent Threat | — |
| AT-02(06) | Cyber Threat Environment | — |

</details>
<details>
<summary><b>AT-03</b> — Role-based Training [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AT-03(01) | Environmental Controls | — |
| AT-03(02) | Physical Security Controls | — |
| AT-03(03) | Practical Exercises | — |
| AT-03(05) | Processing Personally Identifiable Information | — |

</details>
- **AT-04** — Training Records [L/M/H]
- **AT-06** — Training Feedback [—]

</details>

<details>
<summary><b>AU — Audit and Accountability (15 base / 41 enhancement)</b></summary>

- **AU-01** — Policy and Procedures [L/M/H]
- **AU-02** — Event Logging [L/M/H]
<details>
<summary><b>AU-03</b> — Content of Audit Records [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-03(01) | Additional Audit Information | M/H |
| AU-03(03) | Limit Personally Identifiable Information Elements | — |

</details>
<details>
<summary><b>AU-04</b> — Audit Log Storage Capacity [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-04(01) | Transfer to Alternate Storage | — |

</details>
<details>
<summary><b>AU-05</b> — Response to Audit Logging Process Failures [L/M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-05(01) | Storage Capacity Warning | H |
| AU-05(02) | Real-time Alerts | H |
| AU-05(03) | Configurable Traffic Volume Thresholds | — |
| AU-05(04) | Shutdown on Failure | — |
| AU-05(05) | Alternate Audit Logging Capability | — |

</details>
<details>
<summary><b>AU-06</b> — Audit Record Review, Analysis, and Reporting [L/M/H] (8개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-06(01) | Automated Process Integration | M/H |
| AU-06(03) | Correlate Audit Record Repositories | M/H |
| AU-06(04) | Central Review and Analysis | — |
| AU-06(05) | Integrated Analysis of Audit Records | H |
| AU-06(06) | Correlation with Physical Monitoring | H |
| AU-06(07) | Permitted Actions | — |
| AU-06(08) | Full Text Analysis of Privileged Commands | — |
| AU-06(09) | Correlation with Information from Nontechnical Sources | — |

</details>
<details>
<summary><b>AU-07</b> — Audit Record Reduction and Report Generation [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-07(01) | Automatic Processing | M/H |

</details>
- **AU-08** — Time Stamps [L/M/H]
<details>
<summary><b>AU-09</b> — Protection of Audit Information [L/M/H] (7개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-09(01) | Hardware Write-once Media | — |
| AU-09(02) | Store on Separate Physical Systems or Components | H |
| AU-09(03) | Cryptographic Protection | H |
| AU-09(04) | Access by Subset of Privileged Users | M/H |
| AU-09(05) | Dual Authorization | — |
| AU-09(06) | Read-only Access | — |
| AU-09(07) | Store on Component with Different Operating System | — |

</details>
<details>
<summary><b>AU-10</b> — Non-repudiation [H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-10(01) | Association of Identities | — |
| AU-10(02) | Validate Binding of Information Producer Identity | — |
| AU-10(03) | Chain of Custody | — |
| AU-10(04) | Validate Binding of Information Reviewer Identity | — |

</details>
<details>
<summary><b>AU-11</b> — Audit Record Retention [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-11(01) | Long-term Retrieval Capability | — |

</details>
<details>
<summary><b>AU-12</b> — Audit Record Generation [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-12(01) | System-wide and Time-correlated Audit Trail | H |
| AU-12(02) | Standardized Formats | — |
| AU-12(03) | Changes by Authorized Individuals | H |
| AU-12(04) | Query Parameter Audits of Personally Identifiable Information | — |

</details>
<details>
<summary><b>AU-13</b> — Monitoring for Information Disclosure [—] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-13(01) | Use of Automated Tools | — |
| AU-13(02) | Review of Monitored Sites | — |
| AU-13(03) | Unauthorized Replication of Information | — |

</details>
<details>
<summary><b>AU-14</b> — Session Audit [—] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-14(01) | System Start-up | — |
| AU-14(03) | Remote Viewing and Listening | — |

</details>
<details>
<summary><b>AU-16</b> — Cross-organizational Audit Logging [—] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| AU-16(01) | Identity Preservation | — |
| AU-16(02) | Sharing of Audit Information | — |
| AU-16(03) | Disassociability | — |

</details>

</details>

<details>
<summary><b>CA — Assessment, Authorization, and Monitoring (8 base / 17 enhancement)</b></summary>

- **CA-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>CA-02</b> — Control Assessments [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CA-02(01) | Independent Assessors | M/H |
| CA-02(02) | Specialized Assessments | H |
| CA-02(03) | Leveraging Results from External Organizations | — |

</details>
<details>
<summary><b>CA-03</b> — Information Exchange [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CA-03(06) | Transfer Authorizations | H |
| CA-03(07) | Transitive Information Exchanges | — |

</details>
<details>
<summary><b>CA-05</b> — Plan of Action and Milestones [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CA-05(01) | Automation Support for Accuracy and Currency | — |

</details>
<details>
<summary><b>CA-06</b> — Authorization [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CA-06(01) | Joint Authorization — Intra-organization | — |
| CA-06(02) | Joint Authorization — Inter-organization | — |

</details>
<details>
<summary><b>CA-07</b> — Continuous Monitoring [L/M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CA-07(01) | Independent Assessment | M/H |
| CA-07(03) | Trend Analyses | — |
| CA-07(04) | Risk Monitoring | L/M/H |
| CA-07(05) | Consistency Analysis | — |
| CA-07(06) | Automation Support for Monitoring | — |

</details>
<details>
<summary><b>CA-08</b> — Penetration Testing [H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CA-08(01) | Independent Penetration Testing Agent or Team | H |
| CA-08(02) | Red Team Exercises | — |
| CA-08(03) | Facility Penetration Testing | — |

</details>
<details>
<summary><b>CA-09</b> — Internal System Connections [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CA-09(01) | Compliance Checks | — |

</details>

</details>

<details>
<summary><b>CM — Configuration Management (14 base / 42 enhancement)</b></summary>

- **CM-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>CM-02</b> — Baseline Configuration [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-02(02) | Automation Support for Accuracy and Currency | M/H |
| CM-02(03) | Retention of Previous Configurations | M/H |
| CM-02(06) | Development and Test Environments | — |
| CM-02(07) | Configure Systems and Components for High-risk Areas | M/H |

</details>
<details>
<summary><b>CM-03</b> — Configuration Change Control [M/H] (8개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-03(01) | Automated Documentation, Notification, and Prohibition of Changes | H |
| CM-03(02) | Testing, Validation, and Documentation of Changes | M/H |
| CM-03(03) | Automated Change Implementation | — |
| CM-03(04) | Security and Privacy Representatives | M/H |
| CM-03(05) | Automated Security Response | — |
| CM-03(06) | Cryptography Management | H |
| CM-03(07) | Review System Changes | — |
| CM-03(08) | Prevent or Restrict Configuration Changes | — |

</details>
<details>
<summary><b>CM-04</b> — Impact Analyses [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-04(01) | Separate Test Environments | H |
| CM-04(02) | Verification of Controls | M/H |

</details>
<details>
<summary><b>CM-05</b> — Access Restrictions for Change [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-05(01) | Automated Access Enforcement and Audit Records | H |
| CM-05(04) | Dual Authorization | — |
| CM-05(05) | Privilege Limitation for Production and Operation | — |
| CM-05(06) | Limit Library Privileges | — |

</details>
<details>
<summary><b>CM-06</b> — Configuration Settings [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-06(01) | Automated Management, Application, and Verification | H |
| CM-06(02) | Respond to Unauthorized Changes | H |

</details>
<details>
<summary><b>CM-07</b> — Least Functionality [L/M/H] (9개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-07(01) | Periodic Review | M/H |
| CM-07(02) | Prevent Program Execution | M/H |
| CM-07(03) | Registration Compliance | — |
| CM-07(04) | Unauthorized Software — Deny-by-exception | — |
| CM-07(05) | Authorized Software — Allow-by-exception | M/H |
| CM-07(06) | Confined Environments with Limited Privileges | — |
| CM-07(07) | Code Execution in Protected Environments | — |
| CM-07(08) | Binary or Machine Executable Code | — |
| CM-07(09) | Prohibiting The Use of Unauthorized Hardware | — |

</details>
<details>
<summary><b>CM-08</b> — System Component Inventory [L/M/H] (8개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-08(01) | Updates During Installation and Removal | M/H |
| CM-08(02) | Automated Maintenance | H |
| CM-08(03) | Automated Unauthorized Component Detection | M/H |
| CM-08(04) | Accountability Information | H |
| CM-08(06) | Assessed Configurations and Approved Deviations | — |
| CM-08(07) | Centralized Repository | — |
| CM-08(08) | Automated Location Tracking | — |
| CM-08(09) | Assignment of Components to Systems | — |

</details>
<details>
<summary><b>CM-09</b> — Configuration Management Plan [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-09(01) | Assignment of Responsibility | — |

</details>
<details>
<summary><b>CM-10</b> — Software Usage Restrictions [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-10(01) | Open-source Software | — |

</details>
<details>
<summary><b>CM-11</b> — User-installed Software [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-11(02) | Software Installation with Privileged Status | — |
| CM-11(03) | Automated Enforcement and Monitoring | — |

</details>
<details>
<summary><b>CM-12</b> — Information Location [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CM-12(01) | Automated Tools to Support Information Location | M/H |

</details>
- **CM-13** — Data Action Mapping [—]
- **CM-14** — Signed Components [—]

</details>

<details>
<summary><b>CP — Contingency Planning (12 base / 37 enhancement)</b></summary>

- **CP-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>CP-02</b> — Contingency Plan [L/M/H] (7개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CP-02(01) | Coordinate with Related Plans | M/H |
| CP-02(02) | Capacity Planning | H |
| CP-02(03) | Resume Mission and Business Functions | M/H |
| CP-02(05) | Continue Mission and Business Functions | H |
| CP-02(06) | Alternate Processing and Storage Sites | — |
| CP-02(07) | Coordinate with External Service Providers | — |
| CP-02(08) | Identify Critical Assets | M/H |

</details>
<details>
<summary><b>CP-03</b> — Contingency Training [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CP-03(01) | Simulated Events | H |
| CP-03(02) | Mechanisms Used in Training Environments | — |

</details>
<details>
<summary><b>CP-04</b> — Contingency Plan Testing [L/M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CP-04(01) | Coordinate with Related Plans | M/H |
| CP-04(02) | Alternate Processing Site | H |
| CP-04(03) | Automated Testing | — |
| CP-04(04) | Full Recovery and Reconstitution | — |
| CP-04(05) | Self-challenge | — |

</details>
<details>
<summary><b>CP-06</b> — Alternate Storage Site [M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CP-06(01) | Separation from Primary Site | M/H |
| CP-06(02) | Recovery Time and Recovery Point Objectives | H |
| CP-06(03) | Accessibility | M/H |

</details>
<details>
<summary><b>CP-07</b> — Alternate Processing Site [M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CP-07(01) | Separation from Primary Site | M/H |
| CP-07(02) | Accessibility | M/H |
| CP-07(03) | Priority of Service | M/H |
| CP-07(04) | Preparation for Use | H |
| CP-07(06) | Inability to Return to Primary Site | — |

</details>
<details>
<summary><b>CP-08</b> — Telecommunications Services [M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CP-08(01) | Priority of Service Provisions | M/H |
| CP-08(02) | Single Points of Failure | M/H |
| CP-08(03) | Separation of Primary and Alternate Providers | H |
| CP-08(04) | Provider Contingency Plan | H |
| CP-08(05) | Alternate Telecommunication Service Testing | — |

</details>
<details>
<summary><b>CP-09</b> — System Backup [L/M/H] (7개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CP-09(01) | Testing for Reliability and Integrity | M/H |
| CP-09(02) | Test Restoration Using Sampling | H |
| CP-09(03) | Separate Storage for Critical Information | H |
| CP-09(05) | Transfer to Alternate Storage Site | H |
| CP-09(06) | Redundant Secondary System | — |
| CP-09(07) | Dual Authorization for Deletion or Destruction | — |
| CP-09(08) | Cryptographic Protection | M/H |

</details>
<details>
<summary><b>CP-10</b> — System Recovery and Reconstitution [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| CP-10(02) | Transaction Recovery | M/H |
| CP-10(04) | Restore Within Time Period | H |
| CP-10(06) | Component Protection | — |

</details>
- **CP-11** — Alternate Communications Protocols [—]
- **CP-12** — Safe Mode [—]
- **CP-13** — Alternative Security Mechanisms [—]

</details>

<details>
<summary><b>IA — Identification and Authentication (13 base / 46 enhancement)</b></summary>

- **IA-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>IA-02</b> — Identification and Authentication (Organizational Users) [L/M/H] (8개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IA-02(01) | Multi-factor Authentication to Privileged Accounts | L/M/H |
| IA-02(02) | Multi-factor Authentication to Non-privileged Accounts | L/M/H |
| IA-02(05) | Individual Authentication with Group Authentication | H |
| IA-02(06) | Access to Accounts —separate Device | — |
| IA-02(08) | Access to Accounts — Replay Resistant | L/M/H |
| IA-02(10) | Single Sign-on | — |
| IA-02(12) | Acceptance of PIV Credentials | L/M/H |
| IA-02(13) | Out-of-band Authentication | — |

</details>
<details>
<summary><b>IA-03</b> — Device Identification and Authentication [M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IA-03(01) | Cryptographic Bidirectional Authentication | — |
| IA-03(03) | Dynamic Address Allocation | — |
| IA-03(04) | Device Attestation | — |

</details>
<details>
<summary><b>IA-04</b> — Identifier Management [L/M/H] (6개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IA-04(01) | Prohibit Account Identifiers as Public Identifiers | — |
| IA-04(04) | Identify User Status | M/H |
| IA-04(05) | Dynamic Management | — |
| IA-04(06) | Cross-organization Management | — |
| IA-04(08) | Pairwise Pseudonymous Identifiers | — |
| IA-04(09) | Attribute Maintenance and Protection | — |

</details>
<details>
<summary><b>IA-05</b> — Authenticator Management [L/M/H] (15개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IA-05(01) | Password-based Authentication | L/M/H |
| IA-05(02) | Public Key-based Authentication | M/H |
| IA-05(05) | Change Authenticators Prior to Delivery | — |
| IA-05(06) | Protection of Authenticators | M/H |
| IA-05(07) | No Embedded Unencrypted Static Authenticators | — |
| IA-05(08) | Multiple System Accounts | — |
| IA-05(09) | Federated Credential Management | — |
| IA-05(10) | Dynamic Credential Binding | — |
| IA-05(12) | Biometric Authentication Performance | — |
| IA-05(13) | Expiration of Cached Authenticators | — |
| IA-05(14) | Managing Content of PKI Trust Stores | — |
| IA-05(15) | GSA-approved Products and Services | — |
| IA-05(16) | In-person or Trusted External Party Authenticator Issuance | — |
| IA-05(17) | Presentation Attack Detection for Biometric Authenticators | — |
| IA-05(18) | Password Managers | — |

</details>
- **IA-06** — Authentication Feedback [L/M/H]
- **IA-07** — Cryptographic Module Authentication [L/M/H]
<details>
<summary><b>IA-08</b> — Identification and Authentication (Non-organizational Users) [L/M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IA-08(01) | Acceptance of PIV Credentials from Other Agencies | L/M/H |
| IA-08(02) | Acceptance of External Authenticators | L/M/H |
| IA-08(04) | Use of Defined Profiles | L/M/H |
| IA-08(05) | Acceptance of PIV-I Credentials | — |
| IA-08(06) | Disassociability | — |

</details>
- **IA-09** — Service Identification and Authentication [—]
- **IA-10** — Adaptive Authentication [—]
- **IA-11** — Re-authentication [L/M/H]
<details>
<summary><b>IA-12</b> — Identity Proofing [M/H] (6개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IA-12(01) | Supervisor Authorization | — |
| IA-12(02) | Identity Evidence | M/H |
| IA-12(03) | Identity Evidence Validation and Verification | M/H |
| IA-12(04) | In-person Validation and Verification | H |
| IA-12(05) | Address Confirmation | M/H |
| IA-12(06) | Accept Externally-proofed Identities | — |

</details>
<details>
<summary><b>IA-13</b> — Identity Providers and Authorization Servers [—] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IA-13(01) | Protection of Cryptographic Keys | — |
| IA-13(02) | Verification of Identity Assertions and Access Tokens | — |
| IA-13(03) | Token Management | — |

</details>

</details>

<details>
<summary><b>IR — Incident Response (9 base / 31 enhancement)</b></summary>

- **IR-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>IR-02</b> — Incident Response Training [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IR-02(01) | Simulated Events | H |
| IR-02(02) | Automated Training Environments | H |
| IR-02(03) | Breach | — |

</details>
<details>
<summary><b>IR-03</b> — Incident Response Testing [M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IR-03(01) | Automated Testing | — |
| IR-03(02) | Coordination with Related Plans | M/H |
| IR-03(03) | Continuous Improvement | — |

</details>
<details>
<summary><b>IR-04</b> — Incident Handling [L/M/H] (15개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IR-04(01) | Automated Incident Handling Processes | M/H |
| IR-04(02) | Dynamic Reconfiguration | — |
| IR-04(03) | Continuity of Operations | — |
| IR-04(04) | Information Correlation | H |
| IR-04(05) | Automatic Disabling of System | — |
| IR-04(06) | Insider Threats | — |
| IR-04(07) | Insider Threats — Intra-organization Coordination | — |
| IR-04(08) | Correlation with External Organizations | — |
| IR-04(09) | Dynamic Response Capability | — |
| IR-04(10) | Supply Chain Coordination | — |
| IR-04(11) | Integrated Incident Response Team | H |
| IR-04(12) | Malicious Code and Forensic Analysis | — |
| IR-04(13) | Behavior Analysis | — |
| IR-04(14) | Security Operations Center | — |
| IR-04(15) | Public Relations and Reputation Repair | — |

</details>
<details>
<summary><b>IR-05</b> — Incident Monitoring [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IR-05(01) | Automated Tracking, Data Collection, and Analysis | H |

</details>
<details>
<summary><b>IR-06</b> — Incident Reporting [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IR-06(01) | Automated Reporting | M/H |
| IR-06(02) | Vulnerabilities Related to Incidents | — |
| IR-06(03) | Supply Chain Coordination | M/H |

</details>
<details>
<summary><b>IR-07</b> — Incident Response Assistance [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IR-07(01) | Automation Support for Availability of Information and Support | M/H |
| IR-07(02) | Coordination with External Providers | — |

</details>
<details>
<summary><b>IR-08</b> — Incident Response Plan [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IR-08(01) | Breaches | — |

</details>
<details>
<summary><b>IR-09</b> — Information Spillage Response [—] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| IR-09(02) | Training | — |
| IR-09(03) | Post-spill Operations | — |
| IR-09(04) | Exposure to Unauthorized Personnel | — |

</details>

</details>

<details>
<summary><b>MA — Maintenance (7 base / 21 enhancement)</b></summary>

- **MA-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>MA-02</b> — Controlled Maintenance [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MA-02(02) | Automated Maintenance Activities | H |

</details>
<details>
<summary><b>MA-03</b> — Maintenance Tools [M/H] (6개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MA-03(01) | Inspect Tools | M/H |
| MA-03(02) | Inspect Media | M/H |
| MA-03(03) | Prevent Unauthorized Removal | M/H |
| MA-03(04) | Restricted Tool Use | — |
| MA-03(05) | Execution with Privilege | — |
| MA-03(06) | Software Updates and Patches | — |

</details>
<details>
<summary><b>MA-04</b> — Nonlocal Maintenance [L/M/H] (6개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MA-04(01) | Logging and Review | — |
| MA-04(03) | Comparable Security and Sanitization | H |
| MA-04(04) | Authentication and Separation of Maintenance Sessions | — |
| MA-04(05) | Approvals and Notifications | — |
| MA-04(06) | Cryptographic Protection | — |
| MA-04(07) | Disconnect Verification | — |

</details>
<details>
<summary><b>MA-05</b> — Maintenance Personnel [L/M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MA-05(01) | Individuals Without Appropriate Access | H |
| MA-05(02) | Security Clearances for Classified Systems | — |
| MA-05(03) | Citizenship Requirements for Classified Systems | — |
| MA-05(04) | Foreign Nationals | — |
| MA-05(05) | Non-system Maintenance | — |

</details>
<details>
<summary><b>MA-06</b> — Timely Maintenance [M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MA-06(01) | Preventive Maintenance | — |
| MA-06(02) | Predictive Maintenance | — |
| MA-06(03) | Automated Support for Predictive Maintenance | — |

</details>
- **MA-07** — Field Maintenance [—]

</details>

<details>
<summary><b>MP — Media Protection (8 base / 12 enhancement)</b></summary>

- **MP-01** — Policy and Procedures [L/M/H]
- **MP-02** — Media Access [L/M/H]
- **MP-03** — Media Marking [M/H]
<details>
<summary><b>MP-04</b> — Media Storage [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MP-04(02) | Automated Restricted Access | — |

</details>
<details>
<summary><b>MP-05</b> — Media Transport [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MP-05(03) | Custodians | — |

</details>
<details>
<summary><b>MP-06</b> — Media Sanitization [L/M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MP-06(01) | Review, Approve, Track, Document, and Verify | H |
| MP-06(02) | Equipment Testing | H |
| MP-06(03) | Nondestructive Techniques | H |
| MP-06(07) | Dual Authorization | — |
| MP-06(08) | Remote Purging or Wiping of Information | — |

</details>
<details>
<summary><b>MP-07</b> — Media Use [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MP-07(02) | Prohibit Use of Sanitization-resistant Media | — |

</details>
<details>
<summary><b>MP-08</b> — Media Downgrading [—] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| MP-08(01) | Documentation of Process | — |
| MP-08(02) | Equipment Testing | — |
| MP-08(03) | Controlled Unclassified Information | — |
| MP-08(04) | Classified Information | — |

</details>

</details>

<details>
<summary><b>PE — Physical and Environmental Protection (22 base / 29 enhancement)</b></summary>

- **PE-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>PE-02</b> — Physical Access Authorizations [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-02(01) | Access by Position or Role | — |
| PE-02(02) | Two Forms of Identification | — |
| PE-02(03) | Restrict Unescorted Access | — |

</details>
<details>
<summary><b>PE-03</b> — Physical Access Control [L/M/H] (7개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-03(01) | System Access | H |
| PE-03(02) | Facility and Systems | — |
| PE-03(03) | Continuous Guards | — |
| PE-03(04) | Lockable Casings | — |
| PE-03(05) | Tamper Protection | — |
| PE-03(07) | Physical Barriers | — |
| PE-03(08) | Access Control Vestibules | — |

</details>
- **PE-04** — Access Control for Transmission [M/H]
<details>
<summary><b>PE-05</b> — Access Control for Output Devices [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-05(02) | Link to Individual Identity | — |

</details>
<details>
<summary><b>PE-06</b> — Monitoring Physical Access [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-06(01) | Intrusion Alarms and Surveillance Equipment | M/H |
| PE-06(02) | Automated Intrusion Recognition and Responses | — |
| PE-06(03) | Video Surveillance | — |
| PE-06(04) | Monitoring Physical Access to Systems | H |

</details>
<details>
<summary><b>PE-08</b> — Visitor Access Records [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-08(01) | Automated Records Maintenance and Review | H |
| PE-08(03) | Limit Personally Identifiable Information Elements | — |

</details>
<details>
<summary><b>PE-09</b> — Power Equipment and Cabling [M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-09(01) | Redundant Cabling | — |
| PE-09(02) | Automatic Voltage Controls | — |

</details>
- **PE-10** — Emergency Shutoff [M/H]
<details>
<summary><b>PE-11</b> — Emergency Power [M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-11(01) | Alternate Power Supply — Minimal Operational Capability | H |
| PE-11(02) | Alternate Power Supply — Self-contained | — |

</details>
<details>
<summary><b>PE-12</b> — Emergency Lighting [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-12(01) | Essential Mission and Business Functions | — |

</details>
<details>
<summary><b>PE-13</b> — Fire Protection [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-13(01) | Detection Systems — Automatic Activation and Notification | M/H |
| PE-13(02) | Suppression Systems — Automatic Activation and Notification | H |
| PE-13(04) | Inspections | — |

</details>
<details>
<summary><b>PE-14</b> — Environmental Controls [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-14(01) | Automatic Controls | — |
| PE-14(02) | Monitoring with Alarms and Notifications | — |

</details>
<details>
<summary><b>PE-15</b> — Water Damage Protection [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-15(01) | Automation Support | H |

</details>
- **PE-16** — Delivery and Removal [L/M/H]
- **PE-17** — Alternate Work Site [M/H]
- **PE-18** — Location of System Components [H]
<details>
<summary><b>PE-19</b> — Information Leakage [—] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PE-19(01) | National Emissions Policies and Procedures | — |

</details>
- **PE-20** — Asset Monitoring and Tracking [—]
- **PE-21** — Electromagnetic Pulse Protection [—]
- **PE-22** — Component Marking [—]
- **PE-23** — Facility Location [—]

</details>

<details>
<summary><b>PL — Planning (8 base / 3 enhancement)</b></summary>

- **PL-01** — Policy and Procedures [L/M/H]
- **PL-02** — System Security and Privacy Plans [L/M/H]
<details>
<summary><b>PL-04</b> — Rules of Behavior [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PL-04(01) | Social Media and External Site/Application Usage Restrictions | L/M/H |

</details>
- **PL-07** — Concept of Operations [—]
<details>
<summary><b>PL-08</b> — Security and Privacy Architectures [M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PL-08(01) | Defense in Depth | — |
| PL-08(02) | Supplier Diversity | — |

</details>
- **PL-09** — Central Management [—]
- **PL-10** — Baseline Selection [L/M/H]
- **PL-11** — Baseline Tailoring [L/M/H]

</details>

<details>
<summary><b>PM — Program Management (32 base / 5 enhancement)</b></summary>

- **PM-01** — Information Security Program Plan
- **PM-02** — Information Security Program Leadership Role
- **PM-03** — Information Security and Privacy Resources
- **PM-04** — Plan of Action and Milestones Process
<details>
<summary><b>PM-05</b> — System Inventory (1개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PM-05(01) | Inventory of Personally Identifiable Information |

</details>
- **PM-06** — Measures of Performance
<details>
<summary><b>PM-07</b> — Enterprise Architecture (1개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PM-07(01) | Offloading |

</details>
- **PM-08** — Critical Infrastructure Plan
- **PM-09** — Risk Management Strategy
- **PM-10** — Authorization Process
- **PM-11** — Mission and Business Process Definition
- **PM-12** — Insider Threat Program
- **PM-13** — Security and Privacy Workforce
- **PM-14** — Testing, Training, and Monitoring
- **PM-15** — Security and Privacy Groups and Associations
<details>
<summary><b>PM-16</b> — Threat Awareness Program (1개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PM-16(01) | Automated Means for Sharing Threat Intelligence |

</details>
- **PM-17** — Protecting Controlled Unclassified Information on External Systems
- **PM-18** — Privacy Program Plan
- **PM-19** — Privacy Program Leadership Role
<details>
<summary><b>PM-20</b> — Dissemination of Privacy Program Information (1개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PM-20(01) | Privacy Policies on Websites, Applications, and Digital Services |

</details>
- **PM-21** — Accounting of Disclosures
- **PM-22** — Personally Identifiable Information Quality Management
- **PM-23** — Data Governance Body
- **PM-24** — Data Integrity Board
- **PM-25** — Minimization of Personally Identifiable Information Used in Testing, Training, and Research
- **PM-26** — Complaint Management
- **PM-27** — Privacy Reporting
- **PM-28** — Risk Framing
- **PM-29** — Risk Management Program Leadership Roles
<details>
<summary><b>PM-30</b> — Supply Chain Risk Management Strategy (1개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PM-30(01) | Suppliers of Critical or Mission-essential Items |

</details>
- **PM-31** — Continuous Monitoring Strategy
- **PM-32** — Purposing

</details>

<details>
<summary><b>PS — Personnel Security (9 base / 8 enhancement)</b></summary>

- **PS-01** — Policy and Procedures [L/M/H]
- **PS-02** — Position Risk Designation [L/M/H]
<details>
<summary><b>PS-03</b> — Personnel Screening [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PS-03(01) | Classified Information | — |
| PS-03(02) | Formal Indoctrination | — |
| PS-03(03) | Information Requiring Special Protective Measures | — |
| PS-03(04) | Citizenship Requirements | — |

</details>
<details>
<summary><b>PS-04</b> — Personnel Termination [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PS-04(01) | Post-employment Requirements | — |
| PS-04(02) | Automated Actions | H |

</details>
- **PS-05** — Personnel Transfer [L/M/H]
<details>
<summary><b>PS-06</b> — Access Agreements [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| PS-06(02) | Classified Information Requiring Special Protection | — |
| PS-06(03) | Post-employment Requirements | — |

</details>
- **PS-07** — External Personnel Security [L/M/H]
- **PS-08** — Personnel Sanctions [L/M/H]
- **PS-09** — Position Descriptions [L/M/H]

</details>

<details>
<summary><b>PT — Personally Identifiable Information Processing and Transparency (8 base / 13 enhancement)</b></summary>

- **PT-01** — Policy and Procedures
<details>
<summary><b>PT-02</b> — Authority to Process Personally Identifiable Information (2개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PT-02(01) | Data Tagging |
| PT-02(02) | Automation |

</details>
<details>
<summary><b>PT-03</b> — Personally Identifiable Information Processing Purposes (2개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PT-03(01) | Data Tagging |
| PT-03(02) | Automation |

</details>
<details>
<summary><b>PT-04</b> — Consent (3개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PT-04(01) | Tailored Consent |
| PT-04(02) | Just-in-time Consent |
| PT-04(03) | Revocation |

</details>
<details>
<summary><b>PT-05</b> — Privacy Notice (2개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PT-05(01) | Just-in-time Notice |
| PT-05(02) | Privacy Act Statements |

</details>
<details>
<summary><b>PT-06</b> — System of Records Notice (2개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PT-06(01) | Routine Uses |
| PT-06(02) | Exemption Rules |

</details>
<details>
<summary><b>PT-07</b> — Specific Categories of Personally Identifiable Information (2개 enhancement)</summary>

| Enhancement | 제목 |
|-------------|------|
| PT-07(01) | Social Security Numbers |
| PT-07(02) | First Amendment Information |

</details>
- **PT-08** — Computer Matching Requirements

</details>

<details>
<summary><b>RA — Risk Assessment (9 base / 13 enhancement)</b></summary>

- **RA-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>RA-02</b> — Security Categorization [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| RA-02(01) | Impact-level Prioritization | — |

</details>
<details>
<summary><b>RA-03</b> — Risk Assessment [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| RA-03(01) | Supply Chain Risk Assessment | L/M/H |
| RA-03(02) | Use of All-source Intelligence | — |
| RA-03(03) | Dynamic Threat Awareness | — |
| RA-03(04) | Predictive Cyber Analytics | — |

</details>
<details>
<summary><b>RA-05</b> — Vulnerability Monitoring and Scanning [L/M/H] (8개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| RA-05(02) | Update Vulnerabilities to Be Scanned | L/M/H |
| RA-05(03) | Breadth and Depth of Coverage | — |
| RA-05(04) | Discoverable Information | H |
| RA-05(05) | Privileged Access | M/H |
| RA-05(06) | Automated Trend Analyses | — |
| RA-05(08) | Review Historic Audit Logs | — |
| RA-05(10) | Correlate Scanning Information | — |
| RA-05(11) | Public Disclosure Program | L/M/H |

</details>
- **RA-06** — Technical Surveillance Countermeasures Survey [—]
- **RA-07** — Risk Response [L/M/H]
- **RA-08** — Privacy Impact Assessments [—]
- **RA-09** — Criticality Analysis [M/H]
- **RA-10** — Threat Hunting [—]

</details>

<details>
<summary><b>SA — System and Services Acquisition (17 base / 91 enhancement)</b></summary>

- **SA-01** — Policy and Procedures [L/M/H]
- **SA-02** — Allocation of Resources [L/M/H]
<details>
<summary><b>SA-03</b> — System Development Life Cycle [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SA-03(01) | Manage Preproduction Environment | — |
| SA-03(02) | Use of Live or Operational Data | — |
| SA-03(03) | Technology Refresh | — |

</details>
<details>
<summary><b>SA-04</b> — Acquisition Process [L/M/H] (11개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SA-04(01) | Functional Properties of Controls | M/H |
| SA-04(02) | Design and Implementation Information for Controls | M/H |
| SA-04(03) | Development Methods, Techniques, and Practices | — |
| SA-04(05) | System, Component, and Service Configurations | H |
| SA-04(06) | Use of Information Assurance Products | — |
| SA-04(07) | NIAP-approved Protection Profiles  | — |
| SA-04(08) | Continuous Monitoring Plan for Controls | — |
| SA-04(09) | Functions, Ports, Protocols, and Services in Use | M/H |
| SA-04(10) | Use of Approved PIV Products | L/M/H |
| SA-04(11) | System of Records | — |
| SA-04(12) | Data Ownership | — |

</details>
- **SA-05** — System Documentation [L/M/H]
<details>
<summary><b>SA-08</b> — Security and Privacy Engineering Principles [L/M/H] (33개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SA-08(01) | Clear Abstractions | — |
| SA-08(02) | Least Common Mechanism | — |
| SA-08(03) | Modularity and Layering | — |
| SA-08(04) | Partially Ordered Dependencies | — |
| SA-08(05) | Efficiently Mediated Access | — |
| SA-08(06) | Minimized Sharing | — |
| SA-08(07) | Reduced Complexity | — |
| SA-08(08) | Secure Evolvability | — |
| SA-08(09) | Trusted Components | — |
| SA-08(10) | Hierarchical Trust | — |
| SA-08(11) | Inverse Modification Threshold | — |
| SA-08(12) | Hierarchical Protection | — |
| SA-08(13) | Minimized Security Elements | — |
| SA-08(14) | Least Privilege | — |
| SA-08(15) | Predicate Permission | — |
| SA-08(16) | Self-reliant Trustworthiness | — |
| SA-08(17) | Secure Distributed Composition | — |
| SA-08(18) | Trusted Communications Channels | — |
| SA-08(19) | Continuous Protection | — |
| SA-08(20) | Secure Metadata Management | — |
| SA-08(21) | Self-analysis | — |
| SA-08(22) | Accountability and Traceability | — |
| SA-08(23) | Secure Defaults | — |
| SA-08(24) | Secure Failure and Recovery | — |
| SA-08(25) | Economic Security | — |
| SA-08(26) | Performance Security | — |
| SA-08(27) | Human Factored Security | — |
| SA-08(28) | Acceptable Security | — |
| SA-08(29) | Repeatable and Documented Procedures | — |
| SA-08(30) | Procedural Rigor | — |
| SA-08(31) | Secure System Modification | — |
| SA-08(32) | Sufficient Documentation | — |
| SA-08(33) | Minimization | — |

</details>
<details>
<summary><b>SA-09</b> — External System Services [L/M/H] (8개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SA-09(01) | Risk Assessments and Organizational Approvals | — |
| SA-09(02) | Identification of Functions, Ports, Protocols, and Services | M/H |
| SA-09(03) | Establish and Maintain Trust Relationship with Providers | — |
| SA-09(04) | Consistent Interests of Consumers and Providers | — |
| SA-09(05) | Processing, Storage, and Service Location | — |
| SA-09(06) | Organization-controlled Cryptographic Keys | — |
| SA-09(07) | Organization-controlled Integrity Checking | — |
| SA-09(08) | Processing and Storage Location — U.S. Jurisdiction | — |

</details>
<details>
<summary><b>SA-10</b> — Developer Configuration Management [M/H] (7개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SA-10(01) | Software and Firmware Integrity Verification | — |
| SA-10(02) | Alternative Configuration Management Processes | — |
| SA-10(03) | Hardware Integrity Verification | — |
| SA-10(04) | Trusted Generation | — |
| SA-10(05) | Mapping Integrity for Version Control | — |
| SA-10(06) | Trusted Distribution | — |
| SA-10(07) | Security and Privacy Representatives | — |

</details>
<details>
<summary><b>SA-11</b> — Developer Testing and Evaluation [M/H] (9개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SA-11(01) | Static Code Analysis | — |
| SA-11(02) | Threat Modeling and Vulnerability Analyses | — |
| SA-11(03) | Independent Verification of Assessment Plans and Evidence | — |
| SA-11(04) | Manual Code Reviews | — |
| SA-11(05) | Penetration Testing | — |
| SA-11(06) | Attack Surface Reviews | — |
| SA-11(07) | Verify Scope of Testing and Evaluation | — |
| SA-11(08) | Dynamic Code Analysis | — |
| SA-11(09) | Interactive Application Security Testing | — |

</details>
<details>
<summary><b>SA-15</b> — Development Process, Standards, and Tools [M/H] (11개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SA-15(01) | Quality Metrics | — |
| SA-15(02) | Security and Privacy Tracking Tools | — |
| SA-15(03) | Criticality Analysis | M/H |
| SA-15(05) | Attack Surface Reduction | — |
| SA-15(06) | Continuous Improvement | — |
| SA-15(07) | Automated Vulnerability Analysis | — |
| SA-15(08) | Reuse of Threat and Vulnerability Information | — |
| SA-15(10) | Incident Response Plan | — |
| SA-15(11) | Archive System or Component | — |
| SA-15(12) | Minimize Personally Identifiable Information | — |
| SA-15(13) | Logging Syntax | — |

</details>
- **SA-16** — Developer-provided Training [H]
<details>
<summary><b>SA-17</b> — Developer Security and Privacy Architecture and Design [H] (9개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SA-17(01) | Formal Policy Model | — |
| SA-17(02) | Security-relevant Components | — |
| SA-17(03) | Formal Correspondence | — |
| SA-17(04) | Informal Correspondence | — |
| SA-17(05) | Conceptually Simple Design | — |
| SA-17(06) | Structure for Testing | — |
| SA-17(07) | Structure for Least Privilege | — |
| SA-17(08) | Orchestration | — |
| SA-17(09) | Design Diversity | — |

</details>
- **SA-20** — Customized Development of Critical Components [—]
- **SA-21** — Developer Screening [H]
- **SA-22** — Unsupported System Components [L/M/H]
- **SA-23** — Specialization [—]
- **SA-24** — Design For Cyber Resiliency [—]

</details>

<details>
<summary><b>SC — System and Communications Protection (47 base / 92 enhancement)</b></summary>

- **SC-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>SC-02</b> — Separation of System and User Functionality [M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-02(01) | Interfaces for Non-privileged Users | — |
| SC-02(02) | Disassociability | — |

</details>
<details>
<summary><b>SC-03</b> — Security Function Isolation [H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-03(01) | Hardware Separation | — |
| SC-03(02) | Access and Flow Control Functions | — |
| SC-03(03) | Minimize Nonsecurity Functionality | — |
| SC-03(04) | Module Coupling and Cohesiveness | — |
| SC-03(05) | Layered Structures | — |

</details>
<details>
<summary><b>SC-04</b> — Information in Shared System Resources [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-04(02) | Multilevel or Periods Processing | — |

</details>
<details>
<summary><b>SC-05</b> — Denial-of-service Protection [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-05(01) | Restrict Ability to Attack Other Systems | — |
| SC-05(02) | Capacity, Bandwidth, and Redundancy | — |
| SC-05(03) | Detection and Monitoring | — |

</details>
- **SC-06** — Resource Availability [—]
<details>
<summary><b>SC-07</b> — Boundary Protection [L/M/H] (26개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-07(03) | Access Points | M/H |
| SC-07(04) | External Telecommunications Services | M/H |
| SC-07(05) | Deny by Default — Allow by Exception | M/H |
| SC-07(07) | Split Tunneling for Remote Devices | M/H |
| SC-07(08) | Route Traffic to Authenticated Proxy Servers | M/H |
| SC-07(09) | Restrict Threatening Outgoing Communications Traffic | — |
| SC-07(10) | Prevent Exfiltration | — |
| SC-07(11) | Restrict Incoming Communications Traffic | — |
| SC-07(12) | Host-based Protection | — |
| SC-07(13) | Isolation of Security Tools, Mechanisms, and Support Components | — |
| SC-07(14) | Protect Against Unauthorized Physical Connections | — |
| SC-07(15) | Networked Privileged Accesses | — |
| SC-07(16) | Prevent Discovery of System Components | — |
| SC-07(17) | Automated Enforcement of Protocol Formats | — |
| SC-07(18) | Fail Secure | H |
| SC-07(19) | Block Communication from Non-organizationally Configured Hosts | — |
| SC-07(20) | Dynamic Isolation and Segregation | — |
| SC-07(21) | Isolation of System Components | H |
| SC-07(22) | Separate Subnets for Connecting to Different Security Domains | — |
| SC-07(23) | Disable Sender Feedback on Protocol Validation Failure | — |
| SC-07(24) | Personally Identifiable Information | — |
| SC-07(25) | Unclassified National Security System Connections | — |
| SC-07(26) | Classified National Security System Connections | — |
| SC-07(27) | Unclassified Non-national Security System Connections | — |
| SC-07(28) | Connections to Public Networks | — |
| SC-07(29) | Separate Subnets to Isolate Functions | — |

</details>
<details>
<summary><b>SC-08</b> — Transmission Confidentiality and Integrity [M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-08(01) | Cryptographic Protection | M/H |
| SC-08(02) | Pre- and Post-transmission Handling | — |
| SC-08(03) | Cryptographic Protection for Message Externals | — |
| SC-08(04) | Conceal or Randomize Communications | — |
| SC-08(05) | Protected Distribution System | — |

</details>
- **SC-10** — Network Disconnect [M/H]
<details>
<summary><b>SC-11</b> — Trusted Path [—] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-11(01) | Irrefutable Communications Path | — |

</details>
<details>
<summary><b>SC-12</b> — Cryptographic Key Establishment and Management [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-12(01) | Availability | H |
| SC-12(02) | Symmetric Keys | — |
| SC-12(03) | Asymmetric Keys | — |
| SC-12(06) | Physical Control of Keys | — |

</details>
- **SC-13** — Cryptographic Protection [L/M/H]
<details>
<summary><b>SC-15</b> — Collaborative Computing Devices and Applications [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-15(01) | Physical or Logical Disconnect | — |
| SC-15(03) | Disabling and Removal in Secure Work Areas | — |
| SC-15(04) | Explicitly Indicate Current Participants | — |

</details>
<details>
<summary><b>SC-16</b> — Transmission of Security and Privacy Attributes [—] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-16(01) | Integrity Verification | — |
| SC-16(02) | Anti-spoofing Mechanisms | — |
| SC-16(03) | Cryptographic Binding | — |

</details>
- **SC-17** — Public Key Infrastructure Certificates [M/H]
<details>
<summary><b>SC-18</b> — Mobile Code [M/H] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-18(01) | Identify Unacceptable Code and Take Corrective Actions | — |
| SC-18(02) | Acquisition, Development, and Use | — |
| SC-18(03) | Prevent Downloading and Execution | — |
| SC-18(04) | Prevent Automatic Execution | — |
| SC-18(05) | Allow Execution Only in Confined Environments | — |

</details>
<details>
<summary><b>SC-20</b> — Secure Name/Address Resolution Service (Authoritative Source) [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-20(02) | Data Origin and Integrity | — |

</details>
- **SC-21** — Secure Name/Address Resolution Service (Recursive or Caching Resolver) [L/M/H]
- **SC-22** — Architecture and Provisioning for Name/Address Resolution Service [L/M/H]
<details>
<summary><b>SC-23</b> — Session Authenticity [M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-23(01) | Invalidate Session Identifiers at Logout | — |
| SC-23(03) | Unique System-generated Session Identifiers | — |
| SC-23(05) | Allowed Certificate Authorities | — |

</details>
- **SC-24** — Fail in Known State [H]
- **SC-25** — Thin Nodes [—]
- **SC-26** — Decoys [—]
- **SC-27** — Platform-independent Applications [—]
<details>
<summary><b>SC-28</b> — Protection of Information at Rest [M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-28(01) | Cryptographic Protection | M/H |
| SC-28(02) | Offline Storage | — |
| SC-28(03) | Cryptographic Keys | — |

</details>
<details>
<summary><b>SC-29</b> — Heterogeneity [—] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-29(01) | Virtualization Techniques | — |

</details>
<details>
<summary><b>SC-30</b> — Concealment and Misdirection [—] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-30(02) | Randomness | — |
| SC-30(03) | Change Processing and Storage Locations | — |
| SC-30(04) | Misleading Information | — |
| SC-30(05) | Concealment of System Components | — |

</details>
<details>
<summary><b>SC-31</b> — Covert Channel Analysis [—] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-31(01) | Test Covert Channels for Exploitability | — |
| SC-31(02) | Maximum Bandwidth | — |
| SC-31(03) | Measure Bandwidth in Operational Environments | — |

</details>
<details>
<summary><b>SC-32</b> — System Partitioning [—] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-32(01) | Separate Physical Domains for Privileged Functions | — |

</details>
<details>
<summary><b>SC-34</b> — Non-modifiable Executable Programs [—] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-34(01) | No Writable Storage | — |
| SC-34(02) | Integrity Protection on Read-only Media | — |

</details>
- **SC-35** — External Malicious Code Identification [—]
<details>
<summary><b>SC-36</b> — Distributed Processing and Storage [—] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-36(01) | Polling Techniques | — |
| SC-36(02) | Synchronization | — |

</details>
<details>
<summary><b>SC-37</b> — Out-of-band Channels [—] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-37(01) | Ensure Delivery and Transmission | — |

</details>
- **SC-38** — Operations Security [—]
<details>
<summary><b>SC-39</b> — Process Isolation [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-39(01) | Hardware Separation | — |
| SC-39(02) | Separate Execution Domain Per Thread | — |

</details>
<details>
<summary><b>SC-40</b> — Wireless Link Protection [—] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-40(01) | Electromagnetic Interference | — |
| SC-40(02) | Reduce Detection Potential | — |
| SC-40(03) | Imitative or Manipulative Communications Deception | — |
| SC-40(04) | Signal Parameter Identification | — |

</details>
- **SC-41** — Port and I/O Device Access [—]
<details>
<summary><b>SC-42</b> — Sensor Capability and Data [—] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-42(01) | Reporting to Authorized Individuals or Roles | — |
| SC-42(02) | Authorized Use | — |
| SC-42(04) | Notice of Collection | — |
| SC-42(05) | Collection Minimization | — |

</details>
- **SC-43** — Usage Restrictions [—]
- **SC-44** — Detonation Chambers [—]
<details>
<summary><b>SC-45</b> — System Time Synchronization [—] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-45(01) | Synchronization with Authoritative Time Source | — |
| SC-45(02) | Secondary Authoritative Time Source | — |

</details>
- **SC-46** — Cross Domain Policy Enforcement [—]
- **SC-47** — Alternate Communications Paths [—]
<details>
<summary><b>SC-48</b> — Sensor Relocation [—] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SC-48(01) | Dynamic Relocation of Sensors or Monitoring Capabilities | — |

</details>
- **SC-49** — Hardware-enforced Separation and Policy Enforcement [—]
- **SC-50** — Software-enforced Separation and Policy Enforcement [—]
- **SC-51** — Hardware-based Protection [—]

</details>

<details>
<summary><b>SI — System and Information Integrity (22 base / 80 enhancement)</b></summary>

- **SI-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>SI-02</b> — Flaw Remediation [L/M/H] (6개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-02(02) | Automated Flaw Remediation Status | M/H |
| SI-02(03) | Time to Remediate Flaws and Benchmarks for Corrective Actions | — |
| SI-02(04) | Automated Patch Management Tools | — |
| SI-02(05) | Automatic Software and Firmware Updates | — |
| SI-02(06) | Removal of Previous Versions of Software and Firmware | — |
| SI-02(07) | Root Cause Analysis | — |

</details>
<details>
<summary><b>SI-03</b> — Malicious Code Protection [L/M/H] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-03(04) | Updates Only by Privileged Users | — |
| SI-03(06) | Testing and Verification | — |
| SI-03(08) | Detect Unauthorized Commands | — |
| SI-03(10) | Malicious Code Analysis | — |

</details>
<details>
<summary><b>SI-04</b> — System Monitoring [L/M/H] (23개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-04(01) | System-wide Intrusion Detection System | — |
| SI-04(02) | Automated Tools and Mechanisms for Real-time Analysis | M/H |
| SI-04(03) | Automated Tool and Mechanism Integration | — |
| SI-04(04) | Inbound and Outbound Communications Traffic | M/H |
| SI-04(05) | System-generated Alerts | M/H |
| SI-04(07) | Automated Response to Suspicious Events | — |
| SI-04(09) | Testing of Monitoring Tools and Mechanisms | — |
| SI-04(10) | Visibility of Encrypted Communications | H |
| SI-04(11) | Analyze Communications Traffic Anomalies | — |
| SI-04(12) | Automated Organization-generated Alerts | H |
| SI-04(13) | Analyze Traffic and Event Patterns | — |
| SI-04(14) | Wireless Intrusion Detection | H |
| SI-04(15) | Wireless to Wireline Communications | — |
| SI-04(16) | Correlate Monitoring Information | — |
| SI-04(17) | Integrated Situational Awareness | — |
| SI-04(18) | Analyze Traffic and Covert Exfiltration | — |
| SI-04(19) | Risk for Individuals | — |
| SI-04(20) | Privileged Users | H |
| SI-04(21) | Probationary Periods | — |
| SI-04(22) | Unauthorized Network Services | H |
| SI-04(23) | Host-based Devices | — |
| SI-04(24) | Indicators of Compromise | — |
| SI-04(25) | Optimize Network Traffic Analysis | — |

</details>
<details>
<summary><b>SI-05</b> — Security Alerts, Advisories, and Directives [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-05(01) | Automated Alerts and Advisories | H |

</details>
<details>
<summary><b>SI-06</b> — Security and Privacy Function Verification [H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-06(02) | Automation Support for Distributed Testing | — |
| SI-06(03) | Report Verification Results | — |

</details>
<details>
<summary><b>SI-07</b> — Software, Firmware, and Information Integrity [M/H] (13개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-07(01) | Integrity Checks | M/H |
| SI-07(02) | Automated Notifications of Integrity Violations | H |
| SI-07(03) | Centrally Managed Integrity Tools | — |
| SI-07(05) | Automated Response to Integrity Violations | H |
| SI-07(06) | Cryptographic Protection | — |
| SI-07(07) | Integration of Detection and Response | M/H |
| SI-07(08) | Auditing Capability for Significant Events | — |
| SI-07(09) | Verify Boot Process | — |
| SI-07(10) | Protection of Boot Firmware | — |
| SI-07(12) | Integrity Verification | — |
| SI-07(15) | Code Authentication | H |
| SI-07(16) | Time Limit on Process Execution Without Supervision | — |
| SI-07(17) | Runtime Application Self-protection | — |

</details>
<details>
<summary><b>SI-08</b> — Spam Protection [M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-08(02) | Automatic Updates | M/H |
| SI-08(03) | Continuous Learning Capability | — |

</details>
<details>
<summary><b>SI-10</b> — Information Input Validation [M/H] (6개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-10(01) | Manual Override Capability | — |
| SI-10(02) | Review and Resolve Errors | — |
| SI-10(03) | Predictable Behavior | — |
| SI-10(04) | Timing Interactions | — |
| SI-10(05) | Restrict Inputs to Trusted Sources and Approved Formats | — |
| SI-10(06) | Injection Prevention | — |

</details>
- **SI-11** — Error Handling [M/H]
<details>
<summary><b>SI-12</b> — Information Management and Retention [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-12(01) | Limit Personally Identifiable Information Elements | — |
| SI-12(02) | Minimize Personally Identifiable Information in Testing, Training, and Research | — |
| SI-12(03) | Information Disposal | — |

</details>
<details>
<summary><b>SI-13</b> — Predictable Failure Prevention [—] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-13(01) | Transferring Component Responsibilities | — |
| SI-13(03) | Manual Transfer Between Components | — |
| SI-13(04) | Standby Component Installation and Notification | — |
| SI-13(05) | Failover Capability | — |

</details>
<details>
<summary><b>SI-14</b> — Non-persistence [—] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-14(01) | Refresh from Trusted Sources | — |
| SI-14(02) | Non-persistent Information | — |
| SI-14(03) | Non-persistent Connectivity | — |

</details>
- **SI-15** — Information Output Filtering [—]
- **SI-16** — Memory Protection [M/H]
- **SI-17** — Fail-safe Procedures [—]
<details>
<summary><b>SI-18</b> — Personally Identifiable Information Quality Operations [—] (5개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-18(01) | Automation Support | — |
| SI-18(02) | Data Tags | — |
| SI-18(03) | Collection | — |
| SI-18(04) | Individual Requests | — |
| SI-18(05) | Notice of Correction or Deletion | — |

</details>
<details>
<summary><b>SI-19</b> — De-identification [—] (8개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SI-19(01) | Collection | — |
| SI-19(02) | Archiving | — |
| SI-19(03) | Release | — |
| SI-19(04) | Removal, Masking, Encryption, Hashing, or Replacement of Direct Identifiers | — |
| SI-19(05) | Statistical Disclosure Control | — |
| SI-19(06) | Differential Privacy | — |
| SI-19(07) | Validated Algorithms and Software | — |
| SI-19(08) | Motivated Intruder | — |

</details>
- **SI-20** — Tainting [—]
- **SI-21** — Information Refresh [—]
- **SI-22** — Information Diversity [—]
- **SI-23** — Information Fragmentation [—]

</details>

<details>
<summary><b>SR — Supply Chain Risk Management (12 base / 15 enhancement)</b></summary>

- **SR-01** — Policy and Procedures [L/M/H]
<details>
<summary><b>SR-02</b> — Supply Chain Risk Management Plan [L/M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SR-02(01) | Establish SCRM Team | L/M/H |

</details>
<details>
<summary><b>SR-03</b> — Supply Chain Controls and Processes [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SR-03(01) | Diverse Supply Base | — |
| SR-03(02) | Limitation of Harm | — |
| SR-03(03) | Sub-tier Flow Down | — |

</details>
<details>
<summary><b>SR-04</b> — Provenance [—] (4개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SR-04(01) | Identity | — |
| SR-04(02) | Track and Trace | — |
| SR-04(03) | Validate as Genuine and Not Altered | — |
| SR-04(04) | Supply Chain Integrity — Pedigree | — |

</details>
<details>
<summary><b>SR-05</b> — Acquisition Strategies, Tools, and Methods [L/M/H] (2개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SR-05(01) | Adequate Supply | — |
| SR-05(02) | Assessments Prior to Selection, Acceptance, Modification, or Update | — |

</details>
<details>
<summary><b>SR-06</b> — Supplier Assessments and Reviews [M/H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SR-06(01) | Testing and Analysis | — |

</details>
- **SR-07** — Supply Chain Operations Security [—]
- **SR-08** — Notification Agreements [L/M/H]
<details>
<summary><b>SR-09</b> — Tamper Resistance and Detection [H] (1개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SR-09(01) | Multiple Stages of System Development Life Cycle | H |

</details>
- **SR-10** — Inspection of Systems or Components [L/M/H]
<details>
<summary><b>SR-11</b> — Component Authenticity [L/M/H] (3개 enhancement)</summary>

| Enhancement | 제목 | 기준선 |
|-------------|------|--------|
| SR-11(01) | Anti-counterfeit Training | L/M/H |
| SR-11(02) | Configuration Control for Component Service and Repair | L/M/H |
| SR-11(03) | Anti-counterfeit Scanning | — |

</details>
- **SR-12** — Component Disposal [L/M/H]

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
