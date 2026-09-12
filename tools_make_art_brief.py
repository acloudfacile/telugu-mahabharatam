#!/usr/bin/env python3
"""Write notes/portrait-art-brief.md — one house style plus a ready prompt for
every character, generated from the same table that draws the fallback icons,
so the brief can never drift out of step with the site.

  python3 tools_make_art_brief.py
"""
import os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))
# Evaluate the colour constants and the CHARS table out of draw_icons.py.
# Regexes break on the RGB tuples; this cannot drift from the real table.
src = open(os.path.join(ROOT, 'draw_icons.py'), encoding='utf8').read()
ns = {}
for line in src.splitlines():
    if re.match(r'^[A-Z][A-Z0-9_]*\s*=\s*\(?[\d(]', line):
        try: exec(line, ns)
        except Exception: pass
start = src.index('CHARS = [')
end = src.index('\n]\n', start) + 2
exec(src[start:end], ns)
rows = ns['CHARS']

SIDE = {
 'pandava':('Pandava',      'deep indigo ring'),
 'kaurava':('Kaurava',      'madder-red ring'),
 'guru':   ('sage/teacher', 'turmeric-gold ring'),
 'deva':   ('divine',       'bright gold ring'),
 'kuru':   ('Kuru elder',   'muted violet ring'),
 'other':  ('other',        'forest-green ring'),
}
HAIR = {
 'crown': 'a jewelled crown or royal headdress',
 'jata':  'matted ascetic jata coiled on the head, forehead marked with ash',
 'woman': 'long dark hair, centre-parted, gold ornaments and a bindi',
 'turban':'a wound cloth turban',
 'plain': 'plain cropped hair, no crown',
}
ATTR = {
 'bow':'a longbow held upright','mace':'a heavy iron mace resting on the shoulder',
 'chakra':'a flaming discus (chakra)','dice':'gambling dice cupped in one hand',
 'book':'a palm-leaf manuscript bundle','sun':'a solar disc glowing behind the head',
 'flame':'a ritual flame rising from one palm','serpent':'a hooded serpent coiled at the shoulder',
 'axe':'a battle-axe','lotus':'a lotus bloom held at the breast',
 'crown':'a raised sceptre','conch':'a white conch lifted to the lips',
 'water':'water streaming from cupped hands','pen':'an iron stylus and palm leaf',
 'boat':'a river ferry behind the shoulder','tusk':'a single broken tusk',
 'star':'a thunderbolt (vajra)','wing':'great outspread feathered wings',
}

# Image models read Telugu poorly, so the prompt itself is pure English; the
# Telugu name and role sit above it in the brief for the human's reference.
ENGLISH = {
 'vyasa':'Vyasa, the aged sage who composed this epic',
 'ganapati':'Ganesha, the elephant-headed god, acting as scribe',
 'vaishampayana':'Vaishampayana, a sage reciting the epic to a king',
 'sauti':'Ugrashravas the bard, a travelling storyteller',
 'shaunaka':'Shaunaka, an elder sage presiding over a long sacrifice',
 'rajarajanarendra':'Rajaraja Narendra, an 11th-century Telugu king and patron',
 'nannaya':'Nannaya, the first poet of Telugu, stylus in hand',
 'narayanabhatta':'Narayana Bhatta, a scholar-companion to the poet',
 'paila':'Paila, a vedic sage and teacher',
 'shuka':'Shuka, the young ascetic son of Vyasa, radiant and detached',
 'sarama':'Sarama, the divine hound of the gods, luminous and wrathful',
 'udanka':'Udanka, a young brahmin student on a quest',
 'paushya':'King Paushya, a bearded monarch',
 'indra':'Indra, king of the gods, thunderbolt in hand',
 'bhrigu':'Bhrigu, an ancient and severe sage',
 'puloma':'Puloma, wife of the sage Bhrigu',
 'chyavana':'Chyavana, a sage born blazing with light',
 'ruru':'Ruru, a young brahmin, grief turned to anger',
 'pramadvara':'Pramadvara, a young woman restored to life',
 'kadru':'Kadru, mother of the serpent race, hard-faced',
 'vinata':'Vinata, mother of Garuda, held in servitude',
 'aruna':'Aruna, the charioteer of the sun, half-formed and glowing red',
 'vasuki':'Vasuki, king of the serpents, many-hooded',
 'garuda':'Garuda, the great eagle-man, wings outspread',
 'jaratkaru':'Jaratkaru, an ascetic sage, gaunt from fasting',
 'uparichara':'King Uparichara Vasu, a monarch who flew among the gods',
 'adrika':'Adrika, an apsara cursed into the form of a fish',
 'parashara':'Parashara, a powerful sage, father of Vyasa',
 'kacha':'Kacha, a handsome young god-student',
 'shukra':'Shukracharya, preceptor of the asuras, fierce and red-robed',
 'devayani':'Devayani, a proud young brahmin woman',
 'sharmishtha':'Sharmishtha, an asura princess made a servant',
 'vrishaparva':'Vrishaparva, king of the asuras',
 'yayati':'King Yayati, aged by a curse',
 'puru':'Puru, the youngest prince, newly crowned',
 'yadu':'Yadu, an eldest prince who refused his father',
 'brihaspati':'Brihaspati, preceptor of the gods',
 'dushyanta':'King Dushyanta, a hunter-king',
 'shakuntala':'Shakuntala, a forest-raised young woman of great dignity',
 'kanva':'Kanva, a gentle old forest sage',
 'menaka':'Menaka, a celestial dancer',
 'vishvamitra':'Vishvamitra, a royal sage of terrible austerity',
 'vasishtha':'Vasishtha, a serene white-bearded brahmin sage',
 'parikshit':'King Parikshit, last heir of the Kuru line',
 'shamika':'Shamika, an old sage in silent meditation',
 'shringi':'Shringi, a hot-tempered young ascetic',
 'takshaka':'Takshaka, a serpent king in human form, cunning',
 'janamejaya':'King Janamejaya, a young monarch bent on revenge',
 'astika':'Astika, a boy sage of great composure',
 'bharata':'Bharata, a boy-king who gave his name to a country',
 'pratipa':'King Pratipa, an old monarch in meditation',
 'shantanu':'King Shantanu, a handsome monarch',
 'ganga':'Ganga, the river goddess, water-crowned',
 'bhishma':'Bhishma, the aged Kuru patriarch, white-bearded warrior in ornate armour',
 'satyavati':'Satyavati, a fisherwoman who became queen',
 'dasharaja':'Dasharaja, a chief of fisherfolk',
 'chitrangada-k':'Prince Chitrangada, a young Kuru heir',
 'vichitravirya':'Prince Vichitravirya, a frail young king',
 'amba':'Amba, a wronged princess, resolute and cold',
 'dhritarashtra':'Dhritarashtra, the blind Kuru king',
 'pandu':'King Pandu, pale-complexioned monarch',
 'vidura':'Vidura, the wise half-brother and counsellor',
 'gandhari':'Gandhari, a queen who bound her own eyes',
 'kunti':'Kunti, mother of the Pandavas, dignified and sorrowful',
 'madri':'Madri, second queen of Pandu',
 'karna':'Karna, a radiant warrior wearing golden earrings and breastplate',
 'yudhishthira':'Yudhishthira, the eldest Pandava, calm and upright',
 'bhima':'Bhima, the immensely powerful second Pandava',
 'arjuna':'Arjuna, the great archer, blue-tinged and serene',
 'nakula':'Nakula, a handsome young Pandava',
 'sahadeva':'Sahadeva, the youngest Pandava, thoughtful',
 'pandavas':'the five Pandava brothers together',
 'duryodhana':'Duryodhana, the proud eldest Kaurava',
 'dushasana':'Dushasana, a brutal Kaurava prince',
 'shakuni':'Shakuni, a thin scheming uncle with dice',
 'drona':'Dronacharya, a lean ascetic warrior-teacher',
 'kripa':'Kripacharya, an old teacher of arms',
 'parashurama':'Parashurama, the axe-bearing warrior sage',
 'ekalavya':'Ekalavya, a forest-dwelling youth, devoted and maimed',
 'ashvatthama':'Ashvatthama, a fierce young warrior with a gem on his brow',
 'purochana':'Purochana, a furtive royal builder',
 'hidimbi':'Hidimbi, a rakshasa woman of great beauty',
 'ghatotkacha':'Ghatotkacha, a huge half-rakshasa warrior',
 'bakasura':'Bakasura, a monstrous man-eating giant',
 'drupada':'King Drupada of Panchala, proud and bitter',
 'draupadi':'Draupadi, a dark-complexioned princess of great presence',
 'dhrishtadyumna':'Dhrishtadyumna, a warrior born of sacrificial fire',
 'krishna':'Krishna, blue-skinned, peacock-feathered, serene',
 'dhaumya':'Dhaumya, a household priest',
 'ulupi':'Ulupi, a naga princess',
 'chitrangada':'Chitrangada, a warrior princess of Manipura',
 'subhadra':'Subhadra, a gentle young princess',
 'agni':'Agni, the fire god, flame-haired',
 'maya':'Maya, an asura master-architect',
}

HOUSE = """\
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring."""

def prompt(cid, name, role, side, hair, attr, extra):
    bits = [HOUSE, ""]
    en = ENGLISH.get(cid)
    bits.append('Subject: ' + (en if en else cid.replace('-', ' ').title() + ', ' + SIDE[side][0]) + '.')
    look = [HAIR.get(hair, '')]
    if 'beard' in extra:
        look.append('full beard' + (', white with age' if cid in (
            'bhishma','vyasa','drona','kripa','parashurama','pratipa','shaunaka','shamika',
            'bhrigu','chyavana','parashara','shukra','brihaspati','vasishtha','jaratkaru',
            'vishvamitra','kanva','paila','nannaya','narayanabhatta') else ', dark'))
    if 'blindfold' in extra: look.append('eyes bound with a cloth blindfold')
    elif 'blind' in extra:  look.append('eyes closed, sightless')
    bits.append('Appearance: ' + '; '.join(x for x in look if x) + '.')
    if attr: bits.append(f"Holding/marked by: {ATTR.get(attr, attr)}.")
    label, ring = SIDE[side]
    bits.append(f"Ring colour: {ring} ({label}).")
    return '\n'.join(bits)

out = ["""# Portrait art brief

94 characters. The drawn icons in `icons/` are a placeholder that works; this
is how to replace them with real art, one character at a time.

## How to use a finished painting

Save it as `site_src/portraits/<id>.png` — the id is the first column below —
then:

```bash
python3 draw_icons.py     # applies whatever is in portraits/
python3 build_site.py     # publishes it
```

`draw_icons.py` cover-crops to a square biased toward the upper middle,
resizes to 256px, applies the circular mask and draws the side-coloured ring.
Characters with no file keep their drawn icon, so **a half-finished set still
looks like one series**. Supply 512px or larger; 1024 is ideal.

## The house style — paste this above every prompt

```
""" + HOUSE + """
```

Two things make the set cohere, and both matter more than any single portrait:
the **ring colour encodes the character's side** (the site already uses this,
so keep it), and the **crop is always a bust in a circle**. If a generator
drifts on either, the grid stops reading as one work.

## Sources, if you would rather not generate

- **Raja Ravi Varma** (1848–1906) painted many Mahabharata subjects and his
  work is **public domain** — Wikimedia Commons has good scans. This is the
  closest thing to free, legitimate, beautiful art for this project, and it
  already looks like the reference style because that style descends from him.
- **Chitrashala Press** and other pre-1930 Indian oleographs are generally
  public domain in India (life + 60 years). Check each item.
- Anything still in copyright — Amar Chitra Katha, Gita Press, modern film
  art — **cannot** be used. The site is public and forkable; borrowed art
  would make it undistributable, which defeats the point of the whole project.

Check the licence of every file before it goes in the repo, and note the
source in `notes/portrait-credits.md` as you go.

## The 94

| id | character | side | done |
|---|---|---|---|
"""]
rows_sorted = rows
for cid, name, al, role, side, skin, hair, robe, attr, extra in rows_sorted:
    out.append(f"| `{cid}` | {name} | {SIDE[side][0]} | ☐ |")
out.append("\n---\n\n## Prompts\n")
for cid, name, al, role, side, skin, hair, robe, attr, extra in rows_sorted:
    out.append(f"### `{cid}` — {name}\n")
    if role: out.append(f"*{role}*\n")
    out.append("```\n" + prompt(cid, name, role, side, hair, attr, extra) + "\n```\n")

os.makedirs(os.path.join(ROOT, 'notes'), exist_ok=True)
path = os.path.join(ROOT, 'notes', 'portrait-art-brief.md')
open(path, 'w', encoding='utf8').write('\n'.join(out))
print(f'wrote {path} — {len(rows)} characters')
