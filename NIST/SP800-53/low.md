# SP 800-53 LOW 체크리스트

## 개요

| 항목 | 내용 |
|------|------|
| **기준선** | LOW (낮음) |
| **영향도** | 제한적 피해 |
| **적용 대상** | 기밀성, 무결성, 가용성의 손실이 조직 운영, 자산, 개인에게 **제한적인** 부정적 영향을 미치는 시스템 |
| **총 컨트롤 수** | 149개 (base 131개 + enhancement 18개) |
| **적용 패밀리** | 18개 (PM, PT 제외) |
| **근거** | SP 800-53B, FIPS 199 |

> LOW 기준선은 가장 기본적인 컨트롤 세트입니다. MODERATE와 HIGH 기준선은 LOW를 **완전히 포함**하며 추가 컨트롤을 요구합니다. (LOW ⊂ MODERATE ⊂ HIGH)

---

## 패밀리별 컨트롤

### 한눈에 보기

| 패밀리 | 컨트롤 수 |
|--------|----------|
| AC — Access Control | 11개 |
| AT — Awareness and Training | 5개 |
| AU — Audit and Accountability | 10개 |
| CA — Assessment, Authorization, and Monitoring | 8개 |
| CM — Configuration Management | 9개 |
| CP — Contingency Planning | 6개 |
| IA — Identification and Authentication | 16개 |
| IR — Incident Response | 7개 |
| MA — Maintenance | 4개 |
| MP — Media Protection | 4개 |
| PE — Physical and Environmental Protection | 10개 |
| PL — Planning | 6개 |
| PS — Personnel Security | 9개 |
| RA — Risk Assessment | 8개 |
| SA — System and Services Acquisition | 9개 |
| SC — System and Communications Protection | 10개 |
| SI — System and Information Integrity | 6개 |
| SR — Supply Chain Risk Management | 11개 |
| **합계** | **149개** |

---

<details>
<summary><b>AC — Access Control (11개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **AC-01** | **Policy and Procedures** | **Base** |
| **AC-02** | **Account Management** | **Base** |
| **AC-03** | **Access Enforcement** | **Base** |
| **AC-07** | **Unsuccessful Logon Attempts** | **Base** |
| **AC-08** | **System Use Notification** | **Base** |
| **AC-14** | **Permitted Actions Without Identification or Authentication** | **Base** |
| **AC-17** | **Remote Access** | **Base** |
| **AC-18** | **Wireless Access** | **Base** |
| **AC-19** | **Access Control for Mobile Devices** | **Base** |
| **AC-20** | **Use of External Systems** | **Base** |
| **AC-22** | **Publicly Accessible Content** | **Base** |

</details>

<details>
<summary><b>AT — Awareness and Training (5개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **AT-01** | **Policy and Procedures** | **Base** |
| **AT-02** | **Literacy Training and Awareness** | **Base** |
| ↳ AT-02(02) | Insider Threat | Enhancement |
| **AT-03** | **Role-based Training** | **Base** |
| **AT-04** | **Training Records** | **Base** |

</details>

<details>
<summary><b>AU — Audit and Accountability (10개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **AU-01** | **Policy and Procedures** | **Base** |
| **AU-02** | **Event Logging** | **Base** |
| **AU-03** | **Content of Audit Records** | **Base** |
| **AU-04** | **Audit Log Storage Capacity** | **Base** |
| **AU-05** | **Response to Audit Logging Process Failures** | **Base** |
| **AU-06** | **Audit Record Review, Analysis, and Reporting** | **Base** |
| **AU-08** | **Time Stamps** | **Base** |
| **AU-09** | **Protection of Audit Information** | **Base** |
| **AU-11** | **Audit Record Retention** | **Base** |
| **AU-12** | **Audit Record Generation** | **Base** |

</details>

<details>
<summary><b>CA — Assessment, Authorization, and Monitoring (8개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **CA-01** | **Policy and Procedures** | **Base** |
| **CA-02** | **Control Assessments** | **Base** |
| **CA-03** | **Information Exchange** | **Base** |
| **CA-05** | **Plan of Action and Milestones** | **Base** |
| **CA-06** | **Authorization** | **Base** |
| **CA-07** | **Continuous Monitoring** | **Base** |
| ↳ CA-07(04) | Risk Monitoring | Enhancement |
| **CA-09** | **Internal System Connections** | **Base** |

</details>

<details>
<summary><b>CM — Configuration Management (9개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **CM-01** | **Policy and Procedures** | **Base** |
| **CM-02** | **Baseline Configuration** | **Base** |
| **CM-04** | **Impact Analyses** | **Base** |
| **CM-05** | **Access Restrictions for Change** | **Base** |
| **CM-06** | **Configuration Settings** | **Base** |
| **CM-07** | **Least Functionality** | **Base** |
| **CM-08** | **System Component Inventory** | **Base** |
| **CM-10** | **Software Usage Restrictions** | **Base** |
| **CM-11** | **User-installed Software** | **Base** |

</details>

<details>
<summary><b>CP — Contingency Planning (6개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **CP-01** | **Policy and Procedures** | **Base** |
| **CP-02** | **Contingency Plan** | **Base** |
| **CP-03** | **Contingency Training** | **Base** |
| **CP-04** | **Contingency Plan Testing** | **Base** |
| **CP-09** | **System Backup** | **Base** |
| **CP-10** | **System Recovery and Reconstitution** | **Base** |

</details>

<details>
<summary><b>IA — Identification and Authentication (16개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **IA-01** | **Policy and Procedures** | **Base** |
| **IA-02** | **Identification and Authentication (Organizational Users)** | **Base** |
| ↳ IA-02(01) | Multi-factor Authentication to Privileged Accounts | Enhancement |
| ↳ IA-02(02) | Multi-factor Authentication to Non-privileged Accounts | Enhancement |
| ↳ IA-02(08) | Access to Accounts — Replay Resistant | Enhancement |
| ↳ IA-02(12) | Acceptance of PIV Credentials | Enhancement |
| **IA-04** | **Identifier Management** | **Base** |
| **IA-05** | **Authenticator Management** | **Base** |
| ↳ IA-05(01) | Password-based Authentication | Enhancement |
| **IA-06** | **Authentication Feedback** | **Base** |
| **IA-07** | **Cryptographic Module Authentication** | **Base** |
| **IA-08** | **Identification and Authentication (Non-organizational Users)** | **Base** |
| ↳ IA-08(01) | Acceptance of PIV Credentials from Other Agencies | Enhancement |
| ↳ IA-08(02) | Acceptance of External Authenticators | Enhancement |
| ↳ IA-08(04) | Use of Defined Profiles | Enhancement |
| **IA-11** | **Re-authentication** | **Base** |

</details>

<details>
<summary><b>IR — Incident Response (7개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **IR-01** | **Policy and Procedures** | **Base** |
| **IR-02** | **Incident Response Training** | **Base** |
| **IR-04** | **Incident Handling** | **Base** |
| **IR-05** | **Incident Monitoring** | **Base** |
| **IR-06** | **Incident Reporting** | **Base** |
| **IR-07** | **Incident Response Assistance** | **Base** |
| **IR-08** | **Incident Response Plan** | **Base** |

</details>

<details>
<summary><b>MA — Maintenance (4개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **MA-01** | **Policy and Procedures** | **Base** |
| **MA-02** | **Controlled Maintenance** | **Base** |
| **MA-04** | **Nonlocal Maintenance** | **Base** |
| **MA-05** | **Maintenance Personnel** | **Base** |

</details>

<details>
<summary><b>MP — Media Protection (4개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **MP-01** | **Policy and Procedures** | **Base** |
| **MP-02** | **Media Access** | **Base** |
| **MP-06** | **Media Sanitization** | **Base** |
| **MP-07** | **Media Use** | **Base** |

</details>

<details>
<summary><b>PE — Physical and Environmental Protection (10개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **PE-01** | **Policy and Procedures** | **Base** |
| **PE-02** | **Physical Access Authorizations** | **Base** |
| **PE-03** | **Physical Access Control** | **Base** |
| **PE-06** | **Monitoring Physical Access** | **Base** |
| **PE-08** | **Visitor Access Records** | **Base** |
| **PE-12** | **Emergency Lighting** | **Base** |
| **PE-13** | **Fire Protection** | **Base** |
| **PE-14** | **Environmental Controls** | **Base** |
| **PE-15** | **Water Damage Protection** | **Base** |
| **PE-16** | **Delivery and Removal** | **Base** |

</details>

<details>
<summary><b>PL — Planning (6개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **PL-01** | **Policy and Procedures** | **Base** |
| **PL-02** | **System Security and Privacy Plans** | **Base** |
| **PL-04** | **Rules of Behavior** | **Base** |
| ↳ PL-04(01) | Social Media and External Site/Application Usage Restrictions | Enhancement |
| **PL-10** | **Baseline Selection** | **Base** |
| **PL-11** | **Baseline Tailoring** | **Base** |

</details>

<details>
<summary><b>PS — Personnel Security (9개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **PS-01** | **Policy and Procedures** | **Base** |
| **PS-02** | **Position Risk Designation** | **Base** |
| **PS-03** | **Personnel Screening** | **Base** |
| **PS-04** | **Personnel Termination** | **Base** |
| **PS-05** | **Personnel Transfer** | **Base** |
| **PS-06** | **Access Agreements** | **Base** |
| **PS-07** | **External Personnel Security** | **Base** |
| **PS-08** | **Personnel Sanctions** | **Base** |
| **PS-09** | **Position Descriptions** | **Base** |

</details>

<details>
<summary><b>RA — Risk Assessment (8개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **RA-01** | **Policy and Procedures** | **Base** |
| **RA-02** | **Security Categorization** | **Base** |
| **RA-03** | **Risk Assessment** | **Base** |
| ↳ RA-03(01) | Supply Chain Risk Assessment | Enhancement |
| **RA-05** | **Vulnerability Monitoring and Scanning** | **Base** |
| ↳ RA-05(02) | Update Vulnerabilities to Be Scanned | Enhancement |
| ↳ RA-05(11) | Public Disclosure Program | Enhancement |
| **RA-07** | **Risk Response** | **Base** |

</details>

<details>
<summary><b>SA — System and Services Acquisition (9개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **SA-01** | **Policy and Procedures** | **Base** |
| **SA-02** | **Allocation of Resources** | **Base** |
| **SA-03** | **System Development Life Cycle** | **Base** |
| **SA-04** | **Acquisition Process** | **Base** |
| ↳ SA-04(10) | Use of Approved PIV Products | Enhancement |
| **SA-05** | **System Documentation** | **Base** |
| **SA-08** | **Security and Privacy Engineering Principles** | **Base** |
| **SA-09** | **External System Services** | **Base** |
| **SA-22** | **Unsupported System Components** | **Base** |

</details>

<details>
<summary><b>SC — System and Communications Protection (10개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **SC-01** | **Policy and Procedures** | **Base** |
| **SC-05** | **Denial-of-service Protection** | **Base** |
| **SC-07** | **Boundary Protection** | **Base** |
| **SC-12** | **Cryptographic Key Establishment and Management** | **Base** |
| **SC-13** | **Cryptographic Protection** | **Base** |
| **SC-15** | **Collaborative Computing Devices and Applications** | **Base** |
| **SC-20** | **Secure Name/Address Resolution Service (Authoritative Source)** | **Base** |
| **SC-21** | **Secure Name/Address Resolution Service (Recursive or Caching Resolver)** | **Base** |
| **SC-22** | **Architecture and Provisioning for Name/Address Resolution Service** | **Base** |
| **SC-39** | **Process Isolation** | **Base** |

</details>

<details>
<summary><b>SI — System and Information Integrity (6개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **SI-01** | **Policy and Procedures** | **Base** |
| **SI-02** | **Flaw Remediation** | **Base** |
| **SI-03** | **Malicious Code Protection** | **Base** |
| **SI-04** | **System Monitoring** | **Base** |
| **SI-05** | **Security Alerts, Advisories, and Directives** | **Base** |
| **SI-12** | **Information Management and Retention** | **Base** |

</details>

<details>
<summary><b>SR — Supply Chain Risk Management (11개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **SR-01** | **Policy and Procedures** | **Base** |
| **SR-02** | **Supply Chain Risk Management Plan** | **Base** |
| ↳ SR-02(01) | Establish SCRM Team | Enhancement |
| **SR-03** | **Supply Chain Controls and Processes** | **Base** |
| **SR-05** | **Acquisition Strategies, Tools, and Methods** | **Base** |
| **SR-08** | **Notification Agreements** | **Base** |
| **SR-10** | **Inspection of Systems or Components** | **Base** |
| **SR-11** | **Component Authenticity** | **Base** |
| ↳ SR-11(01) | Anti-counterfeit Training | Enhancement |
| ↳ SR-11(02) | Configuration Control for Component Service and Repair | Enhancement |
| **SR-12** | **Component Disposal** | **Base** |

</details>

---

## 참고

- 이 체크리스트는 NIST OSCAL 공식 프로파일에서 추출한 데이터 기준입니다.
- PM(Program Management)과 PT(PII Processing and Transparency) 패밀리는 기준선에 포함되지 않으며, 조직 수준에서 별도 적용됩니다.
- 컨트롤 상세(Statement, Guidance 등)는 [SP 800-53 상세 문서](../README.md)를 참고하세요.