"""App icons for the installed site — same palm-leaf mark as the favicon.
Regenerate with: python3 draw_appicons.py"""
from PIL import Image, ImageDraw
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site_src", "appicons")
os.makedirs(OUT, exist_ok=True)
INDIGO=(27,37,64); CLOTH=(243,237,223); LEAF=(234,217,168); MADDER=(142,43,30); TURMERIC=(217,162,27)

def mark(S, pad_frac=0.0, bleed=False):
    """pad_frac leaves room for the safe area a maskable icon needs."""
    im = Image.new("RGB", (S, S), INDIGO); d = ImageDraw.Draw(im)
    if not bleed:
        d.ellipse([S*0.02, S*0.02, S*0.98, S*0.98], fill=INDIGO)
    inset = pad_frac * S
    c = S / 2
    r = (S / 2 - inset) * 0.84
    d.ellipse([c-r, c-r, c+r, c+r], fill=CLOTH)
    # palm-leaf manuscript, bound with a cord
    w, h = r*0.80, r*0.40
    d.rounded_rectangle([c-w, c-h, c+w, c+h], radius=max(2, int(S*0.02)),
                        fill=LEAF, outline=MADDER, width=max(2, int(S*0.016)))
    for k in (-1, 1):
        y = c + k * h * 0.42
        d.line([(c-w*0.74, y), (c+w*0.74, y)], fill=MADDER, width=max(1, int(S*0.011)))
    d.line([(c, c-h*1.55), (c, c+h*1.55)], fill=MADDER, width=max(2, int(S*0.018)))
    rr = r*0.17
    d.ellipse([c-rr, c-rr, c+rr, c+rr], fill=TURMERIC, outline=MADDER, width=max(2, int(S*0.014)))
    return im

for size, name, pad, bleed in [(192,"icon-192.png",0.0,False), (512,"icon-512.png",0.0,False),
                               (512,"icon-maskable-512.png",0.11,True), (180,"apple-touch-icon.png",0.0,True)]:
    mark(size, pad, bleed).save(os.path.join(OUT, name), optimize=True)
    print("wrote", name, size)
