---
hide:
  - navigation
  - toc
---

# Security Framework

> 글로벌 정보보호 프레임워크의 핵심을 한국어로 정리한 레퍼런스입니다.
> 보안 실무자가 필요할 때 허들 없이 참고할 수 있도록 만들었습니다.

!!! warning "비공식 학습 자료"
    이 프로젝트는 NIST/OWASP 공식 자료가 아닌 **비공식 학습 자료**입니다. 정확한 내용은 반드시 [NIST 원문](https://csrc.nist.gov) 및 [OWASP 원문](https://owasp.org)을 확인하세요.

---

<div class="grid cards" markdown>

-   :material-shield-lock:{ .lg .middle } **NIST 사이버보안/프라이버시**

    ---

    미국 국립표준기술연구소의 프레임워크, 컨트롤, 가이드라인을 체계적으로 정리합니다.

    **CSF 2.0** · **PF 1.0** · **SP 800-37 RMF** · **SP 800-53** · SP 800/1800 시리즈

    [:octicons-arrow-right-24: NIST 문서 체계 가이드](NIST/README.md)

-   :material-web-check:{ .lg .middle } **OWASP 애플리케이션 보안**

    ---

    OWASP의 웹/앱 보안 프로젝트를 체계적으로 정리합니다.

    **Top 10 2025** · **ASVS v5.0** · **WSTG v4.2** · 프로젝트 목록

    [:octicons-arrow-right-24: OWASP 프로젝트 체계 가이드](OWASP/README.md)

</div>

---

## NIST 주요 문서

| 문서 | 내용 |
|------|------|
| [**CSF 2.0**](NIST/CSF-2.0/README.md) | 사이버보안 프레임워크 — 6 Functions, 22 Categories, 106 Subcategories |
| [**PF 1.0**](NIST/PF-1.0/README.md) | 프라이버시 프레임워크 — 5 Functions, 18 Categories, 100 Subcategories |
| [**SP 800-37 (RMF)**](NIST/SP800-37/README.md) | 위험관리 프레임워크 — 7단계, 47 Tasks |
| [**SP 800-53**](NIST/SP800-53/README.md) | 보안/프라이버시 컨트롤 — 20 Families, 1,014 Active Controls |
| [**SP 800-53A**](NIST/SP800-53/assessment.md) | 컨트롤 평가 절차 — Examine/Interview/Test |
| [**SP 800-53B 기준선**](NIST/SP800-53/low.md) | [LOW](NIST/SP800-53/low.md) (149) · [MODERATE](NIST/SP800-53/moderate.md) (287) · [HIGH](NIST/SP800-53/high.md) (370) |
| [**SP 800 시리즈**](NIST/SP800/README.md) | 209건 주제별 분류 + 한국어 요약 |
| [**SP 1800 시리즈**](NIST/SP1800/README.md) | 37건 실무 구현 가이드 + 한국어 요약 |
| [**도구 및 데이터 소스**](NIST/tools.md) | NIST API, MCP 서버, CLI — 프로그래밍 방식 활용 |

## OWASP 주요 문서

| 문서 | 내용 |
|------|------|
| [**Top 10 2025**](OWASP/Top10-2025/README.md) | 웹 10대 보안 위험 — 2025년 공식 릴리스 |
| [**ASVS v5.0**](OWASP/ASVS/README.md) | 애플리케이션 보안 검증 표준 — 17 챕터, 345 요구사항, 3 Level |
| [**WSTG v4.2**](OWASP/WSTG/README.md) | 웹 보안 테스트 가이드 — 12 카테고리, 128 테스트 케이스 |
| [**프로젝트 목록**](OWASP/projects.md) | Flagship 15 + Production 11 + Lab + Incubator |
| [**Top 10 전체 목록**](OWASP/top10-catalog.md) | 26개 도메인별 Top 10 프로젝트 모음 |

---

이 프로젝트의 콘텐츠는 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 라이선스로 제공됩니다. 오류 발견, 내용 보강, 번역 개선 등은 [Issue 또는 PR](https://github.com/zer0-kr/security-framework/issues)로 알려주세요.
