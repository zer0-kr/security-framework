# OWASP ASVS v5.0: 애플리케이션 보안 검증 표준

## 개요

| 항목 | 내용 |
|------|------|
| **정식 명칭** | Application Security Verification Standard v5.0.0 |
| **발행일** | 2025년 5월 30일 (Global AppSec EU Barcelona) |
| **이전 버전** | v4.0.3 (2021) |
| **라이선스** | CC BY-SA 4.0 |
| **GitHub** | https://github.com/OWASP/ASVS |
| **원문** | https://asvs.owasp.org |

ASVS는 웹 애플리케이션의 보안 요구사항을 정의하는 **검증 표준**입니다. NIST 체계에서 SP 800-53이 "어떤 컨트롤을 적용하는가"를 정의하듯, ASVS는 애플리케이션 수준에서 "어떤 보안 요구사항을 충족해야 하는가"를 정의합니다.

---

## v5.0의 주요 변경점 (vs v4.0)

| 변경 사항 | 설명 |
|-----------|------|
| **챕터 전면 재구성** | v4.0의 14 챕터 → v5.0의 17 챕터. 5개 신규 챕터 추가 |
| **요구사항 확대** | 286개 → 345개 |
| **보안 목표 중심** | 특정 메커니즘 지정에서 보안 목표 중심으로 전환 |
| **Level 진입장벽 완화** | L1 비율을 46% → 20%로 축소하여 진입장벽 낮춤 |
| **신규 영역** | Web Frontend, OAuth/OIDC, Self-contained Tokens, WebRTC 등 |

---

## 3단계 검증 레벨

| Level | 명칭 | 요구사항 | 대상 |
|-------|------|---------|------|
| **L1** | 초기 방어 | ~70개 (20%) | 초기 스타트업, 제한된 민감 데이터 |
| **L2** | 표준 보안 | ~175개 (50%) | 대부분의 상용 웹 애플리케이션 |
| **L3** | 고급 보증 | ~100개 (30%) | 금융, 의료, 정부 — 최고 수준 |

> **L1 ⊂ L2 ⊂ L3** — 상위 레벨은 하위를 완전히 포함합니다. SP 800-53의 기준선(LOW ⊂ MOD ⊂ HIGH)과 동일한 구조입니다.

---

## 수치 요약

| 구분 | 수량 |
|------|------|
| 챕터 | 17개 |
| 총 요구사항 | 345개 |
| 검증 레벨 | 3단계 (L1/L2/L3) |

---

## 17개 챕터 전체 구조

### 한눈에 보기

| 챕터 | 명칭 | 한국어 | 요구사항 |
|------|------|--------|---------|
| V1 | Encoding and Sanitization | 인코딩 및 새니타이제이션 | 30개 |
| V2 | Validation and Business Logic | 검증 및 비즈니스 로직 | 13개 |
| V3 | Web Frontend Security | 웹 프론트엔드 보안 | 31개 |
| V4 | API and Web Service | API 및 웹 서비스 | 16개 |
| V5 | File Handling | 파일 처리 | 13개 |
| V6 | Authentication | 인증 | 47개 |
| V7 | Session Management | 세션 관리 | 19개 |
| V8 | Authorization | 인가 | 13개 |
| V9 | Self-contained Tokens | 자체 포함 토큰 | 7개 |
| V10 | OAuth and OIDC | OAuth 및 OIDC | 36개 |
| V11 | Cryptography | 암호화 | 24개 |
| V12 | Secure Communication | 안전한 통신 | 12개 |
| V13 | Configuration | 설정 | 21개 |
| V14 | Data Protection | 데이터 보호 | 13개 |
| V15 | Secure Coding and Architecture | 안전한 코딩 및 아키텍처 | 21개 |
| V16 | Security Logging and Error Handling | 보안 로깅 및 오류 처리 | 17개 |
| V17 | WebRTC | WebRTC | 12개 |
| | | **합계** | **345개** |

> 아래 각 챕터를 클릭하면 섹션 구조를 확인할 수 있습니다.

---

<details>
<summary><b>V1 — Encoding and Sanitization (30개)</b></summary>

- V1.1 Encoding and Sanitization Architecture
- V1.2 Injection Prevention
- V1.3 Sanitization
- V1.4 Memory, String, and Unmanaged Code
- V1.5 Safe Deserialization

</details>

<details>
<summary><b>V2 — Validation and Business Logic (13개)</b></summary>

- V2.1 Validation and Business Logic Documentation
- V2.2 Input Validation
- V2.3 Business Logic Security
- V2.4 Anti-automation

</details>

<details>
<summary><b>V3 — Web Frontend Security (31개)</b></summary>

- V3.1 Web Frontend Security Documentation
- V3.2 Unintended Content Interpretation
- V3.3 Cookie Setup
- V3.4 Browser Security Mechanism Headers
- V3.5 Browser Origin Separation
- V3.6 External Resource Integrity
- V3.7 Other Browser Security Considerations

</details>

<details>
<summary><b>V4 — API and Web Service (16개)</b></summary>

- V4.1 Generic Web Service Security
- V4.2 HTTP Message Structure Validation
- V4.3 GraphQL
- V4.4 WebSocket

</details>

<details>
<summary><b>V5 — File Handling (13개)</b></summary>

- V5.1 File Handling Documentation
- V5.2 File Upload and Content
- V5.3 File Storage
- V5.4 File Download

</details>

<details>
<summary><b>V6 — Authentication (47개) — 가장 큰 챕터</b></summary>

- V6.1 Authentication Documentation
- V6.2 Password Security
- V6.3 General Authentication Security
- V6.4 Authentication Factor Lifecycle and Recovery
- V6.5 General Multi-factor Authentication Requirements
- V6.6 Out-of-Band Authentication Mechanisms
- V6.7 Cryptographic Authentication Mechanism
- V6.8 Authentication with an Identity Provider

</details>

<details>
<summary><b>V7 — Session Management (19개)</b></summary>

- V7.1 Session Management Documentation
- V7.2 Fundamental Session Management Security
- V7.3 Session Timeout
- V7.4 Session Termination
- V7.5 Defenses Against Session Abuse
- V7.6 Federated Re-authentication

</details>

<details>
<summary><b>V8 — Authorization (13개)</b></summary>

- V8.1 Authorization Documentation
- V8.2 General Authorization Design
- V8.3 Operation Level Authorization
- V8.4 Other Authorization Considerations

</details>

<details>
<summary><b>V9 — Self-contained Tokens (7개)</b></summary>

- V9.1 Token Source and Integrity
- V9.2 Token Content

</details>

<details>
<summary><b>V10 — OAuth and OIDC (36개)</b></summary>

- V10.1 Generic OAuth and OIDC Security
- V10.2 OAuth Client
- V10.3 OAuth Resource Server
- V10.4 OAuth Authorization Server
- V10.5 OIDC Client
- V10.6 OpenID Provider
- V10.7 Consent Management

</details>

<details>
<summary><b>V11 — Cryptography (24개)</b></summary>

- V11.1 Cryptographic Inventory and Documentation
- V11.2 Secure Cryptography Implementation
- V11.3 Encryption Algorithms
- V11.4 Hashing and Hash-based Functions
- V11.5 Random Values
- V11.6 Public Key Cryptography
- V11.7 In-Use Data Cryptography

</details>

<details>
<summary><b>V12 — Secure Communication (12개)</b></summary>

- V12.1 General TLS Security Guidance
- V12.2 HTTPS Communication with External Facing Services
- V12.3 General Service to Service Communication Security

</details>

<details>
<summary><b>V13 — Configuration (21개)</b></summary>

- V13.1 Configuration Documentation
- V13.2 Backend Communication Configuration
- V13.3 Secret Management
- V13.4 Unintended Information Leakage

</details>

<details>
<summary><b>V14 — Data Protection (13개)</b></summary>

- V14.1 Data Protection Documentation
- V14.2 General Data Protection
- V14.3 Client-side Data Protection

</details>

<details>
<summary><b>V15 — Secure Coding and Architecture (21개)</b></summary>

- V15.1 Secure Coding and Architecture Documentation
- V15.2 Security Architecture and Dependencies
- V15.3 Defensive Coding
- V15.4 Safe Concurrency

</details>

<details>
<summary><b>V16 — Security Logging and Error Handling (17개)</b></summary>

- V16.1 Security Logging Documentation
- V16.2 General Logging
- V16.3 Security Events
- V16.4 Log Protection
- V16.5 Error Handling

</details>

<details>
<summary><b>V17 — WebRTC (12개)</b></summary>

- V17.1 TURN Server
- V17.2 Media
- V17.3 Signaling

</details>

---

## 요구사항 ID 형식

```
<챕터>.<섹션>.<요구사항>
```

예시: `1.2.4` = V1(Encoding) → V1.2(Injection Prevention) → 4번째 요구사항

버전 포함 형식: `v5.0.0-1.2.4`

---

## 참고 자료

| 리소스 | URL |
|--------|-----|
| ASVS v5.0 원문 | https://asvs.owasp.org |
| GitHub | https://github.com/OWASP/ASVS |
| OWASP Top 10 | [Top 10 2025 상세](../Top10-2025/README.md) |
| OWASP WSTG | [WSTG v4.2 상세](../WSTG/README.md) |
| v4.0→v5.0 매핑 | https://github.com/OWASP/ASVS/tree/master/5.0/mappings |
