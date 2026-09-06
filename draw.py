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
    save(img, "02_vyasa_ganapati")


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
    save(img, "11_sarpa_yagna")


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
    save(img, "12_ganga_shantanu")


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
    save(img, "13_bhishma_pratigna")


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
    save(img, "14_pandava_janana")


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
    save(img, "15_gurukulam")


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
    save(img, "16_lakshagriha")


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
    save(img, "17_swayamvara")


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
    save(img, "18_khandava_dahanam")


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
    save(img, "01_naimisharanya")


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
    save(img, "03_parva_sangraha")


# 4. Utanka — the nagaloka descent, the horse of fire, the stolen earrings
def uttanka():
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
    save(img, "04_uttanka")


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
    save(img, "05_janamejaya")


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
    save(img, "06_pauloma")


# 7. Ruru — the lifted stick, and the snake that spoke
def ruru():
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    gradient(d, (200, 220, 175), (150, 175, 120), 0, int(H * 0.60))
    d.rectangle([0, H * 0.60, W, H], fill=(120, 150, 95))
    for x, hh in [(0.05, 430), (0.16, 350), (0.88, 420), (0.97, 340)]:
        tree(d, W * x, H * 0.66, hh)
    # Ruru, stick raised — then held
    figure(d, W * 0.32, H * 0.86, 250, robe=CREAM, skin=(200, 150, 100))
    d.line([(W * 0.36, H * 0.70), (W * 0.46, H * 0.44)], fill=BROWN, width=13)
    # the dundubha, harmless, speaking
    pts = [(W * (0.56 + i * 0.011), H * 0.80 + 40 * math.sin(i * 0.55)) for i in range(28)]
    d.line(pts, fill=(120, 155, 85), width=22)
    hx, hy = pts[-1]
    d.ellipse([hx - 30, hy - 20, hx + 30, hy + 20], fill=(120, 155, 85))
    d.ellipse([hx + 6, hy - 9, hx + 16, hy + 1], fill=CREAM)
    d.ellipse([hx + 9, hy - 7, hx + 14, hy - 2], fill=INK)
    # a small flower for Pramadvara, alive again
    lotus(d, W * 0.20, H * 0.90, 34)
    save(img, "07_ruru")


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
    save(img, "08_kadru_vinata")


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
    save(img, "09_garuda")


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
    save(img, "10_parikshit")


SCENES = [naimisharanya, cover, parva_sangraha, uttanka, janamejaya, pauloma, ruru,
          kadru_vinata, garuda, parikshit, sarpa, ganga, bhishma, pandava_birth,
          gurukulam, lakshagriha, swayamvara, khandava]
for f in SCENES:
    f()
print(len(SCENES), 'illustrations ->', OUT)
