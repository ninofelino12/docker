const cacheName = 'flask-pwa-cache-v1';
const filesToCache = [
  '/',
  '/static/manifest.json',
  '/static/icon.png',
  '/static/sw.js',
];

self.addEventListener('install', (event) => {
  alert("LISTEN");
  event.waitUntil(
    caches.open(cacheName).then((cache) => {
      return cache.addAll(filesToCache);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
