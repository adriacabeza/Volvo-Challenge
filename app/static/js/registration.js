document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});




/////////////
function readURLSelfie(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          var img = document.getElementById('selfie');
          img.src = e.target.result;
          img.width = 150;
          img.height = 200;
      };
      reader.readAsDataURL(input.files[0]);
  }
}

function readURLLicense(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          var img = document.getElementById('license');
          img.src = e.target.result;
          img.width = 150;
          img.height = 200;
      };
      reader.readAsDataURL(input.files[0]);
  }
}
