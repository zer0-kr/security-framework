"""MkDocs hook: inject markdown="1" into <details> tags at build time.

The md_in_html extension only processes markdown inside HTML blocks that
carry markdown="1". Source files use raw <details> without it, and the
constraint is to never modify source content. This hook bridges the gap.
"""

import re

_DETAILS_RE = re.compile(r'<details(?![^>]*markdown\s*=)([^>]*)>', re.IGNORECASE)


def on_page_markdown(markdown, **kwargs):
    return _DETAILS_RE.sub(r'<details\1 markdown="1">', markdown)
