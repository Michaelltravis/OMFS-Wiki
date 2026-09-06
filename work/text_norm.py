"""Shared normalization helpers for pdf_to_verbatim.py and coverage.py."""
import re

FRONTMATTER_RE = re.compile(r'^---\n.*?\n---\n', re.DOTALL)
PARA_COMMENT_RE = re.compile(r'^<!--.*?-->\s*$', re.MULTILINE)


def normalize(text):
    text = text.replace('�', '')
    text = text.replace("'", "").replace("'", "").replace("'", "")
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def words(text):
    n = normalize(text)
    return n.split() if n else []


def shingles(word_list, k=8):
    if len(word_list) < k:
        return []
    return [tuple(word_list[i:i + k]) for i in range(len(word_list) - k + 1)]


def strip_page_file(body_text):
    """Strip YAML frontmatter and any HTML comments (paragraph markers, recovered-block
    marker) from a rendered verbatim page file, leaving just the body prose/tables."""
    body = FRONTMATTER_RE.sub('', body_text, count=1)
    body = PARA_COMMENT_RE.sub('', body)
    return body
