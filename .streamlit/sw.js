const CACHE_NAME = 'traductor-pwa-v1';
const urlsToCache = [
  '/',
  '/static/css/main.css',
  '/static/js/main.js'
];

// Evento de Instalación: Almacena en caché los recursos principales
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Caché abierta exitosamente');
        return cache.addAll(urlsToCache);
      })
  );
});

// Evento Fetch: Intercepta las peticiones para servir desde caché o red
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
