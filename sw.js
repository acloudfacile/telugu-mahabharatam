/* సంపూర్ణ మహాభారతము — offline.
   The whole site is small and finite, so it is simply kept. Once read, it can
   be read again on a train, in a village with no signal, or in ten years when
   this domain may no longer answer.

   Strategy:
     navigations  network first, cache as backup  (so a new parva shows up)
     everything else  cache first, refresh behind (so reading is instant)
   The cache name carries a build stamp; a new build drops the old cache. */
const VERSION = '64d3b11d20ef';
const CACHE = 'mb-' + VERSION;
const ASSETS = [
"./",
"./index.html",
"./assets/style.css",
"./assets/app.js",
"./data/parvas.js",
"./data/content.js",
"./data/characters.js",
"./favicon.svg",
"./manifest.webmanifest",
"./appicons/icon-192.png",
"./appicons/icon-512.png",
"./appicons/icon-maskable-512.png",
"./appicons/apple-touch-icon.png",
"./img/01_nannaya.jpg",
"./img/02_naimisharanya.jpg",
"./img/03_vyasa_ganapati.jpg",
"./img/04_parva_sangraha.jpg",
"./img/05_sarama.jpg",
"./img/06_udanka.jpg",
"./img/07_janamejaya.jpg",
"./img/08_pauloma.jpg",
"./img/09_ruru.jpg",
"./img/10_kadru_vinata.jpg",
"./img/11_garuda.jpg",
"./img/12_parikshit.jpg",
"./img/13_sarpa_yagna.jpg",
"./img/14_uparichara.jpg",
"./img/15_bhubharam.jpg",
"./img/16_kacha.jpg",
"./img/17_devayani.jpg",
"./img/18_yayati.jpg",
"./img/19_puru.jpg",
"./img/20_shakuntala.jpg",
"./img/21_bharata.jpg",
"./img/22_vasus.jpg",
"./img/23_ganga_shantanu.jpg",
"./img/24_bhishma_pratigna.jpg",
"./img/25_amba.jpg",
"./img/26_vyasa_niyoga.jpg",
"./img/27_karna_janana.jpg",
"./img/28_pandu_shapam.jpg",
"./img/29_pandava_janana.jpg",
"./img/30_kaurava_janana.jpg",
"./img/31_drona.jpg",
"./img/32_ekalavya.jpg",
"./img/33_ranga_bhumi.jpg",
"./img/34_drupada.jpg",
"./img/35_yuvaraja.jpg",
"./img/36_lakshagriha.jpg",
"./img/37_escape.jpg",
"./img/38_hidimbi.jpg",
"./img/39_bakasura.jpg",
"./img/40_swayamvara.jpg",
"./img/41_khandava_dahanam.jpg",
"./icons/adrika.png",
"./icons/agni.png",
"./icons/amba.png",
"./icons/arjuna.png",
"./icons/aruna.png",
"./icons/ashvatthama.png",
"./icons/astika.png",
"./icons/bakasura.png",
"./icons/bharata.png",
"./icons/bhima.png",
"./icons/bhishma.png",
"./icons/bhrigu.png",
"./icons/brihaspati.png",
"./icons/chitrangada-k.png",
"./icons/chitrangada.png",
"./icons/chyavana.png",
"./icons/dasharaja.png",
"./icons/devayani.png",
"./icons/dhaumya.png",
"./icons/dhrishtadyumna.png",
"./icons/dhritarashtra.png",
"./icons/draupadi.png",
"./icons/drona.png",
"./icons/drupada.png",
"./icons/duryodhana.png",
"./icons/dushasana.png",
"./icons/dushyanta.png",
"./icons/ekalavya.png",
"./icons/ganapati.png",
"./icons/gandhari.png",
"./icons/ganga.png",
"./icons/garuda.png",
"./icons/ghatotkacha.png",
"./icons/hidimbi.png",
"./icons/indra.png",
"./icons/janamejaya.png",
"./icons/jaratkaru.png",
"./icons/kacha.png",
"./icons/kadru.png",
"./icons/kanva.png",
"./icons/karna.png",
"./icons/kripa.png",
"./icons/krishna.png",
"./icons/kunti.png",
"./icons/madri.png",
"./icons/maya.png",
"./icons/menaka.png",
"./icons/nakula.png",
"./icons/nannaya.png",
"./icons/narayanabhatta.png",
"./icons/paila.png",
"./icons/pandavas.png",
"./icons/pandu.png",
"./icons/parashara.png",
"./icons/parashurama.png",
"./icons/parikshit.png",
"./icons/parva_01.png",
"./icons/parva_02.png",
"./icons/parva_03.png",
"./icons/parva_04.png",
"./icons/parva_05.png",
"./icons/parva_06.png",
"./icons/parva_07.png",
"./icons/parva_08.png",
"./icons/parva_09.png",
"./icons/parva_10.png",
"./icons/parva_11.png",
"./icons/parva_12.png",
"./icons/parva_13.png",
"./icons/parva_14.png",
"./icons/parva_15.png",
"./icons/parva_16.png",
"./icons/parva_17.png",
"./icons/parva_18.png",
"./icons/paushya.png",
"./icons/pramadvara.png",
"./icons/pratipa.png",
"./icons/puloma.png",
"./icons/purochana.png",
"./icons/puru.png",
"./icons/rajarajanarendra.png",
"./icons/ruru.png",
"./icons/sahadeva.png",
"./icons/sarama.png",
"./icons/satyavati.png",
"./icons/sauti.png",
"./icons/shakuni.png",
"./icons/shakuntala.png",
"./icons/shamika.png",
"./icons/shantanu.png",
"./icons/sharmishtha.png",
"./icons/shaunaka.png",
"./icons/shringi.png",
"./icons/shuka.png",
"./icons/shukra.png",
"./icons/subhadra.png",
"./icons/takshaka.png",
"./icons/udanka.png",
"./icons/ulupi.png",
"./icons/uparichara.png",
"./icons/vaishampayana.png",
"./icons/vasishtha.png",
"./icons/vasuki.png",
"./icons/vichitravirya.png",
"./icons/vidura.png",
"./icons/vinata.png",
"./icons/vishvamitra.png",
"./icons/vrishaparva.png",
"./icons/vyasa.png",
"./icons/yadu.png",
"./icons/yayati.png",
"./icons/yudhishthira.png"
];

self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    // one bad URL must not fail the whole install
    await Promise.all(ASSETS.map(u => c.add(u).catch(() => {})));
    self.skipWaiting();
  })());
});

self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k.startsWith('mb-') && k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;   // fonts etc. are the browser's business

  if (req.mode === 'navigate') {
    e.respondWith((async () => {
      try {
        const fresh = await fetch(req);
        (await caches.open(CACHE)).put('./', fresh.clone());
        return fresh;
      } catch (err) {
        return (await caches.match('./')) || (await caches.match('./index.html')) || Response.error();
      }
    })());
    return;
  }

  e.respondWith((async () => {
    const hit = await caches.match(req, { ignoreSearch: true });
    const net = fetch(req).then(res => {
      if (res && res.ok) caches.open(CACHE).then(c => c.put(req, res.clone()));
      return res;
    }).catch(() => null);
    return hit || (await net) || Response.error();
  })());
});
