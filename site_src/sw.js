/* సంపూర్ణ మహాభారతము — offline.
   The whole site is small and finite, so it is simply kept. Once read, it can
   be read again on a train, in a village with no signal, or in ten years when
   this domain may no longer answer.

   Strategy:
     install      only the frame of the site (pages, style, code, small index)
     navigations  network first, cache as backup  (so a new parva shows up)
     everything else  cache first, refresh behind (so reading is instant) —
                  pictures, icons and each parva's text are kept once read
   The cache name carries a build stamp; a new build drops the old cache. */
const VERSION = '__BUILD__';
const CACHE = 'mb-' + VERSION;
const ASSETS = __ASSETS__;

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
        // keep each page under its own address (an episode page must not replace the home page)
        if (fresh && fresh.ok) { const copy = fresh.clone(); (await caches.open(CACHE)).put(req, copy); }
        return fresh;
      } catch (err) {
        return (await caches.match(req, { ignoreSearch: true })) || (await caches.match('./')) || (await caches.match('./index.html')) || Response.error();
      }
    })());
    return;
  }

  e.respondWith((async () => {
    const hit = await caches.match(req, { ignoreSearch: true });
    const net = fetch(req).then(res => {
      // copy now, before the page reads the body — a later clone() fails silently
      if (res && res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
      return res;
    }).catch(() => null);
    return hit || (await net) || Response.error();
  })());
});
