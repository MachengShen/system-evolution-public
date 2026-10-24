#!/usr/bin/env python3
"""
build_preprints.py — System Evolution arXiv-style open-preprint PDF compiler.

Renders existing interactive HTML treatises (and one Markdown-only paper) into
clean academic A4 PDFs via Chromium page.pdf(), injecting:
  - papers/arxiv-print.css  (body.print-mode academic override)
  - a left vertical arXiv-style identifier banner
  - a References + How-to-Cite BibTeX box appended at the end
  - running header (short title) + footer (preprint id + page numbers) via
    Playwright header/footer templates

Run with the Playwright venv:
    /home/ubuntu/.venvs/webgrab/bin/python scripts/build_preprints.py

No fabricated data. No stock photos. PCSE-clean (author 'Macheng Shen' only).
Apache-2.0.
"""
import hashlib
import html as _html
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
PAPERS = REPO / "papers"
PRINT_CSS = PAPERS / "arxiv-print.css"
BASE_URL = "https://machengshen.github.io/system-evolution-public"

# ---------------------------------------------------------------------------
# Preprint catalog (single source of truth for ids, metadata, BibTeX keys).
# ---------------------------------------------------------------------------
PREPRINTS = [
    {
        "id": "SE-2026.10024", "ver": "v1", "lang": "en",
        "out": "SE-2026.10024-physics-of-learning-en.pdf",
        "source": "physics-of-learning-reachability-en.html", "source_type": "html",
        "title": "The First-Principles Physics of Learning and Intelligence: Irreversible Computation, the Thermodynamic Speed Limit, and Grounded Dissipative Structure",
        "short": "Physics of Learning and Intelligence",
        "cats": "cond-mat.stat-mech / cs.AI", "date": "24 Oct 2026",
        "bibkey": "shen2026physicslearning",
        "sha_token": "SHA256_PLACEHOLDER_10024en",
    },
    {
        "id": "SE-2026.10024", "ver": "v1", "lang": "zh",
        "out": "SE-2026.10024-physics-of-learning-zh.pdf",
        "source": "physics-of-learning-reachability.html", "source_type": "html",
        "title": "从物理学第一性原理理解「学习」与「智能」：不可逆计算、达未速率极限与耗散结构",
        "short": "Physics of Learning (ZH)",
        "cats": "cond-mat.stat-mech / cs.AI", "date": "24 Oct 2026",
        "bibkey": "shen2026physicslearningzh",
        "sha_token": "SHA256_PLACEHOLDER_10024zh",
    },
    {
        "id": "SE-2026.10022", "ver": "v1", "lang": "zh",
        "out": "SE-2026.10022-trajectory-substrate-rl-zh.pdf",
        "source": "trajectory-rl-substrate-evolution.html", "source_type": "html",
        "title": "轨迹滚动与基质强化学习：模型权重冻结时，智能体进化发生在环境侧",
        "short": "Trajectory-Rollout Substrate RL (ZH)",
        "cats": "cs.AI / cs.LG", "date": "22 Oct 2026",
        "bibkey": "shen2026substraterl",
        "sha_token": "SHA256_PLACEHOLDER_10022zh",
    },
    {
        "id": "SE-2026.10021", "ver": "v1", "lang": "zh",
        "out": "SE-2026.10021-anatomy-of-certainty-zh.pdf",
        "source": "anatomy-of-certainty.html", "source_type": "html",
        "title": "「确定性」的解剖学：判断力是内核引擎，蒙特卡洛是物理验证",
        "short": "The Anatomy of Certainty (ZH)",
        "cats": "cs.AI / stat.ME / econ.TH", "date": "21 Oct 2026",
        "bibkey": "shen2026certainty",
        "sha_token": "SHA256_PLACEHOLDER_10021zh",
    },
    {
        "id": "SE-2026.10019", "ver": "v1", "lang": "en",
        "out": "SE-2026.10019-thermodynamic-ledger-dependent-origination-en.pdf",
        "source": "emptiness-causality-intervention-ledger-en.html", "source_type": "html",
        "title": "The Thermodynamic Ledger of Dependent Origination: Quantum Causal Indefiniteness, Interventional Backfire, and Self-Referential Cosmology",
        "short": "Thermodynamic Ledger of Dependent Origination",
        "cats": "cond-mat.stat-mech / quant-ph / cs.AI", "date": "19 Oct 2026",
        "bibkey": "shen2026ledger",
        "sha_token": "SHA256_PLACEHOLDER_10019en",
    },
    {
        "id": "SE-2026.10019", "ver": "v1", "lang": "zh",
        "out": "SE-2026.10019-thermodynamic-ledger-dependent-origination-zh.pdf",
        "source": "emptiness-causality-intervention-ledger-zh.html", "source_type": "html",
        "title": "缘起性空的热力学账本：量子因果、干预反噬与自指宇宙",
        "short": "Thermodynamic Ledger (ZH)",
        "cats": "cond-mat.stat-mech / quant-ph / cs.AI", "date": "19 Oct 2026",
        "bibkey": "shen2026ledgerzh",
        "sha_token": "SHA256_PLACEHOLDER_10019zh",
    },
    {
        "id": "SE-2026.10016", "ver": "v1", "lang": "en",
        "out": "SE-2026.10016-neural-oscillations-fleet-optimality-en.pdf",
        "source": "essays/2026-10-16-neural-oscillations-and-agent-fleet-optimality.md",
        "source_type": "md",
        "title": "The Optimality of Oscillatory Propagation in Cognitive Substrates: From Whole-Brain Quantum-Like Connectomics to Multi-Agent Fleet Architecture",
        "short": "Oscillatory Propagation & Fleet Optimality",
        "cats": "q-bio.NC / cs.AI / cond-mat.dis-nn", "date": "16 Oct 2026",
        "bibkey": "shen2026oscillations",
        "sha_token": "SHA256_PLACEHOLDER_10016en",
    },
]

KATEX_HEAD = (
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">'
    '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>'
    '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" '
    'onload="renderMathInElement(document.body,{delimiters:[{left:\'$$\',right:\'$$\',display:true},'
    '{left:\'$\',right:\'$\',display:false},{left:\'\\\\(\',right:\'\\\\)\',display:false},'
    '{left:\'\\\\[\',right:\'\\\\]\',display:true}],throwOnError:false});"></script>'
)


def bibtex_for(p):
    url = f"{BASE_URL}/papers/{p['out']}"
    return (
        f"@techreport{{{p['bibkey']},\n"
        f"  author      = {{Shen, Macheng}},\n"
        f"  title       = {{{p['title']}}},\n"
        f"  institution = {{System Evolution (self-hosted open preprint series)}},\n"
        f"  number      = {{{p['id']}{p['ver']}}},\n"
        f"  year        = {{2026}},\n"
        f"  month       = {{oct}},\n"
        f"  note        = {{System Evolution Preprint {p['id']}{p['ver']}}},\n"
        f"  howpublished= {{\\url{{{url}}}}}\n"
        f"}}"
    )


def apa_for(p):
    return (f"Shen, M. (2026). {p['title']}. "
            f"System Evolution Preprint {p['id']}{p['ver']}. {BASE_URL}/papers/{p['out']}")


def cite_block_html(p):
    """A References + How-to-Cite section appended to each paper before PDF render."""
    bib = _html.escape(bibtex_for(p))
    apa = _html.escape(apa_for(p))
    return f"""
<section class="section-card" id="se-cite-appendix">
  <h2>How to Cite &amp; Index This Preprint</h2>
  <p>This is an open, self-hosted preprint in the <strong>System Evolution</strong> series
  (arXiv-style, Apache-2.0, BYOK). Stable identifier: <code>{p['id']}{p['ver']}</code>
  &nbsp;[{_html.escape(p['cats'])}]&nbsp;{p['date']}. Canonical landing page:
  <a href="{BASE_URL}/papers/index.html">{BASE_URL}/papers/index.html</a>.
  Machine clients may index <code>papers/catalog.json</code> and the root <code>CITATION.cff</code>.</p>
  <div class="bibtex-box">{bib}</div>
  <p style="margin-top:8pt;"><strong>APA:</strong> {apa}</p>
  <p style="font-size:9pt;color:#444;">PDF SHA-256 is published on the preprint index page and in
  <code>papers/catalog.json</code> for integrity verification.</p>
</section>
"""


def md_to_html_doc(md_path, p):
    """Minimal, dependency-free Markdown -> academic HTML for the md-only paper."""
    raw = md_path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    out = []
    in_code = False
    in_table = False

    def inline(s):
        s = _html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
        return s

    for ln in lines:
        if ln.strip().startswith("```"):
            if not in_code:
                out.append("<pre><code>")
                in_code = True
            else:
                out.append("</code></pre>")
                in_code = False
            continue
        if in_code:
            out.append(_html.escape(ln))
            continue
        # tables
        if "|" in ln and ln.strip().startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if re.match(r"^[\s:|-]+$", ln.strip()):
                continue  # separator row
            if not in_table:
                out.append("<table>")
                in_table = True
                tag = "th"
            else:
                tag = "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
            continue
        else:
            if in_table:
                out.append("</table>")
                in_table = False
        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            continue
        if re.match(r"^\s*[-*]\s+", ln):
            out.append(f"<li>{inline(re.sub(r'^\s*[-*]\s+', '', ln))}</li>")
            continue
        if ln.strip().startswith(">"):
            out.append(f"<blockquote>{inline(ln.strip().lstrip('>').strip())}</blockquote>")
            continue
        if ln.strip() == "":
            out.append("")
        else:
            out.append(f"<p>{inline(ln)}</p>")
    if in_table:
        out.append("</table>")
    body = "\n".join(out)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(p['title'])}</title>
{KATEX_HEAD}
<style>body{{font-family:'Latin Modern Roman','Noto Serif CJK SC','Noto Serif',Georgia,serif;
max-width:860px;margin:0 auto;padding:24px;line-height:1.5}}
h1{{font-size:1.8rem;text-align:center}} table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #333;padding:5px 7px}} pre{{background:#f5f5f5;padding:8px}}</style>
</head><body><main class="container"><h1>{_html.escape(p['title'])}</h1>{body}</main></body></html>"""


HEADER_TMPL = (
    '<div style="font-family:serif;font-size:7pt;color:#555;width:100%;'
    'padding:0 16mm;text-align:center;">{short}</div>'
)
FOOTER_TMPL = (
    '<div style="font-family:monospace;font-size:7pt;color:#555;width:100%;'
    'padding:0 16mm;display:flex;justify-content:space-between;">'
    '<span>System Evolution Preprint {pid}{ver}</span>'
    '<span>Page <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
)


def build(p, page):
    src = REPO / p["source"]
    if p["source_type"] == "md":
        doc = md_to_html_doc(src, p)
        page.set_content(doc, wait_until="networkidle")
        # inject print css + katex not strictly needed for md path (already has katex head)
    else:
        page.goto(src.as_uri(), wait_until="networkidle")

    # Inject the print stylesheet (read content + inject as <style> to tolerate @import).
    css_text = PRINT_CSS.read_text(encoding="utf-8")
    page.evaluate(
        """(css) => {
            const s = document.createElement('style');
            s.setAttribute('data-arxiv-print', '1');
            s.textContent = css;
            document.head.appendChild(s);
        }""",
        css_text,
    )
    # Enter print-mode, add the vertical arXiv banner, append the cite appendix.
    banner_text = f"{p['id']}{p['ver']}  [{p['cats']}]  {p['date']}"
    cite_html = cite_block_html(p)
    page.evaluate(
        """({banner, cite}) => {
            document.body.classList.add('print-mode');
            const b = document.createElement('div');
            b.className = 'arxiv-banner';
            b.textContent = banner;
            document.body.appendChild(b);
            const main = document.querySelector('main') || document.body;
            const wrap = document.createElement('div');
            wrap.innerHTML = cite;
            main.appendChild(wrap);
        }""",
        {"banner": banner_text, "cite": cite_html},
    )
    # Give KaTeX auto-render + any canvas draws a moment to settle.
    page.wait_for_timeout(2500)

    out_path = PAPERS / p["out"]
    page.pdf(
        path=str(out_path),
        format="A4",
        print_background=True,
        display_header_footer=True,
        header_template=HEADER_TMPL.format(short=_html.escape(p["short"])),
        footer_template=FOOTER_TMPL.format(pid=p["id"], ver=p["ver"]),
        margin={"top": "24mm", "bottom": "22mm", "left": "24mm", "right": "18mm"},
    )
    return out_path


def main():
    from playwright.sync_api import sync_playwright
    PAPERS.mkdir(exist_ok=True)
    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context()
        for p in PREPRINTS:
            page = ctx.new_page()
            try:
                out_path = build(p, page)
                data = out_path.read_bytes()
                sha = hashlib.sha256(data).hexdigest()
                results.append({**p, "bytes": len(data), "sha256": sha,
                                "pdf_url": f"{BASE_URL}/papers/{p['out']}"})
                print(f"[OK] {p['out']}  {len(data):>9,} bytes  sha256={sha[:16]}...")
            except Exception as e:
                print(f"[FAIL] {p['out']}: {e!r}", file=sys.stderr)
                raise
            finally:
                page.close()
        browser.close()

    # Fill SHA tokens into papers/index.html.
    idx = PAPERS / "index.html"
    if idx.exists():
        txt = idx.read_text(encoding="utf-8")
        for r in results:
            txt = txt.replace(r["sha_token"], r["sha256"])
        idx.write_text(txt, encoding="utf-8")
        print(f"[OK] injected {len(results)} SHA-256 values into papers/index.html")

    # Emit catalog.json (machine catalog).
    catalog = {
        "series": "System Evolution Open Preprints",
        "id_scheme": "SE-YYYY.NNNNN",
        "license": "Apache-2.0",
        "author": "Shen, Macheng",
        "base_url": BASE_URL,
        "index_url": f"{BASE_URL}/papers/index.html",
        "generated_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        "papers": [
            {
                "preprint_id": r["id"] + r["ver"], "lang": r["lang"],
                "title": r["title"], "categories": r["cats"], "date": r["date"],
                "pdf": r["out"], "pdf_url": r["pdf_url"],
                "sha256": r["sha256"], "bytes": r["bytes"], "bibtex_key": r["bibkey"],
            }
            for r in results
        ],
    }
    (PAPERS / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] wrote papers/catalog.json ({len(results)} papers)")

    # Summary for the caller.
    print("\n=== BUILD SUMMARY ===")
    for r in results:
        print(f"{r['id']}{r['ver']} {r['lang']}  {r['bytes']:>9,}B  {r['out']}")


if __name__ == "__main__":
    main()
