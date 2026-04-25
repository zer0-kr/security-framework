# SP 800-53 HIGH 체크리스트

## 개요

| 항목 | 내용 |
|------|------|
| **기준선** | HIGH (높음) |
| **영향도** | 치명적/재앙적 피해 |
| **적용 대상** | 기밀성, 무결성, 가용성의 손실이 조직 운영, 자산, 개인에게 **치명적이거나 재앙적인** 부정적 영향을 미치는 시스템 |
| **총 컨트롤 수** | 370개 (base 188개 + enhancement 182개) |
| **적용 패밀리** | 18개 (PM, PT 제외) |
| **근거** | SP 800-53B, FIPS 199 |

> HIGH 기준선은 MODERATE(287개)를 **완전히 포함**하며, 83개가 추가된 총 370개입니다. HIGH만 충족하면 LOW와 MODERATE는 별도로 충족할 필요가 없습니다. (LOW ⊂ MODERATE ⊂ HIGH)

---

## 패밀리별 컨트롤

### 한눈에 보기

| 패밀리 | 컨트롤 수 |
|--------|----------|
| AC — Access Control | 46개 |
| AT — Awareness and Training | 6개 |
| AU — Audit and Accountability | 25개 |
| CA — Assessment, Authorization, and Monitoring | 14개 |
| CM — Configuration Management | 32개 |
| CP — Contingency Planning | 35개 |
| IA — Identification and Authentication | 26개 |
| IR — Incident Response | 18개 |
| MA — Maintenance | 12개 |
| MP — Media Protection | 10개 |
| PE — Physical and Environmental Protection | 25개 |
| PL — Planning | 7개 |
| PS — Personnel Security | 10개 |
| RA — Risk Assessment | 11개 |
| SA — System and Services Acquisition | 21개 |
| SC — System and Communications Protection | 30개 |
| SI — System and Information Integrity | 28개 |
| SR — Supply Chain Risk Management | 14개 |
| **합계** | **370개** |

---

<details>
<summary><b>AC — Access Control (46개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **AC-01** | **Policy and Procedures** | **Base** |
| **AC-02** | **Account Management** | **Base** |
| ↳ AC-02(01) | Automated System Account Management | Enhancement |
| ↳ AC-02(02) | Automated Temporary and Emergency Account Management | Enhancement |
| ↳ AC-02(03) | Disable Accounts | Enhancement |
| ↳ AC-02(04) | Automated Audit Actions | Enhancement |
| ↳ AC-02(05) | Inactivity Logout | Enhancement |
| ↳ AC-02(11) | Usage Conditions | Enhancement |
| ↳ AC-02(12) | Account Monitoring for Atypical Usage | Enhancement |
| ↳ AC-02(13) | Disable Accounts for High-risk Individuals | Enhancement |
| **AC-03** | **Access Enforcement** | **Base** |
| **AC-04** | **Information Flow Enforcement** | **Base** |
| ↳ AC-04(04) | Flow Control of Encrypted Information | Enhancement |
| **AC-05** | **Separation of Duties** | **Base** |
| **AC-06** | **Least Privilege** | **Base** |
| ↳ AC-06(01) | Authorize Access to Security Functions | Enhancement |
| ↳ AC-06(02) | Non-privileged Access for Nonsecurity Functions | Enhancement |
| ↳ AC-06(03) | Network Access to Privileged Commands | Enhancement |
| ↳ AC-06(05) | Privileged Accounts | Enhancement |
| ↳ AC-06(07) | Review of User Privileges | Enhancement |
| ↳ AC-06(09) | Log Use of Privileged Functions | Enhancement |
| ↳ AC-06(10) | Prohibit Non-privileged Users from Executing Privileged Functions | Enhancement |
| **AC-07** | **Unsuccessful Logon Attempts** | **Base** |
| **AC-08** | **System Use Notification** | **Base** |
| **AC-10** | **Concurrent Session Control** | **Base** |
| **AC-11** | **Device Lock** | **Base** |
| ↳ AC-11(01) | Pattern-hiding Displays | Enhancement |
| **AC-12** | **Session Termination** | **Base** |
| **AC-14** | **Permitted Actions Without Identification or Authentication** | **Base** |
| **AC-17** | **Remote Access** | **Base** |
| ↳ AC-17(01) | Monitoring and Control | Enhancement |
| ↳ AC-17(02) | Protection of Confidentiality and Integrity Using Encryption | Enhancement |
| ↳ AC-17(03) | Managed Access Control Points | Enhancement |
| ↳ AC-17(04) | Privileged Commands and Access | Enhancement |
| **AC-18** | **Wireless Access** | **Base** |
| ↳ AC-18(01) | Authentication and Encryption | Enhancement |
| ↳ AC-18(03) | Disable Wireless Networking | Enhancement |
| ↳ AC-18(04) | Restrict Configurations by Users | Enhancement |
| ↳ AC-18(05) | Antennas and Transmission Power Levels | Enhancement |
| **AC-19** | **Access Control for Mobile Devices** | **Base** |
| ↳ AC-19(05) | Full Device or Container-based Encryption | Enhancement |
| **AC-20** | **Use of External Systems** | **Base** |
| ↳ AC-20(01) | Limits on Authorized Use | Enhancement |
| ↳ AC-20(02) | Portable Storage Devices — Restricted Use | Enhancement |
| **AC-21** | **Information Sharing** | **Base** |
| **AC-22** | **Publicly Accessible Content** | **Base** |

</details>

<details>
<summary><b>AT — Awareness and Training (6개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **AT-01** | **Policy and Procedures** | **Base** |
| **AT-02** | **Literacy Training and Awareness** | **Base** |
| ↳ AT-02(02) | Insider Threat | Enhancement |
| ↳ AT-02(03) | Social Engineering and Mining | Enhancement |
| **AT-03** | **Role-based Training** | **Base** |
| **AT-04** | **Training Records** | **Base** |

</details>

<details>
<summary><b>AU — Audit and Accountability (25개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **AU-01** | **Policy and Procedures** | **Base** |
| **AU-02** | **Event Logging** | **Base** |
| **AU-03** | **Content of Audit Records** | **Base** |
| ↳ AU-03(01) | Additional Audit Information | Enhancement |
| **AU-04** | **Audit Log Storage Capacity** | **Base** |
| **AU-05** | **Response to Audit Logging Process Failures** | **Base** |
| ↳ AU-05(01) | Storage Capacity Warning | Enhancement |
| ↳ AU-05(02) | Real-time Alerts | Enhancement |
| **AU-06** | **Audit Record Review, Analysis, and Reporting** | **Base** |
| ↳ AU-06(01) | Automated Process Integration | Enhancement |
| ↳ AU-06(03) | Correlate Audit Record Repositories | Enhancement |
| ↳ AU-06(05) | Integrated Analysis of Audit Records | Enhancement |
| ↳ AU-06(06) | Correlation with Physical Monitoring | Enhancement |
| **AU-07** | **Audit Record Reduction and Report Generation** | **Base** |
| ↳ AU-07(01) | Automatic Processing | Enhancement |
| **AU-08** | **Time Stamps** | **Base** |
| **AU-09** | **Protection of Audit Information** | **Base** |
| ↳ AU-09(02) | Store on Separate Physical Systems or Components | Enhancement |
| ↳ AU-09(03) | Cryptographic Protection | Enhancement |
| ↳ AU-09(04) | Access by Subset of Privileged Users | Enhancement |
| **AU-10** | **Non-repudiation** | **Base** |
| **AU-11** | **Audit Record Retention** | **Base** |
| **AU-12** | **Audit Record Generation** | **Base** |
| ↳ AU-12(01) | System-wide and Time-correlated Audit Trail | Enhancement |
| ↳ AU-12(03) | Changes by Authorized Individuals | Enhancement |

</details>

<details>
<summary><b>CA — Assessment, Authorization, and Monitoring (14개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **CA-01** | **Policy and Procedures** | **Base** |
| **CA-02** | **Control Assessments** | **Base** |
| ↳ CA-02(01) | Independent Assessors | Enhancement |
| ↳ CA-02(02) | Specialized Assessments | Enhancement |
| **CA-03** | **Information Exchange** | **Base** |
| ↳ CA-03(06) | Transfer Authorizations | Enhancement |
| **CA-05** | **Plan of Action and Milestones** | **Base** |
| **CA-06** | **Authorization** | **Base** |
| **CA-07** | **Continuous Monitoring** | **Base** |
| ↳ CA-07(01) | Independent Assessment | Enhancement |
| ↳ CA-07(04) | Risk Monitoring | Enhancement |
| **CA-08** | **Penetration Testing** | **Base** |
| ↳ CA-08(01) | Independent Penetration Testing Agent or Team | Enhancement |
| **CA-09** | **Internal System Connections** | **Base** |

</details>

<details>
<summary><b>CM — Configuration Management (32개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **CM-01** | **Policy and Procedures** | **Base** |
| **CM-02** | **Baseline Configuration** | **Base** |
| ↳ CM-02(02) | Automation Support for Accuracy and Currency | Enhancement |
| ↳ CM-02(03) | Retention of Previous Configurations | Enhancement |
| ↳ CM-02(07) | Configure Systems and Components for High-risk Areas | Enhancement |
| **CM-03** | **Configuration Change Control** | **Base** |
| ↳ CM-03(01) | Automated Documentation, Notification, and Prohibition of Changes | Enhancement |
| ↳ CM-03(02) | Testing, Validation, and Documentation of Changes | Enhancement |
| ↳ CM-03(04) | Security and Privacy Representatives | Enhancement |
| ↳ CM-03(06) | Cryptography Management | Enhancement |
| **CM-04** | **Impact Analyses** | **Base** |
| ↳ CM-04(01) | Separate Test Environments | Enhancement |
| ↳ CM-04(02) | Verification of Controls | Enhancement |
| **CM-05** | **Access Restrictions for Change** | **Base** |
| ↳ CM-05(01) | Automated Access Enforcement and Audit Records | Enhancement |
| **CM-06** | **Configuration Settings** | **Base** |
| ↳ CM-06(01) | Automated Management, Application, and Verification | Enhancement |
| ↳ CM-06(02) | Respond to Unauthorized Changes | Enhancement |
| **CM-07** | **Least Functionality** | **Base** |
| ↳ CM-07(01) | Periodic Review | Enhancement |
| ↳ CM-07(02) | Prevent Program Execution | Enhancement |
| ↳ CM-07(05) | Authorized Software — Allow-by-exception | Enhancement |
| **CM-08** | **System Component Inventory** | **Base** |
| ↳ CM-08(01) | Updates During Installation and Removal | Enhancement |
| ↳ CM-08(02) | Automated Maintenance | Enhancement |
| ↳ CM-08(03) | Automated Unauthorized Component Detection | Enhancement |
| ↳ CM-08(04) | Accountability Information | Enhancement |
| **CM-09** | **Configuration Management Plan** | **Base** |
| **CM-10** | **Software Usage Restrictions** | **Base** |
| **CM-11** | **User-installed Software** | **Base** |
| **CM-12** | **Information Location** | **Base** |
| ↳ CM-12(01) | Automated Tools to Support Information Location | Enhancement |

</details>

<details>
<summary><b>CP — Contingency Planning (35개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **CP-01** | **Policy and Procedures** | **Base** |
| **CP-02** | **Contingency Plan** | **Base** |
| ↳ CP-02(01) | Coordinate with Related Plans | Enhancement |
| ↳ CP-02(02) | Capacity Planning | Enhancement |
| ↳ CP-02(03) | Resume Mission and Business Functions | Enhancement |
| ↳ CP-02(05) | Continue Mission and Business Functions | Enhancement |
| ↳ CP-02(08) | Identify Critical Assets | Enhancement |
| **CP-03** | **Contingency Training** | **Base** |
| ↳ CP-03(01) | Simulated Events | Enhancement |
| **CP-04** | **Contingency Plan Testing** | **Base** |
| ↳ CP-04(01) | Coordinate with Related Plans | Enhancement |
| ↳ CP-04(02) | Alternate Processing Site | Enhancement |
| **CP-06** | **Alternate Storage Site** | **Base** |
| ↳ CP-06(01) | Separation from Primary Site | Enhancement |
| ↳ CP-06(02) | Recovery Time and Recovery Point Objectives | Enhancement |
| ↳ CP-06(03) | Accessibility | Enhancement |
| **CP-07** | **Alternate Processing Site** | **Base** |
| ↳ CP-07(01) | Separation from Primary Site | Enhancement |
| ↳ CP-07(02) | Accessibility | Enhancement |
| ↳ CP-07(03) | Priority of Service | Enhancement |
| ↳ CP-07(04) | Preparation for Use | Enhancement |
| **CP-08** | **Telecommunications Services** | **Base** |
| ↳ CP-08(01) | Priority of Service Provisions | Enhancement |
| ↳ CP-08(02) | Single Points of Failure | Enhancement |
| ↳ CP-08(03) | Separation of Primary and Alternate Providers | Enhancement |
| ↳ CP-08(04) | Provider Contingency Plan | Enhancement |
| **CP-09** | **System Backup** | **Base** |
| ↳ CP-09(01) | Testing for Reliability and Integrity | Enhancement |
| ↳ CP-09(02) | Test Restoration Using Sampling | Enhancement |
| ↳ CP-09(03) | Separate Storage for Critical Information | Enhancement |
| ↳ CP-09(05) | Transfer to Alternate Storage Site | Enhancement |
| ↳ CP-09(08) | Cryptographic Protection | Enhancement |
| **CP-10** | **System Recovery and Reconstitution** | **Base** |
| ↳ CP-10(02) | Transaction Recovery | Enhancement |
| ↳ CP-10(04) | Restore Within Time Period | Enhancement |

</details>

<details>
<summary><b>IA — Identification and Authentication (26개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **IA-01** | **Policy and Procedures** | **Base** |
| **IA-02** | **Identification and Authentication (Organizational Users)** | **Base** |
| ↳ IA-02(01) | Multi-factor Authentication to Privileged Accounts | Enhancement |
| ↳ IA-02(02) | Multi-factor Authentication to Non-privileged Accounts | Enhancement |
| ↳ IA-02(05) | Individual Authentication with Group Authentication | Enhancement |
| ↳ IA-02(08) | Access to Accounts — Replay Resistant | Enhancement |
| ↳ IA-02(12) | Acceptance of PIV Credentials | Enhancement |
| **IA-03** | **Device Identification and Authentication** | **Base** |
| **IA-04** | **Identifier Management** | **Base** |
| ↳ IA-04(04) | Identify User Status | Enhancement |
| **IA-05** | **Authenticator Management** | **Base** |
| ↳ IA-05(01) | Password-based Authentication | Enhancement |
| ↳ IA-05(02) | Public Key-based Authentication | Enhancement |
| ↳ IA-05(06) | Protection of Authenticators | Enhancement |
| **IA-06** | **Authentication Feedback** | **Base** |
| **IA-07** | **Cryptographic Module Authentication** | **Base** |
| **IA-08** | **Identification and Authentication (Non-organizational Users)** | **Base** |
| ↳ IA-08(01) | Acceptance of PIV Credentials from Other Agencies | Enhancement |
| ↳ IA-08(02) | Acceptance of External Authenticators | Enhancement |
| ↳ IA-08(04) | Use of Defined Profiles | Enhancement |
| **IA-11** | **Re-authentication** | **Base** |
| **IA-12** | **Identity Proofing** | **Base** |
| ↳ IA-12(02) | Identity Evidence | Enhancement |
| ↳ IA-12(03) | Identity Evidence Validation and Verification | Enhancement |
| ↳ IA-12(04) | In-person Validation and Verification | Enhancement |
| ↳ IA-12(05) | Address Confirmation | Enhancement |

</details>

<details>
<summary><b>IR — Incident Response (18개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **IR-01** | **Policy and Procedures** | **Base** |
| **IR-02** | **Incident Response Training** | **Base** |
| ↳ IR-02(01) | Simulated Events | Enhancement |
| ↳ IR-02(02) | Automated Training Environments | Enhancement |
| **IR-03** | **Incident Response Testing** | **Base** |
| ↳ IR-03(02) | Coordination with Related Plans | Enhancement |
| **IR-04** | **Incident Handling** | **Base** |
| ↳ IR-04(01) | Automated Incident Handling Processes | Enhancement |
| ↳ IR-04(04) | Information Correlation | Enhancement |
| ↳ IR-04(11) | Integrated Incident Response Team | Enhancement |
| **IR-05** | **Incident Monitoring** | **Base** |
| ↳ IR-05(01) | Automated Tracking, Data Collection, and Analysis | Enhancement |
| **IR-06** | **Incident Reporting** | **Base** |
| ↳ IR-06(01) | Automated Reporting | Enhancement |
| ↳ IR-06(03) | Supply Chain Coordination | Enhancement |
| **IR-07** | **Incident Response Assistance** | **Base** |
| ↳ IR-07(01) | Automation Support for Availability of Information and Support | Enhancement |
| **IR-08** | **Incident Response Plan** | **Base** |

</details>

<details>
<summary><b>MA — Maintenance (12개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **MA-01** | **Policy and Procedures** | **Base** |
| **MA-02** | **Controlled Maintenance** | **Base** |
| ↳ MA-02(02) | Automated Maintenance Activities | Enhancement |
| **MA-03** | **Maintenance Tools** | **Base** |
| ↳ MA-03(01) | Inspect Tools | Enhancement |
| ↳ MA-03(02) | Inspect Media | Enhancement |
| ↳ MA-03(03) | Prevent Unauthorized Removal | Enhancement |
| **MA-04** | **Nonlocal Maintenance** | **Base** |
| ↳ MA-04(03) | Comparable Security and Sanitization | Enhancement |
| **MA-05** | **Maintenance Personnel** | **Base** |
| ↳ MA-05(01) | Individuals Without Appropriate Access | Enhancement |
| **MA-06** | **Timely Maintenance** | **Base** |

</details>

<details>
<summary><b>MP — Media Protection (10개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **MP-01** | **Policy and Procedures** | **Base** |
| **MP-02** | **Media Access** | **Base** |
| **MP-03** | **Media Marking** | **Base** |
| **MP-04** | **Media Storage** | **Base** |
| **MP-05** | **Media Transport** | **Base** |
| **MP-06** | **Media Sanitization** | **Base** |
| ↳ MP-06(01) | Review, Approve, Track, Document, and Verify | Enhancement |
| ↳ MP-06(02) | Equipment Testing | Enhancement |
| ↳ MP-06(03) | Nondestructive Techniques | Enhancement |
| **MP-07** | **Media Use** | **Base** |

</details>

<details>
<summary><b>PE — Physical and Environmental Protection (25개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **PE-01** | **Policy and Procedures** | **Base** |
| **PE-02** | **Physical Access Authorizations** | **Base** |
| **PE-03** | **Physical Access Control** | **Base** |
| ↳ PE-03(01) | System Access | Enhancement |
| **PE-04** | **Access Control for Transmission** | **Base** |
| **PE-05** | **Access Control for Output Devices** | **Base** |
| **PE-06** | **Monitoring Physical Access** | **Base** |
| ↳ PE-06(01) | Intrusion Alarms and Surveillance Equipment | Enhancement |
| ↳ PE-06(04) | Monitoring Physical Access to Systems | Enhancement |
| **PE-08** | **Visitor Access Records** | **Base** |
| ↳ PE-08(01) | Automated Records Maintenance and Review | Enhancement |
| **PE-09** | **Power Equipment and Cabling** | **Base** |
| **PE-10** | **Emergency Shutoff** | **Base** |
| **PE-11** | **Emergency Power** | **Base** |
| ↳ PE-11(01) | Alternate Power Supply — Minimal Operational Capability | Enhancement |
| **PE-12** | **Emergency Lighting** | **Base** |
| **PE-13** | **Fire Protection** | **Base** |
| ↳ PE-13(01) | Detection Systems — Automatic Activation and Notification | Enhancement |
| ↳ PE-13(02) | Suppression Systems — Automatic Activation and Notification | Enhancement |
| **PE-14** | **Environmental Controls** | **Base** |
| **PE-15** | **Water Damage Protection** | **Base** |
| ↳ PE-15(01) | Automation Support | Enhancement |
| **PE-16** | **Delivery and Removal** | **Base** |
| **PE-17** | **Alternate Work Site** | **Base** |
| **PE-18** | **Location of System Components** | **Base** |

</details>

<details>
<summary><b>PL — Planning (7개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **PL-01** | **Policy and Procedures** | **Base** |
| **PL-02** | **System Security and Privacy Plans** | **Base** |
| **PL-04** | **Rules of Behavior** | **Base** |
| ↳ PL-04(01) | Social Media and External Site/Application Usage Restrictions | Enhancement |
| **PL-08** | **Security and Privacy Architectures** | **Base** |
| **PL-10** | **Baseline Selection** | **Base** |
| **PL-11** | **Baseline Tailoring** | **Base** |

</details>

<details>
<summary><b>PS — Personnel Security (10개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **PS-01** | **Policy and Procedures** | **Base** |
| **PS-02** | **Position Risk Designation** | **Base** |
| **PS-03** | **Personnel Screening** | **Base** |
| **PS-04** | **Personnel Termination** | **Base** |
| ↳ PS-04(02) | Automated Actions | Enhancement |
| **PS-05** | **Personnel Transfer** | **Base** |
| **PS-06** | **Access Agreements** | **Base** |
| **PS-07** | **External Personnel Security** | **Base** |
| **PS-08** | **Personnel Sanctions** | **Base** |
| **PS-09** | **Position Descriptions** | **Base** |

</details>

<details>
<summary><b>RA — Risk Assessment (11개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **RA-01** | **Policy and Procedures** | **Base** |
| **RA-02** | **Security Categorization** | **Base** |
| **RA-03** | **Risk Assessment** | **Base** |
| ↳ RA-03(01) | Supply Chain Risk Assessment | Enhancement |
| **RA-05** | **Vulnerability Monitoring and Scanning** | **Base** |
| ↳ RA-05(02) | Update Vulnerabilities to Be Scanned | Enhancement |
| ↳ RA-05(04) | Discoverable Information | Enhancement |
| ↳ RA-05(05) | Privileged Access | Enhancement |
| ↳ RA-05(11) | Public Disclosure Program | Enhancement |
| **RA-07** | **Risk Response** | **Base** |
| **RA-09** | **Criticality Analysis** | **Base** |

</details>

<details>
<summary><b>SA — System and Services Acquisition (21개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **SA-01** | **Policy and Procedures** | **Base** |
| **SA-02** | **Allocation of Resources** | **Base** |
| **SA-03** | **System Development Life Cycle** | **Base** |
| **SA-04** | **Acquisition Process** | **Base** |
| ↳ SA-04(01) | Functional Properties of Controls | Enhancement |
| ↳ SA-04(02) | Design and Implementation Information for Controls | Enhancement |
| ↳ SA-04(05) | System, Component, and Service Configurations | Enhancement |
| ↳ SA-04(09) | Functions, Ports, Protocols, and Services in Use | Enhancement |
| ↳ SA-04(10) | Use of Approved PIV Products | Enhancement |
| **SA-05** | **System Documentation** | **Base** |
| **SA-08** | **Security and Privacy Engineering Principles** | **Base** |
| **SA-09** | **External System Services** | **Base** |
| ↳ SA-09(02) | Identification of Functions, Ports, Protocols, and Services | Enhancement |
| **SA-10** | **Developer Configuration Management** | **Base** |
| **SA-11** | **Developer Testing and Evaluation** | **Base** |
| **SA-15** | **Development Process, Standards, and Tools** | **Base** |
| ↳ SA-15(03) | Criticality Analysis | Enhancement |
| **SA-16** | **Developer-provided Training** | **Base** |
| **SA-17** | **Developer Security and Privacy Architecture and Design** | **Base** |
| **SA-21** | **Developer Screening** | **Base** |
| **SA-22** | **Unsupported System Components** | **Base** |

</details>

<details>
<summary><b>SC — System and Communications Protection (30개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **SC-01** | **Policy and Procedures** | **Base** |
| **SC-02** | **Separation of System and User Functionality** | **Base** |
| **SC-03** | **Security Function Isolation** | **Base** |
| **SC-04** | **Information in Shared System Resources** | **Base** |
| **SC-05** | **Denial-of-service Protection** | **Base** |
| **SC-07** | **Boundary Protection** | **Base** |
| ↳ SC-07(03) | Access Points | Enhancement |
| ↳ SC-07(04) | External Telecommunications Services | Enhancement |
| ↳ SC-07(05) | Deny by Default — Allow by Exception | Enhancement |
| ↳ SC-07(07) | Split Tunneling for Remote Devices | Enhancement |
| ↳ SC-07(08) | Route Traffic to Authenticated Proxy Servers | Enhancement |
| ↳ SC-07(18) | Fail Secure | Enhancement |
| ↳ SC-07(21) | Isolation of System Components | Enhancement |
| **SC-08** | **Transmission Confidentiality and Integrity** | **Base** |
| ↳ SC-08(01) | Cryptographic Protection | Enhancement |
| **SC-10** | **Network Disconnect** | **Base** |
| **SC-12** | **Cryptographic Key Establishment and Management** | **Base** |
| ↳ SC-12(01) | Availability | Enhancement |
| **SC-13** | **Cryptographic Protection** | **Base** |
| **SC-15** | **Collaborative Computing Devices and Applications** | **Base** |
| **SC-17** | **Public Key Infrastructure Certificates** | **Base** |
| **SC-18** | **Mobile Code** | **Base** |
| **SC-20** | **Secure Name/Address Resolution Service (Authoritative Source)** | **Base** |
| **SC-21** | **Secure Name/Address Resolution Service (Recursive or Caching Resolver)** | **Base** |
| **SC-22** | **Architecture and Provisioning for Name/Address Resolution Service** | **Base** |
| **SC-23** | **Session Authenticity** | **Base** |
| **SC-24** | **Fail in Known State** | **Base** |
| **SC-28** | **Protection of Information at Rest** | **Base** |
| ↳ SC-28(01) | Cryptographic Protection | Enhancement |
| **SC-39** | **Process Isolation** | **Base** |

</details>

<details>
<summary><b>SI — System and Information Integrity (28개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **SI-01** | **Policy and Procedures** | **Base** |
| **SI-02** | **Flaw Remediation** | **Base** |
| ↳ SI-02(02) | Automated Flaw Remediation Status | Enhancement |
| **SI-03** | **Malicious Code Protection** | **Base** |
| **SI-04** | **System Monitoring** | **Base** |
| ↳ SI-04(02) | Automated Tools and Mechanisms for Real-time Analysis | Enhancement |
| ↳ SI-04(04) | Inbound and Outbound Communications Traffic | Enhancement |
| ↳ SI-04(05) | System-generated Alerts | Enhancement |
| ↳ SI-04(10) | Visibility of Encrypted Communications | Enhancement |
| ↳ SI-04(12) | Automated Organization-generated Alerts | Enhancement |
| ↳ SI-04(14) | Wireless Intrusion Detection | Enhancement |
| ↳ SI-04(20) | Privileged Users | Enhancement |
| ↳ SI-04(22) | Unauthorized Network Services | Enhancement |
| **SI-05** | **Security Alerts, Advisories, and Directives** | **Base** |
| ↳ SI-05(01) | Automated Alerts and Advisories | Enhancement |
| **SI-06** | **Security and Privacy Function Verification** | **Base** |
| **SI-07** | **Software, Firmware, and Information Integrity** | **Base** |
| ↳ SI-07(01) | Integrity Checks | Enhancement |
| ↳ SI-07(02) | Automated Notifications of Integrity Violations | Enhancement |
| ↳ SI-07(05) | Automated Response to Integrity Violations | Enhancement |
| ↳ SI-07(07) | Integration of Detection and Response | Enhancement |
| ↳ SI-07(15) | Code Authentication | Enhancement |
| **SI-08** | **Spam Protection** | **Base** |
| ↳ SI-08(02) | Automatic Updates | Enhancement |
| **SI-10** | **Information Input Validation** | **Base** |
| **SI-11** | **Error Handling** | **Base** |
| **SI-12** | **Information Management and Retention** | **Base** |
| **SI-16** | **Memory Protection** | **Base** |

</details>

<details>
<summary><b>SR — Supply Chain Risk Management (14개)</b></summary>

| 컨트롤 | 제목 | 유형 |
|--------|------|------|
| **SR-01** | **Policy and Procedures** | **Base** |
| **SR-02** | **Supply Chain Risk Management Plan** | **Base** |
| ↳ SR-02(01) | Establish SCRM Team | Enhancement |
| **SR-03** | **Supply Chain Controls and Processes** | **Base** |
| **SR-05** | **Acquisition Strategies, Tools, and Methods** | **Base** |
| **SR-06** | **Supplier Assessments and Reviews** | **Base** |
| **SR-08** | **Notification Agreements** | **Base** |
| **SR-09** | **Tamper Resistance and Detection** | **Base** |
| ↳ SR-09(01) | Multiple Stages of System Development Life Cycle | Enhancement |
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