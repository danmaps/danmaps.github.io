(function () {
  function parseLatLng(value, fallback) {
    if (!value || typeof value !== 'string') return fallback;
    var parts = value.split(',').map(function (p) { return Number(p.trim()); });
    if (parts.length !== 2 || Number.isNaN(parts[0]) || Number.isNaN(parts[1])) return fallback;
    return [parts[0], parts[1]];
  }

  function parseRoute(value) {
    if (!value) return [];
    return value
      .split(';')
      .map(function (pair) { return parseLatLng(pair, null); })
      .filter(Boolean);
  }

  function create(element, options) {
    if (!element || typeof L === 'undefined') return null;

    var dataset = element.dataset || {};
    var center = parseLatLng(dataset.center, [37.8, -96]);
    var zoom = Number(dataset.zoom || 10);

    var map = L.map(element, { scrollWheelZoom: false }).setView(center, zoom);

    var tileUrl = dataset.tileUrl || 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var attribution = dataset.attribution || '&copy; OpenStreetMap contributors';
    L.tileLayer(tileUrl, { attribution: attribution }).addTo(map);

    var marker = null;
    if (dataset.marker) {
      marker = L.marker(parseLatLng(dataset.marker, center)).addTo(map);
      if (dataset.popup) marker.bindPopup(dataset.popup);
    }

    var routeLayer = null;
    if (dataset.route) {
      var routeLatLngs = parseRoute(dataset.route);
      if (routeLatLngs.length > 1) {
        routeLayer = L.polyline(routeLatLngs, {
          color: options && options.routeColor ? options.routeColor : '#60a5fa',
          weight: 4,
          opacity: 0.9
        }).addTo(map);
      }
    }

    var api = {
      map: map,
      marker: marker,
      routeLayer: routeLayer,
      setView: function (latlng, nextZoom) {
        map.flyTo(latlng, nextZoom, { duration: 0.7 });
      }
    };

    element.__mapEmbed = api;
    return api;
  }

  function initFromDom() {
    var nodes = document.querySelectorAll('.map-embed[data-center]');
    nodes.forEach(function (node) {
      if (!node.__mapEmbed) create(node);
    });
  }

  window.DanMapEmbed = {
    create: create,
    parseLatLng: parseLatLng
  };

  document.addEventListener('DOMContentLoaded', initFromDom);
})();
