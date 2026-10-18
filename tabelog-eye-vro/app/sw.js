const CACHE_NAME = 'tabelog-eye-v4';
const ASSETS = [
  './',
  './index.html',
  './share.html',
  './manifest.json',
  './dataset.json',
  './self-host-kit.json',
  './curation_feedback_ledger.jsonl',
  './kiro-debiasing-methodology.md',
  './icon-192.svg',
  './icon-512.svg',
  './photos/hp-shinjuku-ninomiya.jpg',
  './photos/hp-kyoto-gem.jpg',
  './photos/hp-shinbashi-otako.jpg',
  './photos/hp-hakata-mizune.jpg',
  './photos/hp-hakata-nakagawa.jpg',
  './photos/hp-yumeyagura-umeda.jpg',
  './photos/hp-okoge-umeda.jpg',
  './photos/hp-wan-tamachi.jpg',
  './photos/hp-pronto-shinagawa.jpg',
  './photos/hp-tengu-shinjuku.jpg',
  './photos/tc-akasakashion.jpg',
  './photos/fukuoka-tatsumi-sushi.jpg',
  './photos/kyoto-ogata.jpg',
  './photos/sushi-sugita-tokyo.jpg',
  './photos/yakiniku-jambo-hanare.jpg',
  './photos/ramen-iida-shouta.jpg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    fetch(event.request)
      .then((res) => {
        const copy = res.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy)).catch(() => {});
        return res;
      })
      .catch(() => caches.match(event.request))
  );
});
