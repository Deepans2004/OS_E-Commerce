const CACHE_NAME = 'my-cache-v1';
const urlsToCache = [
  '/',
  '/core/offline.html',
  // add other static files you want cached
];

// Install event — cache files
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
  self.skipWaiting();
});

// Activate event — cleanup old caches if any
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => 
      Promise.all(
        cacheNames.map(name => {
          if (name !== CACHE_NAME) return caches.delete(name);
        })
      )
    )
  );
  self.clients.claim();
});

// Fetch event — respond with cache or fetch from network
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .catch(() => caches.match(event.request))
      .then(response => {
        return response || caches.match('/offline.html');
      })
  );
});
