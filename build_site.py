#!/usr/bin/env python3
"""Build the Mahabharatam site.
  python3 build_site.py        -> regenerates the site in place (repo root) +
                                  Mahabharatam_preview.html (single self-contained file)
Add a parva: drop site_src/<id>.json (same shape as adi.json), set its status to
"published" in site_src/parvas.json, add images to site_src/img/, re-run.
"""
import json, base64, os, shutil, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'site_src')
# The repo root IS the deployable site, so GitHub Pages can serve it directly.
# Only the generated paths below are replaced; site_src/ and the scripts are never touched.
OUT = ROOT
GENERATED = ('data', 'assets', 'img', 'icons')
parvas = json.load(open(f'{SRC}/parvas.json', encoding='utf8'))
content = {}
chars = json.load(open(f'{SRC}/characters.json', encoding='utf8'))
gurus = json.load(open(f'{SRC}/gurus.json', encoding='utf8'))
evolution = json.load(open(f'{SRC}/evolution.json', encoding='utf8'))
moolam = json.load(open(f'{SRC}/moolam.json', encoding='utf8'))
vamsha = json.load(open(f'{SRC}/vamsha.json', encoding='utf8'))
for f in glob.glob(f'{SRC}/*.json'):
    name = os.path.basename(f)[:-5]
    if name not in ('parvas','characters','gurus','evolution','moolam','vamsha'):
        content[name] = json.load(open(f, encoding='utf8'))

css = open(f'{SRC}/style.css', encoding='utf8').read()
js = open(f'{SRC}/app.js', encoding='utf8').read()
# Applied before first paint so a night reader never gets a white flash.
NOFLASH = "<script>(function(){try{var t=localStorage.getItem('mb-theme');if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>"
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Tiro+Telugu&family=Noto+Sans+Telugu:wght@400;600&display=swap" rel="stylesheet">'

def shell(head, scripts, img_mode, favicon='<link rel="icon" href="favicon.svg" type="image/svg+xml">'):
    return f'''<!doctype html>
<html lang="te">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{parvas['site']['title']}</title>
<meta name="description" content="{parvas['site']['tagline']}">
{FONTS}
{favicon}
{NOFLASH}
{head}
</head>
<body>
<header class="top">
  <div class="bar">
    <a class="brand" href="#/"><span class="mark" aria-hidden="true"></span><span>{parvas['site']['title']}</span></a>
    <div class="tools">
      <form id="hsearch" role="search"><input name="q" type="search" placeholder="వెతుకు…" aria-label="వెతుకు"></form>
      <button type="button" id="themebtn" class="theme-btn" aria-label="రాత్రి రూపము" title="రాత్రి రూపము"></button>
      <button type="button" id="navbtn" class="nav-btn" aria-expanded="false" aria-controls="sitenav" aria-label="మెనూ">☰</button>
    </div>
    <nav id="sitenav"><a href="#/">పర్వాలు</a><a href="#/patralu">పాత్రలు</a><a href="#/padakosham">పదకోశము</a><a href="#/guruvulu">గురు పరంపర</a><a href="#/vamsham">వంశ వృక్షము</a><a href="#/moolam">మూల నిర్మాణము</a><a href="#/parinamam">పరిణామం</a></nav>
  </div>
  <div class="frieze"></div>
</header>
<main id="app"></main>
<footer><div class="in"><span>{parvas['site']['title']} — పర్వం పర్వంగా పెరుగుతున్న తెలుగు కథా సంకలనం</span><span>వేదవ్యాస మహాభారతము ఆధారంగా స్వతంత్ర తెలుగు కథనం, స్వంత చిత్రాలు</span></div></footer>
<script>window.MB_IMG={json.dumps(img_mode)};window.MB_ICO={json.dumps('inline' if img_mode=='inline' else 'icons/')};</script>
{scripts}
</body>
</html>'''

# --- deployable site (in place, at the repo root) ---
for d in GENERATED:
    shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)
os.makedirs(f'{OUT}/data'); os.makedirs(f'{OUT}/assets')
shutil.copyfile(f'{SRC}/favicon.svg', f'{OUT}/favicon.svg')
shutil.copytree(f'{SRC}/img', f'{OUT}/img'); shutil.copytree(f'{SRC}/icons', f'{OUT}/icons')
open(f'{OUT}/assets/style.css', 'w', encoding='utf8').write(css)
open(f'{OUT}/assets/app.js', 'w', encoding='utf8').write(js)
open(f'{OUT}/data/parvas.js', 'w', encoding='utf8').write('window.MB_PARVAS=' + json.dumps(parvas, ensure_ascii=False) + ';')
open(f'{OUT}/data/content.js', 'w', encoding='utf8').write('window.MB_CONTENT=' + json.dumps(content, ensure_ascii=False) + ';')
open(f'{OUT}/data/characters.js', 'w', encoding='utf8').write('window.MB_CHARS=' + json.dumps(chars, ensure_ascii=False) + ';window.MB_GURUS=' + json.dumps(gurus, ensure_ascii=False) + ';window.MB_EVOLUTION=' + json.dumps(evolution, ensure_ascii=False) + ';window.MB_MOOLAM=' + json.dumps(moolam, ensure_ascii=False) + ';window.MB_VAMSHA=' + json.dumps(vamsha, ensure_ascii=False) + ';')
open(f'{OUT}/index.html', 'w', encoding='utf8').write(shell(
    '<link rel="stylesheet" href="assets/style.css">',
    '<script src="data/parvas.js"></script><script src="data/content.js"></script><script src="data/characters.js"></script><script src="assets/app.js"></script>',
    'img/'))
# README.md is hand-maintained in the repo; the build never overwrites it.

# --- single-file preview ---
images = {}
for f in sorted(os.listdir(f'{SRC}/img')):
    images[f] = 'data:image/jpeg;base64,' + base64.b64encode(open(f'{SRC}/img/{f}', 'rb').read()).decode()
icons = {}
for f in sorted(os.listdir(f'{SRC}/icons')):
    icons[f] = 'data:image/png;base64,' + base64.b64encode(open(f'{SRC}/icons/{f}', 'rb').read()).decode()
inline = (f'<script>window.MB_PARVAS={json.dumps(parvas, ensure_ascii=False)};window.MB_CHARS={json.dumps(chars, ensure_ascii=False)};window.MB_GURUS={json.dumps(gurus, ensure_ascii=False)};window.MB_EVOLUTION={json.dumps(evolution, ensure_ascii=False)};window.MB_MOOLAM={json.dumps(moolam, ensure_ascii=False)};window.MB_VAMSHA={json.dumps(vamsha, ensure_ascii=False)};window.MB_ICONS={json.dumps(icons)};'
          f'window.MB_CONTENT={json.dumps(content, ensure_ascii=False)};'
          f'window.MB_IMAGES={json.dumps(images)};</script><script>{js}</script>')
fav_inline = ('<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,'
              + base64.b64encode(open(f'{SRC}/favicon.svg','rb').read()).decode() + '">')
open(os.path.join(ROOT, 'Mahabharatam_preview.html'), 'w', encoding='utf8').write(
    shell(f'<style>{css}</style>', inline, 'inline', favicon=fav_inline))
print('built site in', OUT)
print('built Mahabharatam_preview.html', os.path.getsize(os.path.join(ROOT, 'Mahabharatam_preview.html')) // 1024, 'KB')
