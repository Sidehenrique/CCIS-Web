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



function displayFileName(input) {
    var fileName = input.files[0].name;
    document.getElementById('file-name').textContent = fileName;
}

document.addEventListener("DOMContentLoaded", function() {

    const form1 = document.getElementById("form1");
    const form2 = document.getElementById("form2");

    document.getElementById("nextBtn1").addEventListener("click", function() {
        form1.style.display = "none";
        form2.style.display = "block";
    });


    document.getElementById("prevBtn2").addEventListener("click", function() {
        form2.style.display = "none";
        form1.style.display = "block";
    });

});
