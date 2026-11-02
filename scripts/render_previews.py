"""Gera docs/*.html autônomos (tokens.css + bundle.css embutidos) e, com --png, capturas PNG via Playwright.
Uso: python scripts/render_previews.py [--png] [--theme ambar|gelo|esmeralda]"""
import os, re, sys
REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
COMP = os.path.join(REPO, 'design', 'components')
DOCS = os.path.join(REPO, 'docs')
theme = sys.argv[sys.argv.index('--theme') + 1] if '--theme' in sys.argv else 'ambar'
tokens = open(os.path.join(REPO, 'design', 'tokens.css'), encoding='utf-8').read()
bundle = open(os.path.join(COMP, 'bundle.css'), encoding='utf-8').read()
os.makedirs(DOCS, exist_ok=True)
pages = []
for n in sorted(os.listdir(COMP)):
    p = os.path.join(COMP, n, 'preview.html')
    if not os.path.exists(p): continue
    src = open(p, encoding='utf-8').read()
    src = src.replace('<head>', f'<head><style>{tokens}\n{bundle}</style>', 1).replace('<html>', f'<html data-theme="{theme}">', 1)
    open(os.path.join(DOCS, f'{n}.html'), 'w', encoding='utf-8').write(src)
    pages.append(n)
links = ''.join(f'<li><a href="{n}.html">{n}</a></li>' for n in pages)
open(os.path.join(DOCS, 'index.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><meta charset="utf-8"><title>Ardósia — prévias</title>'
    f'<body style="background:#171B21;color:#D9DFE6;font-family:Inter,Segoe UI,sans-serif;padding:32px">'
    f'<h1>Ardósia — prévias ({theme})</h1><ul>{links}</ul></body>')
print(f'{len(pages)} prévias em docs/')
if '--png' in sys.argv:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for n in pages:
            first = open(os.path.join(COMP, n, 'preview.html'), encoding='utf-8').readline()
            m = re.search(r'width=(\d+)', first)
            pg = b.new_page(viewport={'width': int(m.group(1)) if m else 960, 'height': 600})
            pg.goto('file://' + os.path.abspath(os.path.join(DOCS, f'{n}.html')), wait_until='networkidle')
            pg.screenshot(path=os.path.join(DOCS, f'{n}-{theme}.png'), full_page=True)
        b.close()
    print('PNGs em docs/')
