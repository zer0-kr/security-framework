# NIST 사이버보안 도구 및 데이터 소스

NIST 문서를 프로그래밍 방식으로 조회하거나, AI 에이전트와 연동하여 활용할 수 있는 도구들을 정리합니다.

---

## 1. NIST 공식 데이터 소스

### API

| 도구 | 설명 | 인증 | URL |
|------|------|------|-----|
| **NVD API 2.0** | CVE 취약점, CPE 제품 정보를 REST API로 조회 | API Key 권장 (무료). 미사용 시 5req/30초, Key 사용 시 대폭 상향 | https://nvd.nist.gov/developers |
| **CPRT** | 컨트롤 간 관계(CSF↔SP 800-53↔PF) 데이터를 JSON/XLSX로 제공 | 없음 | https://csrc.nist.gov/projects/cprt |

### 다운로드

| 도구 | 설명 | 형식 | URL |
|------|------|------|-----|
| **OSCAL** | SP 800-53 컨트롤 카탈로그, 기준선 프로파일을 기계 판독 가능 형식으로 제공 | JSON, XML, YAML | https://github.com/usnistgov/oscal-content |
| **Publications XLSX** | 전체 NIST 사이버보안 출판물 메타데이터 (제목, 번호, 상태, 날짜) | XLSX | [다운로드](https://csrc.nist.gov/files/pubs/shared/docs/NIST-Cybersecurity-Publications.xlsx) |
| **CSF 2.0 Core** | CSF 2.0 전체 구조 (Functions→Categories→Subcategories) | XLSX, PDF | https://www.nist.gov/cyberframework |
| **PF 1.0 Core** | Privacy Framework 전체 구조 | XLSX | https://www.nist.gov/document/nist-privacy-framework-v10-core |
| **NIST Tech Pubs** | 전체 NIST 기술 출판물 메타데이터 (MODS XML) | XML | https://github.com/usnistgov/NIST-Tech-Pubs |

### 피드

| 도구 | 설명 | 형식 | URL |
|------|------|------|-----|
| **Draft Publications Feed** | 공개 의견 수렴 중인 초안 문서 알림 | JSON | https://csrc.nist.gov/CSRC/media/feeds/pubs/drafts-open-for-comment.json |
| **Draft Publications Feed** | 동일 (RSS 형식) | XML/RSS | https://csrc.nist.gov/CSRC/media/feeds/pubs/drafts-open-for-comment.xml |

### CLI 도구

| 도구 | 설명 | URL |
|------|------|-----|
| **OSCAL CLI** | OSCAL 문서의 변환(XML↔JSON↔YAML), 검증, 비교를 수행하는 Java 기반 CLI | https://github.com/usnistgov/oscal-cli |

---

## 2. MCP 서버 (AI 에이전트 연동)

MCP(Model Context Protocol) 서버를 사용하면 Claude, Cursor 등 AI 도구에서 NIST 데이터를 직접 조회할 수 있습니다.

### 종합 (NIST + OWASP 통합)

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **zer0-kr/security-framework-mcp** | **NIST:** SP 800-53 (1,196 + 53A 평가 + 53B 기준선), CSF 2.0, PF 1.0, SP 800-37 RMF, 613 출판물, CMVP, NICE, 용어사전 **+ OWASP:** Top 10 4종, ASVS, WSTG, MASVS, Cheat Sheets 등 11개 소스 | **OWASP+NIST 통합 유일.** 33개 도구, 3,329 레코드, STRIDE 위협 모델링, 컴플라이언스 매핑(PCI-DSS/ISO27001/800-53), MCP Top 10 보안 평가, 실시간 NVD | [GitHub](https://github.com/zer0-kr/security-framework-mcp) |

### SP 800-53 컨트롤 특화

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **tnicholson/nist-mcp-server** | SP 800-53 (1,196), CSF 2.0, CMMC 2.0, FedRAMP, SP 800-171 | 갭 분석, 리스크 평가, SOC2/ISO27001 매핑 | [GitHub](https://github.com/tnicholson/nist-mcp-server) |
| **Ansvar-Systems/security-controls-mcp** | 1,451 SCF 컨트롤 × 262 프레임워크 | 양방향 프레임워크 매핑. PyPI 배포 | [GitHub](https://github.com/Ansvar-Systems/security-controls-mcp) |
| **MarkAC007/mcp-server-scf** | 1,451 SCF + 354 프레임워크 + 증거 추적 | 39 도구. GRC 플랫폼급 | [GitHub](https://github.com/MarkAC007/mcp-server-scf) |

### CSF 2.0 평가 특화

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **rocklambros/nist-csf-2-mcp-server** | CSF 2.0 전체 (자체 확장 구조 포함) | 740개 평가 질문, 40+ 도구, 대시보드. NIST 공식 커뮤니티 리소스 등재 | [GitHub](https://github.com/rocklambros/nist-csf-2-mcp-server) |

### NVD 취약점 특화

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **HaroldFinchIFT/vuln-nist-mcp-server** | NVD (CVE, CPE, CISA KEV) | Docker Hub 등록. 자동 청킹/병렬 처리 | [GitHub](https://github.com/HaroldFinchIFT/vuln-nist-mcp-server) |
| **Cyreslab-AI/nist-nvd-mcp-server** | NVD (CVE, CVSS v2/v3/v4) | JavaScript. 캐싱/레이트리밋 내장 | [GitHub](https://github.com/Cyreslab-AI/nist-nvd-mcp-server) |

### OSCAL / GRC 자동화

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **awslabs/mcp-server-for-oscal** | NIST OSCAL (SP 800-53, SP 800-171, FedRAMP) | AWS 공식. SSP/SAR/POA&M 자동화 | [GitHub](https://github.com/awslabs/mcp-server-for-oscal) |

### 기타 보안 프레임워크

| MCP | 커버리지 | 특징 | GitHub |
|-----|---------|------|--------|
| **Ansvar-Systems/ot-security-mcp** | IEC 62443, NIST 800-82, NIST 800-53, MITRE ATT&CK ICS | OT/산업제어 보안 전문 | [GitHub](https://github.com/ansvar-systems/ot-security-mcp) |
| **Ansvar-Systems/US_Compliance_MCP** | HIPAA, CCPA, SOX, GLBA + NIST 800-53/CSF 매핑 | 미국 규제법 + NIST 교차 참조 | [GitHub](https://github.com/ansvar-systems/us_compliance_mcp) |
| **ethanolivertroy/fedramp-docs-mcp** | FedRAMP 20x KSI + NIST SP 800-53 매핑 | 20 도구. FRMR JSON 파싱 | [GitHub](https://github.com/ethanolivertroy/fedramp-docs-mcp) |

---

## 3. 용도별 추천

| 나는 이런 게 필요하다 | 추천 도구 |
|---------------------|----------|
| NIST + OWASP를 통합해서 AI로 검색하고 싶다 | **zer0-kr/security-framework-mcp** |
| STRIDE 위협 모델링을 자동화하고 싶다 | **zer0-kr/security-framework-mcp** (`threat_model`) |
| SP 800-53 컨트롤을 기준선별로 조회하고 싶다 | **zer0-kr/security-framework-mcp** (`get_nist_control baseline=LOW`) |
| ASVS를 PCI-DSS/ISO 27001/800-53에 매핑하고 싶다 | **zer0-kr/security-framework-mcp** (`compliance_map`) |
| NIST 문서를 검색하고 내용을 조회하고 싶다 | **zer0-kr/security-framework-mcp** (`get_nist_publication`, `search_nist`) |
| SP 800-53 컨트롤을 조회하고 갭 분석하고 싶다 | **tnicholson/nist-mcp-server** |
| CSF 2.0 기반으로 조직 평가를 수행하고 싶다 | **rocklambros/nist-csf-2-mcp-server** |
| CVE 취약점을 조회하고 싶다 | **zer0-kr/security-framework-mcp** (`search_cve`) 또는 **HaroldFinchIFT/vuln-nist-mcp-server** |
| 여러 프레임워크 간 매핑이 필요하다 (ISO 27001, SOC 2 등) | **Ansvar-Systems/security-controls-mcp** |
| OSCAL 기반 GRC 자동화를 하고 싶다 | **awslabs/mcp-server-for-oscal** |
| 코드 없이 데이터만 다운로드하고 싶다 | **NIST Publications XLSX** + **OSCAL Content** |

---

## 4. NIST 공식 GitHub 저장소

| 저장소 | 내용 | URL |
|--------|------|-----|
| **usnistgov/OSCAL** | OSCAL 스키마 및 도구 | https://github.com/usnistgov/OSCAL |
| **usnistgov/oscal-content** | SP 800-53, CSF 2.0, FedRAMP 기준선의 OSCAL 데이터 | https://github.com/usnistgov/oscal-content |
| **usnistgov/NIST-Tech-Pubs** | 전체 NIST 기술 출판물 메타데이터 | https://github.com/usnistgov/NIST-Tech-Pubs |
| **usnistgov/SCAP** | 보안 콘텐츠 자동화 프로토콜 사양 | https://github.com/usnistgov/SCAP |
| **usnistgov/800-63-3** | 디지털 신원 가이드라인 (SP 800-63) | https://github.com/usnistgov/800-63-3 |
| **usnistgov/macos_security** | macOS 보안 준수 프로젝트 (mSCP) | https://github.com/usnistgov/macos_security |
