# OWASP 보안 도구 및 데이터 소스

OWASP 문서를 프로그래밍 방식으로 조회하거나, AI 에이전트와 연동하여 활용할 수 있는 도구들을 정리합니다.

---

## 1. OWASP 공식 데이터 소스

### 구조화 데이터

| 데이터 | 설명 | 형식 | URL |
|--------|------|------|-----|
| **projects.json** | 418개+ 전체 프로젝트 메타데이터 (이름, 레벨, 타입, URL) | JSON | [다운로드](https://raw.githubusercontent.com/OWASP/owasp.github.io/main/_data/projects.json) |
| **ASVS 5.0 Flat** | 345개 보안 검증 요구사항 (챕터별, 레벨별) | JSON | [다운로드](https://raw.githubusercontent.com/OWASP/ASVS/master/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.flat.json) |
| **WSTG Checklist** | 111개 웹 보안 테스트 케이스 (카테고리별, 목표 포함) | JSON | [다운로드](https://raw.githubusercontent.com/OWASP/wstg/master/checklists/checklist.json) |

### 문서 저장소

| 프로젝트 | 설명 | GitHub |
|---------|------|--------|
| **Top 10 2021** | 웹 10대 보안 위험 + CWE 매핑 | [OWASP/Top10](https://github.com/OWASP/Top10) |
| **API Security** | API 10대 보안 위험 (2023 에디션) | [OWASP/API-Security](https://github.com/OWASP/API-Security) |
| **LLM Top 10** | LLM/AI 10대 보안 위험 (2025 v2.0) | [OWASP GenAI](https://genai.owasp.org/llm-top-10/) |
| **MCP Top 10** | MCP 서버 10대 보안 위험 (2025 Beta) | [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) |
| **Proactive Controls** | 개발자 10대 보안 통제 (2024) | [OWASP Proactive Controls](https://owasp.org/www-project-proactive-controls/) |
| **MASVS** | 모바일 앱 보안 검증 표준 (8 카테고리, 23 통제) | [OWASP/owasp-masvs](https://github.com/OWASP/owasp-masvs) |
| **Cheat Sheet Series** | 113개+ 보안 구현 가이드 (Markdown) | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) |

---

## 2. MCP 서버 (AI 에이전트 연동)

MCP(Model Context Protocol) 서버를 사용하면 Claude, Cursor 등 AI 도구에서 OWASP 데이터를 직접 조회할 수 있습니다.

### 종합 (OWASP 전체 통합 조회)

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **zer0-kr/security-framework-mcp** | 418+ 프로젝트, ASVS 5.0, WSTG, Top 10 2021, API Top 10 2023, LLM Top 10 2025, MCP Top 10 2025, Proactive Controls 2024, MASVS, CWE 39종, Cheat Sheets 113+, NVD CVE 실시간 | **가장 넓은 커버리지.** 24개 도구, 4개 프롬프트 템플릿, 6개 리소스. SQLite FTS5 전문 검색. STRIDE 위협 모델링, MCP 보안 자체 평가, 컴플라이언스 매핑(PCI-DSS/ISO27001/NIST 800-53), 기술 스택 보안 진단, 체크리스트 생성 | [GitHub](https://github.com/zer0-kr/security-framework-mcp) |

**설치 및 설정:**

```bash
pip install git+https://github.com/zer0-kr/security-framework-mcp.git
```

Claude Desktop (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "owasp": {
      "command": "security-framework-mcp"
    }
  }
}
```

??? note "owasp-mcp 상세 도구 목록 (24개)"

    **프로젝트 탐색**

    | 도구 | 설명 |
    |------|------|
    | `list_projects` | 전체 프로젝트 목록. level(flagship/production/lab/incubator), type(code/documentation/tool) 필터 |
    | `search_projects` | 프로젝트 전문 검색 (이름, 제목, 설명) |
    | `get_project` | 특정 프로젝트 상세 조회 (URL, 코드 저장소, 설명, 날짜) |

    **표준 & 가이드라인**

    | 도구 | 설명 |
    |------|------|
    | `get_asvs` | ASVS 5.0 요구사항 조회. chapter(V1-V14), level(1/2/3), query 필터 |
    | `get_wstg` | WSTG 테스트 케이스 조회. category(WSTG-INFO 등), query 필터 |
    | `get_top10` | Top 10 2021 항목 + CWE 매핑 |
    | `get_api_top10` | API Security Top 10 2023 항목 + CWE 매핑 |
    | `get_llm_top10` | LLM Top 10 2025 항목 — AI/LLM 보안 위험 |
    | `get_mcp_top10` | MCP Top 10 2025 — MCP 서버 배포 보안 위험 |
    | `get_proactive_controls` | Proactive Controls 2024 — 개발자 방어 조치 |
    | `get_masvs` | MASVS 모바일 보안 통제. category, query 필터 |
    | `get_cheatsheet` | Cheat Sheet 조회 또는 전체 목록 |

    **취약점 & CWE 조회**

    | 도구 | 설명 |
    |------|------|
    | `get_cwe` | CWE ID로 상세 조회 — 설명, MITRE 링크, OWASP 교차 참조 자동 생성 |
    | `search_cve` | **실시간 NVD** CVE 검색 (키워드, CWE, CVSS 심각도) |
    | `get_cve_detail` | CVE 상세 조회 — CVSS 점수, 설명, 약점, 참조 |

    **교차 참조 & 분석**

    | 도구 | 설명 |
    |------|------|
    | `search_owasp` | **11개 데이터 소스** 통합 검색 |
    | `cross_reference` | CWE → Top 10/ASVS/WSTG 교차 참조 |
    | `compliance_map` | ASVS 챕터를 **PCI-DSS 4.0**, **ISO 27001:2022**, **NIST 800-53 Rev.5**에 매핑 |
    | `assess_stack` | 기술 스택 입력 → 맞춤형 보안 권장사항 |
    | `generate_checklist` | 프로젝트 유형(web/api/mobile/llm/full) × 깊이(basic/standard/comprehensive) 체크리스트 생성 |
    | `assess_mcp_security` | MCP 서버 배포를 MCP Top 10 기준으로 자동 평가 |
    | `threat_model` | **STRIDE 기반** 위협 모델 자동 생성 + OWASP 대응책 매핑 |

    **데이터베이스 관리**

    | 도구 | 설명 |
    |------|------|
    | `update_database` | 로컬 인덱스를 OWASP 소스에서 재빌드 |
    | `database_status` | 데이터베이스 가용성, 빌드 시간, 크기 표시 |

### Cheat Sheets 특화

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **santosomar/owasp-cheatsheets-mcp** | Cheat Sheet Series (113+) | Cheat Sheet 전문 검색 및 내용 조회 | [GitHub](https://github.com/santosomar/owasp-cheatsheets-mcp) |

### ASVS 특화

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **clintcan/asvs-mcp** | ASVS (검증 표준) | ASVS 요구사항 검색 및 필터링 | [GitHub](https://github.com/clintcan/asvs-mcp) |

---

## 3. 용도별 추천

| 나는 이런 게 필요하다 | 추천 도구 |
|---------------------|----------|
| OWASP 전체 데이터를 AI로 검색하고 싶다 | **zer0-kr/security-framework-mcp** |
| 기술 스택에 맞는 보안 가이드가 필요하다 | **zer0-kr/security-framework-mcp** (`assess_stack`) |
| STRIDE 위협 모델링을 자동화하고 싶다 | **zer0-kr/security-framework-mcp** (`threat_model`) |
| MCP 서버의 보안을 점검하고 싶다 | **zer0-kr/security-framework-mcp** (`assess_mcp_security`) |
| ASVS를 PCI-DSS/ISO 27001에 매핑하고 싶다 | **zer0-kr/security-framework-mcp** (`compliance_map`) |
| Cheat Sheet만 빠르게 조회하고 싶다 | **santosomar/owasp-cheatsheets-mcp** |
| 코드 없이 데이터만 다운로드하고 싶다 | **OWASP projects.json** + **ASVS Flat JSON** |

---

## 4. OWASP 공식 GitHub 저장소

| 저장소 | 내용 | URL |
|--------|------|-----|
| **OWASP/Top10** | 웹 10대 보안 위험 | https://github.com/OWASP/Top10 |
| **OWASP/API-Security** | API 보안 Top 10 | https://github.com/OWASP/API-Security |
| **OWASP/ASVS** | 애플리케이션 보안 검증 표준 | https://github.com/OWASP/ASVS |
| **OWASP/wstg** | 웹 보안 테스트 가이드 | https://github.com/OWASP/wstg |
| **OWASP/CheatSheetSeries** | 보안 구현 가이드 113개+ | https://github.com/OWASP/CheatSheetSeries |
| **OWASP/owasp-masvs** | 모바일 앱 보안 검증 표준 | https://github.com/OWASP/owasp-masvs |
| **OWASP/owasp.github.io** | OWASP 웹사이트 + projects.json | https://github.com/OWASP/owasp.github.io |
| **OWASP/www-project-mcp-top-10** | MCP 서버 Top 10 보안 위험 | https://github.com/OWASP/www-project-mcp-top-10 |
| **OWASP/www-project-proactive-controls** | 개발자 10대 보안 통제 | https://github.com/OWASP/www-project-proactive-controls |
