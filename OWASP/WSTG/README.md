# OWASP WSTG v4.2: 웹 보안 테스트 가이드

## 개요

| 항목 | 내용 |
|------|------|
| **정식 명칭** | Web Security Testing Guide v4.2 |
| **발행일** | 2020년 12월 3일 |
| **개발 버전** | v5.0 (진행 중) |
| **라이선스** | CC BY-SA 4.0 |
| **GitHub** | https://github.com/OWASP/wstg |
| **원문** | https://owasp.org/www-project-web-security-testing-guide/v42/ |

WSTG는 웹 애플리케이션 보안 테스트를 **어떻게 수행하는지** 구체적 방법론을 제공합니다. ASVS가 "무엇을 검증해야 하는가"를 정의한다면, WSTG는 "어떻게 테스트하는가"를 설명합니다.

> NIST 체계와 비교하면: ASVS = SP 800-53 (컨트롤), WSTG = SP 800-53A (평가 절차)

---

## 수치 요약

| 구분 | 수량 |
|------|------|
| 테스트 카테고리 | 12개 |
| 총 테스트 케이스 | 128개 |

---

## 테스트 ID 형식

```
WSTG-<카테고리>-<번호>
```

예시: `WSTG-INPV-05` = Input Validation Testing의 5번째 테스트 (SQL Injection)

버전 포함: `WSTG-v42-INPV-05`

---

## 12개 테스트 카테고리 전체 구조

### 한눈에 보기

| 코드 | 카테고리 | 한국어 | 테스트 수 |
|------|---------|--------|----------|
| INFO | Information Gathering | 정보 수집 | 10개 |
| CONF | Configuration and Deployment Management | 설정 및 배포 관리 | 14개 |
| IDNT | Identity Management | 신원 관리 | 5개 |
| ATHN | Authentication | 인증 | 11개 |
| ATHZ | Authorization | 인가 | 7개 |
| SESS | Session Management | 세션 관리 | 11개 |
| INPV | Input Validation | 입력 검증 | 31개 |
| ERRH | Error Handling | 오류 처리 | 2개 |
| CRYP | Weak Cryptography | 암호화 | 4개 |
| BUSL | Business Logic | 비즈니스 로직 | 11개 |
| CLNT | Client-side | 클라이언트 측 | 16개 |
| APIT | API Testing | API 테스트 | 6개 |
| | | **합계** | **128개** |

> 아래 각 카테고리를 클릭하면 테스트 목록을 확인할 수 있습니다.

---

<details>
<summary><b>INFO — 정보 수집 (10개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-INFO-01 | Conduct Search Engine Discovery Reconnaissance for Information Leakage |
| WSTG-INFO-02 | Fingerprint Web Server |
| WSTG-INFO-03 | Review Webserver Metafiles for Information Leakage |
| WSTG-INFO-04 | Enumerate Applications on Webserver |
| WSTG-INFO-05 | Review Webpage Content for Information Leakage |
| WSTG-INFO-06 | Identify Application Entry Points |
| WSTG-INFO-07 | Map Execution Paths Through Application |
| WSTG-INFO-08 | Fingerprint Web Application Framework |
| WSTG-INFO-09 | Fingerprint Web Application |
| WSTG-INFO-10 | Map Application Architecture |

</details>

<details>
<summary><b>CONF — 설정 및 배포 관리 (14개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-CONF-01 | Test Network Infrastructure Configuration |
| WSTG-CONF-02 | Test Application Platform Configuration |
| WSTG-CONF-03 | Test File Extensions Handling for Sensitive Information |
| WSTG-CONF-04 | Review Old Backup and Unreferenced Files for Sensitive Information |
| WSTG-CONF-05 | Enumerate Infrastructure and Application Admin Interfaces |
| WSTG-CONF-06 | Test HTTP Methods |
| WSTG-CONF-07 | Test HTTP Strict Transport Security |
| WSTG-CONF-08 | Test RIA Cross Domain Policy |
| WSTG-CONF-09 | Test File Permission |
| WSTG-CONF-10 | Test for Subdomain Takeover |
| WSTG-CONF-11 | Test Cloud Storage |
| WSTG-CONF-12 | Test for Content Security Policy |
| WSTG-CONF-13 | Test for Path Confusion |
| WSTG-CONF-14 | Test for Verb Tampering |

</details>

<details>
<summary><b>IDNT — 신원 관리 (5개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-IDNT-01 | Test Role Definitions |
| WSTG-IDNT-02 | Test User Registration Process |
| WSTG-IDNT-03 | Test Account Provisioning Process |
| WSTG-IDNT-04 | Testing for Account Enumeration and Guessable User Account |
| WSTG-IDNT-05 | Testing for Weak or Unenforced Username Policy |

</details>

<details>
<summary><b>ATHN — 인증 (11개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-ATHN-01 | Testing for Credentials Transported over an Encrypted Channel |
| WSTG-ATHN-02 | Testing for Default Credentials |
| WSTG-ATHN-03 | Testing for Weak Lock Out Mechanism |
| WSTG-ATHN-04 | Testing for Bypassing Authentication Schema |
| WSTG-ATHN-05 | Testing for Vulnerable Remember Password |
| WSTG-ATHN-06 | Testing for Browser Cache Weaknesses |
| WSTG-ATHN-07 | Testing for Weak Password Policy |
| WSTG-ATHN-08 | Testing for Weak Security Question Answer |
| WSTG-ATHN-09 | Testing for Weak Password Change or Reset Functionalities |
| WSTG-ATHN-10 | Testing for Weaker Authentication in Alternative Channel |
| WSTG-ATHN-11 | Testing Multi-Factor Authentication |

</details>

<details>
<summary><b>ATHZ — 인가 (7개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-ATHZ-01 | Testing Directory Traversal File Include |
| WSTG-ATHZ-02 | Testing for Bypassing Authorization Schema |
| WSTG-ATHZ-03 | Testing for Privilege Escalation |
| WSTG-ATHZ-04 | Testing for Insecure Direct Object References |
| WSTG-ATHZ-05 | Testing for OAuth Weaknesses |
| WSTG-ATHZ-06 | Testing for Broken Access Control |
| WSTG-ATHZ-07 | Testing for Missing Function Level Access Control |

</details>

<details>
<summary><b>SESS — 세션 관리 (11개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-SESS-01 | Testing for Session Management Schema |
| WSTG-SESS-02 | Testing for Cookies Attributes |
| WSTG-SESS-03 | Testing for Session Fixation |
| WSTG-SESS-04 | Testing for Exposed Session Variables |
| WSTG-SESS-05 | Testing for Cross Site Request Forgery |
| WSTG-SESS-06 | Testing for Logout Functionality |
| WSTG-SESS-07 | Testing Session Timeout |
| WSTG-SESS-08 | Testing for Session Puzzling |
| WSTG-SESS-09 | Testing for Session Hijacking |
| WSTG-SESS-10 | Testing JSON Web Tokens |
| WSTG-SESS-11 | Testing for Concurrent Sessions |

</details>

<details>
<summary><b>INPV — 입력 검증 (31개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-INPV-01 | Testing for Reflected Cross Site Scripting |
| WSTG-INPV-02 | Testing for Stored Cross Site Scripting |
| WSTG-INPV-03 | Testing for HTTP Verb Tampering |
| WSTG-INPV-04 | Testing for HTTP Parameter Pollution |
| WSTG-INPV-05 | Testing for SQL Injection |
| WSTG-INPV-06 | Testing for LDAP Injection |
| WSTG-INPV-07 | Testing for XML Injection |
| WSTG-INPV-08 | Testing for SSI Injection |
| WSTG-INPV-09 | Testing for XPath Injection |
| WSTG-INPV-10 | Testing for IMAP SMTP Injection |
| WSTG-INPV-11 | Testing for Code Injection |
| WSTG-INPV-12 | Testing for Command Injection |
| WSTG-INPV-13 | Testing for Format String Injection |
| WSTG-INPV-14 | Testing for Incubated Vulnerability |
| WSTG-INPV-15 | Testing for HTTP Splitting Smuggling |
| WSTG-INPV-16 | Testing for HTTP Incoming Requests |
| WSTG-INPV-17 | Testing for Host Header Injection |
| WSTG-INPV-18 | Testing for Server-side Template Injection |
| WSTG-INPV-19 | Testing for Server-Side Request Forgery |
| WSTG-INPV-20 | Testing for Mass Assignment |
| WSTG-INPV-21 | Testing for WebSocket Security |
| WSTG-INPV-22 | Testing for ORM Injection |
| WSTG-INPV-23 | Testing for Client-side |
| WSTG-INPV-24 | Testing for NoSQL Injection |
| WSTG-INPV-25 | Testing for GraphQL |
| WSTG-INPV-26 | Testing for CRLF Injection |
| WSTG-INPV-27 | Testing for Open Redirect |
| WSTG-INPV-28 | Testing for Local File Inclusion |
| WSTG-INPV-29 | Testing for Remote File Inclusion |
| WSTG-INPV-30 | Testing for CSV Injection |
| WSTG-INPV-31 | Testing for DOM-Based Cross Site Scripting |

</details>

<details>
<summary><b>ERRH — 오류 처리 (2개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-ERRH-01 | Testing for Improper Error Handling |
| WSTG-ERRH-02 | Testing for Stack Traces |

</details>

<details>
<summary><b>CRYP — 암호화 (4개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-CRYP-01 | Testing for Weak Transport Layer Security |
| WSTG-CRYP-02 | Testing for Padding Oracle |
| WSTG-CRYP-03 | Testing for Sensitive Information Sent via Unencrypted Channels |
| WSTG-CRYP-04 | Testing for Weak Encryption |

</details>

<details>
<summary><b>BUSL — 비즈니스 로직 (11개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-BUSL-01 | Test Business Logic Data Validation |
| WSTG-BUSL-02 | Test Ability to Forge Requests |
| WSTG-BUSL-03 | Test Integrity Checks |
| WSTG-BUSL-04 | Test for Process Timing |
| WSTG-BUSL-05 | Test Number of Times a Function Can Be Used Limits |
| WSTG-BUSL-06 | Testing for the Circumvention of Work Flows |
| WSTG-BUSL-07 | Test Defenses Against Application Misuse |
| WSTG-BUSL-08 | Test Upload of Unexpected File Types |
| WSTG-BUSL-09 | Test Upload of Malicious Files |
| WSTG-BUSL-10 | Test Payment Functionality |
| WSTG-BUSL-11 | Test for Lack of Non-Repudiation |

</details>

<details>
<summary><b>CLNT — 클라이언트 측 (16개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-CLNT-01 | Testing for DOM-Based Cross Site Scripting |
| WSTG-CLNT-02 | Testing for JavaScript Execution |
| WSTG-CLNT-03 | Testing for HTML Injection |
| WSTG-CLNT-04 | Testing for Client-side URL Redirect |
| WSTG-CLNT-05 | Testing for CSS Injection |
| WSTG-CLNT-06 | Testing for Client-side Resource Manipulation |
| WSTG-CLNT-07 | Testing Cross Origin Resource Sharing |
| WSTG-CLNT-08 | Testing for Cross Site Flashing |
| WSTG-CLNT-09 | Testing for Clickjacking |
| WSTG-CLNT-10 | Testing WebSockets |
| WSTG-CLNT-11 | Testing Web Messaging |
| WSTG-CLNT-12 | Testing Browser Storage |
| WSTG-CLNT-13 | Testing for Cross Site Script Inclusion |
| WSTG-CLNT-14 | Testing for Reverse Tabnabbing |
| WSTG-CLNT-15 | Testing for Broken Link Hijacking |
| WSTG-CLNT-16 | Testing for Content Security Policy |

</details>

<details>
<summary><b>APIT — API 테스트 (6개)</b></summary>

| ID | 테스트 |
|----|--------|
| WSTG-APIT-01 | Testing GraphQL |
| WSTG-APIT-02 | Testing for Content Type Mishandling |
| WSTG-APIT-03 | Testing for Mass Assignment |
| WSTG-APIT-04 | Testing for API Rate Limiting |
| WSTG-APIT-05 | Testing for Broken Object Level Authorization |
| WSTG-APIT-06 | Testing for Broken Function Level Authorization |

</details>

---

## 참고 자료

| 리소스 | URL |
|--------|-----|
| WSTG v4.2 원문 | https://owasp.org/www-project-web-security-testing-guide/v42/ |
| WSTG v4.2 PDF | https://github.com/OWASP/wstg/releases/download/v4.2/wstg-v4.2.pdf |
| GitHub | https://github.com/OWASP/wstg |
| OWASP Top 10 | [Top 10 2025 상세](../Top10-2025/README.md) |
| OWASP ASVS | [ASVS v5.0 상세](../ASVS/README.md) |
