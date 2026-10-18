const CACHE_NAME = 'tabelog-eye-v5';
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
  './photos/anmei-sumiyoshi.jpg',
  './photos/chikaro-haruyoshi.jpg',
  './photos/fukuoka-tatsumi-sushi.jpg',
  './photos/hanayoshi-uratenjin.jpg',
  './photos/hp-fukuoka-hamadaya.jpg',
  './photos/hp-fukuoka-kawano.jpg',
  './photos/hp-fukuoka-moegi-yakuin.jpg',
  './photos/hp-fukuoka-nana-haruyoshi.jpg',
  './photos/hp-fukuoka-shogetsutei.jpg',
  './photos/hp-fukuoka-torabi.jpg',
  './photos/hp-hakata-mizune.jpg',
  './photos/hp-hakata-nakagawa.jpg',
  './photos/hp-kyoto-gem.jpg',
  './photos/hp-okoge-umeda.jpg',
  './photos/hp-pronto-shinagawa.jpg',
  './photos/hp-shinbashi-otako.jpg',
  './photos/hp-shinjuku-ninomiya.jpg',
  './photos/hp-tengu-shinjuku.jpg',
  './photos/hp-wan-tamachi.jpg',
  './photos/hp-yumeyagura-umeda.jpg',
  './photos/kanbee-haruyoshi.jpg',
  './photos/kyoto-ogata.jpg',
  './photos/matsushita-haruyoshi.jpg',
  './photos/oishi-sumiyoshi.jpg',
  './photos/ramen-iida-shouta.jpg',
  './photos/sendou-sumiyoshi.jpg',
  './photos/sushi-mitsu.jpg',
  './photos/sushi-sugita-tokyo.jpg',
  './photos/sushi-suigyo.jpg',
  './photos/tc-akasakashion.jpg',
  './photos/yakiniku-jambo-hanare.jpg'
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
