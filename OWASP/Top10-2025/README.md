# OWASP Top 10: 2025

## 개요

| 항목 | 내용 |
|------|------|
| **정식 명칭** | OWASP Top 10 Web Application Security Risks — 2025 |
| **발행** | 2025년 |
| **이전 버전** | 2021, 2017 |
| **데이터 기반** | 13개 조직, 280만+ 애플리케이션 테스트 데이터 |
| **CWE 매핑** | 248개 CWE (평균 25개/카테고리) |
| **라이선스** | CC BY-SA 4.0 |
| **원문** | https://owasp.org/Top10/2025/ |

OWASP Top 10은 웹 애플리케이션에서 가장 심각한 **10대 보안 위험**을 식별한 목록입니다. 실제 취약점 데이터와 커뮤니티 설문을 기반으로 약 3~4년 주기로 갱신됩니다.

---

## 2025 Top 10 전체 항목

| 순위 | 코드 | 위험 | 설명 |
|------|------|------|------|
| 1 | A01:2025 | **Broken Access Control** | 사용자가 의도된 권한을 벗어나 행동할 수 있는 취약점. URL/상태 변조, IDOR, CORS 오설정, JWT 조작 등 |
| 2 | A02:2025 | **Security Misconfiguration** | 애플리케이션 스택 전반의 보안 설정 미흡. 기본 계정, 불필요 기능, 에러 메시지 노출 등 |
| 3 | A03:2025 | **Software Supply Chain Failures** | 소프트웨어 공급망의 취약점이나 악의적 변경. 취약한 컴포넌트, 미검증 소스, 무결성 미확인 **(신규)** |
| 4 | A04:2025 | **Cryptographic Failures** | 암호화 관련 실패. 평문 전송, 약한 알고리즘(MD5/SHA1), 키 관리 부실, 초기화 벡터 재사용 등 |
| 5 | A05:2025 | **Injection** | 신뢰할 수 없는 입력이 인터프리터에 전달되어 명령으로 실행. SQL, NoSQL, OS 명령, LDAP, ORM 인젝션 |
| 6 | A06:2025 | **Insecure Design** | 설계 단계에서의 보안 통제 부재. 위협 모델링 미수행, 보안 설계 패턴 미적용, 비즈니스 리스크 프로파일링 부재 |
| 7 | A07:2025 | **Authentication Failures** | 인증 메커니즘의 약점. 크리덴셜 스터핑, 약한 비밀번호 허용, MFA 미적용, 세션 ID 노출 |
| 8 | A08:2025 | **Software or Data Integrity Failures** | 코드/인프라의 무결성 미보호. 비신뢰 소스의 플러그인, 안전하지 않은 CI/CD, 자동 업데이트 무결성 미검증 |
| 9 | A09:2025 | **Security Logging and Alerting Failures** | 로깅·모니터링·알림 부족. 감사 이벤트 미기록, 로그 무결성 미보호, 실시간 탐지/알림 부재 **(명칭 변경)** |
| 10 | A10:2025 | **Mishandling of Exceptional Conditions** | 예외 상황의 부적절한 처리. 입력 검증 미비, 메모리/권한/네트워크 이상 상태 대응 실패, 예외 미처리 **(신규)** |

---

## 2021 대비 변경 사항

### 신규 항목 (2개)

| 항목 | 설명 |
|------|------|
| **A03:2025 Software Supply Chain Failures** | 2021의 A06 "Vulnerable and Outdated Components"를 확장. 전체 소프트웨어 공급망 범위로 확대 |
| **A10:2025 Mishandling of Exceptional Conditions** | 부적절한 오류 처리, 논리적 에러, fail-open, 비정상 조건 처리 포커스. 24개 CWE 포함 |

### 순위 변동

| 위험 | 2021 | 2025 | 변동 |
|------|------|------|------|
| Broken Access Control | #1 | #1 | — |
| Security Misconfiguration | #5 | #2 | ↑3 |
| Cryptographic Failures | #2 | #4 | ↓2 |
| Injection | #3 | #5 | ↓2 |
| Insecure Design | #4 | #6 | ↓2 |
| Authentication Failures | #7 | #7 | — |

### 명칭 변경

| 2021 | 2025 | 변경 이유 |
|------|------|----------|
| Identification and Authentication Failures | **Authentication Failures** | 더 정확한 범위 |
| Security Logging and Monitoring Failures | **Security Logging and Alerting Failures** | 알림(alerting)의 중요성 강조 |

### 제거된 항목

| 항목 | 처리 |
|------|------|
| A10:2021 Server-Side Request Forgery (SSRF) | A01:2025 Broken Access Control에 통합 |

---

## ASVS/WSTG와의 관계

Top 10은 **위험 식별** 도구입니다. 이를 기반으로 보안을 구현·검증하려면:

| 단계 | 문서 | 역할 |
|------|------|------|
| 위험 인식 | **Top 10** (이 문서) | "무엇이 위험한가?" |
| 검증 기준 수립 | [ASVS v5.0](../ASVS/README.md) | "보안 요구사항을 충족하는가?" |
| 테스트 실행 | [WSTG v4.2](../WSTG/README.md) | "어떻게 테스트하는가?" |

---

## 참고 자료

| 리소스 | URL |
|--------|-----|
| Top 10 2025 원문 | https://owasp.org/Top10/2025/ |
| GitHub | https://github.com/OWASP/Top10 |
| OWASP ASVS | [ASVS v5.0 상세](../ASVS/README.md) |
| OWASP WSTG | [WSTG v4.2 상세](../WSTG/README.md) |
