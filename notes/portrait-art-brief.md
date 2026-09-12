# Portrait art brief

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
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.
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

| `vyasa` | వేదవ్యాసుడు | sage/teacher | ☐ |
| `ganapati` | గణపతి | divine | ☐ |
| `vaishampayana` | వైశంపాయనుడు | sage/teacher | ☐ |
| `sauti` | ఉగ్రశ్రవుడు (సౌతి) | sage/teacher | ☐ |
| `shaunaka` | శౌనకుడు | sage/teacher | ☐ |
| `dushyanta` | దుష్యంతుడు | Kuru elder | ☐ |
| `shakuntala` | శకుంతల | Kuru elder | ☐ |
| `kanva` | కణ్వుడు | sage/teacher | ☐ |
| `menaka` | మేనక | divine | ☐ |
| `vishvamitra` | విశ్వామిత్రుడు | sage/teacher | ☐ |
| `vasishtha` | వసిష్ఠుడు | sage/teacher | ☐ |
| `uparichara` | ఉపరిచర వసువు | Kuru elder | ☐ |
| `adrika` | అద్రిక | other | ☐ |
| `parashara` | పరాశరుడు | sage/teacher | ☐ |
| `kacha` | కచుడు | divine | ☐ |
| `shukra` | శుక్రాచార్యుడు | sage/teacher | ☐ |
| `devayani` | దేవయాని | other | ☐ |
| `sharmishtha` | శర్మిష్ఠ | other | ☐ |
| `vrishaparva` | వృషపర్వుడు | other | ☐ |
| `yayati` | యయాతి | Kuru elder | ☐ |
| `puru` | పూరుడు | Kuru elder | ☐ |
| `yadu` | యదువు | Kuru elder | ☐ |
| `brihaspati` | బృహస్పతి | divine | ☐ |
| `rajarajanarendra` | రాజరాజనరేంద్రుడు | Kuru elder | ☐ |
| `nannaya` | నన్నయ | sage/teacher | ☐ |
| `narayanabhatta` | నారాయణభట్టు | sage/teacher | ☐ |
| `paila` | పైలుడు | sage/teacher | ☐ |
| `shuka` | శుక మహర్షి | sage/teacher | ☐ |
| `sarama` | సరమ | divine | ☐ |
| `udanka` | ఉదంకుడు | sage/teacher | ☐ |
| `paushya` | పౌష్యుడు | other | ☐ |
| `indra` | ఇంద్రుడు | divine | ☐ |
| `bhrigu` | భృగువు | sage/teacher | ☐ |
| `puloma` | పులోమ | other | ☐ |
| `chyavana` | చ్యవనుడు | sage/teacher | ☐ |
| `ruru` | రురువు | sage/teacher | ☐ |
| `pramadvara` | ప్రమద్వర | other | ☐ |
| `kadru` | కద్రువ | other | ☐ |
| `vinata` | వినత | other | ☐ |
| `aruna` | అరుణుడు | divine | ☐ |
| `vasuki` | వాసుకి | other | ☐ |
| `garuda` | గరుత్మంతుడు | divine | ☐ |
| `parikshit` | పరీక్షిత్తు | Pandava | ☐ |
| `shamika` | శమీకుడు | sage/teacher | ☐ |
| `shringi` | శృంగి | sage/teacher | ☐ |
| `takshaka` | తక్షకుడు | other | ☐ |
| `janamejaya` | జనమేజయుడు | Pandava | ☐ |
| `jaratkaru` | జరత్కారువు | sage/teacher | ☐ |
| `astika` | ఆస్తీకుడు | sage/teacher | ☐ |
| `bharata` | భరతుడు | Kuru elder | ☐ |
| `pratipa` | ప్రతీపుడు | Kuru elder | ☐ |
| `shantanu` | శంతనుడు | Kuru elder | ☐ |
| `ganga` | గంగాదేవి | divine | ☐ |
| `bhishma` | భీష్ముడు | Kuru elder | ☐ |
| `satyavati` | సత్యవతి | Kuru elder | ☐ |
| `dasharaja` | దాశరాజు | other | ☐ |
| `chitrangada-k` | చిత్రాంగదుడు | Kuru elder | ☐ |
| `vichitravirya` | విచిత్రవీర్యుడు | Kuru elder | ☐ |
| `amba` | అంబ | other | ☐ |
| `dhritarashtra` | ధృతరాష్ట్రుడు | Kaurava | ☐ |
| `pandu` | పాండురాజు | Pandava | ☐ |
| `vidura` | విదురుడు | sage/teacher | ☐ |
| `gandhari` | గాంధారి | Kaurava | ☐ |
| `kunti` | కుంతి | Pandava | ☐ |
| `madri` | మాద్రి | Pandava | ☐ |
| `karna` | కర్ణుడు | Kaurava | ☐ |
| `yudhishthira` | యుధిష్ఠిరుడు | Pandava | ☐ |
| `bhima` | భీముడు | Pandava | ☐ |
| `arjuna` | అర్జునుడు | Pandava | ☐ |
| `nakula` | నకులుడు | Pandava | ☐ |
| `sahadeva` | సహదేవుడు | Pandava | ☐ |
| `pandavas` | పాండవులు | Pandava | ☐ |
| `duryodhana` | దుర్యోధనుడు | Kaurava | ☐ |
| `dushasana` | దుశ్శాసనుడు | Kaurava | ☐ |
| `shakuni` | శకుని | Kaurava | ☐ |
| `drona` | ద్రోణుడు | sage/teacher | ☐ |
| `kripa` | కృపాచార్యుడు | sage/teacher | ☐ |
| `parashurama` | పరశురాముడు | sage/teacher | ☐ |
| `ekalavya` | ఏకలవ్యుడు | other | ☐ |
| `ashvatthama` | అశ్వత్థామ | Kaurava | ☐ |
| `purochana` | పురోచనుడు | Kaurava | ☐ |
| `hidimbi` | హిడింబి | other | ☐ |
| `ghatotkacha` | ఘటోత్కచుడు | Pandava | ☐ |
| `bakasura` | బకాసురుడు | other | ☐ |
| `drupada` | ద్రుపదుడు | Pandava | ☐ |
| `draupadi` | ద్రౌపది | Pandava | ☐ |
| `dhrishtadyumna` | ధృష్టద్యుమ్నుడు | Pandava | ☐ |
| `krishna` | శ్రీకృష్ణుడు | divine | ☐ |
| `dhaumya` | ధౌమ్యుడు | sage/teacher | ☐ |
| `ulupi` | ఉలూపి | other | ☐ |
| `chitrangada` | చిత్రాంగద | other | ☐ |
| `subhadra` | సుభద్ర | Pandava | ☐ |
| `agni` | అగ్నిదేవుడు | divine | ☐ |
| `maya` | మయుడు | other | ☐ |

---

## Prompts

### `vyasa` — వేదవ్యాసుడు

*మహాభారత రచయిత, పరాశర సత్యవతుల కుమారుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Vyasa, the aged sage who composed this epic.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: an iron stylus and palm leaf.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `ganapati` — గణపతి

*భారత రచనకు లేఖకుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Ganesha, the elephant-headed god, acting as scribe.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a single broken tusk.
Ring colour: bright gold ring (divine).
```

### `vaishampayana` — వైశంపాయనుడు

*వ్యాస శిష్యుడు, జనమేజయునికి కథ చెప్పినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Vaishampayana, a sage reciting the epic to a king.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `sauti` — ఉగ్రశ్రవుడు (సౌతి)

*నైమిశారణ్య మునులకు కథ చెప్పిన సూతుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Ugrashravas the bard, a travelling storyteller.
Appearance: a wound cloth turban.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `shaunaka` — శౌనకుడు

*నైమిశారణ్య సత్రయాగ కులపతి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Shaunaka, an elder sage presiding over a long sacrifice.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `dushyanta` — దుష్యంతుడు

*పౌరవ వంశ రాజు, భరతుని తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Dushyanta, a hunter-king.
Appearance: a jewelled crown or royal headdress; full beard, dark.
Holding/marked by: a longbow held upright.
Ring colour: muted violet ring (Kuru elder).
```

### `shakuntala` — శకుంతల

*మేనక విశ్వామిత్రుల కుమార్తె, కణ్వుని పెంపుడు కూతురు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Shakuntala, a forest-raised young woman of great dignity.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: muted violet ring (Kuru elder).
```

### `kanva` — కణ్వుడు

*శకుంతలను పెంచిన మహర్షి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Kanva, a gentle old forest sage.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `menaka` — మేనక

*అప్సరస, శకుంతల తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Menaka, a celestial dancer.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: bright gold ring (divine).
```

### `vishvamitra` — విశ్వామిత్రుడు

*రాజర్షి, శకుంతల తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Vishvamitra, a royal sage of terrible austerity.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `vasishtha` — వసిష్ఠుడు

*బ్రహ్మర్షి, అష్ట వసువులను శపించినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Vasishtha, a serene white-bearded brahmin sage.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a thunderbolt (vajra).
Ring colour: turmeric-gold ring (sage/teacher).
```

### `uparichara` — ఉపరిచర వసువు

*చేది రాజు, ఇంద్ర మిత్రుడు, సత్యవతి తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Uparichara Vasu, a monarch who flew among the gods.
Appearance: a jewelled crown or royal headdress; full beard, dark.
Holding/marked by: a thunderbolt (vajra).
Ring colour: muted violet ring (Kuru elder).
```

### `adrika` — అద్రిక

*శాపవశాత్తు చేపగా మారిన అప్సరస*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Adrika, an apsara cursed into the form of a fish.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: water streaming from cupped hands.
Ring colour: forest-green ring (other).
```

### `parashara` — పరాశరుడు

*వసిష్ఠుని మనుమడు, వ్యాసుని తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Parashara, a powerful sage, father of Vyasa.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a thunderbolt (vajra).
Ring colour: turmeric-gold ring (sage/teacher).
```

### `kacha` — కచుడు

*బృహస్పతి కుమారుడు, మృతసంజీవని విద్య నేర్చినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Kacha, a handsome young god-student.
Appearance: plain cropped hair, no crown.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: bright gold ring (divine).
```

### `shukra` — శుక్రాచార్యుడు

*రాక్షస గురువు, మృతసంజీవని విద్య తెలిసినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Shukracharya, preceptor of the asuras, fierce and red-robed.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a thunderbolt (vajra).
Ring colour: turmeric-gold ring (sage/teacher).
```

### `devayani` — దేవయాని

*శుక్రాచార్యుని కుమార్తె, యయాతి భార్య*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Devayani, a proud young brahmin woman.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: forest-green ring (other).
```

### `sharmishtha` — శర్మిష్ఠ

*వృషపర్వుని కుమార్తె, పూరుని తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Sharmishtha, an asura princess made a servant.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: forest-green ring (other).
```

### `vrishaparva` — వృషపర్వుడు

*రాక్షస రాజు, శర్మిష్ఠ తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Vrishaparva, king of the asuras.
Appearance: a jewelled crown or royal headdress; full beard, dark.
Holding/marked by: a raised sceptre.
Ring colour: forest-green ring (other).
```

### `yayati` — యయాతి

*నహుషుని కుమారుడు, పూరుని తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Yayati, aged by a curse.
Appearance: a jewelled crown or royal headdress; full beard, dark.
Holding/marked by: a raised sceptre.
Ring colour: muted violet ring (Kuru elder).
```

### `puru` — పూరుడు

*యయాతి కుమారుడు, పౌరవ వంశ మూలపురుషుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Puru, the youngest prince, newly crowned.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a raised sceptre.
Ring colour: muted violet ring (Kuru elder).
```

### `yadu` — యదువు

*యయాతి పెద్ద కుమారుడు, యదు వంశ మూలపురుషుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Yadu, an eldest prince who refused his father.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a raised sceptre.
Ring colour: muted violet ring (Kuru elder).
```

### `brihaspati` — బృహస్పతి

*దేవ గురువు, కచుని తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Brihaspati, preceptor of the gods.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: bright gold ring (divine).
```

### `rajarajanarendra` — రాజరాజనరేంద్రుడు

*వేంగి రాజు, తెలుగులో భారతము రచింపమని నన్నయను కోరినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Rajaraja Narendra, an 11th-century Telugu king and patron.
Appearance: a jewelled crown or royal headdress; full beard, dark.
Holding/marked by: a raised sceptre.
Ring colour: muted violet ring (Kuru elder).
```

### `nannaya` — నన్నయ

*ఆదికవి, ఆంధ్ర మహాభారత రచన ఆరంభించినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Nannaya, the first poet of Telugu, stylus in hand.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: an iron stylus and palm leaf.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `narayanabhatta` — నారాయణభట్టు

*నన్నయకు సహాయపడిన సహపాఠి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Narayana Bhatta, a scholar-companion to the poet.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `paila` — పైలుడు

*వ్యాసుని శిష్యుడు, ఋగ్వేద ప్రవర్తకుడు, ఉదంకుని గురువు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Paila, a vedic sage and teacher.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `shuka` — శుక మహర్షి

*వ్యాసుని కుమారుడు, విరాగి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Shuka, the young ascetic son of Vyasa, radiant and detached.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `sarama` — సరమ

*దేవతల కుక్క, జనమేజయుని శపించినది*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Sarama, the divine hound of the gods, luminous and wrathful.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a thunderbolt (vajra).
Ring colour: bright gold ring (divine).
```

### `udanka` — ఉదంకుడు

*పైలుని శిష్యుడు, తక్షకునిపై పగతో జనమేజయుని ప్రేరేపించినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Udanka, a young brahmin student on a quest.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `paushya` — పౌష్యుడు

*కుండలములు దానమిచ్చిన రాజు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Paushya, a bearded monarch.
Appearance: a jewelled crown or royal headdress; full beard, dark.
Holding/marked by: a raised sceptre.
Ring colour: forest-green ring (other).
```

### `indra` — ఇంద్రుడు

*దేవతల రాజు, వజ్రాయుధధారి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Indra, king of the gods, thunderbolt in hand.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a thunderbolt (vajra).
Ring colour: bright gold ring (divine).
```

### `bhrigu` — భృగువు

*భృగు వంశ మూలపురుషుడు, అగ్నిని శపించిన మహర్షి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Bhrigu, an ancient and severe sage.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `puloma` — పులోమ

*భృగు మహర్షి భార్య, చ్యవనుని తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Puloma, wife of the sage Bhrigu.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: forest-green ring (other).
```

### `chyavana` — చ్యవనుడు

*పుట్టుకతోనే తేజస్వి, భృగు పులోమల కుమారుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Chyavana, a sage born blazing with light.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a solar disc glowing behind the head.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `ruru` — రురువు

*ప్రమద్వర భర్త, సర్పద్వేషాన్ని వదిలిన మహర్షి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Ruru, a young brahmin, grief turned to anger.
Appearance: plain cropped hair, no crown.
Holding/marked by: a hooded serpent coiled at the shoulder.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `pramadvara` — ప్రమద్వర

*మేనక విశ్వావసుల కుమార్తె, రురువు భార్య*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Pramadvara, a young woman restored to life.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: forest-green ring (other).
```

### `kadru` — కద్రువ

*కశ్యపుని భార్య, నాగుల తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Kadru, mother of the serpent race, hard-faced.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a hooded serpent coiled at the shoulder.
Ring colour: forest-green ring (other).
```

### `vinata` — వినత

*కశ్యపుని భార్య, అరుణ గరుడుల తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Vinata, mother of Garuda, held in servitude.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: great outspread feathered wings.
Ring colour: forest-green ring (other).
```

### `aruna` — అరుణుడు

*వినత మొదటి కుమారుడు, సూర్యుని రథసారథి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Aruna, the charioteer of the sun, half-formed and glowing red.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a solar disc glowing behind the head.
Ring colour: bright gold ring (divine).
```

### `vasuki` — వాసుకి

*నాగరాజు, ఆస్తీకుని మేనమామ*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Vasuki, king of the serpents, many-hooded.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a hooded serpent coiled at the shoulder.
Ring colour: forest-green ring (other).
```

### `garuda` — గరుత్మంతుడు

*వినత కుమారుడు, అమృతము తెచ్చినవాడు, విష్ణు వాహనము*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Garuda, the great eagle-man, wings outspread.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: great outspread feathered wings.
Ring colour: bright gold ring (divine).
```

### `parikshit` — పరీక్షిత్తు

*అభిమన్యు కుమారుడు, తక్షకుని కాటుకు బలైన రాజు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Parikshit, last heir of the Kuru line.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a longbow held upright.
Ring colour: deep indigo ring (Pandava).
```

### `shamika` — శమీకుడు

*మౌన వ్రతంలో ఉన్న మహర్షి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Shamika, an old sage in silent meditation.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `shringi` — శృంగి

*శమీకుని కుమారుడు, పరీక్షిత్తును శపించినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Shringi, a hot-tempered young ascetic.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `takshaka` — తక్షకుడు

*నాగరాజు, ఇంద్రుని మిత్రుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Takshaka, a serpent king in human form, cunning.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a hooded serpent coiled at the shoulder.
Ring colour: forest-green ring (other).
```

### `janamejaya` — జనమేజయుడు

*పరీక్షిత్తు కుమారుడు, సర్పయాగం చేసిన రాజు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Janamejaya, a young monarch bent on revenge.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: deep indigo ring (Pandava).
```

### `jaratkaru` — జరత్కారువు

*ఆస్తీకుని తండ్రి, పితరుల కోసం వివాహమాడిన ముని*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Jaratkaru, an ascetic sage, gaunt from fasting.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `astika` — ఆస్తీకుడు

*జరత్కారు కుమారుడు, సర్పజాతిని రక్షించిన బాలుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Astika, a boy sage of great composure.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash.
Holding/marked by: a hooded serpent coiled at the shoulder.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `bharata` — భరతుడు

*దుష్యంత శకుంతలల కుమారుడు, భరత వంశ మూలపురుషుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Bharata, a boy-king who gave his name to a country.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a raised sceptre.
Ring colour: muted violet ring (Kuru elder).
```

### `pratipa` — ప్రతీపుడు

*శంతనుని తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Pratipa, an old monarch in meditation.
Appearance: a jewelled crown or royal headdress; full beard, white with age.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: muted violet ring (Kuru elder).
```

### `shantanu` — శంతనుడు

*కురు వంశ రాజు, భీష్ముని తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Shantanu, a handsome monarch.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a longbow held upright.
Ring colour: muted violet ring (Kuru elder).
```

### `ganga` — గంగాదేవి

*నదీ దేవత, భీష్ముని తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Ganga, the river goddess, water-crowned.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: water streaming from cupped hands.
Ring colour: bright gold ring (divine).
```

### `bhishma` — భీష్ముడు

*గంగా శంతనుల కుమారుడు, ఆజన్మ బ్రహ్మచారి, కురు వంశ రక్షకుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Bhishma, the aged Kuru patriarch, white-bearded warrior in ornate armour.
Appearance: a jewelled crown or royal headdress; full beard, white with age.
Holding/marked by: a longbow held upright.
Ring colour: muted violet ring (Kuru elder).
```

### `satyavati` — సత్యవతి

*దాశరాజు కుమార్తె, శంతనుని రాణి, వ్యాసుని తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Satyavati, a fisherwoman who became queen.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a river ferry behind the shoulder.
Ring colour: muted violet ring (Kuru elder).
```

### `dasharaja` — దాశరాజు

*సత్యవతి పెంపుడు తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Dasharaja, a chief of fisherfolk.
Appearance: a wound cloth turban.
Holding/marked by: a river ferry behind the shoulder.
Ring colour: forest-green ring (other).
```

### `chitrangada-k` — చిత్రాంగదుడు

*శంతను సత్యవతుల పెద్ద కుమారుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Prince Chitrangada, a young Kuru heir.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a longbow held upright.
Ring colour: muted violet ring (Kuru elder).
```

### `vichitravirya` — విచిత్రవీర్యుడు

*శంతను సత్యవతుల చిన్న కుమారుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Prince Vichitravirya, a frail young king.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: muted violet ring (Kuru elder).
```

### `amba` — అంబ

*కాశీ రాజకుమార్తె, తరువాతి జన్మలో శిఖండి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Amba, a wronged princess, resolute and cold.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: forest-green ring (other).
```

### `dhritarashtra` — ధృతరాష్ట్రుడు

*అంధుడైన కురు రాజు, కౌరవుల తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Dhritarashtra, the blind Kuru king.
Appearance: a jewelled crown or royal headdress; eyes closed, sightless.
Holding/marked by: a raised sceptre.
Ring colour: madder-red ring (Kaurava).
```

### `pandu` — పాండురాజు

*హస్తినాపుర రాజు, పాండవుల తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Pandu, pale-complexioned monarch.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a longbow held upright.
Ring colour: deep indigo ring (Pandava).
```

### `vidura` — విదురుడు

*ధర్మ స్వరూపుడు, కురు మంత్రి, ధర్మ బోధకుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Vidura, the wise half-brother and counsellor.
Appearance: a wound cloth turban.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `gandhari` — గాంధారి

*ధృతరాష్ట్రుని రాణి, కళ్ళకు గంతలు కట్టుకున్న సాధ్వి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Gandhari, a queen who bound her own eyes.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi; eyes bound with a cloth blindfold.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: madder-red ring (Kaurava).
```

### `kunti` — కుంతి

*పాండురాజు రాణి, పాండవుల తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Kunti, mother of the Pandavas, dignified and sorrowful.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a solar disc glowing behind the head.
Ring colour: deep indigo ring (Pandava).
```

### `madri` — మాద్రి

*పాండురాజు రెండవ రాణి, నకుల సహదేవుల తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Madri, second queen of Pandu.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a thunderbolt (vajra).
Ring colour: deep indigo ring (Pandava).
```

### `karna` — కర్ణుడు

*కుంతి సూర్యుల కుమారుడు, అంగ రాజు, దుర్యోధన మిత్రుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Karna, a radiant warrior wearing golden earrings and breastplate.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a solar disc glowing behind the head.
Ring colour: madder-red ring (Kaurava).
```

### `yudhishthira` — యుధిష్ఠిరుడు

*పెద్ద పాండవుడు, యమధర్మరాజు వరపుత్రుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Yudhishthira, the eldest Pandava, calm and upright.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a raised sceptre.
Ring colour: deep indigo ring (Pandava).
```

### `bhima` — భీముడు

*వాయు పుత్రుడు, పది వేల ఏనుగుల బలుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Bhima, the immensely powerful second Pandava.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a heavy iron mace resting on the shoulder.
Ring colour: deep indigo ring (Pandava).
```

### `arjuna` — అర్జునుడు

*ఇంద్ర పుత్రుడు, గాండీవధారి, లోకైక విలుకాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Arjuna, the great archer, blue-tinged and serene.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a longbow held upright.
Ring colour: deep indigo ring (Pandava).
```

### `nakula` — నకులుడు

*అశ్వినీ దేవతల కుమారుడు, అశ్వ శాస్త్ర నిపుణుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Nakula, a handsome young Pandava.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a thunderbolt (vajra).
Ring colour: deep indigo ring (Pandava).
```

### `sahadeva` — సహదేవుడు

*అశ్వినీ దేవతల కుమారుడు, జ్యోతిష్య నిపుణుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Sahadeva, the youngest Pandava, thoughtful.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a thunderbolt (vajra).
Ring colour: deep indigo ring (Pandava).
```

### `pandavas` — పాండవులు

*పాండురాజు ఐదుగురు కుమారులు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: the five Pandava brothers together.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a thunderbolt (vajra).
Ring colour: deep indigo ring (Pandava).
```

### `duryodhana` — దుర్యోధనుడు

*పెద్ద కౌరవుడు, హస్తినాపుర యువరాజు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Duryodhana, the proud eldest Kaurava.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a heavy iron mace resting on the shoulder.
Ring colour: madder-red ring (Kaurava).
```

### `dushasana` — దుశ్శాసనుడు

*దుర్యోధనుని తమ్ముడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Dushasana, a brutal Kaurava prince.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a heavy iron mace resting on the shoulder.
Ring colour: madder-red ring (Kaurava).
```

### `shakuni` — శకుని

*గాంధారి సోదరుడు, జూద నిపుణుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Shakuni, a thin scheming uncle with dice.
Appearance: a wound cloth turban.
Holding/marked by: gambling dice cupped in one hand.
Ring colour: madder-red ring (Kaurava).
```

### `drona` — ద్రోణుడు

*భరద్వాజ కుమారుడు, పాండవ కౌరవుల విలువిద్యా గురువు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Dronacharya, a lean ascetic warrior-teacher.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a longbow held upright.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `kripa` — కృపాచార్యుడు

*కురు రాజకుమారుల మొదటి గురువు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Kripacharya, an old teacher of arms.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a palm-leaf manuscript bundle.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `parashurama` — పరశురాముడు

*భీష్మ ద్రోణ కర్ణుల గురువు, విష్ణు అవతారము*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Parashurama, the axe-bearing warrior sage.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, white with age.
Holding/marked by: a battle-axe.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `ekalavya` — ఏకలవ్యుడు

*నిషాద రాజకుమారుడు, స్వయంశిక్షిత విలుకాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Ekalavya, a forest-dwelling youth, devoted and maimed.
Appearance: a wound cloth turban.
Holding/marked by: a longbow held upright.
Ring colour: forest-green ring (other).
```

### `ashvatthama` — అశ్వత్థామ

*ద్రోణుని కుమారుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Ashvatthama, a fierce young warrior with a gem on his brow.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a thunderbolt (vajra).
Ring colour: madder-red ring (Kaurava).
```

### `purochana` — పురోచనుడు

*లక్క ఇల్లు నిర్మించిన దుర్యోధన మంత్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Purochana, a furtive royal builder.
Appearance: a wound cloth turban.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: madder-red ring (Kaurava).
```

### `hidimbi` — హిడింబి

*రాక్షస కన్య, భీముని భార్య*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Hidimbi, a rakshasa woman of great beauty.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: forest-green ring (other).
```

### `ghatotkacha` — ఘటోత్కచుడు

*భీమ హిడింబిల కుమారుడు, మాయా యోధుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Ghatotkacha, a huge half-rakshasa warrior.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a heavy iron mace resting on the shoulder.
Ring colour: deep indigo ring (Pandava).
```

### `bakasura` — బకాసురుడు

*ఏకచక్రపుర రాక్షసుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Bakasura, a monstrous man-eating giant.
Appearance: a wound cloth turban.
Holding/marked by: a heavy iron mace resting on the shoulder.
Ring colour: forest-green ring (other).
```

### `drupada` — ద్రుపదుడు

*పాంచాల రాజు, ద్రౌపది తండ్రి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: King Drupada of Panchala, proud and bitter.
Appearance: a jewelled crown or royal headdress; full beard, dark.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: deep indigo ring (Pandava).
```

### `draupadi` — ద్రౌపది

*యాగాగ్ని నుంచి జన్మించిన పాంచాల రాజకుమార్తె, పాండవుల భార్య*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Draupadi, a dark-complexioned princess of great presence.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: deep indigo ring (Pandava).
```

### `dhrishtadyumna` — ధృష్టద్యుమ్నుడు

*ద్రుపదుని కుమారుడు, పాండవ సేనాపతి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Dhrishtadyumna, a warrior born of sacrificial fire.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a longbow held upright.
Ring colour: deep indigo ring (Pandava).
```

### `krishna` — శ్రీకృష్ణుడు

*యదు వంశ నాయకుడు, పాండవ సఖుడు, గీతాచార్యుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Krishna, blue-skinned, peacock-feathered, serene.
Appearance: a jewelled crown or royal headdress.
Holding/marked by: a flaming discus (chakra).
Ring colour: bright gold ring (divine).
```

### `dhaumya` — ధౌమ్యుడు

*పాండవుల పురోహితుడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Dhaumya, a household priest.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, dark.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: turmeric-gold ring (sage/teacher).
```

### `ulupi` — ఉలూపి

*నాగ కన్య, అర్జునుని భార్య*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Ulupi, a naga princess.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a hooded serpent coiled at the shoulder.
Ring colour: forest-green ring (other).
```

### `chitrangada` — చిత్రాంగద

*మణిపూర రాజకుమార్తె, అర్జునుని భార్య*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Chitrangada, a warrior princess of Manipura.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: forest-green ring (other).
```

### `subhadra` — సుభద్ర

*కృష్ణుని సోదరి, అర్జునుని భార్య, అభిమన్యు తల్లి*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Subhadra, a gentle young princess.
Appearance: long dark hair, centre-parted, gold ornaments and a bindi.
Holding/marked by: a lotus bloom held at the breast.
Ring colour: deep indigo ring (Pandava).
```

### `agni` — అగ్నిదేవుడు

*అగ్ని దేవత, ఖాండవ వనాన్ని దహించినవాడు*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Agni, the fire god, flame-haired.
Appearance: matted ascetic jata coiled on the head, forehead marked with ash; full beard, dark.
Holding/marked by: a ritual flame rising from one palm.
Ring colour: bright gold ring (divine).
```

### `maya` — మయుడు

*దానవ శిల్పి, మయసభ నిర్మాత*

```
Circular medallion bust portrait, tight double gold ring border with a small
lotus at the base of the ring, fully transparent outside the circle.
Painted digital illustration in the manner of a classical Indian oleograph —
warm saturated colour, soft modelled light, visible brushwork, ornate detail.
Three-quarter view, shoulders and head only, eyes turned slightly off camera.
Background inside the circle: open sky, distant fort or temple silhouette,
tall cloth banners. Square image, 1024x1024, centred, head in the upper half.
No text, no lettering, no signature, no watermark, no border outside the ring.

Subject: Maya, an asura master-architect.
Appearance: a wound cloth turban.
Holding/marked by: a thunderbolt (vajra).
Ring colour: forest-green ring (other).
```
