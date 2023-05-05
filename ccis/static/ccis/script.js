function filterTable() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("inputUser");
  filter = input.value.toUpperCase();
  table = document.getElementById("tableUser");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td");
    for (var j = 0; j < td.length; j++) {
      txtValue = td[j].textContent || td[j].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        break;
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'

// Fetch all the forms we want to apply custom Bootstrap validation styles to
var forms = document.querySelectorAll('.needs-validation')

// Loop over them and prevent submission
Array.prototype.slice.call(forms)
.forEach(function (form) {
form.addEventListener('submit', function (event) {
if (!form.checkValidity()) {
event.preventDefault()
event.stopPropagation()
}

form.classList.add('was-validated')
}, false)
})
})()


//
//jQuery(document).ready(function() {
//
//    $('.dismiss, .overlay').on('click', function() {
//        $('.sidebar').removeClass('active');
//        $('.overlay').removeClass('active');
//    });
//
//    $('.open-menu').on('click', function(e) {
//        e.preventDefault();
//        $('.sidebar').addClass('active');
//        $('.overlay').addClass('active');
//        // close opened sub-menus
//        $('.collapse.show').toggleClass('show');
//        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
//    });
//
//    /* other code */
//
//});
//
///*
//  Navigation
//*/
//
//$('a.scroll-link').on('click', function(e) {
//    e.preventDefault();
//    scroll_to($(this), 0);
//});
//
//function scroll_to(clicked_link, nav_height) {
//    var element_class = clicked_link.attr('href').replace('#', '.');
//    var scroll_to = 0;
//    if(element_class != '.top-content') {
//        element_class += '-container';
//        scroll_to = $(element_class).offset().top - nav_height;
//    }
//    if($(window).scrollTop() != scroll_to) {
//        $('html, body').stop().animate({scrollTop: scroll_to}, 1000);
//    }
//}
//
//
//$('.sidebar').mCustomScrollbar({
//    theme: "minimal-dark"
//});