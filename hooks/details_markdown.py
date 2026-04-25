"""MkDocs hook: enable markdown rendering inside <details> blocks.

Raw HTML <details> tags require markdown="1" attribute for the md_in_html
extension to process their content as markdown. This hook injects the
attribute at build time so source files stay unchanged.
"""

import re


def on_page_markdown(markdown, **kwargs):
    return re.sub(r'<details>', '<details markdown="1">', markdown)
