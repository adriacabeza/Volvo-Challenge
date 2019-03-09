var mymap = L.map("mapid").setView([47.371637, 8.542088, -0.09], 13);

var geocoder = L.Control.Geocoder.nominatim();

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
  iconSize: [38, 38] // size of the icon
});
const greenCarIcon = L.icon({
  iconUrl: "carGreen.png",
  iconSize: [38, 38] // size of the icon
});

// Fake route coordinates
const fakeRoute = [
  [8.53684, 47.374991],
  [8.537446, 47.375113],
  [8.537148, 47.375663],
  [8.538688, 47.377254],
  [8.54382, 47.376391],
  [8.544428, 47.379361],
  [8.545379, 47.378802],
  [8.547295, 47.375369],
  [8.549012, 47.375745],
  [8.549553, 47.374735],
  [8.55237, 47.374773],
  [8.553359, 47.375987],
  [8.552843, 47.377149],
  [8.558202, 47.37541],
  [8.560014, 47.37655],
  [8.556334, 47.378956],
  [8.551755, 47.382316],
  [8.549021, 47.383664],
  [8.548393, 47.384488],
  [8.548498, 47.385919],
  [8.54769, 47.386742],
  [8.544311, 47.387608],
  [8.538942, 47.391381],
  [8.534833, 47.39143],
  [8.531629, 47.393036],
  [8.526872, 47.39439],
  [8.525316, 47.394271],
  [8.524882, 47.395016],
  [8.525466, 47.39465],
  [8.523771, 47.392675],
  [8.519464, 47.395156],
  [8.520625, 47.394959],
  [8.524712, 47.393657],
  [8.524331, 47.392829],
  [8.510534, 47.378507],
  [8.493118, 47.385827],
  [8.492906, 47.38468],
  [8.494383, 47.384011],
  [8.491598, 47.381181],
  [8.498596, 47.377597],
  [8.503946, 47.373221],
  [8.502431, 47.371657],
  [8.501262, 47.368661],
  [8.502868, 47.364368],
  [8.507209, 47.359826],
  [8.507612, 47.359377],
  [8.505324, 47.358344],
  [8.502426, 47.36125],
  [8.504659, 47.36246],
  [8.502868, 47.364368],
  [8.501249, 47.368752],
  [8.502431, 47.371657],
  [8.503946, 47.373221],
  [8.499365, 47.377328],
  [8.510567, 47.378073],
  [8.513943, 47.38194],
  [8.522142, 47.390291],
  [8.523292, 47.390715],
  [8.524809, 47.390522],
  [8.536737, 47.383415],
  [8.538093, 47.38138],
  [8.53744, 47.379499],
  [8.541372, 47.378284],
  [8.541692, 47.374429],
  [8.537412, 47.374679],
  [8.535419, 47.373164],
  [8.53509, 47.373712],
  [8.538688, 47.377254],
  [8.543096, 47.376811],
  [8.54357, 47.376374],
  [8.544451, 47.376725],
  [8.548456, 47.370452],
  [8.553446, 47.366827],
  [8.552369, 47.365445],
  [8.556414, 47.364012],
  [8.562158, 47.360716],
  [8.568442, 47.360082],
  [8.572739, 47.357397],
  [8.576178, 47.353296],
  [8.577955, 47.3489],
  [8.577051, 47.344628]
];

console.log(fakeRoute);

const cars = [];
for (let i = 0; i < 10; i++) {
  let index = Math.floor(Math.random() * fakeRoute.length);
  cars.push({
    lng: fakeRoute[index][0],
    lat: fakeRoute[index][1],
    name: `Best Volvo ever #${i + 1}`
  });
}

let selectedCar;
let route;
let destination;

// Fake cars coordinates.
// const cars = [
//   {
//     lat: 47.4245,
//     lng: 9.3767,
//     name: "Best Volvo ever"
//   }
// {
//   lat: 47.4445,
//   lng: 9.3967
// }
// ];

// Bind icons to map at coordinates of cars.
const icons = cars.map((c, i) => {
  var popcontainer = L.DomUtil.create("div");
  let name = popcontainer.appendChild(document.createElement("h5"));
  name.innerHTML = c.name;
  let selectButton = createButton("Select this car", popcontainer);
  selectButton.onclick = () => {
    if (route) {
      mymap.removeControl(route);
    }
    if (selectedCar != null) {
      // if a car is already selected, change its color back to black.
      for (let i = 0; i < cars.length; i++) {
        if (cars[i].name === selectedCar.name) {
          icons[i].setIcon(carIcon);
        }
      }
    }
    mymap.closePopup();
    selectedCar = c;
    icons[i].setIcon(greenCarIcon);
  };
  return L.marker([c.lat, c.lng], { icon: carIcon })
    .addTo(mymap)
    .bindPopup(popcontainer);
});

console.log(cars);

// const popups = cars.map(c => {
//   var popcontainer = L.DomUtil.create("div");
//   let name = popcontainer.appendChild(document.createElement("h5"));
//   name.innerHTML = c.name;
//   L.popup()
//     .setContent(popcontainer)
//     .setLatLng(c);
//   // .openOn(mymap);
// });

// Button when map is clicked to get destination.
function createButton(label, container) {
  var btn = L.DomUtil.create("button", "", container);
  btn.setAttribute("type", "button");
  btn.innerHTML = label;
  return btn;
}

// If click on map, set it to destination for the route.
mymap.on("click", function(e) {
  if (selectedCar == null) {
    return null;
  }
  var container = L.DomUtil.create("div");
  let destBtn = createButton("Go to this location", container);

  geocoder.reverse(
    e.latlng,
    mymap.options.crs.scale(mymap.getZoom()),
    results => {
      destination = results[0].name;
      let destinationDiv = document.querySelector("#destination");
      let destinationAddress = document.querySelector("#destinationAddress");
      destinationAddress.innerHTML = destination;
      destinationDiv.style.opacity = 1;
    }
  );

  L.popup()
    .setContent(container)
    .setLatLng(e.latlng)
    .openOn(mymap);
  L.DomEvent.on(destBtn, "click", function() {
    if (route) {
      mymap.removeControl(route);
    }
    getRoute(e.latlng);
    document.querySelector("#confirm").style.opacity = 1;
    mymap.closePopup();
  });
});

// Compute the route given the destination point.
function getRoute(latlng) {
  route = L.Routing.control({
    waypoints: [
      L.latLng(selectedCar.lat, selectedCar.lng),
      L.latLng(latlng.lat, latlng.lng)
    ],
    routeWhileDragging: true,
    show: false,
    createMarker: function(i, start) {
      if (i === 0) {
        return null;
      } else {
        return L.marker(start.latLng);
      }
    }
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
