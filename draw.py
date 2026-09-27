from PIL import Image, ImageDraw, ImageFilter
import math, random, os

W, H = 1600, 900
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site_src", "img")
OW, OH = 1200, 675          # what the site actually serves
os.makedirs(OUT, exist_ok=True)
random.seed(7)

# Palette
GOLD = (212, 160, 60); DGOLD = (150, 105, 30); CREAM = (250, 240, 215)
SAFF = (232, 120, 40); RED = (170, 40, 30); MAROON = (100, 20, 25)
NIGHT = (20, 25, 60); DUSK = (60, 40, 90); SKYB = (120, 170, 210)
WATER = (40, 90, 140); WATER2 = (80, 140, 190); GREEN = (40, 95, 55)
DGREEN = (25, 60, 40); BROWN = (95, 60, 35); SAND = (225, 195, 140)
INK = (35, 25, 20); WHITE = (255, 252, 240); SMOKE = (70, 60, 70)


def gradient(draw, top, bottom, y0=0, y1=H):
    for y in range(y0, y1):
        t = (y - y0) / max(1, (y1 - y0))
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line([(0, y), (W, y)], fill=c)


def border(img):
    d = ImageDraw.Draw(img)
    for i, c in enumerate([DGOLD, GOLD, DGOLD]):
        d.rectangle([14 + i * 6, 14 + i * 6, W - 15 - i * 6, H - 15 - i * 6], outline=c, width=4)
    # corner lotus motifs
    for cx, cy in [(45, 45), (W - 45, 45), (45, H - 45), (W - 45, H - 45)]:
        for k in range(8):
            a = k * math.pi / 4
            d.ellipse([cx + 14 * math.cos(a) - 9, cy + 14 * math.sin(a) - 9,
                       cx + 14 * math.cos(a) + 9, cy + 14 * math.sin(a) + 9], fill=GOLD, outline=DGOLD)
        d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED)
    return img


def sun(d, cx, cy, r, color=GOLD, rays=True):
    if rays:
        for k in range(24):
            a = k * math.pi / 12
            d.line([(cx + r * 1.15 * math.cos(a), cy + r * 1.15 * math.sin(a)),
                    (cx + r * 1.6 * math.cos(a), cy + r * 1.6 * math.sin(a))], fill=color, width=6)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def tree(d, x, base, h, canopy=GREEN):
    d.rectangle([x - h * 0.05, base - h * 0.55, x + h * 0.05, base], fill=BROWN)
    for i, (dx, dy, rr) in enumerate([(0, -0.75, 0.35), (-0.28, -0.55, 0.26), (0.28, -0.55, 0.26), (0, -0.5, 0.3)]):
        cx, cy, r = x + dx * h, base + dy * h, rr * h
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=canopy if i % 2 == 0 else DGREEN)


def lotus(d, cx, cy, s, fill=(240, 120, 150), outline=RED):
    for k in range(-3, 4):
        a = math.pi / 2 + k * 0.32
        px, py = cx + s * 1.6 * math.cos(a), cy - s * 1.6 * math.sin(a)
        d.polygon([(cx, cy), (cx + s * 0.55 * math.cos(a - 0.5), cy - s * 0.55 * math.sin(a - 0.5) - s * 0.5),
                   (px, py), (cx + s * 0.55 * math.cos(a + 0.5), cy - s * 0.55 * math.sin(a + 0.5) - s * 0.5)],
                  fill=fill, outline=outline)
    d.ellipse([cx - s * 0.35, cy - s * 0.35, cx + s * 0.35, cy + s * 0.35], fill=GOLD)


def flame(d, cx, base, h, w):
    for i, (c, f) in enumerate([(RED, 1.0), (SAFF, 0.75), (GOLD, 0.5), (CREAM, 0.25)]):
        hh, ww = h * f, w * f
        pts = []
        for k in range(21):
            t = k / 20
            y = base - hh * t
            xw = ww * math.sin(math.pi * t) * (1 - t * 0.5) + ww * 0.15 * (1 - t)
            pts.append((cx - xw * (1 - t) - ww * 0.05 * math.sin(t * 9), y))
        for k in range(20, -1, -1):
            t = k / 20
            y = base - hh * t
            xw = ww * math.sin(math.pi * t) * (1 - t * 0.5) + ww * 0.15 * (1 - t)
            pts.append((cx + xw * (1 - t) + ww * 0.05 * math.sin(t * 7), y))
        d.polygon(pts, fill=c)


def stars(d, n=120, ymax=H * 0.6):
    for _ in range(n):
        x, y = random.randint(40, W - 40), random.randint(40, int(ymax))
        r = random.choice([1, 1, 2, 2, 3])
        d.ellipse([x - r, y - r, x + r, y + r], fill=WHITE)


def figure(d, cx, base, h, robe=SAFF, skin=(200, 150, 100), seated=False):
    """Simple stylised silhouette figure."""
    if seated:
        d.ellipse([cx - h * 0.45, base - h * 0.35, cx + h * 0.45, base + h * 0.05], fill=robe)
        d.rectangle([cx - h * 0.28, base - h * 0.65, cx + h * 0.28, base - h * 0.2], fill=robe)
        d.ellipse([cx - h * 0.13, base - h * 0.92, cx + h * 0.13, base - h * 0.66], fill=skin)
    else:
        d.polygon([(cx - h * 0.22, base), (cx + h * 0.22, base), (cx + h * 0.16, base - h * 0.62), (cx - h * 0.16, base - h * 0.62)], fill=robe)
        d.ellipse([cx - h * 0.11, base - h * 0.86, cx + h * 0.11, base - h * 0.64], fill=skin)


def bow(d, cx, cy, r, color=DGOLD, arrow=True):
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=color, width=12)
    ax1 = cx + r * math.cos(math.radians(200)); ay1 = cy + r * math.sin(math.radians(200))
    ax2 = cx + r * math.cos(math.radians(340)); ay2 = cy + r * math.sin(math.radians(340))
    d.line([(ax1, ay1), (cx, cy + r * 0.25), (ax2, ay2)], fill=CREAM, width=3)
    if arrow:
        d.line([(cx, cy + r * 0.25), (cx, cy - r * 1.3)], fill=INK, width=6)
        d.polygon([(cx, cy - r * 1.45), (cx - 14, cy - r * 1.2), (cx + 14, cy - r * 1.2)], fill=(170, 170, 180))
        d.polygon([(cx, cy + r * 0.25), (cx - 18, cy + r * 0.45), (cx, cy + r * 0.38), (cx + 18, cy + r * 0.45)], fill=RED)


def save(img, name):
    """Draw the gold border, downsample to the served size, write the final JPEG."""
    out = border(img).resize((OW, OH), Image.LANCZOS).convert("RGB")
    out.save(os.path.join(OUT, f"{name}.jpg"), quality=82, optimize=True, progressive=True)


# 1. Cover — Vyasa dictating under banyan; Ganesha as symbolic Om-lamp; palm-leaf manuscript
def cover():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 205, 130), CREAM, 0, int(H * 0.7)); gradient(d, SAND, (200, 165, 110), int(H * 0.7), H)
    sun(d, W * 0.5, H * 0.33, 150, (240, 190, 90))
    d.rectangle([0, H * 0.7, W, H], fill=(200, 165, 110))
    tree(d, W * 0.2, H * 0.72, 420); tree(d, W * 0.82, H * 0.72, 380)
    # manuscript scroll
    d.rounded_rectangle([W * 0.3, H * 0.52, W * 0.7, H * 0.66], 20, fill=(245, 225, 175), outline=BROWN, width=5)
    for i in range(5):
        y = H * 0.55 + i * 22
        d.line([(W * 0.33, y), (W * 0.67 - random.randint(0, 120), y)], fill=BROWN, width=4)
    # seated sage and scribe
    figure(d, W * 0.36, H * 0.79, 220, robe=SAFF, seated=True)
    figure(d, W * 0.64, H * 0.79, 230, robe=RED, skin=(215, 170, 120), seated=True)
    # lamp between
    d.polygon([(W * 0.48, H * 0.79), (W * 0.52, H * 0.79), (W * 0.51, H * 0.74), (W * 0.49, H * 0.74)], fill=DGOLD)
    flame(d, W * 0.5, H * 0.74, 60, 22)
    for x in [W * 0.12, W * 0.88]:
        lotus(d, x, H * 0.9, 40)
    save(img, "03_vyasa_ganapati")


# 2. Sarpa yagna — great fire altar with serpents drawn into it
def sarpa():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, NIGHT, (90, 40, 40)); stars(d)
    d.rectangle([0, H * 0.78, W, H], fill=(60, 40, 35))
    # altar
    d.rectangle([W * 0.35, H * 0.62, W * 0.65, H * 0.78], fill=(120, 90, 70), outline=INK, width=4)
    d.rectangle([W * 0.3, H * 0.74, W * 0.7, H * 0.78], fill=(140, 105, 80), outline=INK, width=3)
    flame(d, W * 0.5, H * 0.62, 400, 150)
    flame(d, W * 0.44, H * 0.62, 280, 90); flame(d, W * 0.56, H * 0.62, 300, 95)
    # serpents spiralling in
    for k, (sx, sy, dirn) in enumerate([(W * 0.08, H * 0.2, 1), (W * 0.92, H * 0.15, -1), (W * 0.1, H * 0.5, 1), (W * 0.9, H * 0.45, -1)]):
        pts = []
        for i in range(40):
            t = i / 39
            x = sx + (W * 0.5 - sx) * t
            y = sy + (H * 0.55 - sy) * t + 40 * math.sin(t * 12)
            pts.append((x, y))
        d.line(pts, fill=(60, 140, 90) if k % 2 else (150, 120, 60), width=14 - int(8 * (k % 2)) + 6)
        hx, hy = pts[0]
        d.ellipse([hx - 20, hy - 14, hx + 20, hy + 14], fill=(60, 140, 90) if k % 2 else (150, 120, 60))
        d.ellipse([hx - 4 + 8 * dirn, hy - 6, hx + 4 + 8 * dirn, hy - 2], fill=RED)
    # priests
    for x in [W * 0.2, W * 0.8]:
        figure(d, x, H * 0.78, 200, robe=CREAM, seated=True)
    save(img, "13_sarpa_yagna")


# 3. Ganga & Shantanu — moonlit river with royal figure on the bank
def ganga():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, NIGHT, DUSK, 0, int(H * 0.5)); stars(d, 90, H * 0.45)
    d.ellipse([W * 0.7 - 70, H * 0.15 - 70, W * 0.7 + 70, H * 0.15 + 70], fill=(245, 240, 210))
    gradient(d, WATER, WATER2, int(H * 0.5), H)
    for i in range(30):
        y = H * 0.55 + i * 12 + random.randint(0, 8)
        x0 = random.randint(0, W // 2)
        d.line([(x0, y), (x0 + random.randint(80, 300), y)], fill=(160, 200, 230), width=2)
    # distant far bank
    d.polygon([(0, H * 0.5), (W * 0.3, H * 0.44), (W * 0.6, H * 0.47), (W, H * 0.42), (W, H * 0.52), (0, H * 0.52)], fill=DGREEN)
    # near bank
    d.polygon([(0, H), (0, H * 0.82), (W * 0.42, H * 0.78), (W * 0.5, H)], fill=(50, 70, 45))
    tree(d, W * 0.12, H * 0.82, 300, (50, 110, 70))
    figure(d, W * 0.36, H * 0.8, 240, robe=(200, 60, 60))
    d.ellipse([W * 0.36 - 30, H * 0.8 - 240 * 0.9 - 30, W * 0.36 + 30, H * 0.8 - 240 * 0.9 + 6], outline=GOLD, width=5)
    # river goddess as luminous form on the water
    gx, gy = W * 0.72, H * 0.72
    for r, a in [(140, 30), (110, 70), (80, 130)]:
        d.ellipse([gx - r, gy - r * 0.6, gx + r, gy + r * 0.6], fill=(160 + a // 3, 200 + a // 4, 240))
    figure(d, gx, gy + 40, 220, robe=WHITE, skin=(225, 200, 180))
    lotus(d, gx - 190, gy + 60, 34); lotus(d, gx + 200, gy + 70, 30)
    save(img, "23_ganga_shantanu")


# 4. Bhishma's vow — lone warrior raising bow to the sky, flowers falling
def bhishma():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 170, 90), (255, 220, 160), 0, int(H * 0.72)); sun(d, W * 0.5, H * 0.3, 130, (255, 210, 110))
    gradient(d, (200, 165, 110), SAND, int(H * 0.72), H)
    # chariot silhouette hint: wheel
    d.ellipse([W * 0.7, H * 0.55, W * 0.7 + 200, H * 0.55 + 200], outline=INK, width=10)
    for k in range(8):
        a = k * math.pi / 4
        d.line([(W * 0.7 + 100, H * 0.55 + 100), (W * 0.7 + 100 + 95 * math.cos(a), H * 0.55 + 100 + 95 * math.sin(a))], fill=INK, width=6)
    figure(d, W * 0.35, H * 0.74, 330, robe=(210, 200, 190), skin=(190, 140, 95))
    bow(d, W * 0.35, H * 0.44, 110, DGOLD, arrow=False)
    d.line([(W * 0.35, H * 0.56), (W * 0.35, H * 0.74 - 330 * 0.55)], fill=(190, 140, 95), width=18)
    # falling flowers
    for _ in range(60):
        x, y = random.randint(60, W - 60), random.randint(60, int(H * 0.7))
        c = random.choice([(255, 180, 190), (255, 230, 120), (250, 250, 250)])
        d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=c)
    save(img, "24_bhishma_pratigna")


# 5. Birth of the Pandavas — forest ashram, five stars, mountains
def pandava_birth():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (30, 40, 90), (150, 120, 170), 0, int(H * 0.6)); stars(d, 60, H * 0.35)
    # five bright stars
    for i, x in enumerate([0.25, 0.37, 0.5, 0.63, 0.75]):
        cx, cy = W * x, H * (0.14 + 0.05 * math.sin(i * 1.3))
        for k in range(8):
            a = k * math.pi / 4
            d.line([(cx, cy), (cx + 34 * math.cos(a), cy + 34 * math.sin(a))], fill=(255, 240, 180), width=4)
        d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=WHITE)
    # mountains
    d.polygon([(0, H * 0.6), (W * 0.2, H * 0.3), (W * 0.35, H * 0.5), (W * 0.55, H * 0.25), (W * 0.75, H * 0.48), (W * 0.9, H * 0.35), (W, H * 0.55), (W, H * 0.6)], fill=(90, 80, 120))
    d.polygon([(W * 0.55, H * 0.25), (W * 0.5, H * 0.34), (W * 0.6, H * 0.34)], fill=WHITE)
    gradient(d, DGREEN, GREEN, int(H * 0.6), H)
    for x in [0.08, 0.9]:
        tree(d, W * x, H * 0.72, 330)
    # hut
    d.polygon([(W * 0.38, H * 0.66), (W * 0.5, H * 0.5), (W * 0.62, H * 0.66)], fill=(160, 120, 70))
    d.rectangle([W * 0.41, H * 0.66, W * 0.59, H * 0.8], fill=(200, 170, 120), outline=BROWN, width=4)
    d.rectangle([W * 0.47, H * 0.7, W * 0.53, H * 0.8], fill=(80, 55, 35))
    # mother figure and child cradle
    figure(d, W * 0.3, H * 0.82, 230, robe=(200, 80, 90), skin=(215, 170, 120))
    d.ellipse([W * 0.66, H * 0.76, W * 0.66 + 120, H * 0.76 + 50], fill=(230, 200, 150), outline=BROWN, width=4)
    lotus(d, W * 0.2, H * 0.92, 30); lotus(d, W * 0.8, H * 0.93, 30)
    save(img, "29_pandava_janana")


# 6. Gurukulam — archery training, target on tree, teacher & pupils
def gurukulam():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, SKYB, (215, 235, 245), 0, int(H * 0.65)); sun(d, W * 0.85, H * 0.15, 70, (255, 230, 150))
    gradient(d, (110, 150, 80), (150, 180, 100), int(H * 0.65), H)
    tree(d, W * 0.8, H * 0.7, 420)
    # bird target
    d.ellipse([W * 0.8 - 40, H * 0.7 - 420 * 0.75 - 22, W * 0.8 + 40, H * 0.7 - 420 * 0.75 + 22], fill=(220, 220, 230), outline=INK, width=3)
    d.polygon([(W * 0.8 + 40, H * 0.7 - 420 * 0.75), (W * 0.8 + 70, H * 0.7 - 420 * 0.75 - 6), (W * 0.8 + 70, H * 0.7 - 420 * 0.75 + 6)], fill=SAFF)
    # teacher
    figure(d, W * 0.15, H * 0.72, 300, robe=CREAM, skin=(190, 140, 95))
    # pupils with bows
    for i, x in enumerate([0.3, 0.42, 0.54]):
        figure(d, W * x, H * 0.76, 230, robe=[SAFF, (60, 90, 170), (200, 60, 60)][i])
        bow(d, W * x + 40, H * 0.62, 55, DGOLD, arrow=(i == 1))
    # arrow in flight to target
    d.line([(W * 0.46, H * 0.55), (W * 0.76, H * 0.7 - 420 * 0.75)], fill=INK, width=5)
    save(img, "27_gurukulam")


# 7. Lakshagriha — palace burning at night, tunnel escape
def lakshagriha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, NIGHT, (110, 40, 30)); stars(d, 50, H * 0.3)
    d.rectangle([0, H * 0.78, W, H], fill=(45, 35, 35))
    # palace
    d.rectangle([W * 0.3, H * 0.45, W * 0.7, H * 0.78], fill=(120, 80, 60), outline=INK, width=4)
    d.polygon([(W * 0.28, H * 0.45), (W * 0.5, H * 0.3), (W * 0.72, H * 0.45)], fill=(90, 55, 45), outline=INK)
    for i in range(3):
        x = W * (0.36 + i * 0.12)
        d.rounded_rectangle([x, H * 0.55, x + 70, H * 0.7], 30, fill=(255, 150, 40))
    for cx, h, w in [(W * 0.36, 330, 100), (W * 0.5, 460, 150), (W * 0.64, 340, 110), (W * 0.43, 250, 80), (W * 0.57, 270, 85)]:
        flame(d, cx, H * 0.45, h, w)
    # smoke
    for _ in range(25):
        x, y, r = random.randint(int(W * 0.25), int(W * 0.75)), random.randint(40, int(H * 0.3)), random.randint(25, 60)
        d.ellipse([x - r, y - r, x + r, y + r], fill=SMOKE)
    # tunnel
    d.arc([W * 0.55, H * 0.78, W * 0.95, H * 1.1], 180, 360, fill=(30, 25, 25), width=60)
    for i, x in enumerate([0.86, 0.9, 0.94]):
        figure(d, W * x, H * 0.95 - i * 8, 140, robe=[SAFF, RED, (60, 90, 170)][i])
    save(img, "36_lakshagriha")


# 8. Draupadi swayamvara — revolving fish target above water pool, bow drawn
def swayamvara():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 235, 200), (245, 215, 170), 0, int(H * 0.7))
    # pillars & canopy
    for x in [0.06, 0.94]:
        d.rectangle([W * x - 30, H * 0.15, W * x + 30, H * 0.78], fill=(200, 160, 110), outline=DGOLD, width=4)
    d.rectangle([0, H * 0.1, W, H * 0.16], fill=RED)
    for i in range(18):
        d.polygon([(i * W / 18, H * 0.16), ((i + 1) * W / 18, H * 0.16), ((i + 0.5) * W / 18, H * 0.21)], fill=GOLD)
    # wheel with fish
    wx, wy = W * 0.5, H * 0.3
    d.ellipse([wx - 110, wy - 110, wx + 110, wy + 110], outline=DGOLD, width=12)
    for k in range(8):
        a = k * math.pi / 4
        d.line([(wx, wy), (wx + 105 * math.cos(a), wy + 105 * math.sin(a))], fill=DGOLD, width=5)
    d.polygon([(wx - 60, wy), (wx - 10, wy - 30), (wx + 40, wy - 10), (wx + 70, wy - 30), (wx + 70, wy + 30), (wx + 40, wy + 10), (wx - 10, wy + 30)], fill=(230, 180, 60), outline=INK)
    d.ellipse([wx - 45, wy - 8, wx - 35, wy + 2], fill=INK)
    # pool
    d.ellipse([W * 0.3, H * 0.62, W * 0.7, H * 0.8], fill=WATER2, outline=(60, 110, 150), width=6)
    d.ellipse([wx - 60, H * 0.685, wx + 60, H * 0.735], fill=(200, 220, 240))
    # archer
    figure(d, W * 0.22, H * 0.78, 330, robe=(60, 90, 170), skin=(190, 140, 95))
    bow(d, W * 0.24, H * 0.5, 120, DGOLD, arrow=True)
    # court spectators
    for i, x in enumerate([0.72, 0.8, 0.88]):
        figure(d, W * x, H * 0.76, 200, robe=[GOLD, (200, 60, 60), (120, 60, 140)][i])
    # Draupadi with garland
    figure(d, W * 0.62, H * 0.78, 250, robe=(180, 30, 60), skin=(215, 170, 120))
    d.arc([W * 0.62 - 60, H * 0.6, W * 0.62 + 60, H * 0.72], 0, 180, fill=(255, 180, 60), width=14)
    d.rectangle([0, H * 0.78, W, H], fill=(215, 185, 140))
    save(img, "45_swayamvara")


# 9. Khandava dahana — forest fire, chariot, rain deflected, Maya sabha silhouette
def khandava():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (60, 50, 90), (200, 90, 50), 0, int(H * 0.55))
    # rain streaks
    for _ in range(200):
        x, y = random.randint(0, W), random.randint(0, int(H * 0.35))
        d.line([(x, y), (x - 6, y + 30)], fill=(150, 170, 210), width=2)
    # arrow canopy shield arc
    d.arc([W * 0.05, H * 0.2, W * 0.95, H * 1.3], 190, 350, fill=GOLD, width=10)
    for k in range(20):
        a = math.radians(190 + k * 8)
        cx, cy = W * 0.5 + W * 0.45 * math.cos(a), H * 0.75 + H * 0.55 * math.sin(a)
        d.line([(cx, cy), (cx + 22 * math.cos(a), cy + 22 * math.sin(a))], fill=INK, width=4)
    gradient(d, (80, 40, 30), (40, 25, 20), int(H * 0.55), H)
    # burning trees
    for x in [0.08, 0.2, 0.32, 0.68, 0.8, 0.92]:
        tree(d, W * x, H * 0.75, 260, (70, 60, 40))
        flame(d, W * x, H * 0.75 - 260 * 0.5, 240, 70)
    # chariot in centre
    d.rectangle([W * 0.42, H * 0.6, W * 0.58, H * 0.7], fill=RED, outline=DGOLD, width=4)
    for wx in [W * 0.44, W * 0.56]:
        d.ellipse([wx - 40, H * 0.66, wx + 40, H * 0.66 + 80], outline=INK, width=8)
    figure(d, W * 0.47, H * 0.62, 190, robe=(60, 90, 170))
    figure(d, W * 0.53, H * 0.62, 190, robe=(30, 60, 140), skin=(90, 120, 200))
    bow(d, W * 0.47 + 30, H * 0.45, 60, DGOLD)
    save(img, "56_khandava")


# 1. Nannaya at Rajamahendravaram — the king's request, the Telugu link in the chain
def nannaya():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 212, 140), (238, 216, 172), 0, int(H * 0.70))
    d.rectangle([0, H * 0.70, W, H], fill=(178, 140, 96))
    sun(d, W * 0.50, H * 0.17, 96, (244, 200, 100))
    # the hall: two pillars framing the meeting
    for x in [0.10, 0.90]:
        d.rectangle([W * x - 30, H * 0.20, W * x + 30, H * 0.70], fill=(158, 124, 86), outline=INK, width=3)
        d.rectangle([W * x - 44, H * 0.16, W * x + 44, H * 0.22], fill=GOLD, outline=DGOLD, width=3)
    # the king, on a low seat, asking
    d.rectangle([W * 0.20, H * 0.60, W * 0.34, H * 0.78], fill=MAROON, outline=DGOLD, width=4)
    figure(d, W * 0.27, H * 0.74, 250, robe=RED, skin=(205, 155, 105), seated=True)
    d.polygon([(W * 0.245, H * 0.615), (W * 0.27, H * 0.575), (W * 0.295, H * 0.615)], fill=GOLD, outline=DGOLD)
    # the poet, seated with palm leaf and stylus
    figure(d, W * 0.72, H * 0.74, 250, robe=CREAM, skin=(200, 150, 100), seated=True)
    d.rounded_rectangle([W * 0.60, H * 0.655, W * 0.84, H * 0.715], 10,
                        fill=(246, 230, 182), outline=BROWN, width=4)
    for k in range(3):
        d.line([(W * 0.625, H * 0.668 + k * 18), (W * 0.815 - random.randint(0, 60), H * 0.668 + k * 18)],
               fill=(140, 105, 60), width=3)
    d.line([(W * 0.865, H * 0.70), (W * 0.905, H * 0.63)], fill=INK, width=7)
    # the lamp between them — the work about to begin
    d.polygon([(W * 0.485, H * 0.78), (W * 0.515, H * 0.78), (W * 0.508, H * 0.735), (W * 0.492, H * 0.735)], fill=DGOLD)
    flame(d, W * 0.50, H * 0.735, 120, 42)
    for x in [W * 0.06, W * 0.94]:
        lotus(d, x, H * 0.90, 38)
    save(img, "01_nannaya")


# 5. Sarama — the pup at the sacrifice, and the first curse in the epic
def sarama():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (60, 46, 86), (150, 96, 70))
    d.rectangle([0, H * 0.74, W, H], fill=(122, 88, 66))
    # the sacrificial enclosure
    for x in [0.16, 0.84]:
        d.rectangle([W * x - 22, H * 0.26, W * x + 22, H * 0.74], fill=(152, 118, 82), outline=INK, width=3)
    d.rectangle([W * 0.40, H * 0.56, W * 0.60, H * 0.74], fill=(128, 94, 70), outline=INK, width=4)
    flame(d, W * 0.50, H * 0.56, 260, 92)
    # the king's brothers, turned toward the pup
    figure(d, W * 0.28, H * 0.86, 235, robe=(150, 45, 40), skin=(205, 155, 105))
    figure(d, W * 0.38, H * 0.87, 225, robe=(120, 60, 110), skin=(205, 155, 105))
    # the pup, small, alone, between them and the fire
    px, py = W * 0.62, H * 0.855
    d.ellipse([px - 62, py - 34, px + 46, py + 26], fill=(226, 214, 196))
    d.ellipse([px + 30, py - 62, px + 92, py - 4], fill=(226, 214, 196))
    d.polygon([(px + 40, py - 58), (px + 32, py - 96), (px + 62, py - 70)], fill=(196, 182, 162))
    d.polygon([(px + 74, py - 60), (px + 88, py - 96), (px + 92, py - 58)], fill=(196, 182, 162))
    d.ellipse([px + 62, py - 42, px + 76, py - 28], fill=INK)
    d.ellipse([px + 84, py - 26, px + 96, py - 14], fill=(90, 70, 60))
    d.line([(px - 58, py - 24), (px - 96, py - 62)], fill=(226, 214, 196), width=13)
    # the mother, standing apart, luminous — the curse about to be spoken
    d.ellipse([W * 0.90 - 92, H * 0.50 - 92, W * 0.90 + 92, H * 0.50 + 92], fill=(60, 46, 86))
    sun(d, W * 0.90, H * 0.50, 46, (238, 232, 224), rays=True)
    save(img, "05_sarama")


# ---------------------------------------------------------------------------
# Batch five — the grudge repaid, the lac house, the forest.
# ---------------------------------------------------------------------------

# 34. Drupada bound — the answer twenty years in the writing
def drupada_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (234, 202, 150), (198, 164, 122), 0, int(H * 0.70))
    d.rectangle([0, H * 0.70, W, H], fill=(152, 118, 84))
    for x in [0.05, 0.95]:
        d.rectangle([W * x - 26, H * 0.18, W * x + 26, H * 0.70], fill=(148, 116, 80), outline=INK, width=3)
    # the teacher, standing, hands empty
    figure(d, W * 0.26, H * 0.90, 330, robe=CREAM, skin=(198, 148, 98))
    d.polygon([(W * 0.26 - 32, H * 0.665), (W * 0.26 + 32, H * 0.665), (W * 0.26, H * 0.745)], fill=(226, 222, 214))
    # the king, on his knees, bound
    kx = W * 0.62
    d.polygon([(kx - 76, H * 0.92), (kx + 76, H * 0.92), (kx + 46, H * 0.66), (kx - 46, H * 0.66)], fill=(120, 60, 110))
    d.ellipse([kx - 30, H * 0.595, kx + 30, H * 0.665], fill=(200, 150, 100))
    for k in range(3):   # the ropes
        d.line([(kx - 84, H * (0.72 + k * 0.045)), (kx + 84, H * (0.72 + k * 0.045))], fill=(214, 198, 160), width=9)
    # the student who brought him, bow lowered
    figure(d, W * 0.86, H * 0.90, 300, robe=(60, 96, 160), skin=(206, 156, 106))
    d.arc([W * 0.90, H * 0.60, W * 1.00, H * 0.86], 250, 470, fill=DGOLD, width=11)
    # the kingdom, split in two
    d.line([(0, H * 0.10), (W, H * 0.10)], fill=DGOLD, width=6)
    d.line([(W * 0.5, H * 0.04), (W * 0.5, H * 0.16)], fill=MADDER if False else (150, 45, 40), width=8)
    save(img, "34_drupada")


# 35. The yuvaraja's crown, and the son watching from the side
def yuvaraja():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (248, 208, 138), (234, 210, 166), 0, int(H * 0.70))
    d.rectangle([0, H * 0.70, W, H], fill=(170, 132, 92))
    sun(d, W * 0.34, H * 0.17, 96, (246, 200, 100))
    for x in [0.04, 0.96]:
        d.rectangle([W * x - 26, H * 0.20, W * x + 26, H * 0.70], fill=(152, 120, 84), outline=INK, width=3)
    # the ceremony, lit
    d.rectangle([W * 0.24, H * 0.56, W * 0.44, H * 0.78], fill=MAROON, outline=DGOLD, width=5)
    figure(d, W * 0.34, H * 0.74, 265, robe=CREAM, skin=(206, 156, 106), seated=True)
    cx, cy = W * 0.34, H * 0.545
    d.polygon([(cx - 44, cy + 18), (cx - 36, cy - 20), (cx - 15, cy - 2), (cx, cy - 30),
               (cx + 15, cy - 2), (cx + 36, cy - 20), (cx + 44, cy + 18)], fill=GOLD, outline=DGOLD)
    for x in [0.13, 0.52]:
        figure(d, W * x, H * 0.90, 205, robe=CREAM, skin=(198, 148, 98), seated=True)
    # him, apart, in shadow, arms down
    d.polygon([(W * 0.70, 0), (W, 0), (W, H), (W * 0.70, H)], fill=(72, 56, 62))
    figure(d, W * 0.84, H * 0.90, 320, robe=(96, 40, 44), skin=(190, 140, 92))
    # the uncle beside him, half-lit
    figure(d, W * 0.955, H * 0.92, 250, robe=(60, 48, 66), skin=(180, 132, 88))
    save(img, "35_yuvaraja")


# 37. The tunnel — six carried out, six left behind
def escape_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (40, 26, 30), (128, 52, 30))
    # the house burning, upper right
    d.rectangle([W * 0.56, H * 0.10, W, H * 0.52], fill=(46, 30, 30))
    d.polygon([(W * 0.60, H * 0.30), (W * 0.78, H * 0.10), (W * 0.96, H * 0.30)], fill=(96, 62, 44))
    d.rectangle([W * 0.63, H * 0.30, W * 0.93, H * 0.52], fill=(112, 72, 48), outline=INK, width=4)
    for k, x in enumerate([0.66, 0.72, 0.78, 0.84, 0.90]):
        flame(d, W * x, H * 0.52, 220 + (k % 3) * 60, 62)
    for _ in range(70):
        sx, sy = random.uniform(W * 0.56, W), random.uniform(0, H * 0.42)
        r = random.choice([2, 3, 4])
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(250, 190, 90))
    # the earth, and the tunnel mouth at lower left
    d.rectangle([0, H * 0.56, W, H], fill=(58, 42, 34))
    d.ellipse([W * 0.30 - 150, H * 0.56 - 62, W * 0.30 + 150, H * 0.56 + 62], fill=(28, 20, 18))
    # him, out of the mouth, carrying all five
    bx = W * 0.20
    d.polygon([(bx - 96, H), (bx + 96, H), (bx + 60, H * 0.66), (bx - 60, H * 0.66)], fill=(52, 92, 62))
    d.ellipse([bx - 40, H * 0.585, bx + 40, H * 0.675], fill=(200, 150, 100))
    figure(d, bx, H * 0.60, 150, robe=(150, 45, 40), skin=(210, 160, 110))          # mother, on his shoulder
    for dx, robe in [(-108, CREAM), (108, (60, 96, 160))]:
        figure(d, bx + dx, H * 0.74, 128, robe=robe, skin=(206, 156, 106))
    for dx in (-176, 176):
        figure(d, bx + dx, H * 0.90, 112, robe=GOLD, skin=(206, 156, 106))
    save(img, "37_escape")


# 38. Hidimbi — the one who stood against her own house
def hidimbi_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (26, 30, 62), (58, 80, 62))
    stars(d, 110, H * 0.5)
    d.ellipse([W * 0.16 - 66, H * 0.14 - 66, W * 0.16 + 66, H * 0.14 + 66], fill=(240, 236, 214))
    d.rectangle([0, H * 0.68, W, H], fill=(38, 62, 46))
    for x, hh in [(0.05, 470), (0.17, 380), (0.93, 460)]:
        tree(d, W * x, H * 0.74, hh, canopy=(30, 58, 42))
    # the sleepers under the tree
    for k, x in enumerate([0.34, 0.44, 0.54, 0.64, 0.74]):
        d.ellipse([W * x - 66, H * 0.90 - 20, W * x + 66, H * 0.90 + 20], fill=(206, 176, 130))
        d.ellipse([W * x - 76, H * 0.90 - 26, W * x - 44, H * 0.90 + 6], fill=(200, 150, 100))
    # him, awake, keeping watch
    figure(d, W * 0.30, H * 0.86, 250, robe=(52, 92, 62), skin=(206, 156, 106), seated=True)
    # her, behind the trunk, half-stepped-out
    hx = W * 0.86
    d.rectangle([hx - 34, H * 0.44, hx + 34, H * 0.78], fill=BROWN)   # the trunk she stands behind
    d.polygon([(hx + 26, H * 0.94), (hx + 116, H * 0.94), (hx + 92, H * 0.56), (hx + 40, H * 0.56)],
              fill=(176, 66, 104))
    d.ellipse([hx + 44, H * 0.485, hx + 96, H * 0.565], fill=(198, 148, 98))
    d.chord([hx + 40, H * 0.475, hx + 100, H * 0.575], 180, 360, fill=(34, 26, 26))
    save(img, "38_hidimbi")


# 39. Bakasura — the cartload, and the man who ate it
def bakasura_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (206, 224, 180), (150, 176, 118), 0, int(H * 0.58))
    d.rectangle([0, H * 0.58, W, H], fill=(126, 152, 96))
    for x, hh in [(0.04, 440), (0.96, 430)]:
        tree(d, W * x, H * 0.64, hh)
    # the cart of rice
    cx, cy = W * 0.34, H * 0.74
    d.rectangle([cx - 190, cy - 60, cx + 190, cy + 40], fill=(140, 100, 60), outline=INK, width=5)
    for k in range(5):
        d.ellipse([cx - 150 + k * 74 - 34, cy - 104, cx - 150 + k * 74 + 34, cy - 44], fill=(246, 242, 228))
    for wx in [cx - 130, cx + 130]:
        d.ellipse([wx - 56, cy + 26, wx + 56, cy + 138], outline=INK, width=9)
    # him, seated at the cart, eating
    figure(d, cx + 250, H * 0.90, 290, robe=(52, 92, 62), skin=(206, 156, 106), seated=True)
    # the demon, arriving, huge
    bx = W * 0.80
    d.polygon([(bx - 130, H * 0.96), (bx + 130, H * 0.96), (bx + 82, H * 0.40), (bx - 82, H * 0.40)],
              fill=(84, 62, 66))
    d.ellipse([bx - 62, H * 0.30, bx + 62, H * 0.43], fill=(112, 84, 84))
    for ex in (bx - 30, bx + 30):
        d.ellipse([ex - 14, H * 0.345, ex + 14, H * 0.375], fill=(230, 90, 60))
    d.polygon([(bx - 40, H * 0.405), (bx + 40, H * 0.405), (bx, H * 0.435)], fill=(40, 30, 30))
    d.line([(bx - 82, H * 0.56), (bx - 190, H * 0.46)], fill=(84, 62, 66), width=26)
    save(img, "39_bakasura")


# ---------------------------------------------------------------------------
# Batch four — the births, the teachers, and the day Karna walked in.
# ---------------------------------------------------------------------------

# 27. Karna set adrift — the mother left standing on the bank
def karna_janana():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (248, 196, 124), (240, 214, 168), 0, int(H * 0.50))
    sun(d, W * 0.22, H * 0.20, 96, (250, 206, 108))
    gradient(d, (96, 140, 176), (44, 88, 134), int(H * 0.50), H)
    for i in range(8):
        y = H * (0.54 + i * 0.055)
        d.arc([W * 0.02, y, W * 0.98, y + H * 0.09], 190, 350, fill=(130, 176, 206), width=5)
    d.polygon([(0, H * 0.50), (W * 0.30, H * 0.50), (W * 0.22, H), (0, H)], fill=(168, 148, 108))
    # the basket, already out on the water, with a small light in it
    bx, by = W * 0.66, H * 0.72
    d.rounded_rectangle([bx - 86, by - 34, bx + 86, by + 40], 12, fill=(160, 118, 68), outline=INK, width=5)
    d.rounded_rectangle([bx - 96, by - 46, bx + 96, by - 26], 8, fill=(186, 142, 86), outline=INK, width=4)
    sun(d, bx, by - 66, 30, (252, 224, 140))
    # her, on the bank, watching it go
    figure(d, W * 0.13, H * 0.86, 300, robe=(196, 84, 118), skin=(210, 160, 110))
    d.line([(W * 0.165, H * 0.66), (W * 0.27, H * 0.62)], fill=(210, 160, 110), width=15)
    save(img, "27_karna_janana")


# 28. Pandu — the arrow loosed at the wrong moment
def pandu_shapam():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (198, 220, 176), (146, 176, 116), 0, int(H * 0.56))
    d.rectangle([0, H * 0.56, W, H], fill=(122, 152, 96))
    for x, hh in [(0.05, 440), (0.17, 350), (0.90, 430), (0.99, 340)]:
        tree(d, W * x, H * 0.62, hh)
    # the two deer, the struck one down
    dx, dy = W * 0.68, H * 0.80
    d.ellipse([dx - 130, dy - 46, dx + 70, dy + 34], fill=(178, 128, 74))
    d.ellipse([dx + 46, dy - 96, dx + 138, dy - 16], fill=(178, 128, 74))
    for hx, hy in [(dx + 66, dy - 92), (dx + 112, dy - 92)]:
        d.line([(hx, hy), (hx - 14, hy - 62)], fill=(120, 88, 52), width=8)
        d.line([(hx - 14, hy - 62), (hx - 40, hy - 84)], fill=(120, 88, 52), width=6)
        d.line([(hx - 14, hy - 62), (hx + 8, hy - 92)], fill=(120, 88, 52), width=6)
    d.ellipse([dx + 96, dy - 70, dx + 116, dy - 50], fill=INK)
    # the arrow in its side
    d.line([(dx - 30, dy - 20), (dx - 150, dy - 96)], fill=(96, 70, 44), width=7)
    d.polygon([(dx - 26, dy - 18), (dx - 58, dy - 26), (dx - 48, dy - 46)], fill=(180, 180, 190))
    d.ellipse([dx - 44, dy - 8, dx - 16, dy + 12], fill=(150, 40, 36))
    # the king, bow lowered
    figure(d, W * 0.24, H * 0.90, 310, robe=(60, 96, 160), skin=(206, 156, 106))
    d.arc([W * 0.30, H * 0.60, W * 0.40, H * 0.86], 250, 470, fill=DGOLD, width=12)
    save(img, "28_pandu_shapam")


# 30. Gandhari — the hundred and one jars
def kaurava_janana():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (58, 46, 84), (146, 106, 88))
    d.rectangle([0, H * 0.74, W, H], fill=(118, 90, 70))
    for x in [0.05, 0.95]:
        d.rectangle([W * x - 24, H * 0.16, W * x + 24, H * 0.74], fill=(148, 116, 80), outline=INK, width=3)
    # rows of jars
    for row, (y, n, sc) in enumerate([(0.50, 9, 0.72), (0.62, 8, 0.86), (0.75, 7, 1.0)]):
        for k in range(n):
            jx = W * (0.5 + (k - (n - 1) / 2) * 0.105 * sc)
            jy = H * y
            rr = 46 * sc
            d.ellipse([jx - rr, jy - rr * 0.9, jx + rr, jy + rr * 1.15], fill=(168, 128, 82), outline=INK, width=3)
            d.ellipse([jx - rr * 0.62, jy - rr * 1.25, jx + rr * 0.62, jy - rr * 0.72], fill=(196, 154, 96), outline=INK, width=3)
            flame(d, jx, jy - rr * 1.05, 34 * sc, 13 * sc)
    # the blindfolded mother
    figure(d, W * 0.14, H * 0.92, 280, robe=(150, 45, 40), skin=(210, 160, 110))
    d.rectangle([W * 0.14 - 40, H * 0.665, W * 0.14 + 40, H * 0.695], fill=CREAM, outline=INK, width=3)
    # the father, who cannot see either
    figure(d, W * 0.87, H * 0.92, 280, robe=(92, 72, 142), skin=(200, 150, 100))
    for ex in (W * 0.87 - 16, W * 0.87 + 16):
        d.line([(ex - 9, H * 0.678), (ex + 9, H * 0.678)], fill=INK, width=3)
    save(img, "30_kaurava_janana")


# 31. Drona — turned away in the court of a friend
def drona_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (236, 206, 156), (200, 166, 124), 0, int(H * 0.72))
    d.rectangle([0, H * 0.72, W, H], fill=(156, 122, 86))
    for x in [0.06, 0.94]:
        d.rectangle([W * x - 28, H * 0.18, W * x + 28, H * 0.72], fill=(150, 118, 82), outline=INK, width=3)
        d.rectangle([W * x - 42, H * 0.14, W * x + 42, H * 0.20], fill=GOLD, outline=DGOLD, width=3)
    # the throne, raised high
    d.rectangle([W * 0.68, H * 0.44, W * 0.88, H * 0.74], fill=MAROON, outline=DGOLD, width=5)
    d.rectangle([W * 0.64, H * 0.70, W * 0.92, H * 0.76], fill=(140, 106, 74), outline=INK, width=3)
    d.polygon([(W * 0.68, H * 0.44), (W * 0.78, H * 0.30), (W * 0.88, H * 0.44)], fill=GOLD, outline=DGOLD)
    figure(d, W * 0.78, H * 0.64, 250, robe=RED, skin=(205, 155, 105), seated=True)
    # the courtiers, amused
    for x in [0.55, 0.62]:
        figure(d, W * x, H * 0.88, 190, robe=CREAM, skin=(198, 148, 98), seated=True)
    # him, standing below, thin, holding nothing
    figure(d, W * 0.24, H * 0.90, 320, robe=CREAM, skin=(198, 148, 98))
    d.polygon([(W * 0.24 - 32, H * 0.665), (W * 0.24 + 32, H * 0.665), (W * 0.24, H * 0.745)], fill=(74, 58, 44))
    # the boy at his side
    figure(d, W * 0.35, H * 0.92, 175, robe=(206, 176, 130), skin=(206, 156, 106))
    save(img, "31_drona")


# 32. Ekalavya — the clay teacher, and what was asked of him
def ekalavya_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (204, 224, 180), (150, 178, 118), 0, int(H * 0.58))
    d.rectangle([0, H * 0.58, W, H], fill=(126, 154, 98))
    for x, hh in [(0.04, 450), (0.15, 360), (0.95, 440)]:
        tree(d, W * x, H * 0.64, hh)
    # the clay image on its mound
    mx, my = W * 0.74, H * 0.74
    d.ellipse([mx - 150, my - 20, mx + 150, my + 66], fill=(140, 112, 76))
    d.polygon([(mx - 62, my - 16), (mx + 62, my - 16), (mx + 40, my - 210), (mx - 40, my - 210)], fill=(158, 122, 82))
    d.ellipse([mx - 46, my - 292, mx + 46, my - 196], fill=(158, 122, 82))
    d.polygon([(mx - 36, my - 210), (mx + 36, my - 210), (mx, my - 130)], fill=(132, 100, 66))
    for k in range(7):
        a = math.radians(196 + k * 24)
        d.line([(mx, my - 258), (mx + 78 * math.cos(a), my - 258 + 78 * math.sin(a))], fill=(132, 100, 66), width=9)
    # him, kneeling, right hand held out
    figure(d, W * 0.28, H * 0.92, 320, robe=(150, 118, 70), skin=(160, 110, 72))
    d.line([(W * 0.315, H * 0.70), (W * 0.44, H * 0.74)], fill=(160, 110, 72), width=17)
    d.ellipse([W * 0.44 - 22, H * 0.74 - 20, W * 0.44 + 22, H * 0.74 + 20], fill=(160, 110, 72))
    # the bow, set down
    d.arc([W * 0.14, H * 0.74, W * 0.24, H * 0.98], 250, 470, fill=DGOLD, width=11)
    save(img, "32_ekalavya")


# 33. The arena — a stranger at the gate
def ranga_bhumi():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 208, 132), (236, 214, 172), 0, int(H * 0.60))
    sun(d, W * 0.80, H * 0.20, 116, (250, 200, 96))
    d.rectangle([0, H * 0.60, W, H], fill=(196, 168, 118))
    # the tiers of the crowd
    for row, y in enumerate([0.60, 0.545, 0.49]):
        d.rectangle([0, H * y, W, H * (y + 0.055)], fill=(150 - row * 12, 120 - row * 10, 96 - row * 8))
        for k in range(22):
            hx = W * (0.02 + k * 0.045)
            d.ellipse([hx - 13, H * y - 24, hx + 13, H * y + 2], fill=(206, 160, 112))
    # Arjuna, mid-shot
    figure(d, W * 0.36, H * 0.92, 320, robe=(60, 96, 160), skin=(206, 156, 106))
    bow(d, W * 0.44, H * 0.70, 78, DGOLD)
    # the stranger at the gate, lit from behind
    gx = W * 0.80
    d.rectangle([gx - 130, H * 0.60, gx + 130, H], fill=(168, 142, 100))
    sun(d, gx, H * 0.72, 132, (250, 226, 160), rays=False)
    figure(d, gx, H * 0.94, 340, robe=(206, 108, 52), skin=(212, 162, 112))
    for ex in (gx - 46, gx + 46):   # the earrings he was born with
        d.ellipse([ex - 15, H * 0.665, ex + 15, H * 0.695], outline=GOLD, width=6)
    save(img, "33_ranga_bhumi")


# ---------------------------------------------------------------------------
# Batch three — Sambhava: Shakuntala to the birth of the three brothers.
# ---------------------------------------------------------------------------

# 20. Shakuntala — standing in the full court, arguing
def shakuntala():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (72, 54, 92), (168, 118, 84))
    d.rectangle([0, H * 0.78, W, H], fill=(126, 94, 72))
    for x in [0.06, 0.94]:
        d.rectangle([W * x - 28, H * 0.18, W * x + 28, H * 0.78], fill=(152, 120, 84), outline=INK, width=3)
        d.rectangle([W * x - 42, H * 0.14, W * x + 42, H * 0.20], fill=GOLD, outline=DGOLD, width=3)
    # the throne, and the king on it, looking away
    d.rectangle([W * 0.68, H * 0.50, W * 0.86, H * 0.80], fill=MAROON, outline=DGOLD, width=5)
    d.polygon([(W * 0.68, H * 0.50), (W * 0.77, H * 0.36), (W * 0.86, H * 0.50)], fill=GOLD, outline=DGOLD)
    figure(d, W * 0.77, H * 0.70, 250, robe=RED, skin=(205, 155, 105), seated=True)
    # the court, seated, watching
    for x in [0.14, 0.24, 0.34]:
        figure(d, W * x, H * 0.88, 195, robe=CREAM, skin=(198, 148, 98), seated=True)
    # her, standing, one hand raised — and the boy beside her
    figure(d, W * 0.46, H * 0.90, 330, robe=(198, 84, 118), skin=(210, 160, 110))
    d.line([(W * 0.492, H * 0.66), (W * 0.575, H * 0.50)], fill=(210, 160, 110), width=16)
    figure(d, W * 0.565, H * 0.92, 175, robe=GOLD, skin=(206, 156, 106))
    # sun and moon, the witnesses she names
    sun(d, W * 0.20, H * 0.14, 52, (246, 214, 128))
    d.ellipse([W * 0.80 - 44, H * 0.12 - 44, W * 0.80 + 44, H * 0.12 + 44], fill=(238, 236, 224))
    d.ellipse([W * 0.815 - 40, H * 0.113 - 40, W * 0.815 + 40, H * 0.113 + 40], fill=(72, 54, 92))
    save(img, "20_shakuntala")


# 21. Bharata — the boy who counted lion cubs
def bharata_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (206, 226, 182), (156, 182, 126), 0, int(H * 0.58))
    sun(d, W * 0.18, H * 0.17, 92, (240, 208, 118))
    d.rectangle([0, H * 0.58, W, H], fill=(128, 158, 100))
    for x, hh in [(0.05, 440), (0.16, 350), (0.88, 430)]:
        tree(d, W * x, H * 0.64, hh)
    # the boy, arm around a cub, counting on his fingers
    figure(d, W * 0.44, H * 0.90, 300, robe=GOLD, skin=(206, 156, 106))
    for cx, cy, sc in [(0.58, 0.88, 1.0), (0.68, 0.91, 0.85), (0.31, 0.90, 0.9)]:
        bx, by, s2 = W * cx, H * cy, sc
        d.ellipse([bx - 78 * s2, by - 40 * s2, bx + 52 * s2, by + 26 * s2], fill=(214, 170, 96))
        d.ellipse([bx + 34 * s2, by - 74 * s2, bx + 104 * s2, by - 8 * s2], fill=(214, 170, 96))
        d.ellipse([bx + 44 * s2, by - 84 * s2, bx + 68 * s2, by - 60 * s2], fill=(186, 142, 74))
        d.ellipse([bx + 72 * s2, by - 84 * s2, bx + 96 * s2, by - 60 * s2], fill=(186, 142, 74))
        d.ellipse([bx + 56 * s2, by - 52 * s2, bx + 70 * s2, by - 38 * s2], fill=INK)
        d.ellipse([bx + 80 * s2, by - 52 * s2, bx + 94 * s2, by - 38 * s2], fill=INK)
        d.line([(bx - 76 * s2, by - 18 * s2), (bx - 120 * s2, by - 58 * s2)], fill=(214, 170, 96), width=int(13 * s2))
    save(img, "21_bharata")


# 22. The eight Vasus — the stolen cow, and the curse
def vasus():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (44, 40, 84), (140, 108, 96), 0, int(H * 0.60))
    stars(d, 90, H * 0.45)
    d.rectangle([0, H * 0.60, W, H], fill=(112, 136, 88))
    for x in [0.06, 0.95]:
        tree(d, W * x, H * 0.66, 400)
    # the eight, in a line across the sky, leading the cow away
    for k in range(8):
        fx = W * (0.16 + k * 0.075)
        figure(d, fx, H * 0.44 + (18 if k % 2 else 0), 150,
               robe=(232, 200, 120) if k else (240, 150, 60), skin=(214, 176, 130))
    # the cow
    cx, cy = W * 0.70, H * 0.80
    d.ellipse([cx - 150, cy - 66, cx + 96, cy + 44], fill=(250, 248, 240))
    d.ellipse([cx + 66, cy - 106, cx + 172, cy - 12], fill=(250, 248, 240))
    d.polygon([(cx + 92, cy - 100), (cx + 78, cy - 148), (cx + 118, cy - 112)], fill=(226, 214, 190))
    d.polygon([(cx + 144, cy - 100), (cx + 168, cy - 146), (cx + 168, cy - 100)], fill=(226, 214, 190))
    d.ellipse([cx + 128, cy - 76, cx + 148, cy - 56], fill=INK)
    for wx in [cx - 108, cx - 48, cx + 16, cx + 66]:
        d.line([(wx, cy + 36), (wx, cy + 130)], fill=(236, 232, 222), width=16)
    # the sage, risen, arm out — the curse in the act of being spoken
    figure(d, W * 0.13, H * 0.92, 330, robe=CREAM, skin=(198, 148, 98))
    d.line([(W * 0.166, H * 0.70), (W * 0.28, H * 0.50)], fill=(198, 148, 98), width=17)
    d.polygon([(W * 0.13 - 36, H * 0.665), (W * 0.13 + 36, H * 0.665), (W * 0.13, H * 0.745)], fill=(240, 238, 232))
    save(img, "22_vasus")


# 25. Amba — the three brought back, and the one who was asked nothing
def amba():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (238, 208, 152), (206, 172, 130), 0, int(H * 0.70))
    d.rectangle([0, H * 0.70, W, H], fill=(160, 124, 88))
    sun(d, W * 0.50, H * 0.18, 96, (244, 198, 100))
    for x in [0.05, 0.95]:
        d.rectangle([W * x - 26, H * 0.20, W * x + 26, H * 0.70], fill=(150, 118, 82), outline=INK, width=3)
    # the chariot
    bx, by = W * 0.60, H * 0.66
    d.rectangle([bx - 190, by, bx + 190, by + 110], fill=MAROON, outline=DGOLD, width=5)
    for wx in [bx - 140, bx + 140]:
        d.ellipse([wx - 62, by + 78, wx + 62, by + 202], outline=INK, width=10)
        for k in range(8):
            a = k * math.pi / 4
            d.line([(wx, by + 140), (wx + 58 * math.cos(a), by + 140 + 58 * math.sin(a))], fill=INK, width=4)
    # the three, standing in it
    for k, (dx, robe) in enumerate([(-115, (196, 84, 118)), (0, (140, 96, 168)), (115, (92, 132, 168))]):
        figure(d, bx + dx, by + 6, 230, robe=robe, skin=(210, 160, 110))
    # him, driving, bow across his back
    figure(d, W * 0.19, H * 0.88, 320, robe=CREAM, skin=(200, 150, 100))
    d.arc([W * 0.10, H * 0.52, W * 0.20, H * 0.80], 250, 470, fill=DGOLD, width=12)
    d.polygon([(W * 0.19 - 34, H * 0.655), (W * 0.19 + 34, H * 0.655), (W * 0.19, H * 0.735)], fill=(238, 234, 226))
    save(img, "25_amba")


# 26. Vyasa comes — the line kept from ending
def vyasa_niyoga():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (52, 44, 88), (150, 106, 84))
    d.rectangle([0, H * 0.76, W, H], fill=(120, 92, 72))
    for x in [0.08, 0.92]:
        d.rectangle([W * x - 26, H * 0.20, W * x + 26, H * 0.76], fill=(150, 118, 82), outline=INK, width=3)
        d.rectangle([W * x - 40, H * 0.16, W * x + 40, H * 0.22], fill=GOLD, outline=DGOLD, width=3)
    # the lamp in the middle of a house with no heir
    d.polygon([(W * 0.485, H * 0.78), (W * 0.515, H * 0.78), (W * 0.508, H * 0.73), (W * 0.492, H * 0.73)], fill=DGOLD)
    flame(d, W * 0.50, H * 0.73, 170, 56)
    # the mother, calling
    figure(d, W * 0.22, H * 0.90, 290, robe=(150, 45, 40), skin=(206, 156, 106))
    # the sage, arrived out of the dark, matted and gaunt
    sx = W * 0.78
    d.polygon([(sx - 78, H * 0.92), (sx + 78, H * 0.92), (sx + 48, H * 0.50), (sx - 48, H * 0.50)], fill=SAFF)
    d.ellipse([sx - 34, H * 0.425, sx + 34, H * 0.505], fill=(196, 146, 96))
    d.ellipse([sx - 44, H * 0.395, sx + 44, H * 0.475], fill=(78, 62, 48))
    d.polygon([(sx - 30, H * 0.485), (sx + 30, H * 0.485), (sx, H * 0.585)], fill=(96, 78, 60))
    for k in range(7):   # matted locks
        a = math.radians(196 + k * 24)
        d.line([(sx, H * 0.435), (sx + 92 * math.cos(a), H * 0.435 + 92 * math.sin(a))], fill=(78, 62, 48), width=11)
    sun(d, sx, H * 0.435, 96, (250, 226, 168), rays=False) if False else None
    save(img, "26_vyasa_niyoga")


# ---------------------------------------------------------------------------
# Batch two — Adivamshavatarana: the dynasties begin.
# ---------------------------------------------------------------------------

# 14. Uparichara Vasu — the ferry on the Yamuna, and how Vyasa came to be
def uparichara():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 205, 130), (238, 220, 180), 0, int(H * 0.52))
    sun(d, W * 0.80, H * 0.18, 92, (245, 200, 100))
    gradient(d, (86, 132, 168), (46, 92, 138), int(H * 0.52), H)
    for i in range(8):
        y = H * (0.56 + i * 0.052)
        d.arc([W * 0.02, y, W * 0.98, y + H * 0.09], 190, 350, fill=(120, 168, 200), width=5)
    for x, hh in [(0.05, 360), (0.95, 340)]:
        tree(d, W * x, H * 0.54, hh)
    # the boat
    bx, by = W * 0.50, H * 0.72
    d.polygon([(bx - 250, by), (bx + 250, by), (bx + 175, by + 78), (bx - 175, by + 78)],
              fill=(126, 84, 50), outline=INK, width=5)
    d.line([(bx - 250, by), (bx + 250, by)], fill=(160, 115, 70), width=9)
    figure(d, bx - 105, by, 235, robe=(196, 82, 116), skin=(206, 156, 106))   # the ferry girl
    d.line([(bx - 60, by - 130), (bx + 40, by + 40)], fill=(150, 108, 62), width=11)  # her pole
    figure(d, bx + 120, by, 235, robe=SAFF, skin=(200, 150, 100))             # the rishi
    # the leaf-cup and the two eagles, high above
    for ex, ey, fl in [(W * 0.30, H * 0.24, 1), (W * 0.42, H * 0.20, -1)]:
        d.polygon([(ex - 60 * fl, ey), (ex + 30 * fl, ey - 26), (ex + 46 * fl, ey + 8), (ex + 12 * fl, ey + 22)],
                  fill=(88, 74, 62))
        d.polygon([(ex, ey - 6), (ex + 54 * fl, ey - 42), (ex + 30 * fl, ey + 2)], fill=(64, 54, 46))
    d.ellipse([W * 0.365 - 17, H * 0.245 - 12, W * 0.365 + 17, H * 0.245 + 12], fill=(238, 214, 150))
    save(img, "14_uparichara")


# 15. Bhu-bharam — the earth asking that her burden be eased
def bhubharam():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (30, 34, 72), (108, 74, 108))
    stars(d, 130, H * 0.55)
    # the three, as three lamps of light above
    for x, col in [(0.30, (250, 236, 190)), (0.50, (206, 226, 250)), (0.70, (250, 210, 160))]:
        sun(d, W * x, H * 0.26, 62, col)
        figure(d, W * x, H * 0.46, 190, robe=CREAM, skin=(214, 176, 130), seated=True)
    # the earth, a heavy globe, and the small figure kneeling before it
    ex, ey, r = W * 0.50, H * 0.86, 250
    d.ellipse([ex - r, ey - r * 0.72, ex + r, ey + r * 0.72], fill=(58, 96, 66), outline=(38, 66, 46), width=5)
    for k, (dx, dy, rr) in enumerate([(-0.42, -0.20, 0.22), (0.28, -0.32, 0.26), (0.10, 0.18, 0.20), (-0.20, 0.26, 0.16)]):
        d.ellipse([ex + dx * r - rr * r, ey + dy * r * 0.72 - rr * r * 0.6,
                   ex + dx * r + rr * r, ey + dy * r * 0.72 + rr * r * 0.6], fill=(92, 126, 84))
    # the weight pressing down on it
    for k in range(9):
        px = W * (0.20 + k * 0.075)
        d.line([(px, H * 0.60), (px, H * 0.68)], fill=(210, 200, 190), width=5)
        d.polygon([(px, H * 0.70), (px - 11, H * 0.655), (px + 11, H * 0.655)], fill=(210, 200, 190))
    figure(d, W * 0.16, H * 0.70, 210, robe=(150, 45, 40), skin=(206, 156, 106), seated=True)
    save(img, "15_bhubharam")


# 16. Kacha — the teaching given from inside, at the cost of the teacher
def kacha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (238, 216, 172), (206, 178, 132), 0, int(H * 0.68))
    d.rectangle([0, H * 0.68, W, H], fill=(150, 120, 82))
    for x in [0.08, 0.92]:
        tree(d, W * x, H * 0.72, 400)
    # the fire between teacher and student
    d.rectangle([W * 0.455, H * 0.62, W * 0.545, H * 0.70], fill=(126, 92, 70), outline=INK, width=4)
    flame(d, W * 0.50, H * 0.62, 210, 72)
    # the teacher, seated, with the student's life held inside him
    figure(d, W * 0.26, H * 0.84, 300, robe=(196, 76, 70), skin=(198, 148, 98), seated=True)
    d.ellipse([W * 0.26 - 62, H * 0.72, W * 0.26 + 62, H * 0.80], fill=(232, 168, 78), outline=DGOLD, width=3)
    sun(d, W * 0.26, H * 0.76, 26, (252, 240, 196), rays=False)
    # the student, restored, standing
    figure(d, W * 0.74, H * 0.86, 285, robe=CREAM, skin=(206, 156, 106))
    # the daughter, apart, watching
    figure(d, W * 0.92, H * 0.90, 230, robe=(198, 84, 118), skin=(210, 160, 110))
    save(img, "16_kacha")


# 17. Devayani in the well — and the hand that reached in
def devayani():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (198, 220, 174), (150, 178, 118), 0, int(H * 0.56))
    d.rectangle([0, H * 0.56, W, H], fill=(132, 158, 100))
    for x, hh in [(0.06, 400), (0.94, 380)]:
        tree(d, W * x, H * 0.62, hh)
    # the disused well
    wx, wy, wr = W * 0.56, H * 0.74, 250
    d.ellipse([wx - wr, wy - wr * 0.34, wx + wr, wy + wr * 0.34], fill=(112, 96, 78), outline=INK, width=6)
    d.ellipse([wx - wr * 0.78, wy - wr * 0.26, wx + wr * 0.78, wy + wr * 0.26], fill=(38, 44, 46))
    for k in range(14):   # the coping stones
        a = k * math.pi / 7
        sx, sy = wx + wr * 0.90 * math.cos(a), wy + wr * 0.30 * math.sin(a)
        d.ellipse([sx - 22, sy - 13, sx + 22, sy + 13], fill=(140, 120, 96), outline=INK, width=2)
    # her, down inside, looking up
    d.ellipse([wx - 34, wy - 30, wx + 34, wy + 38], fill=(198, 84, 118))
    d.ellipse([wx - 20, wy - 58, wx + 20, wy - 18], fill=(210, 160, 110))
    d.line([(wx - 22, wy - 34), (wx - 96, wy - 84)], fill=(210, 160, 110), width=15)
    # the king, kneeling, arm reaching in
    figure(d, W * 0.22, H * 0.90, 300, robe=(150, 45, 40), skin=(206, 156, 106))
    d.line([(W * 0.255, H * 0.70), (wx - 104, wy - 88)], fill=(206, 156, 106), width=17)
    # the other girl, walking away at the edge
    figure(d, W * 0.90, H * 0.66, 190, robe=(92, 72, 142), skin=(198, 148, 98))
    save(img, "17_devayani")


# 18. Yayati — old in a single moment
def yayati():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (86, 62, 96), (170, 118, 86))
    d.rectangle([0, H * 0.76, W, H], fill=(128, 96, 74))
    for x in [0.08, 0.92]:
        d.rectangle([W * x - 26, H * 0.20, W * x + 26, H * 0.76], fill=(152, 120, 84), outline=INK, width=3)
        d.rectangle([W * x - 40, H * 0.16, W * x + 40, H * 0.22], fill=GOLD, outline=DGOLD, width=3)
    # the sage, arm raised, the curse just spoken
    figure(d, W * 0.24, H * 0.88, 320, robe=(196, 76, 70), skin=(198, 148, 98))
    d.line([(W * 0.275, H * 0.70), (W * 0.36, H * 0.44)], fill=(198, 148, 98), width=16)
    beard = [(W * 0.24 - 34, H * 0.665), (W * 0.24 + 34, H * 0.665), (W * 0.24, H * 0.735)]
    d.polygon(beard, fill=(238, 234, 226))
    # the king, bent, white-haired, hands on knees
    kx = W * 0.62
    d.polygon([(kx - 74, H * 0.90), (kx + 74, H * 0.90), (kx + 44, H * 0.60), (kx - 30, H * 0.60)], fill=(150, 45, 40))
    d.ellipse([kx - 26, H * 0.535, kx + 30, H * 0.605], fill=(198, 156, 118))
    d.chord([kx - 30, H * 0.515, kx + 34, H * 0.585], 180, 360, fill=(240, 238, 232))
    d.polygon([(kx - 18, H * 0.585), (kx + 22, H * 0.585), (kx + 2, H * 0.655)], fill=(240, 238, 232))
    d.line([(kx + 74, H * 0.90), (kx + 116, H * 0.60)], fill=(120, 86, 52), width=13)   # his stick
    # the youngest son, stepping forward
    figure(d, W * 0.88, H * 0.90, 250, robe=GOLD, skin=(206, 156, 106))
    save(img, "18_yayati")


# 19. Puru — the youth handed back, and the crown handed on
def puru():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 212, 142), (232, 206, 158), 0, int(H * 0.70))
    d.rectangle([0, H * 0.70, W, H], fill=(176, 138, 94))
    sun(d, W * 0.50, H * 0.20, 108, (246, 202, 104))
    for x in [0.08, 0.92]:
        d.rectangle([W * x - 28, H * 0.22, W * x + 28, H * 0.70], fill=(158, 124, 86), outline=INK, width=3)
        d.rectangle([W * x - 42, H * 0.18, W * x + 42, H * 0.24], fill=GOLD, outline=DGOLD, width=3)
    # the father, old again, seated, at peace
    figure(d, W * 0.28, H * 0.86, 290, robe=(150, 45, 40), skin=(198, 156, 118), seated=True)
    d.chord([W * 0.28 - 30, H * 0.60, W * 0.28 + 30, H * 0.665], 180, 360, fill=(240, 238, 232))
    # the son, young, crowned
    figure(d, W * 0.70, H * 0.88, 320, robe=MAROON, skin=(206, 156, 106))
    cx, cy = W * 0.70, H * 0.575
    d.polygon([(cx - 46, cy + 20), (cx - 38, cy - 22), (cx - 16, cy - 2), (cx, cy - 32),
               (cx + 16, cy - 2), (cx + 38, cy - 22), (cx + 46, cy + 20)], fill=GOLD, outline=DGOLD)
    # the thousand years, marked out as a row of lamps burning down
    for k in range(11):
        lx = W * (0.14 + k * 0.072)
        d.polygon([(lx - 15, H * 0.955), (lx + 15, H * 0.955), (lx + 10, H * 0.925), (lx - 10, H * 0.925)], fill=DGOLD)
        flame(d, lx, H * 0.925, 46 - k * 3, 17)
    save(img, "19_puru")


# ---------------------------------------------------------------------------
# Batch one — the opening frame, the three upakhyanas, Garuda and Astika.
# ---------------------------------------------------------------------------

def _sage_circle(d, cx, cy, r, n, h=150, robe=CREAM):
    """A ring of seated sages, drawn back-to-front so nearer ones overlap."""
    figs = []
    for k in range(n):
        a = math.pi * (0.15 + 0.7 * k / max(1, n - 1))
        figs.append((cx + r * math.cos(a), cy - r * 0.42 * math.sin(a)))
    for x, y in sorted(figs, key=lambda f: f[1]):
        figure(d, x, y, h, robe=robe, skin=(200, 150, 100), seated=True)


# 1. Naimisharanya — the twelve-year satra, Sauti telling, sages listening
def naimisharanya():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 215, 150), (245, 232, 200), 0, int(H * 0.62))
    sun(d, W * 0.5, H * 0.2, 105, (240, 195, 95))
    d.rectangle([0, H * 0.62, W, H], fill=(120, 150, 95))
    d.rectangle([0, H * 0.62, W, H * 0.66], fill=(95, 130, 80))
    for x, hh in [(0.06, 400), (0.17, 340), (0.86, 400), (0.95, 330)]:
        tree(d, W * x, H * 0.66, hh)
    # sacrificial fire at the centre of the long session
    d.rectangle([W * 0.44, H * 0.60, W * 0.56, H * 0.68], fill=(125, 92, 70), outline=INK, width=4)
    flame(d, W * 0.5, H * 0.60, 200, 74)
    _sage_circle(d, W * 0.5, H * 0.86, W * 0.30, 7, 150)
    # Sauti, standing, telling
    figure(d, W * 0.5, H * 0.70, 235, robe=SAFF, skin=(205, 155, 105))
    save(img, "02_naimisharanya")


# 3. Parvasangraha — eighteen palm-leaf bundles, the whole work seen at once
def parva_sangraha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (238, 224, 190), (214, 190, 148))
    d.rectangle([0, H * 0.74, W, H], fill=(150, 115, 80))
    for i in range(18):
        col, row = i % 9, i // 9
        cx = W * 0.10 + col * W * 0.10
        cy = H * 0.40 + row * H * 0.22
        d.rounded_rectangle([cx - 62, cy - 34, cx + 62, cy + 34], 8,
                            fill=(245, 228, 178), outline=BROWN, width=4)
        for k in range(3):
            d.line([(cx - 46, cy - 14 + k * 14), (cx + 46 - random.randint(0, 34), cy - 14 + k * 14)],
                   fill=(140, 105, 60), width=3)
        d.line([(cx, cy - 40), (cx, cy + 40)], fill=MAROON, width=5)   # binding cord
    d.rectangle([0, H * 0.06, W, H * 0.14], fill=None)
    for x in [W * 0.5]:
        lotus(d, x, H * 0.13, 44)
    save(img, "04_parva_sangraha")


# 6. Udanka — the nagaloka descent, the horse of fire, the stolen earrings
def udanka():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (35, 25, 55), (70, 45, 40))
    # the cleft in the earth, opening downward
    d.polygon([(0, H * 0.16), (W, H * 0.16), (W, 0), (0, 0)], fill=(120, 95, 65))
    d.polygon([(W * 0.20, H * 0.16), (W * 0.80, H * 0.16), (W * 0.62, H * 0.40), (W * 0.38, H * 0.40)],
              fill=(45, 32, 60))
    # serpent kingdom: coiled nagas along the walls
    for k, (sx, sy, w) in enumerate([(W * 0.10, H * 0.42, 16), (W * 0.90, H * 0.38, 16),
                                     (W * 0.14, H * 0.72, 12), (W * 0.87, H * 0.70, 12)]):
        pts = [(sx + (W * 0.5 - sx) * (i / 29), sy + 46 * math.sin(i * 0.42)) for i in range(30)]
        d.line(pts, fill=(60, 140, 90) if k % 2 else (150, 120, 60), width=w)
        hx, hy = pts[0]
        d.ellipse([hx - 22, hy - 15, hx + 22, hy + 15], fill=(60, 140, 90) if k % 2 else (150, 120, 60))
    # the horse that is Agni, breathing smoke from every pore
    d.ellipse([W * 0.40, H * 0.56, W * 0.62, H * 0.74], fill=(235, 225, 205))
    d.polygon([(W * 0.60, H * 0.60), (W * 0.70, H * 0.50), (W * 0.72, H * 0.58), (W * 0.63, H * 0.66)],
              fill=(235, 225, 205))
    for wx in [W * 0.43, W * 0.50, W * 0.57]:
        d.line([(wx, H * 0.73), (wx, H * 0.85)], fill=(215, 205, 185), width=11)
    for k in range(9):
        flame(d, W * 0.40 + k * W * 0.028, H * 0.56, 100 + random.randint(0, 60), 30)
    figure(d, W * 0.24, H * 0.86, 230, robe=SAFF)
    # the recovered earrings
    for ex in [W * 0.80, W * 0.86]:
        d.ellipse([ex - 26, H * 0.80 - 26, ex + 26, H * 0.80 + 26], outline=GOLD, width=9)
    save(img, "06_udanka")


# 5. Janamejaya — the court, the vow, the throne
def janamejaya():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (48, 38, 78), (95, 60, 55))
    d.rectangle([0, H * 0.76, W, H], fill=(105, 70, 60))
    # pillared hall
    for x in [0.06, 0.22, 0.78, 0.94]:
        d.rectangle([W * x - 26, H * 0.16, W * x + 26, H * 0.76], fill=(150, 118, 82), outline=INK, width=3)
        d.rectangle([W * x - 40, H * 0.13, W * x + 40, H * 0.18], fill=GOLD, outline=DGOLD, width=3)
    # throne, raised
    d.rectangle([W * 0.42, H * 0.50, W * 0.58, H * 0.78], fill=MAROON, outline=DGOLD, width=5)
    d.polygon([(W * 0.42, H * 0.50), (W * 0.50, H * 0.36), (W * 0.58, H * 0.50)], fill=GOLD, outline=DGOLD)
    figure(d, W * 0.50, H * 0.68, 250, robe=RED, skin=(205, 155, 105))
    # ministers, and the muni who set this in motion
    figure(d, W * 0.30, H * 0.84, 200, robe=CREAM, seated=True)
    figure(d, W * 0.70, H * 0.84, 200, robe=CREAM, seated=True)
    figure(d, W * 0.16, H * 0.86, 215, robe=SAFF)
    # a raised hand's vow, read as a lamp above the throne
    flame(d, W * 0.50, H * 0.32, 150, 52)
    save(img, "07_janamejaya")


# 6. Pauloma — the asked fire, the ashram, the child who blazed
def pauloma():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (245, 200, 130), (225, 195, 145), 0, int(H * 0.66))
    d.rectangle([0, H * 0.66, W, H], fill=(140, 155, 100))
    # thatched hermitage
    d.polygon([(W * 0.12, H * 0.62), (W * 0.34, H * 0.40), (W * 0.56, H * 0.62)], fill=(150, 120, 70), outline=BROWN)
    d.rectangle([W * 0.16, H * 0.62, W * 0.52, H * 0.78], fill=(190, 165, 120), outline=BROWN, width=4)
    tree(d, W * 0.90, H * 0.70, 400)
    # the household fire, made to answer
    d.rectangle([W * 0.60, H * 0.68, W * 0.74, H * 0.76], fill=(125, 92, 70), outline=INK, width=4)
    flame(d, W * 0.67, H * 0.68, 260, 88)
    # the mother, and the child fallen from her, blazing like a small sun
    figure(d, W * 0.34, H * 0.86, 220, robe=(200, 60, 90), skin=(210, 160, 110))
    sun(d, W * 0.44, H * 0.83, 44, (250, 210, 110))
    # the rakshasa, reduced to ash at the edge of that light
    d.polygon([(W * 0.80, H * 0.86), (W * 0.86, H * 0.70), (W * 0.92, H * 0.86)], fill=(85, 75, 80))
    for k in range(5):
        d.line([(W * (0.80 + k * 0.03), H * 0.86), (W * (0.80 + k * 0.03), H * 0.78)], fill=SMOKE, width=6)
    save(img, "08_pauloma")


# 7. Ruru — the lifted stick, and the snake that spoke
def ruru():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (206, 226, 182), (156, 182, 126), 0, int(H * 0.58))
    sun(d, W * 0.50, H * 0.16, 84, (238, 214, 130))
    d.rectangle([0, H * 0.58, W, H], fill=(126, 156, 98))
    d.rectangle([0, H * 0.58, W, H * 0.62], fill=(100, 133, 82))
    for x, hh in [(0.04, 470), (0.15, 380), (0.87, 460), (0.98, 370)]:
        tree(d, W * x, H * 0.64, hh)
    # Ruru, large, the stick raised and then held
    figure(d, W * 0.30, H * 0.94, 400, robe=CREAM, skin=(200, 150, 100))
    d.line([(W * 0.355, H * 0.72), (W * 0.475, H * 0.33)], fill=BROWN, width=20)
    d.ellipse([W * 0.470, H * 0.31, W * 0.492, H * 0.35], fill=(120, 85, 50))
    # the dundubha: coiled, head raised, meeting him at eye level
    ccx, ccy = W * 0.70, H * 0.80
    # coils, drawn widest-first so each sits in front of the one behind it
    for k, rr in enumerate([232, 186, 142, 100]):
        d.ellipse([ccx - rr, ccy - rr * 0.40, ccx + rr, ccy + rr * 0.40],
                  fill=(96, 132, 66) if k % 2 else (132, 168, 92),
                  outline=(70, 100, 50), width=3)
    neck = [(ccx - 40 + 26 * math.sin(i * 0.34), ccy - 22 - i * 15) for i in range(15)]
    d.line(neck, fill=(132, 168, 92), width=32)
    hx, hy = neck[-1]
    d.ellipse([hx - 52, hy - 32, hx + 52, hy + 32], fill=(132, 168, 92))
    d.polygon([(hx - 52, hy), (hx - 96, hy - 10), (hx - 96, hy + 10)], fill=(132, 168, 92))
    d.ellipse([hx + 2, hy - 20, hx + 26, hy + 4], fill=CREAM)      # one eye — head in profile
    d.ellipse([hx + 10, hy - 15, hx + 22, hy - 3], fill=INK)
    d.line([(hx - 96, hy), (hx - 132, hy - 14)], fill=RED, width=6)
    d.line([(hx - 96, hy), (hx - 132, hy + 14)], fill=RED, width=6)
    # Pramadvara, alive again, at the edge of the clearing
    figure(d, W * 0.10, H * 0.96, 300, robe=(198, 84, 118), skin=(210, 160, 110))
    lotus(d, W * 0.20, H * 0.94, 40)
    save(img, "09_ruru")


# 8. Kadru and Vinata — the white horse and the wager on its tail
def kadru_vinata():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (150, 195, 225), (205, 225, 235), 0, int(H * 0.58))
    gradient(d, WATER2, WATER, int(H * 0.58), H)
    sun(d, W * 0.80, H * 0.18, 90, (250, 220, 140))
    for i in range(7):
        y = H * (0.62 + i * 0.055)
        d.arc([W * 0.02, y, W * 0.98, y + H * 0.10], 190, 350, fill=(150, 195, 220), width=5)
    # Uchchaihshravas, risen from the churning
    hx, hy = W * 0.52, H * 0.50
    d.ellipse([hx - 150, hy - 70, hx + 130, hy + 78], fill=(252, 250, 244))
    d.polygon([(hx + 100, hy - 40), (hx + 215, hy - 140), (hx + 240, hy - 66), (hx + 140, hy + 14)],
              fill=(252, 250, 244))
    d.polygon([(hx + 196, hy - 132), (hx + 208, hy - 176), (hx + 226, hy - 138)], fill=(252, 250, 244))
    d.ellipse([hx + 206, hy - 104, hx + 222, hy - 88], fill=INK)
    for wx in [hx - 108, hx - 44, hx + 30, hx + 88]:
        d.line([(wx, hy + 62), (wx, hy + 175)], fill=(238, 234, 226), width=17)
    # the tail — white, with black hairs that are not hairs
    tail = [(hx - 145, hy - 34 + i * 9) for i in range(22)]
    for k, (tx, ty) in enumerate(tail):
        d.line([(tx, ty), (tx - 118 - 24 * math.sin(k * 0.4), ty + 78)],
               fill=(40, 45, 40) if k % 2 else (250, 248, 242), width=8)
    # the two sisters, watching from the shore
    figure(d, W * 0.10, H * 0.92, 240, robe=(60, 90, 60), skin=(180, 130, 90))
    figure(d, W * 0.90, H * 0.92, 240, robe=GOLD, skin=(210, 160, 110))
    save(img, "10_kadru_vinata")


# 9. Garuda — the flight, the wheel, the pot of amrita
def garuda():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (30, 35, 80), (215, 130, 60))
    stars(d, 70, H * 0.4)
    sun(d, W * 0.20, H * 0.24, 110, (250, 200, 100))
    cx, cy = W * 0.56, H * 0.50
    # wings, two great fans of gold and flame
    for side in (-1, 1):
        for k in range(11):
            a = math.radians(200 + k * 13) if side < 0 else math.radians(-20 - k * 13)
            ln = 470 - abs(k - 5) * 26
            col = GOLD if k % 2 else SAFF
            d.line([(cx + side * 60, cy - 30), (cx + side * 60 + ln * math.cos(a), cy - 30 + ln * math.sin(a))],
                   fill=col, width=17)
    d.ellipse([cx - 74, cy - 60, cx + 74, cy + 120], fill=(232, 176, 72), outline=DGOLD, width=4)
    d.ellipse([cx - 46, cy - 132, cx + 46, cy - 40], fill=(250, 246, 236))
    d.polygon([(cx + 34, cy - 100), (cx + 96, cy - 84), (cx + 34, cy - 66)], fill=(235, 150, 40))
    d.ellipse([cx + 6, cy - 108, cx + 26, cy - 88], fill=INK)
    for lx in (cx - 40, cx + 40):
        d.line([(lx, cy + 108), (lx, cy + 186)], fill=(215, 150, 45), width=15)
    # the pot of amrita, held
    d.ellipse([cx - 44, cy + 176, cx + 44, cy + 258], fill=(225, 200, 130), outline=DGOLD, width=6)
    d.rectangle([cx - 22, cy + 154, cx + 22, cy + 188], fill=(225, 200, 130), outline=DGOLD, width=5)
    sun(d, cx, cy + 216, 22, (255, 245, 200), rays=False)
    # the guarding wheel, still turning behind him
    d.ellipse([W * 0.83 - 92, H * 0.30 - 92, W * 0.83 + 92, H * 0.30 + 92], outline=(200, 205, 215), width=13)
    for k in range(10):
        a = k * math.pi / 5
        d.line([(W * 0.83, H * 0.30), (W * 0.83 + 92 * math.cos(a), H * 0.30 + 92 * math.sin(a))],
               fill=(200, 205, 215), width=6)
    save(img, "11_garuda")


# 10. Parikshit — the seated silence, and the dead snake laid on it
def parikshit():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (235, 195, 135), (215, 200, 160), 0, int(H * 0.64))
    d.rectangle([0, H * 0.64, W, H], fill=(160, 150, 105))
    sun(d, W * 0.14, H * 0.20, 88, (245, 200, 105))
    for x, hh in [(0.05, 380), (0.94, 400)]:
        tree(d, W * x, H * 0.70, hh)
    # the muni, eyes shut, hearing nothing
    figure(d, W * 0.62, H * 0.88, 300, robe=CREAM, skin=(195, 145, 95), seated=True)
    d.line([(W * 0.60, H * 0.63), (W * 0.64, H * 0.63)], fill=INK, width=4)
    # the dead snake across his shoulders
    pts = [(W * (0.53 + i * 0.008), H * 0.70 + 16 * math.sin(i * 0.7)) for i in range(24)]
    d.line(pts, fill=(105, 115, 85), width=17)
    d.ellipse([pts[-1][0] - 20, pts[-1][1] - 13, pts[-1][0] + 20, pts[-1][1] + 13], fill=(105, 115, 85))
    # the king, turning away, bow still in hand
    figure(d, W * 0.26, H * 0.90, 275, robe=(150, 40, 35), skin=(205, 155, 105))
    d.arc([W * 0.14, H * 0.56, W * 0.24, H * 0.80], 250, 470, fill=DGOLD, width=10)
    # seven marks of the seven days
    for k in range(7):
        d.ellipse([W * (0.34 + k * 0.038) - 11, H * 0.14 - 11, W * (0.34 + k * 0.038) + 11, H * 0.14 + 11],
                  fill=MAROON if k == 6 else (200, 170, 120), outline=DGOLD, width=3)
    save(img, "12_parikshit")


# ---------------------------------------------------------------------------
# Batches six and seven — the seventh and eighth āśvāsas, to the end of Adi.
# ---------------------------------------------------------------------------

def crown_on(d, cx, top, w=44, col=GOLD):
    """A small crown sitting on a figure() head whose top is at `top`."""
    d.polygon([(cx - w / 2, top + 8), (cx - w / 2, top - 14), (cx - w / 4, top - 2), (cx, top - 20),
               (cx + w / 4, top - 2), (cx + w / 2, top - 14), (cx + w / 2, top + 8)], fill=col, outline=DGOLD)


def cow(d, cx, base, s, col=(248, 244, 232)):
    d.ellipse([cx - s, base - s * 0.95, cx + s * 0.9, base - s * 0.35], fill=col, outline=(150, 140, 120), width=3)
    for lx in (cx - s * 0.7, cx - s * 0.4, cx + s * 0.35, cx + s * 0.62):
        d.rectangle([lx - s * 0.07, base - s * 0.5, lx + s * 0.07, base], fill=col, outline=(150, 140, 120))
    hx, hy = cx + s * 1.05, base - s * 0.95
    d.ellipse([hx - s * 0.3, hy - s * 0.22, hx + s * 0.3, hy + s * 0.28], fill=col, outline=(150, 140, 120), width=3)
    d.line([(hx - s * 0.18, hy - s * 0.16), (hx - s * 0.3, hy - s * 0.45)], fill=DGOLD, width=7)
    d.line([(hx + s * 0.18, hy - s * 0.16), (hx + s * 0.3, hy - s * 0.45)], fill=DGOLD, width=7)
    d.ellipse([hx - 6, hy - 4, hx + 6, hy + 8], fill=INK)
    d.line([(cx - s, base - s * 0.8), (cx - s * 1.25, base - s * 0.3)], fill=col, width=8)


def bird(d, cx, cy, s, col=(120, 90, 60), wings=True):
    d.ellipse([cx - s, cy - s * 0.6, cx + s, cy + s * 0.6], fill=col)
    d.ellipse([cx + s * 0.6, cy - s * 0.9, cx + s * 1.3, cy - s * 0.2], fill=col)
    d.polygon([(cx + s * 1.28, cy - s * 0.6), (cx + s * 1.7, cy - s * 0.5), (cx + s * 1.28, cy - s * 0.4)], fill=GOLD)
    d.ellipse([cx + s * 0.98, cy - s * 0.7, cx + s * 1.12, cy - s * 0.56], fill=INK)
    if wings:
        d.polygon([(cx - s * 0.3, cy - s * 0.2), (cx - s * 1.4, cy - s * 1.6), (cx + s * 0.4, cy - s * 0.3)], fill=col)


def chariot(d, cx, base, s=1.0, body=RED):
    d.rectangle([cx - 110 * s, base - 120 * s, cx + 110 * s, base - 50 * s], fill=body, outline=DGOLD, width=5)
    d.ellipse([cx - 70 * s, base - 110 * s, cx + 10 * s, base - 30 * s], outline=INK, width=int(9 * s))
    d.ellipse([cx + 10 * s, base - 110 * s, cx + 90 * s, base - 30 * s], outline=INK, width=int(9 * s))
    d.line([(cx + 110 * s, base - 80 * s), (cx + 230 * s, base - 95 * s)], fill=BROWN, width=int(8 * s))


def horse(d, cx, base, s=1.0, col=WHITE):
    d.ellipse([cx - 90 * s, base - 130 * s, cx + 60 * s, base - 70 * s], fill=col, outline=(160, 150, 140), width=2)
    for lx, ang in ((-70, -18), (-45, 16), (30, -22), (50, 20)):
        d.line([(cx + lx * s, base - 85 * s), (cx + (lx + ang) * s, base)], fill=col, width=int(12 * s))
    d.polygon([(cx + 40 * s, base - 120 * s), (cx + 100 * s, base - 190 * s), (cx + 130 * s, base - 170 * s),
               (cx + 80 * s, base - 100 * s)], fill=col)
    d.ellipse([cx + 96 * s, base - 200 * s, cx + 150 * s, base - 160 * s], fill=col)
    d.line([(cx - 90 * s, base - 110 * s), (cx - 130 * s, base - 70 * s)], fill=(200, 190, 170), width=int(10 * s))


def pot(d, cx, base, r, col=(170, 90, 50)):
    d.ellipse([cx - r, base - r * 1.7, cx + r, base - r * 0.1], fill=col, outline=(110, 55, 30), width=3)
    d.rectangle([cx - r * 0.45, base - r * 1.95, cx + r * 0.45, base - r * 1.55], fill=col, outline=(110, 55, 30))


# 40. Yajnasena — the two who walked out of Drupada's fire
def yajnasena():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (40, 22, 30), (110, 50, 30))
    for x in (0.08, 0.92):
        d.rectangle([W * x - 26, H * 0.08, W * x + 26, H * 0.82], fill=(90, 50, 40), outline=DGOLD, width=3)
    d.rectangle([0, H * 0.82, W, H], fill=(120, 80, 50))
    # the altar and its fire
    d.polygon([(W * 0.36, H * 0.84), (W * 0.64, H * 0.84), (W * 0.60, H * 0.72), (W * 0.40, H * 0.72)],
              fill=(160, 110, 70), outline=INK)
    flame(d, W * 0.5, H * 0.74, 360, 170)
    # Dhrishtadyumna rising, armoured, bow in hand
    figure(d, W * 0.46, H * 0.44, 250, robe=(200, 170, 80), skin=(214, 164, 104))
    crown_on(d, W * 0.46, H * 0.44 - 250 * 0.86)
    bow(d, W * 0.40, H * 0.30, 70, DGOLD, arrow=False)
    # Krishnaa beside him, dark as a blue lotus
    figure(d, W * 0.56, H * 0.46, 220, robe=(40, 50, 110), skin=(110, 80, 70))
    # the priest and the king
    figure(d, W * 0.20, H * 0.92, 250, robe=(232, 120, 40), skin=(190, 140, 95), seated=True)
    figure(d, W * 0.80, H * 0.92, 260, robe=(120, 60, 110), skin=(200, 150, 100), seated=True)
    crown_on(d, W * 0.80, H * 0.92 - 260 * 0.92)
    save(img, "40_yajnasena")


# 41. Angaraparna — midnight on the Ganga, a torch against a gandharva
def angaraparna():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (12, 16, 44), (30, 40, 80), 0, int(H * 0.6))
    stars(d, 140, H * 0.5)
    d.ellipse([W * 0.82 - 50, H * 0.12 - 50, W * 0.82 + 50, H * 0.12 + 50], fill=(236, 232, 210))
    gradient(d, (26, 50, 90), (16, 30, 60), int(H * 0.6), int(H * 0.8))
    for k in range(12):
        y = H * 0.62 + k * 13
        d.line([(W * 0.05 + k * 40, y), (W * 0.35 + k * 40, y)], fill=(70, 100, 150), width=2)
    d.rectangle([0, H * 0.8, W, H], fill=(60, 56, 40))
    # the gandharva on his chariot, over the water
    chariot(d, W * 0.72, H * 0.52, 1.1, body=(60, 100, 120))
    figure(d, W * 0.72, H * 0.40, 200, robe=(60, 100, 120), skin=(214, 170, 120))
    crown_on(d, W * 0.72, H * 0.40 - 200 * 0.86)
    for k in range(4):
        d.line([(W * 0.64, H * 0.30 + k * 26), (W * 0.40, H * 0.46 + k * 20)], fill=(210, 210, 230), width=3)
    # Arjuna with the torch
    figure(d, W * 0.28, H * 0.95, 320, robe=(60, 90, 170), skin=(200, 150, 100))
    d.line([(W * 0.31, H * 0.72), (W * 0.36, H * 0.46)], fill=BROWN, width=12)
    for r, c in ((90, (120, 60, 30)), (60, (200, 110, 40)), (34, (250, 200, 90))):
        d.ellipse([W * 0.36 - r, H * 0.44 - r, W * 0.36 + r, H * 0.44 + r], outline=c, width=3)
    flame(d, W * 0.36, H * 0.46, 80, 34)
    # the others, asleep on the bank
    for x in (0.08, 0.14):
        figure(d, W * x, H * 0.97, 170, robe=(150, 120, 90), skin=(200, 150, 100), seated=True)
    save(img, "41_angaraparna")


# 42. Tapati — the king on the peak, facing the sun
def tapati():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 210, 140), (240, 150, 90))
    sun(d, W * 0.62, H * 0.28, 120, (255, 220, 110))
    # the daughter of the sun, small, descending
    figure(d, W * 0.62, H * 0.62, 150, robe=(240, 170, 60), skin=(230, 180, 120))
    d.polygon([(0, H), (W * 0.18, H * 0.58), (W * 0.30, H * 0.66), (W * 0.42, H * 0.52),
               (W * 0.58, H * 0.74), (W * 0.72, H * 0.66), (W, H * 0.80), (W, H)], fill=(120, 80, 70))
    d.polygon([(0, H), (W * 0.30, H * 0.78), (W * 0.60, H * 0.90), (W, H * 0.86), (W, H)], fill=(80, 56, 52))
    # Samvarana on the peak, hands joined
    figure(d, W * 0.42, H * 0.53, 230, robe=(110, 80, 120), skin=(200, 150, 100))
    crown_on(d, W * 0.42, H * 0.53 - 230 * 0.86)
    d.polygon([(W * 0.42 - 12, H * 0.53 - 230 * 0.58), (W * 0.42 + 12, H * 0.53 - 230 * 0.58),
               (W * 0.42, H * 0.53 - 230 * 0.74)], fill=(200, 150, 100))
    # the dead horse at the foot of the hill
    d.ellipse([W * 0.12, H * 0.88, W * 0.24, H * 0.93], fill=(150, 120, 100))
    save(img, "42_tapati")


# 43. Nandini — the cow who would not be taken
def nandini():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (200, 222, 190), (160, 190, 140), 0, int(H * 0.6))
    d.rectangle([0, H * 0.6, W, H], fill=(140, 164, 100))
    # the hermitage
    d.polygon([(W * 0.04, H * 0.62), (W * 0.14, H * 0.44), (W * 0.24, H * 0.62)], fill=(170, 130, 70))
    d.rectangle([W * 0.06, H * 0.62, W * 0.22, H * 0.78], fill=(200, 170, 120))
    tree(d, W * 0.30, H * 0.66, 360)
    figure(d, W * 0.16, H * 0.94, 230, robe=(232, 120, 40), skin=(190, 140, 95), seated=True)
    # Nandini, risen
    cow(d, W * 0.44, H * 0.86, 150)
    for k in range(10):
        a = math.radians(-60 + k * 12)
        d.line([(W * 0.46 + 170 * math.cos(a), H * 0.66 + 170 * math.sin(a)),
                (W * 0.46 + 240 * math.cos(a), H * 0.66 + 240 * math.sin(a))], fill=GOLD, width=5)
    # the warriors she made, driving the army back
    cols = [(90, 110, 60), (140, 60, 40), (60, 70, 120), (150, 120, 60), (80, 50, 90)]
    for k, x in enumerate([0.60, 0.66, 0.72, 0.78]):
        figure(d, W * x, H * 0.92, 210, robe=cols[k], skin=(190, 140, 95))
        d.line([(W * x + 20, H * 0.80), (W * x + 70, H * 0.66)], fill=(170, 170, 180), width=6)
    for x in (0.88, 0.94, 0.985):
        figure(d, W * x, H * 0.90, 170, robe=(100, 20, 25), skin=(200, 150, 100))
    save(img, "43_nandini")


# 44. Vipasha — the river that untied Vasishtha
def vipasha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (170, 190, 210), (220, 220, 210), 0, int(H * 0.5))
    d.polygon([(0, H * 0.5), (W * 0.2, H * 0.22), (W * 0.36, H * 0.44), (W * 0.52, H * 0.18), (W * 0.7, H * 0.42),
               (W * 0.86, H * 0.26), (W, H * 0.46), (W, H * 0.55), (0, H * 0.55)], fill=(120, 130, 150))
    for px, py in ((0.2, 0.22), (0.52, 0.18), (0.86, 0.26)):
        d.polygon([(W * px, H * py), (W * px - 40, H * py + 50), (W * px + 40, H * py + 50)], fill=WHITE)
    d.rectangle([0, H * 0.55, W, H], fill=(120, 150, 100))
    # the river, running across
    d.polygon([(W * 0.55, H * 0.55), (W * 0.75, H * 0.55), (W * 0.5, H), (W * 0.1, H)], fill=WATER)
    for k in range(9):
        y = H * 0.6 + k * 40
        x0 = W * 0.62 - k * 50
        d.arc([x0 - 60, y - 10, x0 + 60, y + 10], 0, 180, fill=WATER2, width=4)
    # the cut cords, drifting
    for k in range(4):
        x, y = W * 0.34 + k * 36, H * 0.84 - k * 18
        d.line([(x, y), (x + 40, y - 12)], fill=(200, 180, 120), width=5)
    # Vasishtha on the bank, set down, alive
    figure(d, W * 0.72, H * 0.92, 290, robe=(232, 120, 40), skin=(190, 140, 95), seated=True)
    d.chord([W * 0.72 - 30, H * 0.92 - 290 * 0.8, W * 0.72 + 30, H * 0.92 - 290 * 0.55], 0, 180, fill=(230, 230, 230))
    # Adrishyanti, coming along the bank
    figure(d, W * 0.90, H * 0.95, 230, robe=(200, 150, 90), skin=(210, 160, 110))
    save(img, "44_parashara")


# 46. The potter's house — "we brought alms"
def bhiksha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (240, 170, 110), (120, 70, 90), 0, int(H * 0.7))
    d.rectangle([0, H * 0.7, W, H], fill=(170, 130, 90))
    # the house
    d.rectangle([W * 0.46, H * 0.36, W * 0.96, H * 0.84], fill=(200, 150, 100), outline=(120, 80, 50), width=5)
    d.polygon([(W * 0.42, H * 0.38), (W * 0.71, H * 0.16), (W, H * 0.38)], fill=(150, 90, 50))
    d.rectangle([W * 0.60, H * 0.52, W * 0.74, H * 0.84], fill=(70, 40, 30))
    # Kunti inside, back turned, at her work
    figure(d, W * 0.67, H * 0.82, 170, robe=(240, 235, 225), skin=(200, 150, 100))
    # the potter's wheel and pots
    d.ellipse([W * 0.80, H * 0.78, W * 0.92, H * 0.82], fill=(110, 70, 40))
    for x, r in ((0.84, 34), (0.90, 26), (0.94, 30)):
        pot(d, W * x, H * 0.90, r)
    # at the door — Bhima, Arjuna, and her
    figure(d, W * 0.22, H * 0.94, 350, robe=(52, 92, 62), skin=(206, 156, 106))
    figure(d, W * 0.34, H * 0.94, 310, robe=(60, 90, 170), skin=(200, 150, 100))
    figure(d, W * 0.46, H * 0.94, 280, robe=(170, 30, 60), skin=(150, 110, 90))
    d.arc([W * 0.46 - 44, H * 0.94 - 280 * 0.66, W * 0.46 + 44, H * 0.94 - 280 * 0.48], 0, 180, fill=(255, 190, 70), width=8)
    save(img, "46_bhiksha")


# 47. The test — past the ploughs and the jewels, straight to the weapons
def pariksha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (246, 232, 200), (230, 200, 150))
    d.rectangle([0, H * 0.08, W, H * 0.13], fill=RED)
    for x in (0.03, 0.97):
        d.rectangle([W * x - 22, H * 0.13, W * x + 22, H * 0.78], fill=(200, 160, 110), outline=DGOLD, width=3)
    d.rectangle([0, H * 0.78, W, H], fill=(200, 170, 120))
    # three tables
    for x0, x1 in ((0.07, 0.30), (0.37, 0.60), (0.67, 0.93)):
        d.rectangle([W * x0, H * 0.62, W * x1, H * 0.66], fill=BROWN)
    # ploughs and grain
    d.line([(W * 0.10, H * 0.60), (W * 0.22, H * 0.52)], fill=BROWN, width=10)
    d.polygon([(W * 0.22, H * 0.52), (W * 0.26, H * 0.60), (W * 0.20, H * 0.60)], fill=(130, 130, 140))
    for k in range(3):
        d.ellipse([W * 0.12 + k * 40, H * 0.57, W * 0.12 + k * 40 + 30, H * 0.62], fill=(220, 190, 110))
    # ornaments
    for k in range(4):
        d.ellipse([W * 0.40 + k * 70, H * 0.56, W * 0.40 + k * 70 + 46, H * 0.61], outline=GOLD, width=6)
    # weapons
    for k in range(3):
        d.line([(W * 0.70 + k * 60, H * 0.61), (W * 0.72 + k * 60, H * 0.40)], fill=(170, 170, 180), width=8)
    bow(d, W * 0.88, H * 0.50, 60, DGOLD, arrow=False)
    # the five brothers, all at the weapons table
    for x, hh, robe in ((0.64, 280, (27, 37, 64)), (0.71, 320, (52, 92, 62)), (0.78, 290, (60, 90, 170)),
                        (0.85, 250, (120, 110, 60)), (0.92, 250, (120, 110, 60))):
        figure(d, W * x, H * 0.97, hh, robe=robe, skin=(200, 150, 100))
    # Drupada watching from the left
    figure(d, W * 0.18, H * 0.96, 270, robe=(120, 60, 110), skin=(200, 150, 100))
    crown_on(d, W * 0.18, H * 0.96 - 270 * 0.86)
    save(img, "47_pariksha")


# 48. The five Indras — the cave on the mountain
def five_indras():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (150, 180, 220), (220, 230, 240), 0, int(H * 0.6))
    d.polygon([(0, H * 0.7), (W * 0.3, H * 0.12), (W * 0.6, H * 0.62), (W * 0.8, H * 0.3), (W, H * 0.58), (W, H), (0, H)],
              fill=(130, 130, 150))
    d.polygon([(W * 0.3, H * 0.12), (W * 0.22, H * 0.28), (W * 0.38, H * 0.28)], fill=WHITE)
    d.polygon([(W * 0.8, H * 0.3), (W * 0.74, H * 0.42), (W * 0.86, H * 0.42)], fill=WHITE)
    # the cave, and the four inside it
    d.ellipse([W * 0.16, H * 0.42, W * 0.52, H * 0.90], fill=(40, 34, 50))
    d.ellipse([W * 0.18, H * 0.44, W * 0.50, H * 0.88], fill=(70, 60, 60))
    for x in (0.23, 0.30, 0.37, 0.44):
        figure(d, W * x, H * 0.86, 170, robe=(230, 180, 60), skin=(230, 190, 130))
        crown_on(d, W * x, H * 0.86 - 170 * 0.86, 34)
    # Indra outside, astonished
    figure(d, W * 0.60, H * 0.95, 260, robe=(230, 180, 60), skin=(214, 164, 104))
    crown_on(d, W * 0.60, H * 0.95 - 260 * 0.86)
    # Shiva and the goddess at their dice
    figure(d, W * 0.80, H * 0.86, 200, robe=(240, 235, 225), skin=(90, 120, 180), seated=True)
    figure(d, W * 0.90, H * 0.86, 180, robe=(200, 60, 80), skin=(220, 170, 120), seated=True)
    for k in range(3):
        d.rectangle([W * 0.84 + k * 16, H * 0.88, W * 0.84 + k * 16 + 12, H * 0.90], fill=WHITE, outline=INK)
    # golden lotuses in the river below
    d.rectangle([0, H * 0.93, W, H], fill=WATER)
    for x in (0.08, 0.66, 0.74):
        lotus(d, W * x, H * 0.96, 16, fill=GOLD, outline=DGOLD)
    save(img, "48_five_indras")


# 49. Vidura — the council at Hastinapura
def vidura_sabha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (120, 40, 40), (60, 20, 30))
    d.rectangle([0, H * 0.78, W, H], fill=(90, 60, 50))
    for x in (0.1, 0.3, 0.7, 0.9):
        d.rectangle([W * x - 20, H * 0.05, W * x + 20, H * 0.78], fill=(150, 90, 60), outline=DGOLD, width=3)
    # the throne and the blind king
    d.rectangle([W * 0.43, H * 0.40, W * 0.57, H * 0.80], fill=(200, 150, 60), outline=DGOLD, width=6)
    figure(d, W * 0.50, H * 0.82, 290, robe=(140, 40, 40), skin=(200, 150, 100), seated=True)
    crown_on(d, W * 0.50, H * 0.82 - 290 * 0.92)
    d.rectangle([W * 0.50 - 34, H * 0.82 - 290 * 0.82, W * 0.50 + 34, H * 0.82 - 290 * 0.77], fill=INK)
    # the elders on the left
    for x, robe, beard in ((0.14, (220, 210, 200), True), (0.24, (232, 150, 60), True), (0.34, (240, 225, 190), False)):
        figure(d, W * x, H * 0.96, 270, robe=robe, skin=(200, 150, 100))
        if beard:
            d.chord([W * x - 26, H * 0.96 - 270 * 0.76, W * x + 26, H * 0.96 - 270 * 0.56], 0, 180, fill=(235, 235, 235))
    # Duryodhana and Karna on the right
    figure(d, W * 0.72, H * 0.96, 280, robe=(170, 40, 30), skin=(200, 150, 100))
    crown_on(d, W * 0.72, H * 0.96 - 280 * 0.86)
    figure(d, W * 0.84, H * 0.96, 290, robe=(200, 140, 40), skin=(190, 140, 95))
    save(img, "49_vidura")


# 50. Indraprastha — a white city where a forest was
def indraprastha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 220, 170), (170, 200, 230), 0, int(H * 0.6))
    sun(d, W * 0.84, H * 0.18, 60, (255, 225, 140))
    # the forest still standing at the edge
    for x, hh in ((0.02, 380), (0.08, 320), (0.95, 360)):
        tree(d, W * x, H * 0.70, hh, canopy=(50, 90, 55))
    # walls and gopurams
    d.rectangle([W * 0.12, H * 0.42, W * 0.88, H * 0.70], fill=(246, 242, 230), outline=(190, 180, 160), width=4)
    for k in range(19):
        x = W * 0.12 + k * W * 0.04
        d.rectangle([x, H * 0.39, x + W * 0.02, H * 0.42], fill=(246, 242, 230))
    for x, h in ((0.28, 0.20), (0.5, 0.12), (0.72, 0.20)):
        d.polygon([(W * x - 70, H * 0.42), (W * x - 40, H * h), (W * x + 40, H * h), (W * x + 70, H * 0.42)],
                  fill=(240, 230, 210), outline=DGOLD)
        d.ellipse([W * x - 16, H * h - 26, W * x + 16, H * h + 6], fill=GOLD)
    d.chord([W * 0.46, H * 0.54, W * 0.54, H * 0.78], 180, 360, fill=(90, 60, 40))
    # the moat
    d.rectangle([0, H * 0.72, W, H * 0.82], fill=WATER2)
    for k in range(10):
        d.line([(W * 0.05 + k * W * 0.1, H * 0.77), (W * 0.1 + k * W * 0.1, H * 0.77)], fill=WHITE, width=2)
    d.rectangle([0, H * 0.82, W, H], fill=(120, 150, 90))
    for x in (0.2, 0.35, 0.65, 0.8):
        tree(d, W * x, H * 0.97, 120)
    save(img, "50_indraprastha")


# 51. Sunda and Upasunda — two brothers, one wish
def tilottama():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (120, 90, 140), (230, 160, 140), 0, int(H * 0.6))
    d.polygon([(0, H * 0.6), (W * 0.25, H * 0.4), (W * 0.5, H * 0.56), (W * 0.78, H * 0.36), (W, H * 0.54), (W, H), (0, H)],
              fill=(100, 80, 90))
    d.rectangle([0, H * 0.78, W, H], fill=(90, 110, 70))
    for x in (0.06, 0.94):
        tree(d, W * x, H * 0.82, 300, canopy=(60, 100, 60))
    # the two brothers, maces up
    for x, flip in ((0.30, 1), (0.70, -1)):
        figure(d, W * x, H * 0.96, 380, robe=(100, 20, 25), skin=(110, 80, 70))
        crown_on(d, W * x, H * 0.96 - 380 * 0.86, 52)
        mx = W * x + flip * 90
        d.line([(W * x + flip * 30, H * 0.70), (mx, H * 0.38)], fill=INK, width=12)
        d.ellipse([mx - 34, H * 0.38 - 40, mx + 34, H * 0.38 + 20], fill=(120, 120, 130), outline=INK, width=3)
    # Tilottama between them
    figure(d, W * 0.50, H * 0.96, 300, robe=(220, 120, 150), skin=(230, 180, 130))
    for k in range(6):
        lotus(d, W * (0.40 + k * 0.04), H * 0.99, 10, fill=(250, 200, 210))
    save(img, "51_tilottama")


# 52. Varga — the crocodile that came out an apsara
def varga():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (170, 210, 230), (230, 240, 240), 0, int(H * 0.45))
    gradient(d, (40, 110, 150), (70, 150, 180), int(H * 0.45), int(H * 0.72))
    for k in range(6):
        y = H * 0.5 + k * 36
        d.arc([W * 0.1 + k * 60, y - 12, W * 0.4 + k * 60, y + 12], 180, 360, fill=WHITE, width=3)
    d.rectangle([0, H * 0.72, W, H], fill=(230, 210, 160))
    # the crocodile's tail still in the surf, dragged up
    d.polygon([(W * 0.30, H * 0.76), (W * 0.52, H * 0.72), (W * 0.54, H * 0.80), (W * 0.30, H * 0.82)], fill=(80, 110, 60))
    for k in range(6):
        d.polygon([(W * 0.33 + k * 30, H * 0.76), (W * 0.345 + k * 30, H * 0.735), (W * 0.36 + k * 30, H * 0.755)], fill=(60, 90, 50))
    # Arjuna hauling
    figure(d, W * 0.20, H * 0.97, 330, robe=(60, 90, 170), skin=(200, 150, 100))
    d.line([(W * 0.23, H * 0.78), (W * 0.30, H * 0.78)], fill=(200, 150, 100), width=12)
    # the apsara rising where the head was
    for r in (140, 110, 80):
        d.ellipse([W * 0.62 - r, H * 0.60 - r, W * 0.62 + r, H * 0.60 + r], outline=(255, 230, 160), width=3)
    figure(d, W * 0.62, H * 0.84, 300, robe=(230, 150, 190), skin=(236, 190, 140))
    # four more shapes still in the water
    for x in (0.72, 0.80, 0.87, 0.94):
        d.ellipse([W * x - 40, H * 0.64, W * x + 40, H * 0.68], fill=(60, 90, 60))
    save(img, "52_varga")


# 53. Subhadra — the sannyasi on Raivataka
def subhadra_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (200, 220, 200), (170, 200, 160), 0, int(H * 0.6))
    d.polygon([(0, H * 0.7), (W * 0.35, H * 0.18), (W * 0.7, H * 0.7)], fill=(130, 120, 100))
    d.rectangle([0, H * 0.7, W, H], fill=(130, 160, 100))
    for x, hh in ((0.78, 360), (0.92, 420)):
        tree(d, W * x, H * 0.74, hh)
    # the cave mouth and the sannyasi
    d.chord([W * 0.12, H * 0.46, W * 0.44, H * 0.92], 180, 360, fill=(60, 50, 50))
    d.rectangle([W * 0.12, H * 0.69, W * 0.44, H * 0.72], fill=(60, 50, 50))
    figure(d, W * 0.28, H * 0.90, 290, robe=(220, 110, 40), skin=(200, 150, 100), seated=True)
    d.line([(W * 0.36, H * 0.90), (W * 0.37, H * 0.46)], fill=BROWN, width=8)
    for k in (-1, 0, 1):
        d.line([(W * 0.37, H * 0.47), (W * 0.37 + k * 18, H * 0.42)], fill=BROWN, width=5)
    # Subhadra with flowers and a lamp
    figure(d, W * 0.56, H * 0.96, 300, robe=GOLD, skin=(220, 170, 120))
    d.ellipse([W * 0.52 - 30, H * 0.70, W * 0.52 + 10, H * 0.74], fill=(250, 120, 140))
    flame(d, W * 0.60, H * 0.72, 30, 12)
    # Krishna, watching, amused
    figure(d, W * 0.74, H * 0.96, 270, robe=GOLD, skin=(70, 110, 190))
    crown_on(d, W * 0.74, H * 0.96 - 270 * 0.86)
    d.line([(W * 0.74 + 20, H * 0.96 - 270 * 0.92), (W * 0.74 + 40, H * 0.96 - 270 * 1.02)], fill=(40, 120, 90), width=6)
    save(img, "53_subhadra")


# 54. Harana harika — reins in her hands, the bow in his
def harana():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (140, 190, 230), (230, 220, 190), 0, int(H * 0.62))
    # Dwaraka left behind, by the sea
    d.rectangle([0, H * 0.40, W * 0.32, H * 0.62], fill=(240, 230, 200), outline=DGOLD)
    for x in (0.04, 0.16, 0.28):
        d.polygon([(W * x - 30, H * 0.40), (W * x, H * 0.26), (W * x + 30, H * 0.40)], fill=GOLD)
    d.rectangle([0, H * 0.58, W * 0.32, H * 0.64], fill=WATER2)
    d.rectangle([0, H * 0.62, W, H], fill=(200, 180, 130))
    # dust behind the wheels
    for k in range(8):
        d.ellipse([W * 0.08 + k * 30, H * 0.80 + k * 2, W * 0.16 + k * 30, H * 0.88 + k * 2], fill=(220, 200, 160))
    # the golden chariot, horses in front, running away from the city
    chariot(d, W * 0.40, H * 0.90, 1.4, body=(220, 170, 50))
    for k, x in enumerate((0.64, 0.74)):
        horse(d, W * x, H * 0.86 + k * 12, 1.1)
    # Subhadra driving, Arjuna standing with the bow
    figure(d, W * 0.44, H * 0.74, 190, robe=GOLD, skin=(220, 170, 120))
    d.line([(W * 0.46, H * 0.64), (W * 0.66, H * 0.70)], fill=INK, width=3)
    figure(d, W * 0.35, H * 0.74, 250, robe=(60, 90, 170), skin=(200, 150, 100))
    bow(d, W * 0.30, H * 0.54, 70, DGOLD)
    save(img, "54_harana")


# 55. Gandiva — the day Arjuna got his bow
def gandiva():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 200, 120), (240, 160, 90), 0, int(H * 0.55))
    sun(d, W * 0.5, H * 0.14, 60, (255, 230, 150))
    gradient(d, (40, 70, 120), (30, 60, 100), int(H * 0.55), int(H * 0.75))
    d.rectangle([0, H * 0.75, W, H], fill=(190, 170, 120))
    # the forest across the river, waiting
    for x in (0.6, 0.7, 0.8, 0.9):
        tree(d, W * x, H * 0.56, 200, canopy=(50, 80, 50))
    # Varuna rising out of the water, holding up the bow
    figure(d, W * 0.50, H * 0.74, 260, robe=(40, 90, 140), skin=(90, 130, 190))
    crown_on(d, W * 0.50, H * 0.74 - 260 * 0.86)
    bow(d, W * 0.50, H * 0.30, 120, GOLD, arrow=False)
    # Agni as a brahmin, glowing
    for r in (120, 90):
        d.ellipse([W * 0.20 - r, H * 0.70 - r, W * 0.20 + r, H * 0.70 + r], outline=(250, 150, 60), width=4)
    figure(d, W * 0.20, H * 0.96, 300, robe=(230, 110, 40), skin=(230, 170, 110))
    d.chord([W * 0.20 - 28, H * 0.96 - 300 * 0.78, W * 0.20 + 28, H * 0.96 - 300 * 0.58], 0, 180, fill=(200, 60, 30))
    # Krishna with the discus, Arjuna reaching for the bow
    figure(d, W * 0.72, H * 0.96, 280, robe=GOLD, skin=(70, 110, 190))
    crown_on(d, W * 0.72, H * 0.96 - 280 * 0.86)
    d.ellipse([W * 0.72 + 30, H * 0.56, W * 0.72 + 90, H * 0.62 + 20], outline=GOLD, width=8)
    figure(d, W * 0.84, H * 0.96, 290, robe=(60, 90, 170), skin=(200, 150, 100))
    save(img, "55_gandiva")


# 57. The Sharngakas — four chicks and a promise
def sharngaka():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (60, 40, 50), (180, 80, 40))
    gradient(d, (70, 40, 30), (40, 25, 20), int(H * 0.8), H)
    # fire all round
    for x in (0.06, 0.16, 0.26, 0.74, 0.84, 0.94):
        flame(d, W * x, H * 0.86, 300, 90)
    # the one tree the fire went around
    d.rectangle([W * 0.49, H * 0.40, W * 0.51, H * 0.86], fill=BROWN)
    for cx, cy, r in ((0.5, 0.30, 140), (0.42, 0.38, 100), (0.58, 0.38, 100)):
        d.ellipse([W * cx - r, H * cy - r, W * cx + r, H * cy + r], fill=(40, 100, 55))
    # the nest and the four
    d.chord([W * 0.44, H * 0.40, W * 0.56, H * 0.52], 0, 180, fill=(140, 100, 60))
    for k in range(4):
        bird(d, W * 0.455 + k * 26, H * 0.44, 12, col=(200, 170, 120), wings=False)
    # Jarita, flown up, looking back
    bird(d, W * 0.72, H * 0.18, 40, col=(120, 90, 60))
    save(img, "57_sharngaka")


# 58. Maya — "do not be afraid"
def maya_scene():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (70, 40, 50), (200, 100, 50))
    d.rectangle([0, H * 0.82, W, H], fill=(60, 40, 30))
    for x in (0.04, 0.12, 0.2, 0.28, 0.36):
        flame(d, W * x, H * 0.86, 360, 110)
    # Maya, running out of the fire
    figure(d, W * 0.46, H * 0.95, 290, robe=(90, 70, 50), skin=(150, 105, 70))
    d.line([(W * 0.48, H * 0.72), (W * 0.58, H * 0.64)], fill=(150, 105, 70), width=14)
    # Arjuna, hand raised — abhaya
    figure(d, W * 0.70, H * 0.95, 320, robe=(60, 90, 170), skin=(200, 150, 100))
    d.line([(W * 0.67, H * 0.72), (W * 0.64, H * 0.58)], fill=(200, 150, 100), width=16)
    d.ellipse([W * 0.64 - 22, H * 0.58 - 30, W * 0.64 + 22, H * 0.58 + 6], fill=(200, 150, 100))
    # Krishna, discus lowered
    figure(d, W * 0.86, H * 0.95, 300, robe=GOLD, skin=(70, 110, 190))
    crown_on(d, W * 0.86, H * 0.95 - 300 * 0.86)
    d.ellipse([W * 0.86 + 30, H * 0.74, W * 0.86 + 90, H * 0.80 + 20], outline=GOLD, width=8)
    save(img, "58_maya")


# ---------------------------------------------------------------------------
# Sabha Parva — two halls: the one Maya built, and the one built for dice.
# ---------------------------------------------------------------------------

def hall(d, top=(120, 40, 40), bottom=(60, 20, 30), floor=(90, 60, 50), cols=(0.1, 0.3, 0.7, 0.9)):
    gradient(d, top, bottom)
    d.rectangle([0, H * 0.78, W, H], fill=floor)
    for x in cols:
        d.rectangle([W * x - 20, H * 0.05, W * x + 20, H * 0.78], fill=(150, 90, 60), outline=DGOLD, width=3)


def dice(d, cx, cy, s=22):
    d.rectangle([cx - s, cy - s, cx + s, cy + s], fill=WHITE, outline=INK, width=3)
    for dx, dy in ((-0.45, -0.45), (0, 0), (0.45, 0.45)):
        d.ellipse([cx + dx * s - 5, cy + dy * s - 5, cx + dx * s + 5, cy + dy * s + 5], fill=INK)


def king(d, x, base, h, robe, skin=(200, 150, 100), seated=False):
    figure(d, x, base, h, robe=robe, skin=skin, seated=seated)
    crown_on(d, x, base - h * (0.92 if seated else 0.86), 40 * h / 280)


# S1. Maya's hall — the pool of sapphires
def s_mayasabha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 240, 220), (230, 210, 170))
    for k in range(7):
        x = W * (0.06 + k * 0.148)
        d.rectangle([x - 22, H * 0.06, x + 22, H * 0.62], fill=(240, 230, 210), outline=GOLD, width=4)
        d.ellipse([x - 30, H * 0.04, x + 30, H * 0.10], fill=GOLD)
    d.rectangle([0, H * 0.62, W, H], fill=(236, 226, 206))
    # the pool that is not water
    d.ellipse([W * 0.2, H * 0.68, W * 0.8, H * 0.96], fill=(40, 70, 150), outline=GOLD, width=6)
    for x, c in ((0.3, (200, 40, 60)), (0.42, (240, 240, 250)), (0.56, (200, 40, 60)), (0.68, (240, 240, 250))):
        lotus(d, W * x, H * 0.82, 22, fill=c, outline=DGOLD)
    for x in (0.36, 0.5, 0.62):
        d.polygon([(W * x, H * 0.88), (W * x + 40, H * 0.86), (W * x + 40, H * 0.90)], fill=(220, 230, 250))
    bird(d, W * 0.25, H * 0.66, 22, col=WHITE, wings=False)
    bird(d, W * 0.74, H * 0.66, 22, col=WHITE, wings=False)
    save(img, "s01_mayasabha")


# S2. Narada's questions
def s_narada():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (246, 232, 200), (230, 200, 150), (200, 170, 120))
    king(d, W * 0.62, H * 0.90, 300, (27, 37, 64), seated=True)
    figure(d, W * 0.34, H * 0.95, 320, robe=(240, 225, 190), skin=(214, 164, 104))
    d.ellipse([W * 0.34 - 30, H * 0.95 - 320 * 0.98, W * 0.34 + 30, H * 0.95 - 320 * 0.84], fill=(90, 70, 50))
    # the vina
    d.line([(W * 0.26, H * 0.40), (W * 0.40, H * 0.80)], fill=BROWN, width=10)
    d.ellipse([W * 0.24, H * 0.34, W * 0.30, H * 0.44], fill=(150, 90, 50))
    d.ellipse([W * 0.37, H * 0.76, W * 0.44, H * 0.86], fill=(150, 90, 50))
    for k in range(4):
        d.line([(W * 0.46 + k * 30, H * 0.30 + k * 8), (W * 0.50 + k * 30, H * 0.30 + k * 8)], fill=DGOLD, width=4)
    save(img, "s02_narada")


# S3. The halls of the world-guardians; Pandu in Yama's hall
def s_lokapala():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (30, 40, 90), (120, 100, 160))
    stars(d, 100, H * 0.4)
    for k, (x, c) in enumerate(((0.12, (230, 190, 90)), (0.31, (90, 60, 120)), (0.5, (60, 120, 170)), (0.69, (200, 170, 60)), (0.88, (240, 150, 150)))):
        y = H * (0.36 if k % 2 else 0.30)
        d.ellipse([W * x - 110, y + 70, W * x + 110, y + 110], fill=(240, 240, 250))
        d.rectangle([W * x - 80, y - 60, W * x + 80, y + 90], fill=c, outline=GOLD, width=4)
        d.polygon([(W * x - 90, y - 60), (W * x, y - 120), (W * x + 90, y - 60)], fill=GOLD)
    # Pandu, small, in Yama's hall
    figure(d, W * 0.31, H * 0.36 + 80, 110, robe=(27, 37, 64), skin=(200, 150, 100))
    d.rectangle([0, H * 0.8, W, H], fill=(60, 50, 80))
    figure(d, W * 0.5, H * 0.98, 220, robe=(240, 225, 190), skin=(214, 164, 104))
    save(img, "s03_lokapala")


# S4. Krishna's counsel
def s_mantra():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (240, 220, 180), (210, 170, 120), (180, 140, 100))
    figure(d, W * 0.50, H * 0.92, 320, robe=GOLD, skin=(70, 110, 190))
    crown_on(d, W * 0.50, H * 0.92 - 320 * 0.86)
    king(d, W * 0.28, H * 0.92, 290, (27, 37, 64), seated=True)
    figure(d, W * 0.70, H * 0.95, 360, robe=(52, 92, 62), skin=(206, 156, 106))
    figure(d, W * 0.82, H * 0.95, 320, robe=(60, 90, 170), skin=(200, 150, 100))
    bow(d, W * 0.86, H * 0.52, 60, DGOLD, arrow=False)
    save(img, "s04_mantra")


# S5. Jara joins the two halves at the crossroads
def s_jara():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (14, 18, 46), (40, 36, 70))
    stars(d, 120, H * 0.55)
    d.ellipse([W * 0.84 - 46, H * 0.12 - 46, W * 0.84 + 46, H * 0.12 + 46], fill=(236, 232, 210))
    d.rectangle([0, H * 0.62, W, H], fill=(70, 60, 60))
    d.polygon([(W * 0.44, H * 0.62), (W * 0.56, H * 0.62), (W * 0.9, H), (W * 0.1, H)], fill=(110, 95, 80))
    d.polygon([(0, H * 0.78), (W, H * 0.74), (W, H * 0.84), (0, H * 0.88)], fill=(110, 95, 80))
    # the child, whole
    d.ellipse([W * 0.47, H * 0.76, W * 0.53, H * 0.86], fill=(220, 170, 120))
    d.ellipse([W * 0.475, H * 0.70, W * 0.525, H * 0.77], fill=(220, 170, 120))
    for r in (80, 60):
        d.ellipse([W * 0.5 - r, H * 0.78 - r, W * 0.5 + r, H * 0.78 + r], outline=(250, 220, 140), width=3)
    # Jara bending over it
    figure(d, W * 0.62, H * 0.96, 330, robe=(90, 70, 80), skin=(150, 110, 90))
    d.line([(W * 0.60, H * 0.72), (W * 0.54, H * 0.78)], fill=(150, 110, 90), width=14)
    # the palace behind
    d.rectangle([W * 0.04, H * 0.30, W * 0.30, H * 0.62], fill=(60, 50, 70), outline=DGOLD)
    d.rectangle([W * 0.14, H * 0.44, W * 0.20, H * 0.54], fill=(250, 200, 100))
    save(img, "s05_jara")


# S6. Girivraja — the drums on Chaityaka
def s_girivraja():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (230, 200, 160), (200, 150, 110), 0, int(H * 0.6))
    for x0, x1, h in ((0, 0.3, 0.3), (0.2, 0.55, 0.22), (0.45, 0.8, 0.34), (0.7, 1.0, 0.26)):
        d.polygon([(W * x0, H * 0.8), (W * (x0 + x1) / 2, H * h), (W * x1, H * 0.8)], fill=(130, 100, 80))
    d.rectangle([0, H * 0.8, W, H], fill=(150, 120, 80))
    # three drums, broken
    for k, x in enumerate((0.48, 0.56, 0.64)):
        d.ellipse([W * x - 44, H * 0.30, W * x + 44, H * 0.40], fill=(140, 90, 50), outline=INK, width=3)
        d.rectangle([W * x - 44, H * 0.35, W * x + 44, H * 0.46], fill=(150, 100, 60))
        d.line([(W * x - 30, H * 0.32), (W * x + 20, H * 0.44)], fill=INK, width=4)
    figure(d, W * 0.40, H * 0.62, 220, robe=(52, 92, 62), skin=(206, 156, 106))
    d.line([(W * 0.42, H * 0.46), (W * 0.47, H * 0.36)], fill=(206, 156, 106), width=14)
    figure(d, W * 0.72, H * 0.62, 200, robe=(60, 90, 170), skin=(200, 150, 100))
    figure(d, W * 0.80, H * 0.64, 200, robe=GOLD, skin=(70, 110, 190))
    save(img, "s06_girivraja")


# S7. The wrestling — Bhima lifts Jarasandha
def s_mallayuddha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (240, 200, 150), (210, 150, 100))
    d.ellipse([W * 0.1, H * 0.74, W * 0.9, H * 1.05], fill=(190, 150, 100), outline=(150, 110, 70), width=5)
    for k in range(10):
        x = W * (0.05 + k * 0.1)
        figure(d, x, H * 0.80 + (k % 2) * 10, 130, robe=[(150, 90, 60), (90, 110, 70), (120, 70, 110)][k % 3], skin=(200, 150, 100))
    # Bhima, arms up
    figure(d, W * 0.5, H * 0.96, 380, robe=(52, 92, 62), skin=(206, 156, 106))
    d.line([(W * 0.47, H * 0.70), (W * 0.44, H * 0.44)], fill=(206, 156, 106), width=22)
    d.line([(W * 0.53, H * 0.70), (W * 0.56, H * 0.44)], fill=(206, 156, 106), width=22)
    # Jarasandha, lifted overhead
    d.ellipse([W * 0.34, H * 0.30, W * 0.66, H * 0.44], fill=(120, 50, 40))
    d.ellipse([W * 0.64, H * 0.30, W * 0.70, H * 0.40], fill=(190, 140, 95))
    # motion arcs
    for r in (300, 340):
        d.arc([W * 0.5 - r, H * 0.37 - r * 0.35, W * 0.5 + r, H * 0.37 + r * 0.35], 200, 340, fill=WHITE, width=3)
    save(img, "s07_mallayuddha")


# S8. Digvijaya — four chariots to four quarters
def s_digvijaya():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (200, 220, 240), (240, 230, 200))
    d.rectangle([0, H * 0.6, W, H], fill=(170, 170, 110))
    # the city at the centre
    d.rectangle([W * 0.42, H * 0.46, W * 0.58, H * 0.64], fill=(246, 242, 230), outline=DGOLD, width=3)
    d.polygon([(W * 0.46, H * 0.46), (W * 0.5, H * 0.36), (W * 0.54, H * 0.46)], fill=GOLD)
    # four roads, four chariots
    for (x, y), c in (((0.14, 0.66), (60, 90, 170)), ((0.86, 0.66), (52, 92, 62)), ((0.30, 0.90), (120, 110, 60)), ((0.70, 0.90), (120, 110, 60))):
        d.line([(W * 0.5, H * 0.64), (W * x, H * y)], fill=(210, 190, 140), width=26)
        chariot(d, W * x, H * y, 0.7, body=c)
    for x, y in ((0.06, 0.22), (0.94, 0.22)):
        d.polygon([(W * x - 60, H * 0.6), (W * x, H * y), (W * x + 60, H * 0.6)], fill=(150, 150, 170))
    save(img, "s08_digvijaya")


# S9. The Rajasuya
def s_rajasuya():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (250, 220, 170), (230, 180, 120), (200, 160, 110), cols=(0.05, 0.95))
    d.rectangle([0, H * 0.05, W, H * 0.1], fill=RED)
    d.polygon([(W * 0.40, H * 0.84), (W * 0.60, H * 0.84), (W * 0.57, H * 0.74), (W * 0.43, H * 0.74)], fill=(160, 110, 70), outline=INK)
    flame(d, W * 0.5, H * 0.76, 220, 100)
    king(d, W * 0.5, H * 0.98, 200, (27, 37, 64), seated=True)
    for x in (0.18, 0.28, 0.72, 0.82):
        figure(d, W * x, H * 0.92, 230, robe=(232, 120, 40), skin=(190, 140, 95), seated=True)
    # the heaps of tribute
    for x in (0.10, 0.90):
        for k in range(4):
            d.ellipse([W * x - 60 + k * 10, H * 0.70 - k * 22, W * x + 60 - k * 10, H * 0.78 - k * 22], fill=GOLD, outline=DGOLD)
    save(img, "s09_rajasuya")


# S10. Agra-puja — the first honour
def s_agrapuja():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (250, 225, 180), (225, 185, 130), (200, 160, 110))
    figure(d, W * 0.40, H * 0.95, 320, robe=GOLD, skin=(70, 110, 190))
    crown_on(d, W * 0.40, H * 0.95 - 320 * 0.86)
    king(d, W * 0.56, H * 0.95, 290, (27, 37, 64))
    d.ellipse([W * 0.47, H * 0.64, W * 0.51, H * 0.68], fill=GOLD, outline=DGOLD)
    # Shishupala, standing up in protest
    king(d, W * 0.84, H * 0.95, 320, (150, 40, 60))
    d.line([(W * 0.82, H * 0.70), (W * 0.74, H * 0.60)], fill=(200, 150, 100), width=14)
    for x in (0.14, 0.22):
        figure(d, W * x, H * 0.90, 200, robe=(220, 210, 200), skin=(200, 150, 100), seated=True)
    save(img, "s10_agrapuja")


# S11. Shishupala's birth — the extra arms fall away in Krishna's lap
def s_shishupala_janana():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (240, 210, 170), (200, 160, 120), (170, 130, 90), cols=(0.06, 0.94))
    figure(d, W * 0.44, H * 0.92, 300, robe=GOLD, skin=(70, 110, 190), seated=True)
    # the baby in his lap
    d.ellipse([W * 0.41, H * 0.70, W * 0.49, H * 0.76], fill=(220, 170, 120))
    d.ellipse([W * 0.48, H * 0.68, W * 0.52, H * 0.74], fill=(220, 170, 120))
    # two small arms falling away
    for dx in (-0.03, 0.05):
        d.line([(W * (0.45 + dx), H * 0.80), (W * (0.45 + dx) + 10, H * 0.88)], fill=(220, 170, 120), width=8)
    # the mother, afraid
    figure(d, W * 0.66, H * 0.96, 300, robe=(120, 60, 110), skin=(210, 160, 110))
    d.line([(W * 0.63, H * 0.70), (W * 0.56, H * 0.66)], fill=(210, 160, 110), width=12)
    figure(d, W * 0.24, H * 0.96, 300, robe=(60, 90, 160), skin=(220, 180, 140))
    crown_on(d, W * 0.24, H * 0.96 - 300 * 0.86)
    save(img, "s11_shishupala_janana")


# S12. The discus
def s_sudarshana():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (140, 60, 50), (80, 30, 30), (90, 60, 50))
    figure(d, W * 0.28, H * 0.95, 340, robe=GOLD, skin=(70, 110, 190))
    crown_on(d, W * 0.28, H * 0.95 - 340 * 0.86)
    d.line([(W * 0.31, H * 0.70), (W * 0.38, H * 0.56)], fill=(70, 110, 190), width=14)
    # the discus in flight
    cx, cy = W * 0.58, H * 0.48
    for r, c in ((70, GOLD), (54, (255, 230, 150)), (20, DGOLD)):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=c, width=8)
    for k in range(12):
        a = k * math.pi / 6
        d.line([(cx + 20 * math.cos(a), cy + 20 * math.sin(a)), (cx + 70 * math.cos(a), cy + 70 * math.sin(a))], fill=GOLD, width=4)
    for k in range(5):
        d.line([(W * 0.40 + k * 20, H * 0.54 - k * 2), (W * 0.46 + k * 20, H * 0.52 - k * 2)], fill=(255, 230, 150), width=3)
    king(d, W * 0.82, H * 0.95, 330, (150, 40, 60))
    save(img, "s12_sudarshana")


# S13. Duryodhana in Maya's hall
def s_duryodhana_sabha():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (250, 240, 220), (230, 210, 170))
    for k in range(5):
        x = W * (0.08 + k * 0.21)
        d.rectangle([x - 22, H * 0.06, x + 22, H * 0.62], fill=(240, 230, 210), outline=GOLD, width=4)
    d.rectangle([0, H * 0.62, W, H], fill=(236, 226, 206))
    d.ellipse([W * 0.26, H * 0.70, W * 0.74, H * 0.98], fill=(60, 110, 170), outline=GOLD, width=6)
    # Duryodhana, soaked, climbing out
    king(d, W * 0.50, H * 0.90, 280, (170, 40, 30))
    for k in range(6):
        d.line([(W * 0.46 + k * 14, H * 0.66), (W * 0.46 + k * 14, H * 0.72)], fill=(120, 170, 230), width=3)
    # laughter at the edge
    figure(d, W * 0.84, H * 0.96, 340, robe=(52, 92, 62), skin=(206, 156, 106))
    figure(d, W * 0.93, H * 0.96, 240, robe=(150, 130, 100), skin=(200, 150, 100))
    figure(d, W * 0.12, H * 0.96, 240, robe=(150, 130, 100), skin=(200, 150, 100))
    save(img, "s13_duryodhana_sabha")


# S14. Shakuni shows the dice
def s_shakuni():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (100, 40, 50), (50, 20, 30), (80, 50, 40))
    d.rectangle([W * 0.44, H * 0.40, W * 0.56, H * 0.80], fill=(200, 150, 60), outline=DGOLD, width=6)
    king(d, W * 0.50, H * 0.82, 280, (140, 40, 40), seated=True)
    d.rectangle([W * 0.50 - 34, H * 0.82 - 280 * 0.82, W * 0.50 + 34, H * 0.82 - 280 * 0.77], fill=INK)
    figure(d, W * 0.30, H * 0.96, 310, robe=(80, 60, 90), skin=(200, 150, 100))
    d.line([(W * 0.33, H * 0.72), (W * 0.40, H * 0.64)], fill=(200, 150, 100), width=12)
    dice(d, W * 0.41, H * 0.62, 18)
    dice(d, W * 0.44, H * 0.66, 18)
    king(d, W * 0.72, H * 0.96, 290, (170, 40, 30))
    save(img, "s14_shakuni")


# S15. The game
def s_dyutam():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (110, 40, 45), (60, 20, 30), (100, 70, 55))
    d.rectangle([W * 0.30, H * 0.74, W * 0.70, H * 0.82], fill=(170, 120, 70), outline=DGOLD, width=4)
    for k in range(6):
        d.line([(W * 0.32 + k * W * 0.065, H * 0.745), (W * 0.32 + k * W * 0.065, H * 0.815)], fill=DGOLD, width=2)
    for x, y in ((0.46, 0.70), (0.52, 0.68), (0.56, 0.71)):
        dice(d, W * x, H * y, 16)
    figure(d, W * 0.22, H * 0.94, 300, robe=(80, 60, 90), skin=(200, 150, 100), seated=True)
    king(d, W * 0.78, H * 0.94, 300, (27, 37, 64), seated=True)
    # the watchers, heavy
    for x, robe in ((0.08, (220, 210, 200)), (0.92, (240, 225, 190))):
        figure(d, W * x, H * 0.96, 260, robe=robe, skin=(200, 150, 100))
    save(img, "s15_dyutam")


# S16. Draupadi's question
def s_draupadi_prashna():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (110, 40, 45), (60, 20, 30), (100, 70, 55))
    figure(d, W * 0.50, H * 0.96, 360, robe=(170, 30, 60), skin=(150, 110, 90))
    # loosened hair
    d.polygon([(W * 0.50 - 40, H * 0.96 - 360 * 0.82), (W * 0.50 + 40, H * 0.96 - 360 * 0.82),
               (W * 0.50 + 60, H * 0.96 - 360 * 0.40), (W * 0.50 - 60, H * 0.96 - 360 * 0.40)], fill=(30, 20, 20))
    d.ellipse([W * 0.50 - 40, H * 0.96 - 360 * 0.86, W * 0.50 + 40, H * 0.96 - 360 * 0.64], fill=(150, 110, 90))
    d.line([(W * 0.53, H * 0.70), (W * 0.60, H * 0.56)], fill=(150, 110, 90), width=14)
    for x in (0.16, 0.26):
        figure(d, W * x, H * 0.92, 240, robe=(220, 210, 200), skin=(200, 150, 100), seated=True)
    for x in (0.74, 0.82, 0.90):
        figure(d, W * x, H * 0.92, 230, robe=(27, 37, 64), skin=(200, 150, 100), seated=True)
    save(img, "s16_draupadi_prashna")


# S17. The endless cloth
def s_vastra():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (110, 40, 45), (60, 20, 30), (100, 70, 55))
    for r in (230, 190, 150):
        d.ellipse([W * 0.36 - r * 0.6, H * 0.58 - r, W * 0.36 + r * 0.6, H * 0.58 + r], outline=(255, 220, 150), width=3)
    figure(d, W * 0.36, H * 0.96, 360, robe=(230, 150, 40), skin=(150, 110, 90))
    # the heap of cloth, many colours
    cols = [(200, 40, 60), (240, 200, 60), (60, 140, 90), (60, 90, 170), (240, 240, 230), (160, 60, 140)]
    for k in range(14):
        c = cols[k % len(cols)]
        y = H * 0.94 - k * 16
        d.ellipse([W * 0.50 + (k % 3) * 20, y - 20, W * 0.72 - (k % 2) * 20, y + 10], fill=c)
    # a long band still coming off her
    d.line([(W * 0.40, H * 0.72), (W * 0.52, H * 0.66), (W * 0.62, H * 0.70)], fill=(240, 200, 60), width=18)
    # Dushasana, slumped
    figure(d, W * 0.84, H * 0.96, 260, robe=(170, 40, 30), skin=(200, 150, 100), seated=True)
    save(img, "s17_vastra")


# S18. The boons — omens over the hall
def s_varalu():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    hall(d, (70, 40, 60), (40, 20, 30), (80, 55, 45))
    king(d, W * 0.46, H * 0.90, 290, (140, 40, 40), seated=True)
    d.rectangle([W * 0.46 - 34, H * 0.90 - 290 * 0.82, W * 0.46 + 34, H * 0.90 - 290 * 0.77], fill=INK)
    figure(d, W * 0.60, H * 0.95, 280, robe=(90, 60, 90), skin=(210, 160, 110))
    d.rectangle([W * 0.60 - 28, H * 0.95 - 280 * 0.80, W * 0.60 + 28, H * 0.95 - 280 * 0.74], fill=WHITE)
    figure(d, W * 0.28, H * 0.96, 320, robe=(170, 30, 60), skin=(150, 110, 90))
    figure(d, W * 0.76, H * 0.96, 270, robe=(240, 225, 190), skin=(200, 150, 100))
    # the jackal at the window
    d.rectangle([W * 0.84, H * 0.16, W * 0.96, H * 0.36], fill=(30, 20, 40), outline=DGOLD)
    d.polygon([(W * 0.86, H * 0.34), (W * 0.90, H * 0.24), (W * 0.93, H * 0.30), (W * 0.95, H * 0.34)], fill=(150, 110, 70))
    save(img, "s18_varalu")


# S19. Into the forest
def s_vanavasa():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (120, 110, 130), (200, 170, 140), 0, int(H * 0.6))
    d.rectangle([0, H * 0.6, W, H], fill=(140, 130, 90))
    for x, hh in ((0.72, 380), (0.82, 440), (0.92, 400), (0.99, 360)):
        tree(d, W * x, H * 0.66, hh, canopy=(50, 80, 55))
    # Hastinapura behind, on the left
    d.rectangle([0, H * 0.36, W * 0.16, H * 0.60], fill=(220, 210, 190), outline=DGOLD)
    d.polygon([(W * 0.04, H * 0.36), (W * 0.08, H * 0.24), (W * 0.12, H * 0.36)], fill=GOLD)
    # the procession — Dhaumya ahead with grass in hand
    walkers = [(0.66, 250, (232, 120, 40)), (0.56, 280, (190, 160, 110)), (0.49, 340, (190, 160, 110)),
               (0.42, 300, (190, 160, 110)), (0.35, 260, (190, 160, 110)), (0.29, 260, (190, 160, 110)),
               (0.22, 270, (140, 20, 40))]
    for x, hh, robe in walkers:
        figure(d, W * x, H * 0.95, hh, robe=robe, skin=(200, 150, 100))
    d.line([(W * 0.68, H * 0.72), (W * 0.72, H * 0.62)], fill=(140, 170, 80), width=5)
    d.rectangle([W * 0.56 - 24, H * 0.95 - 280 * 0.86, W * 0.56 + 24, H * 0.95 - 280 * 0.70], fill=(240, 235, 225))
    # her hair loose
    d.polygon([(W * 0.22 - 26, H * 0.95 - 270 * 0.80), (W * 0.22 + 26, H * 0.95 - 270 * 0.80),
               (W * 0.22 + 38, H * 0.95 - 270 * 0.45), (W * 0.22 - 38, H * 0.95 - 270 * 0.45)], fill=(30, 20, 20))
    d.ellipse([W * 0.22 - 24, H * 0.95 - 270 * 0.86, W * 0.22 + 24, H * 0.95 - 270 * 0.64], fill=(150, 110, 90))
    save(img, "s19_vanavasa")


SCENES = [nannaya, naimisharanya, cover, parva_sangraha, sarama, udanka, janamejaya,
          pauloma, ruru, kadru_vinata, garuda, parikshit, sarpa,
          uparichara, bhubharam, kacha, devayani, yayati, puru,
          shakuntala, bharata_scene, vasus, ganga, bhishma, amba, vyasa_niyoga,
          karna_janana, pandu_shapam, pandava_birth, kaurava_janana,
          drona_scene, ekalavya_scene, ranga_bhumi,
          drupada_scene, yuvaraja, lakshagriha, escape_scene,
          hidimbi_scene, bakasura_scene,
          yajnasena, angaraparna, tapati, nandini, vipasha, swayamvara,
          bhiksha, pariksha, five_indras,
          vidura_sabha, indraprastha, tilottama, varga, subhadra_scene, harana,
          gandiva, khandava, sharngaka, maya_scene,
          # Sabha Parva
          s_mayasabha, s_narada, s_lokapala, s_mantra, s_jara, s_girivraja, s_mallayuddha,
          s_digvijaya, s_rajasuya, s_agrapuja, s_shishupala_janana, s_sudarshana,
          s_duryodhana_sabha, s_shakuni, s_dyutam, s_draupadi_prashna, s_vastra, s_varalu, s_vanavasa]
for f in SCENES:
    f()
print(len(SCENES), 'illustrations ->', OUT)
