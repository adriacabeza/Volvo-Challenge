var mymap = L.map("mapid").setView([47.4245, 9.3767, -0.09], 13);

L.tileLayer(
  "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}",
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken:
      "pk.eyJ1Ijoic3RhcnRoYWNrcHJpbmdsZXMiLCJhIjoiY2p0MHE0Mnd1MDB6NzN5cGdxczVoZmNyNiJ9.i0AHQnmU9XumQVTaUE-7NA"
  }
).addTo(mymap);

const carIcon = L.icon({
  iconUrl: "car.png",
  iconSize: [38, 38], // size of the icon
  iconAnchor: [19, 19], // point of the icon which will correspond to marker's location
  popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
});

// Fake cars coordinates.
const cars = [
  {
    lat: 47.4245,
    lng: 9.3767
  }
  // {
  //   lat: 47.4445,
  //   lng: 9.3967
  // }
];

// Bind icons to map at coordinates of cars.
const icons = cars.map(c =>
  L.marker([c.lat, c.lng], { icon: carIcon }).addTo(mymap)
);

// Button when map is clicked to get destination.
function createButton(label, container) {
  var btn = L.DomUtil.create("button", "", container);
  btn.setAttribute("type", "button");
  btn.innerHTML = label;
  return btn;
}

// If click on map, set it to destination for the route.
mymap.on("click", function(e) {
  var container = L.DomUtil.create("div");
  let destBtn = createButton("Go to this location", container);

  L.popup()
    .setContent(container)
    .setLatLng(e.latlng)
    .openOn(mymap);
  L.DomEvent.on(destBtn, "click", function() {
    getRoute(e.latlng);
    mymap.closePopup();
  });
});

// Compute the route given the destination point.
function getRoute(latlng) {
  L.Routing.control({
    waypoints: [
      L.latLng(cars[0].lat, cars[0].lng),
      L.latLng(latlng.lat, latlng.lng)
    ],
    routeWhileDragging: true,
    show: false
  }).addTo(mymap);
}

// let routes;

// L.Routing.control({
//   waypoints: [
//     L.latLng(cars[0].lat, cars[0].lng),
//     L.latLng(cars[1].lat, cars[1].lng)
//   ],
//   routeWhileDragging: true,
//   show: false,
//   createMarker: function() {
//     return null;
//   }
// })
//   .on("routesfound", function(e) {
//     routes = e.routes[0];
//     console.log(routes);
//     // startInterval();
//   })
//   .addTo(mymap);

// function startInterval() {
//   let count = 0;
//   let increasing = true;
//   setInterval(() => {
//     [cars[0].lat, cars[0].lng] = [
//       routes.coordinates[count].lat,
//       routes.coordinates[count].lng
//     ];
//     icons[0].setLatLng(new L.LatLng(cars[0].lat, cars[0].lng));
//     if (count === routes.coordinates.length - 1) {
//       increasing = false;
//     } else if (count === 0) {
//       increasing = true;
//     }
//     count = increasing ? count + 1 : count - 1;
//   }, 200);
// }

// setInterval(() => {
//   cars[1].lng = cars[1].lng - 0.0001;
//   icons[1].setLatLng(new L.LatLng(cars[1].lat, cars[1].lng));
// }, 20);
