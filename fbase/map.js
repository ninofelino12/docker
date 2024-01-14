
var mapOptions = {
    center: [-6.193549, 106.786249],
    zoom: 18,
  };


// Fungsi untuk menangani kesalahan permintaan geolocation

  var map = new L.map("peta", mapOptions);

  var layer = new L.TileLayer(
    "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
  );

  var markerOptions = {
    title: "MyLocations",
    clickable: true,
  };

  var marker = L.marker([-9.5957,206.7978]);

  // marker.bindPopup("Sekolah Sanggar").openPopup();
  // marker.addTo(map);

   map.addLayer(layer);