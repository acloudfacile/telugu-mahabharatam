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
SITE_URL = 'https://acloudfacile.github.io/telugu-mahabharatam/'
parvas = json.load(open(f'{SRC}/parvas.json', encoding='utf8'))
content = {}
chars = json.load(open(f'{SRC}/characters.json', encoding='utf8'))
gurus = json.load(open(f'{SRC}/gurus.json', encoding='utf8'))
evolution = json.load(open(f'{SRC}/evolution.json', encoding='utf8'))
moolam = json.load(open(f'{SRC}/moolam.json', encoding='utf8'))
vamsha = json.load(open(f'{SRC}/vamsha.json', encoding='utf8'))
glossary = json.load(open(f'{SRC}/glossary.json', encoding='utf8'))
for f in glob.glob(f'{SRC}/*.json'):
    name = os.path.basename(f)[:-5]
    if name not in ('parvas','characters','gurus','evolution','moolam','vamsha','glossary'):
        content[name] = json.load(open(f, encoding='utf8'))

css = open(f'{SRC}/style.css', encoding='utf8').read()
js = open(f'{SRC}/app.js', encoding='utf8').read()
# Applied before first paint so a night reader never gets a white flash.
NOFLASH = "<script>(function(){try{var t=localStorage.getItem('mb-theme');if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>"
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Tiro+Telugu&family=Noto+Sans+Telugu:wght@400;600&display=swap" rel="stylesheet">'

def og(title, desc, url, image):
    import html as _h
    t, d = _h.escape(title, quote=True), _h.escape(desc, quote=True)
    return (f'<meta property="og:type" content="article"><meta property="og:site_name" content="{_h.escape(parvas["site"]["title"])}">'
            f'<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">'
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{image}">'
            f'<meta name="twitter:card" content="summary_large_image">')

def shell(head, scripts, img_mode, favicon='<link rel="icon" href="favicon.svg" type="image/svg+xml">', title=None, desc=None, main=''):
    import html as _h
    title = _h.escape(title or parvas['site']['title']); desc = _h.escape(desc or parvas['site']['tagline'], quote=True)
    return f'''<!doctype html>
<html lang="te">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
{favicon}
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#1B2540" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E1626" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="మహాభారతము">
<link rel="apple-touch-icon" href="appicons/apple-touch-icon.png">
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
    <nav id="sitenav"><a href="#/">పర్వాలు</a><a href="#/patralu">పాత్రలు</a><a href="#/padakosham">పదకోశము</a><a href="#/guruvulu">గురు పరంపర</a><a href="#/vamsham">వంశ వృక్షము</a><a href="#/moolam">మూల నిర్మాణము</a><a href="#/parinamam">పరిణామం</a><a href="#/gurinchi">ఈ సైటు గురించి</a></nav>
  </div>
  <div class="frieze"></div>
</header>
<main id="app">{main}</main>
<footer><div class="in"><span>{parvas['site']['title']} — పర్వం పర్వంగా పెరుగుతున్న తెలుగు కథా సంకలనం</span><span>వేదవ్యాస మహాభారతము ఆధారంగా స్వతంత్ర తెలుగు కథనం, స్వంత చిత్రాలు</span></div></footer>
<script>window.MB_IMG={json.dumps(img_mode)};window.MB_ICO={json.dumps('inline' if img_mode=='inline' else 'icons/')};</script>
{scripts}
</body>
</html>'''

# --- deployable site (in place, at the repo root) ---
for d in GENERATED + tuple(content.keys()):
    shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)
os.makedirs(f'{OUT}/data'); os.makedirs(f'{OUT}/assets')
shutil.copyfile(f'{SRC}/favicon.svg', f'{OUT}/favicon.svg')
shutil.copyfile(f'{SRC}/manifest.webmanifest', f'{OUT}/manifest.webmanifest')
shutil.rmtree(f'{OUT}/appicons', ignore_errors=True)
shutil.copytree(f'{SRC}/appicons', f'{OUT}/appicons')
shutil.copytree(f'{SRC}/img', f'{OUT}/img'); shutil.copytree(f'{SRC}/icons', f'{OUT}/icons')
open(f'{OUT}/assets/style.css', 'w', encoding='utf8').write(css)
open(f'{OUT}/assets/app.js', 'w', encoding='utf8').write(js)
open(f'{OUT}/data/parvas.js', 'w', encoding='utf8').write('window.MB_PARVAS=' + json.dumps(parvas, ensure_ascii=False) + ';')
# Text is split per parva and loaded only when that parva is opened. A small
# index (titles, characters, images) loads with the site so the home page,
# character pages and episode lists work without the full text.
os.makedirs(f'{OUT}/data/parva')
index = {}
for pid, c in content.items():
    open(f'{OUT}/data/parva/{pid}.js', 'w', encoding='utf8').write(
        f'(window.MB_CONTENT=window.MB_CONTENT||{{}})[{json.dumps(pid)}]=' + json.dumps(c, ensure_ascii=False) + ';')
    index[pid] = [{'num': e['num'], 'title': e['title'], 'characters': e['characters'], 'image': e['image'],
                   'caption': e['caption']} for e in c['episodes']]
open(f'{OUT}/data/index.js', 'w', encoding='utf8').write('window.MB_INDEX=' + json.dumps(index, ensure_ascii=False) + ';')
open(f'{OUT}/data/characters.js', 'w', encoding='utf8').write('window.MB_CHARS=' + json.dumps(chars, ensure_ascii=False) + ';window.MB_GURUS=' + json.dumps(gurus, ensure_ascii=False) + ';window.MB_EVOLUTION=' + json.dumps(evolution, ensure_ascii=False) + ';window.MB_MOOLAM=' + json.dumps(moolam, ensure_ascii=False) + ';window.MB_VAMSHA=' + json.dumps(vamsha, ensure_ascii=False) + ';window.MB_GLOSSARY=' + json.dumps(glossary, ensure_ascii=False) + ';')
SCRIPTS = '<script src="data/parvas.js"></script><script src="data/index.js"></script><script src="data/characters.js"></script><script src="assets/app.js"></script>'
open(f'{OUT}/index.html', 'w', encoding='utf8').write(shell(
    '<link rel="stylesheet" href="assets/style.css">' + f'<link rel="canonical" href="{SITE_URL}">' + og(parvas['site']['title'], parvas['site']['tagline'], SITE_URL, SITE_URL + 'appicons/icon-512.png'),
    SCRIPTS, 'img/'))

# --- one real page per episode (and per parva), for search engines and link previews ---
import html as _h
def ep_html(pid, p, c, e):
    rows = ''.join(f'<p>{_h.escape(t)}</p>' for t in e['paras'])
    pad = ''.join(f'<blockquote>{"<br>".join(_h.escape(l) for l in x["text"].split(chr(10)))}</blockquote><p>{_h.escape(x.get("gloss",""))}</p>' for x in e.get('padyams', []))
    vy = ''.join(f'<li>{_h.escape(v["text"])} <cite>{_h.escape(v["ref"])}</cite></li>' for v in e.get('vyasa', []))
    return (f'<article class="measure"><p class="crumbs"><a href="./">హోమ్</a> › <a href="{pid}/">{_h.escape(p["te"])}</a></p>'
            f'<h1>{_h.escape(e["title"])}</h1><figure><img src="img/{e["image"]}" alt="{_h.escape(e["caption"])}"><figcaption>{_h.escape(e["caption"])}</figcaption></figure>'
            f'<div class="story">{rows}</div>' + (f'<aside class="padyam">{pad}</aside>' if pad else '')
            + (f'<aside class="vyasa"><b>వ్యాసుని సంస్కృత భారతంలో</b><ul>{vy}</ul></aside>' if vy else '') + '</article>')
sitemap = [SITE_URL]
for pid, c in content.items():
    p = next(x for x in parvas['parvas'] if x['id'] == pid)
    os.makedirs(f'{OUT}/{pid}', exist_ok=True)
    url = f'{SITE_URL}{pid}/'; sitemap.append(url)
    lst = ''.join(f'<li><a href="{pid}/{e["num"]}/">{e["num"]}. {_h.escape(e["title"])}</a></li>' for e in c['episodes'])
    open(f'{OUT}/{pid}/index.html', 'w', encoding='utf8').write(shell(
        '<base href="../">' + '<link rel="stylesheet" href="assets/style.css">' + f'<link rel="canonical" href="{url}">'
        + og(f'{p["te"]} — {parvas["site"]["title"]}', ' '.join(c['intro'])[:200], url, SITE_URL + 'img/' + c['episodes'][0]['image'])
        + f'<script>window.MB_START={json.dumps("parva/" + pid)};</script>',
        SCRIPTS, 'img/', title=f'{p["te"]} — {parvas["site"]["title"]}', desc=' '.join(c['intro'])[:200],
        main=f'<div class="measure"><h1>{_h.escape(p["te"])}</h1>{"".join(f"<p>{_h.escape(t)}</p>" for t in c["intro"])}<ol>{lst}</ol></div>'))
    for e in c['episodes']:
        d = f'{OUT}/{pid}/{e["num"]}'; os.makedirs(d, exist_ok=True)
        url = f'{SITE_URL}{pid}/{e["num"]}/'; sitemap.append(url)
        desc = (e['paras'][0] if e['paras'] else e['caption'])[:180]
        title = f'{e["title"]} — {p["te"]}'
        start = 'parva/%s/%d' % (pid, e['num'])
        open(f'{d}/index.html', 'w', encoding='utf8').write(shell(
            '<base href="../../">' + '<link rel="stylesheet" href="assets/style.css">' + f'<link rel="canonical" href="{url}">'
            + og(title, desc, url, SITE_URL + 'img/' + e['image'])
            + f'<script>window.MB_START={json.dumps(start)};</script>',
            SCRIPTS, 'img/', title=title, desc=desc, main=ep_html(pid, p, c, e)))
open(f'{OUT}/sitemap.xml', 'w', encoding='utf8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'<url><loc>{u}</loc></url>\n' for u in sitemap) + '</urlset>\n')
open(f'{OUT}/robots.txt', 'w', encoding='utf8').write(f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n')
print(f'pages: {len(sitemap)-1} episode/parva pages + sitemap')
# README.md is hand-maintained in the repo; the build never overwrites it.


# --- offline: stamp the service worker with a build id and the file list ---
import hashlib, time
build = hashlib.sha1(
    (css + js + json.dumps(parvas, ensure_ascii=False) + json.dumps(content, ensure_ascii=False)
     + open(f'{SRC}/sw.js', encoding='utf8').read() + json.dumps(chars, ensure_ascii=False)
     ).encode('utf8')).hexdigest()[:12]
assets = ['./', './index.html', './assets/style.css', './assets/app.js',
          './data/parvas.js', './data/index.js', './data/characters.js',
          './favicon.svg', './manifest.webmanifest',
          './appicons/icon-192.png', './appicons/icon-512.png',
          './appicons/icon-maskable-512.png', './appicons/apple-touch-icon.png']
# pictures, icons and each parva's text are kept the first time they are read
sw = open(f'{SRC}/sw.js', encoding='utf8').read()
sw = sw.replace('__BUILD__', build).replace('__ASSETS__', json.dumps(assets, indent=0))
open(f'{OUT}/sw.js', 'w', encoding='utf8').write(sw)
print(f'offline: {len(assets)} files precached, build {build}')

# --- single-file preview ---
images = {}
for f in sorted(os.listdir(f'{SRC}/img')):
    images[f] = 'data:image/jpeg;base64,' + base64.b64encode(open(f'{SRC}/img/{f}', 'rb').read()).decode()
icons = {}
for f in sorted(os.listdir(f'{SRC}/icons')):
    icons[f] = 'data:image/png;base64,' + base64.b64encode(open(f'{SRC}/icons/{f}', 'rb').read()).decode()
inline = (f'<script>window.MB_PARVAS={json.dumps(parvas, ensure_ascii=False)};window.MB_CHARS={json.dumps(chars, ensure_ascii=False)};window.MB_GURUS={json.dumps(gurus, ensure_ascii=False)};window.MB_EVOLUTION={json.dumps(evolution, ensure_ascii=False)};window.MB_MOOLAM={json.dumps(moolam, ensure_ascii=False)};window.MB_VAMSHA={json.dumps(vamsha, ensure_ascii=False)};window.MB_GLOSSARY={json.dumps(glossary, ensure_ascii=False)};window.MB_ICONS={json.dumps(icons)};'
          f'window.MB_CONTENT={json.dumps(content, ensure_ascii=False)};'
          f'window.MB_IMAGES={json.dumps(images)};</script><script>{js}</script>')
fav_inline = ('<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,'
              + base64.b64encode(open(f'{SRC}/favicon.svg','rb').read()).decode() + '">')
open(os.path.join(ROOT, 'Mahabharatam_preview.html'), 'w', encoding='utf8').write(
    shell(f'<style>{css}</style>', inline, 'inline', favicon=fav_inline))
print('built site in', OUT)
print('built Mahabharatam_preview.html', os.path.getsize(os.path.join(ROOT, 'Mahabharatam_preview.html')) // 1024, 'KB')
