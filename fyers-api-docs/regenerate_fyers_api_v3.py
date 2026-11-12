"""Regenerate FYERS_API_v3.md from the live Fyers docs.

https://myapi.fyers.in/docsv3 is a React app; the content is a Redocly OpenAPI
YAML referenced from its JS bundle (the filename hash changes on redeploy).
This script finds that YAML, downloads it and writes it out as one markdown
file in the layout the rest of this folder is used to: one "## <tag>" section
per docs tag, one "### <summary>" per endpoint, cURL and Python samples.

    uv run --with pyyaml regenerate_fyers_api_v3.py            # fetch live
    uv run --with pyyaml regenerate_fyers_api_v3.py --from-file v3.yaml

Descriptions in the spec are markdown with HTML mixed in (<table>, <ul>, <b>,
<a>, <pre>...). They are converted to plain markdown; placeholder tokens that
merely look like tags (<host>, <appId>) are left alone so the text stays
searchable.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

import yaml

SITE = "https://myapi.fyers.in"
OUT = Path(__file__).with_name("FYERS_API_v3.md")
SKIP_TAGS = {"pet_model", "store_model", "pet", "store", "user"}  # petstore template leftovers
SAMPLE_LANGS = {"curl": "bash", "python": "python"}
KNOWN_TAGS = {
    "a", "b", "strong", "br", "p", "div", "span", "code", "pre", "ul", "ol", "li",
    "table", "tr", "td", "th", "h3", "h4", "img", "video", "i", "em", "body",
}


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()


def locate_spec() -> tuple[str, bytes]:
    index = fetch(SITE + "/").decode("utf-8", "replace")
    bundle = re.search(r'static/js/main\.[a-f0-9]+\.js', index).group(0)
    js = fetch(f"{SITE}/{bundle}").decode("utf-8", "replace")
    name = re.search(r'static/media/(v3\.[a-f0-9]+\.yaml)', js).group(1)
    return name, fetch(f"{SITE}/static/media/{name}")


# --- HTML -> markdown -------------------------------------------------------

def _inline(s: str, in_cell: bool = False) -> str:
    s = re.sub(r"<(b|strong)\b[^>]*>(.*?)</\1>", r"**\2**", s, flags=re.S)
    s = re.sub(r"<(i|em)\b[^>]*>(.*?)</\1>", r"*\2*", s, flags=re.S)
    s = re.sub(r"<code\b[^>]*>(.*?)</code>", r"`\1`", s, flags=re.S)
    s = re.sub(r'<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r"[\2](\1)", s, flags=re.S)
    s = re.sub(r"<a\b[^>]*>(.*?)</a>", r"\1", s, flags=re.S)
    s = re.sub(r'<img\b[^>]*src="([^"]*)"[^>]*/?>', r"![image](\1)", s)
    s = re.sub(r'<video\b[^>]*src="([^"]*)"[^>]*>.*?</video>', r"[video](\1)", s, flags=re.S)
    s = re.sub(r'<video\b[^>]*src="([^"]*)"[^>]*/?>', r"[video](\1)", s)
    s = re.sub(r"<h3\b[^>]*>(.*?)</h3>", r"\n\n#### \1\n\n", s, flags=re.S)
    s = re.sub(r"<h4\b[^>]*>(.*?)</h4>", r"\n\n#### \1\n\n", s, flags=re.S)
    s = re.sub(r"<br\s*/?>|</br>", " " if in_cell else "\n", s)
    s = re.sub(r"</?p\b[^>]*>", " " if in_cell else "\n\n", s)
    s = re.sub(r"</?(div|span|body)\b[^>]*>", "", s)
    s = re.sub(r"</?(b|strong)\s*>", "", s)  # orphan openers/closers left behind
    return s


def _table(m: re.Match) -> str:
    rows = re.findall(r"<tr\b[^>]*>(.*?)</tr>", m.group(1), flags=re.S)
    out = []
    for i, row in enumerate(rows):
        cells = re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", row, flags=re.S)
        cells = [
            re.sub(r"\s+", " ", html.unescape(_inline(c, in_cell=True))).strip().replace("|", "\\|")
            for c in cells
        ]
        if not cells:
            continue
        out.append("| " + " | ".join(cells) + " |")
        if i == 0:
            out.append("|" + " --- |" * len(cells))
    return "\n\n" + "\n".join(out) + "\n\n"


def _lists(s: str) -> str:
    parts = re.split(r"(<ul\b[^>]*>|</ul>|<ol\b[^>]*>|</ol>|<li\b[^>]*>|</li>)", s)
    out, stack, counters = [], [], []
    for part in parts:
        low = part.lower()
        if low.startswith("<ul"):
            stack.append("-"); counters.append(0); out.append("\n")
        elif low.startswith("<ol"):
            stack.append("1"); counters.append(0); out.append("\n")
        elif low in ("</ul>", "</ol>"):
            if stack:
                stack.pop(); counters.pop()
            out.append("\n")
        elif low.startswith("<li"):
            if not stack:
                stack.append("-"); counters.append(0)
            counters[-1] += 1
            marker = "-" if stack[-1] == "-" else f"{counters[-1]}."
            out.append("\n" + "  " * (len(stack) - 1) + marker + " ")
        elif low == "</li>":
            pass
        else:
            out.append(part.replace("\n", " ") if stack else part)
    return "".join(out)


def _pre(m: re.Match) -> str:
    body = re.sub(r"<br\s*/?>", "\n", m.group(1))
    body = html.unescape(re.sub(r"<[^>]+>", "", body)).strip("\n")
    return f"\n\n```\n{body}\n```\n\n"


def to_markdown(text: str, base_level: int) -> str:
    if not text:
        return ""
    s = text.replace("\r\n", "\n")
    s = re.sub(r"<pre\b[^>]*>(.*?)</pre>", _pre, s, flags=re.S)
    s = re.sub(r"<table\b[^>]*>(.*?)</table>", _table, s, flags=re.S)
    s = _lists(s)
    s = _inline(s)
    s = html.unescape(s)
    # Demote headings so nothing inside a section outranks its own heading.
    levels = [len(h) for h in re.findall(r"^(#{1,6})\s", s, flags=re.M)]
    if levels:
        shift = max(0, base_level + 1 - min(levels))
        s = re.sub(
            r"^(#{1,6})(\s)",
            lambda m: "#" * min(6, len(m.group(1)) + shift) + m.group(2),
            s,
            flags=re.M,
        )
    s = re.sub(r"[ \t]+$", "", s, flags=re.M)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip() + "\n"


# --- document assembly ------------------------------------------------------

def samples(op: dict) -> str:
    out = []
    for s in op.get("x-codeSamples", []):
        lang = SAMPLE_LANGS.get(str(s.get("lang", "")).lower())
        if lang and s.get("source"):
            out.append(f"**{s['lang']}**\n\n```{lang}\n{s['source'].strip()}\n```\n")
    return "\n".join(out)


def responses(op: dict) -> str:
    out = []
    for code, resp in (op.get("responses") or {}).items():
        for media in (resp.get("content") or {}).values():
            examples = media.get("examples") or {}
            if "example" in media:
                examples = {"example": {"value": media["example"]}}
            for name, ex in examples.items():
                value = ex.get("value", ex) if isinstance(ex, dict) else ex
                body = value if isinstance(value, str) else json.dumps(value, indent=2)
                title = f"Response {code}" + (f" ({name})" if name != "example" else "")
                out.append(f"**{title}**\n\n```json\n{body.strip()}\n```\n")
    return "\n".join(out)


def build(spec: dict, spec_name: str, fetched: str) -> str:
    tags = {t["name"]: t for t in spec.get("tags", [])}
    order = [t for g in spec.get("x-tagGroups", []) for t in g["tags"]]
    order += [n for n in tags if n not in order]
    ops_by_tag: dict[str, list] = {n: [] for n in order}
    for item in spec.get("paths", {}).values():
        for op in item.values():
            if not isinstance(op, dict) or "summary" not in op:
                continue
            for t in op.get("tags", []):
                ops_by_tag.setdefault(t, []).append(op)

    lines = [
        "# FYERS API v3 Documentation",
        "",
        f"> Generated from the live FYERS API v3 reference at {SITE}/docsv3 on {fetched}",
        f"> (OpenAPI spec `static/media/{spec_name}`) by `regenerate_fyers_api_v3.py`.",
        "> Re-run that script to refresh this file; do not edit it by hand. Only the cURL and",
        "> Python code samples are included; the live site also carries Node, Web JS, Java, Go,",
        "> C# and C variants of each.",
        "",
        to_markdown(spec["info"].get("description", ""), 1),
    ]
    for name in order:
        if name in SKIP_TAGS:
            continue
        tag = tags.get(name, {"name": name})
        if not tag.get("description") and not ops_by_tag.get(name):
            continue  # a tag with neither text nor endpoints, e.g. Screeners
        title = tag.get("x-displayName") or name
        lines += ["", f"## {title}", ""]
        if tag.get("description"):
            lines += [to_markdown(tag["description"], 2)]
        for op in ops_by_tag.get(name, []):
            lines += ["", f"### {op['summary']}", ""]
            if op.get("deprecated"):
                lines += ["**Deprecated.**", ""]
            lines += [to_markdown(op.get("description", ""), 3)]
            s = samples(op)
            if s:
                lines += ["", s]
            r = responses(op)
            if r:
                lines += ["", r]
    doc = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", doc).strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-file", help="use a downloaded YAML instead of fetching")
    ap.add_argument("--spec-name", help="spec filename to record when using --from-file")
    ap.add_argument("--out", type=Path, default=OUT)
    a = ap.parse_args()
    if a.from_file:
        raw = Path(a.from_file).read_bytes()
        name = a.spec_name or Path(a.from_file).name
    else:
        name, raw = locate_spec()
    spec = yaml.safe_load(raw)
    doc = build(spec, name, dt.date.today().isoformat())
    a.out.write_text(doc, encoding="utf-8")
    # Self-check on prose only: fenced blocks may legitimately hold HTML (the EDIS
    # TPIN response is an HTML page returned as a JSON string).
    prose, fenced = [], False
    for line in doc.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced:
            prose.append(line)
    leftover = sorted(set(re.findall(r"</?(%s)\b" % "|".join(KNOWN_TAGS), "\n".join(prose))))
    print(f"wrote {a.out} ({len(doc.splitlines())} lines, {len(doc.encode())} bytes) from {name}")
    print("unconverted html tags:", leftover or "none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
