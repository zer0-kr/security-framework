# Security Framework

[![GitHub Pages](https://img.shields.io/badge/📖_Live_Site-GitHub_Pages-blue)](https://zer0-kr.github.io/security-framework/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> ⚠️ 이 프로젝트는 NIST/OWASP 공식 자료가 아닌 **비공식 학습 자료**입니다. 정확한 내용은 반드시 [NIST 원문](https://csrc.nist.gov) 및 [OWASP 원문](https://owasp.org)을 확인하세요.

글로벌 정보보호 프레임워크의 문서 체계를 정리하고, 핵심 내용을 한국어로 요약하여 제공하는 프로젝트입니다. 보안 실무자가 필요할 때 허들 없이 참고할 수 있는 레퍼런스를 목표합니다.

**📖 [https://zer0-kr.github.io/security-framework/](https://zer0-kr.github.io/security-framework/)**

## NIST

NIST(미국 국립표준기술연구소)의 사이버보안/프라이버시 출판물을 체계적으로 정리합니다.

**[📖 NIST 문서 체계 가이드](./NIST/README.md)** — 시리즈 구조, 문서 간 관계도, 전체 개요

| 문서 | 내용 | 링크 |
|------|------|------|
| **CSF 2.0** | 사이버보안 프레임워크 — 6 Functions, 22 Categories, 106 Subcategories | [상세](./NIST/CSF-2.0/README.md) |
| **PF 1.0** | 프라이버시 프레임워크 — 5 Functions, 18 Categories, 100 Subcategories | [상세](./NIST/PF-1.0/README.md) |
| **SP 800-37** | 위험관리 프레임워크 (RMF) — 7단계, 47 Tasks | [상세](./NIST/SP800-37/README.md) |
| **SP 800-53** | 보안/프라이버시 컨트롤 — 20 Families, 1,014 Active Controls | [상세](./NIST/SP800-53/README.md) |
| **SP 800-53A** | 컨트롤 평가 절차 — Examine/Interview/Test | [상세](./NIST/SP800-53/assessment.md) |
| **SP 800-53B** | LOW (149) · MODERATE (287) · HIGH (370) 체크리스트 | [LOW](./NIST/SP800-53/low.md) · [MOD](./NIST/SP800-53/moderate.md) · [HIGH](./NIST/SP800-53/high.md) |
| **SP 800 시리즈** | 209건 주제별 분류 + 한국어 요약 | [상세](./NIST/SP800/README.md) |
| **SP 1800 시리즈** | 37건 실무 구현 가이드 + 한국어 요약 | [상세](./NIST/SP1800/README.md) |
| **도구 및 데이터 소스** | NIST API, MCP 서버, CLI — 프로그래밍 방식 활용 | [상세](./NIST/tools.md) |

## OWASP

OWASP(Open Worldwide Application Security Project)의 애플리케이션 보안 프로젝트를 체계적으로 정리합니다.

**[📖 OWASP 프로젝트 체계 가이드](./OWASP/README.md)** — 프로젝트 분류, 관계도, 학습 경로

| 문서 | 내용 | 링크 |
|------|------|------|
| **Top 10 (2025)** | 웹 10대 보안 위험 — 2025년 공식 릴리스 | [상세](./OWASP/Top10-2025/README.md) |
| **ASVS v5.0** | 애플리케이션 보안 검증 표준 — 17 챕터, 345 요구사항, 3 Level | [상세](./OWASP/ASVS/README.md) |
| **WSTG v4.2** | 웹 보안 테스트 가이드 — 12 카테고리, 128 테스트 케이스 | [상세](./OWASP/WSTG/README.md) |
| **프로젝트 목록** | Flagship 15 + Production 11 + Lab + Incubator | [상세](./OWASP/projects.md) |
| **Top 10 전체 목록** | 26개 도메인별 Top 10 프로젝트 모음 | [상세](./OWASP/top10-catalog.md) |

## 기여

오류 발견, 내용 보강, 번역 개선 등은 [CONTRIBUTING.md](./CONTRIBUTING.md)를 참고하여 Issue 또는 PR로 알려주세요.

## 라이선스

이 프로젝트의 콘텐츠는 [CC BY-NC-SA 4.0](./LICENSE) 라이선스로 제공됩니다. NIST 원문은 미국 정부 저작물로서 퍼블릭 도메인이며, OWASP 원문은 CC BY-SA 4.0입니다.
