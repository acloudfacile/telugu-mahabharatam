#!/usr/bin/env python3
"""Build the Mahabharatam site.
  python3 build_site.py        -> site/ (deployable) + Mahabharatam_preview.html (single file)
Add a parva: drop site_src/<id>.json (same shape as adi.json), set its status to
"published" in site_src/parvas.json, add images to site_src/img/, re-run.
"""
import json, base64, os, shutil, glob

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site_src')
OUT = 'site'
parvas = json.load(open(f'{SRC}/parvas.json', encoding='utf8'))
content = {}
chars = json.load(open(f'{SRC}/characters.json', encoding='utf8'))
gurus = json.load(open(f'{SRC}/gurus.json', encoding='utf8'))
evolution = json.load(open(f'{SRC}/evolution.json', encoding='utf8'))
for f in glob.glob(f'{SRC}/*.json'):
    name = os.path.basename(f)[:-5]
    if name not in ('parvas','characters','gurus','evolution'):
        content[name] = json.load(open(f, encoding='utf8'))

css = open(f'{SRC}/style.css', encoding='utf8').read()
js = open(f'{SRC}/app.js', encoding='utf8').read()
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Tiro+Telugu&family=Noto+Sans+Telugu:wght@400;600&display=swap" rel="stylesheet">'

def shell(head, scripts, img_mode):
    return f'''<!doctype html>
<html lang="te">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{parvas['site']['title']}</title>
<meta name="description" content="{parvas['site']['tagline']}">
{FONTS}
{head}
</head>
<body>
<header class="top">
  <div class="bar">
    <a class="brand" href="#/">{parvas['site']['title']}</a>
    <nav><a href="#/">పర్వాలు</a><a href="#/patralu">పాత్రలు</a><a href="#/guruvulu">గురు పరంపర</a><a href="#/parinamam">పరిణామం</a></nav>
    <form id="hsearch" role="search"><input name="q" type="search" placeholder="వెతుకు…" aria-label="వెతుకు"></form>
  </div>
  <div class="frieze"></div>
</header>
<main id="app"></main>
<footer><div class="in"><span>{parvas['site']['title']} — పర్వం పర్వంగా పెరుగుతున్న తెలుగు కథా సంకలనం</span><span>వేదవ్యాస మహాభారతము ఆధారంగా స్వతంత్ర తెలుగు కథనం, స్వంత చిత్రాలు</span></div></footer>
<script>window.MB_IMG={json.dumps(img_mode)};window.MB_ICO={json.dumps('inline' if img_mode=='inline' else 'icons/')};</script>
{scripts}
</body>
</html>'''

# --- deployable site ---
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(f'{OUT}/data'); os.makedirs(f'{OUT}/assets')
shutil.copytree(f'{SRC}/img', f'{OUT}/img'); shutil.copytree(f'{SRC}/icons', f'{OUT}/icons')
open(f'{OUT}/assets/style.css', 'w', encoding='utf8').write(css)
open(f'{OUT}/assets/app.js', 'w', encoding='utf8').write(js)
open(f'{OUT}/data/parvas.js', 'w', encoding='utf8').write('window.MB_PARVAS=' + json.dumps(parvas, ensure_ascii=False) + ';')
open(f'{OUT}/data/content.js', 'w', encoding='utf8').write('window.MB_CONTENT=' + json.dumps(content, ensure_ascii=False) + ';')
open(f'{OUT}/data/characters.js', 'w', encoding='utf8').write('window.MB_CHARS=' + json.dumps(chars, ensure_ascii=False) + ';window.MB_GURUS=' + json.dumps(gurus, ensure_ascii=False) + ';window.MB_EVOLUTION=' + json.dumps(evolution, ensure_ascii=False) + ';')
open(f'{OUT}/index.html', 'w', encoding='utf8').write(shell(
    '<link rel="stylesheet" href="assets/style.css">',
    '<script src="data/parvas.js"></script><script src="data/content.js"></script><script src="data/characters.js"></script><script src="assets/app.js"></script>',
    'img/'))
open(f'{OUT}/README.md', 'w', encoding='utf8').write('''# సంపూర్ణ మహాభారతము — site

Static site, no build server needed. Open `index.html` or upload the folder to
GitHub Pages / Netlify / Cloudflare Pages.

Structure
- `index.html`        shell + hash router
- `assets/`           style.css, app.js
- `data/parvas.js`    list of 18 parvas and status
- `data/content.js`   episode text for published parvas
- `img/`              one illustration per episode (1200x675 jpg)
- `icons/`            character portraits + parva emblems (256px png)
- `data/characters.js` characters and guru parampara

To add the next parva, edit the source JSON in `site_src/` and re-run `build_site.py`.
''')

# --- single-file preview ---
images = {}
for f in sorted(os.listdir(f'{SRC}/img')):
    images[f] = 'data:image/jpeg;base64,' + base64.b64encode(open(f'{SRC}/img/{f}', 'rb').read()).decode()
icons = {}
for f in sorted(os.listdir(f'{SRC}/icons')):
    icons[f] = 'data:image/png;base64,' + base64.b64encode(open(f'{SRC}/icons/{f}', 'rb').read()).decode()
inline = (f'<script>window.MB_PARVAS={json.dumps(parvas, ensure_ascii=False)};window.MB_CHARS={json.dumps(chars, ensure_ascii=False)};window.MB_GURUS={json.dumps(gurus, ensure_ascii=False)};window.MB_EVOLUTION={json.dumps(evolution, ensure_ascii=False)};window.MB_ICONS={json.dumps(icons)};'
          f'window.MB_CONTENT={json.dumps(content, ensure_ascii=False)};'
          f'window.MB_IMAGES={json.dumps(images)};</script><script>{js}</script>')
open('Mahabharatam_preview.html', 'w', encoding='utf8').write(shell(f'<style>{css}</style>', inline, 'inline'))
print('built', OUT, 'and Mahabharatam_preview.html', os.path.getsize('Mahabharatam_preview.html') // 1024, 'KB')
