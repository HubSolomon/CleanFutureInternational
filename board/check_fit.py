import re, pathlib, json
from playwright.sync_api import sync_playwright

files = sorted(pathlib.Path('.').glob('*.dc.html'))
pages = {}
for f in files:
    s = f.read_text()
    style = re.search(r'<helmet>(.*?)</helmet>', s, re.S).group(1)
    inner = re.search(r'</helmet>\s*(.*?)\s*</x-dc>', s, re.S).group(1)
    # height:auto so we can measure natural content height
    inner_auto = inner.replace('height: 700px;', 'height: auto; min-height: 0;', 1)
    pages[f.name] = f"<!doctype html><html><head><meta charset='utf-8'>{style}</head><body style='margin:0'>{inner_auto}</body></html>"

out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={'width':1200,'height':1400})
    for name, html in pages.items():
        pg.set_content(html)
        pg.wait_for_timeout(350)
        h = pg.evaluate("document.body.firstElementChild.getBoundingClientRect().height")
        out[name] = round(h)
    b.close()

print(f"{'artboard':<26}{'natural h':>10}   frame 700px")
for n,h in sorted(out.items(), key=lambda kv:-kv[1]):
    flag = "  OVERFLOW by %d" % (h-700) if h > 700 else ("  tight" if h > 660 else "")
    print(f"{n:<26}{h:>10}{flag}")
