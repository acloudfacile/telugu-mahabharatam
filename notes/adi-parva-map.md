# Adi Parva — source map

Page numbers are PDF page indices in the Modali Venkata Subrahmanyam
*శ్రీమదాంధ్ర మహాభారతము (తేట తెలుగు భాషలో)*, the Kavitrayam rendered into modern
Telugu prose. Each āśvāsa opens with a title page; content starts the page after.
Verified by reading, not inferred.

| āśvāsa | pages | contents |
|---|---|---|
| ౧ ప్రథమ | 3–24 | Nannaya frame · Naimiśāraṇya · Vyāsa & Gaṇapati · parva saṅgraha · Saramā · Udaṅka/Pauṣya · Paulōma (Bhṛgu, Cyavana, Ruru) |
| ౨ ద్వితీయ | 26–60 | Āstīka — Kadru & Vinatā · Garuḍa · Parīkṣit · sarpayāga · Āstīka |
| ౩ తృతీయ | 61–109 | Ādivaṁśāvataraṇa — Uparicara Vasu, Satyavatī, Vyāsa's birth · bhū-bhāra and the descent of the gods · creation genealogy · Kaca & Devayānī · Devayānī & Śarmiṣṭhā · Yayāti & Pūru |
| ౪ చతుర్థ | 111–156 | Duṣyanta & Śakuntalā · Bharata · Pratīpa · Śantanu & Gaṅgā · the eight Vasus cursed by Vasiṣṭha · Bhīṣma's vow · Satyavatī · Vicitravīrya · Ambā · niyoga |
| ౫ పంచమ | 158–203 | Dhṛtarāṣṭra, Pāṇḍu, Vidura · Kuntī's boon and Karṇa's birth · Pāṇḍu's curse · births of the Pāṇḍavas and the hundred · Kṛpa · Droṇa · Ekalavya |
| ౬ షష్ఠ | 205–253 | the tournament and Karṇa · Drupada's defeat · Yudhiṣṭhira made yuvarāja · Vāraṇāvata and the lac house · Hiḍimba · Baka |
| ౭ సప్తమ | 256–307 | Aṅgāraparṇa (Citraratha) · Tapatī · Vasiṣṭha & Viśvāmitra · Kalmāṣapāda · Draupadī's svayaṁvara · the marriage · the five Indras |
| ౮ అష్టమ | 309–344 | Viduṛāgamana · Indraprastha · Nārada and Sunda–Upasunda · Arjuna's tīrthayātra (Ulūpī, Citrāṅgadā) · Subhadrā · Khāṇḍava dahana · Maya |

## Episode plan

Published: ౧–౧౩ cover āśvāsas ౧–౨ at full density.
Episodes ౧౪–౨౦ are the old compressed chapters and are being replaced
āśvāsa by āśvāsa. Target for a complete Adi Parva is roughly 49 episodes.

| batch | āśvāsa | episodes | status |
|---|---|---|---|
| one | ౧–౨ | ౧–౧౩ | done |
| two | ౩ | ౧౪–౧౯ | done |
| three | ౪ | ౨౦–౨౬ | done |
| four | ౫ + start of ౬ | ౨౭–౩౩ | done |
| five | ౬ | ౩౪–౩౯ | done |
| six | ౭ | ౪౦–౪౮ | done |
| seven | ౮ | ౪౯–౫౮ | done — Adi Parva complete |

Episodes ౪౦ and ౪౧, the last two old compressed chapters, are gone; their two
drawings live on as ౪౫ (svayamvara) and ౫౬ (Khandava). The seventh and eighth
āśvāsa ranges above were re-checked against the title pages: the seventh opens
on 256, the eighth on 309, and Adi Parva ends on 344 (Sabha opens on 347).

## Padyams

The adapter stops four times to quote Nannaya's own verse. Found by searching
the legacy text layer for the byte-form of "నన్నయ" alongside a smart quote —
punctuation survives the encoding even though the Telugu does not. Pages 222
and 232 are references without a quotation; 231 and 289 carry actual verse.

| page | verse | episode |
|---|---|---|
| ౨౩౧ | పతిస్నేహము కామినులకు బలవంతము… | ౩౮ హిడింబి |
| ౨౮౯ | ఆ లలితాంగి యందు హృదయంబులు దృష్టులు నిల్పి… | ౪౬ 'అందరూ పంచుకోండి' |

## Working method

`spread.py a b` renders cropped two-page spreads; `sheet.py a b step name`
builds a contact sheet of page-tops for locating a section without reading it.
Both live in the scratch directory, not the repo — they only need the PDF.
