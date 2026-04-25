# OWASP Top 10 프로젝트 전체 목록

OWASP는 웹 애플리케이션 Top 10 외에도 다양한 도메인에 특화된 Top 10 목록을 발행합니다. 현재 **26개**의 Top 10 프로젝트가 존재합니다.

---

## 한눈에 보기

| 분류 | 프로젝트 수 |
|------|-----------|
| 애플리케이션 보안 | 6개 |
| 인프라·클라우드·DevOps | 5개 |
| AI·ML·LLM | 5개 |
| 신기술·특수 도메인 | 6개 |
| 데이터·프라이버시·거버넌스 | 4개 |

---

## 애플리케이션 보안

| 프로젝트 | 대상 | 최신 버전 | 성숙도 |
|---------|------|----------|--------|
| **[Top 10 Web](https://owasp.org/Top10/)** | 웹 애플리케이션 | 2025 | Flagship |
| **[API Security Top 10](https://owasp.org/www-project-api-security/)** | API | 2023 | Production |
| **[Mobile Top 10](https://owasp.org/www-project-mobile-top-10/)** | 모바일 앱 | 지속 업데이트 | Lab |
| **[Top 10 Client-Side Security Risks](https://owasp.org/www-project-top-10-client-side-security-risks/)** | 클라이언트 측 (브라우저) | — | Lab |
| **[Top 10 for Business Logic Abuse](https://owasp.org/www-project-top-10-for-business-logic-abuse/)** | 비즈니스 로직 악용 | — | Lab |
| **[Desktop App Security Top 10](https://owasp.org/www-project-desktop-app-security-top-10/)** | 데스크톱 앱 | — | Incubator |

## 인프라·클라우드·DevOps

| 프로젝트 | 대상 | 최신 버전 | 성숙도 |
|---------|------|----------|--------|
| **[Docker Top 10](https://owasp.org/www-project-docker-top-10/)** | Docker 컨테이너 | — | Lab |
| **[Kubernetes Top 10](https://owasp.org/www-project-kubernetes-top-ten/)** | 쿠버네티스 | — | Lab |
| **[Serverless Top 10](https://owasp.org/www-project-serverless-top-10/)** | 서버리스 환경 | — | Lab |
| **[Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)** | CI/CD 파이프라인 | — | Lab |
| **[DevSecOps Top 10](https://owasp.org/www-project-devsecops-top-10/)** | DevSecOps | — | Lab |

## AI·ML·LLM

| 프로젝트 | 대상 | 최신 버전 | 성숙도 |
|---------|------|----------|--------|
| **[Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)** | LLM/생성형 AI | v1.1 (GenAI Security로 확대) | Flagship |
| **[Machine Learning Security Top 10](https://owasp.org/www-project-machine-learning-security-top-ten/)** | 머신러닝 모델 | — | Incubator |
| **[MCP Top 10](https://owasp.org/www-project-mcp-top-10/)** | Model Context Protocol | — | Lab |
| **[Agentic Skills Top 10](https://owasp.org/www-project-agentic-skills-top-10/)** | AI 에이전트 스킬 | — | Incubator |
| **[Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/)** | 비인간 ID (서비스 계정, API 키 등) | — | Lab |

## 신기술·특수 도메인

| 프로젝트 | 대상 | 최신 버전 | 성숙도 |
|---------|------|----------|--------|
| **[Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/)** | 스마트 컨트랙트 | — | Lab |
| **[Operational Technology Top 10](https://owasp.org/www-project-operational-technology-top-10/)** | OT/산업제어 | — | Lab |
| **[Top 10 for Maritime Security](https://owasp.org/www-project-top-10-for-maritime-security/)** | 해양 보안 | — | Incubator |
| **[Top 10 in XR](https://owasp.org/www-project-top-10-in-xr/)** | XR (VR/AR/MR) | — | Incubator |
| **[Top 10 Drone Security Risks](https://owasp.org/www-project-top-10-drone-security-risks/)** | 드론 | — | Incubator |
| **[Top 10 Risks for Open Source Software](https://owasp.org/www-project-top-10-risks-for-open-source-software/)** | 오픈소스 소프트웨어 | — | Lab |

## 데이터·프라이버시·거버넌스

| 프로젝트 | 대상 | 최신 버전 | 성숙도 |
|---------|------|----------|--------|
| **[Data Security Top 10](https://owasp.org/www-project-data-security-top-10/)** | 데이터 보안 | — | Incubator |
| **[Top 10 Privacy Risks](https://owasp.org/www-project-top-10-privacy-risks/)** | 프라이버시 | — | Lab |
| **[Citizen Development Top 10](https://owasp.org/www-project-citizen-development-top-10/)** | 시민 개발 (No-Code/Low-Code) | — | Incubator |
| **[Attack Surface Management Top 10](https://owasp.org/www-project-attack-surface-management-top-10/)** | 공격 표면 관리 | — | Lab |

---

## 성숙도별 분포

| 성숙도 | 프로젝트 수 | 비고 |
|--------|-----------|------|
| Flagship | 2개 | Web Top 10, LLM Top 10 |
| Production | 1개 | API Security Top 10 |
| Lab | 15개 | 대부분의 도메인 특화 Top 10 |
| Incubator | 8개 | 신규/실험 단계 |

---

## Proactive Controls

Top 10 "위험" 목록과 반대로, 개발자가 구현해야 할 Top 10 "방어" 목록도 있습니다:

| 프로젝트 | 설명 | 최신 버전 |
|---------|------|----------|
| **[Proactive Controls](https://owasp.org/www-project-proactive-controls/)** | 개발자가 구현해야 할 10대 보안 통제 | 2024 |

---

## 참고

- 전체 프로젝트 목록: https://owasp.org/projects/
- Top 10 Web 상세: [Top 10 2025 문서](./Top10-2025/README.md)
