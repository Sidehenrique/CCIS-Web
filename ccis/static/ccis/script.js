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


// Tratamento da view novo_user para esconder o display
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


// Tratamento da view novo_user para esconder o display ----------------------------------------------------------------
function displayFilePag(input) {
    var filePage = input.files[0].name;
    document.getElementById('file-Page').textContent = filePage;
}

document.addEventListener("DOMContentLoaded", function() {

    const pag1 = document.getElementById("pag1");
    const pag2 = document.getElementById("pag2");

    document.getElementById("pagBtn1").addEventListener("click", function() {
        pag1.style.display = "block";
        pag2.style.display = "none";
    });


    document.getElementById("pagBtn2").addEventListener("click", function() {
        pag1.style.display = "none";
        pag2.style.display = "block";
    });

});



// Tratamento PAGINA TECNOLOGIA ----------------------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {

    const menuInicial = document.getElementById("menu-inicial");
    const informativoTI = document.getElementById("informativoTI");
    const formularioAcessos = document.getElementById("formularioAcessos");
    const formularioEquipamentos = document.getElementById("formularioEquipamentos");
    const formularioServicos = document.getElementById("formularioServicos");

    //------------------------------------------------------------------------------------------------------------------


    //------------------------------------------------------------------------------------------------------------------
    document.getElementById("btnAcessos").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "block";
        formularioEquipamentos.style.display = "none";
        formularioServicos.style.display = "none";
    });


    document.getElementById("btnEquipamentos").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "none";
        formularioEquipamentos.style.display = "block";
        formularioServicos.style.display = "none";
    });


    document.getElementById("btnServicos").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "none";
        formularioEquipamentos.style.display = "none";
        formularioServicos.style.display = "block";
    });
    //------------------------------------------------------------------------------------------------------------------

});
//----------------------------------------------------------------------------------------------------------------------


// Tratamento do modal inativar_usuario da tabela da view usuário ------------------------------------------------------

$('.btn-inativar').click(function() {
var modalId = $(this).data('bs-target');
var nomeUsuario = $(this).siblings('.modal-body').find('p').text().trim();
$(modalId).find('.modal-body p').text(nomeUsuario);
});



function validarFormulario() {
    var password1 = document.getElementById('id_password1').value;
    var password2 = document.getElementById('id_password2').value;
    var group = document.getElementById('id_group').value;

    if (password1.length < 8) {
        document.getElementById('password1-error').textContent = 'A senha deve ter pelo menos 8 caracteres.';
        return false;
    }

    if (/^\d+$/.test(password1)) {
        document.getElementById('password1-error').textContent = 'A senha não pode ser totalmente numérica.';
        return false;
    }

    if (password1 !== password2) {
        document.getElementById('password1-error').textContent = 'As senhas não coincidem.';
        return false;
    }

    if (!group) {
        document.getElementById('password1-error').textContent = 'Selecione um grupo.';
        return false;
    }

    if (true) {document.getElementById('password1-error').textContent = '';
    }

    return true;

}


function handleScroll(event) {
  const container = document.querySelector('.container-buttons');
  container.scrollLeft += event.deltaY; // Ajusta a posição de rolagem horizontal
  event.preventDefault(); // Impede o comportamento padrão do scroll do mouse
}



//---------------------------- MODAL DO PROCESSO -----------------------------------------------------------------------
//function loadCardInfo(cardId) {
//    // Fazer uma solicitação à API para buscar as informações do card com base no cardId
//    fetch(`card_detl/${cardId}`)
//        .then((response) => {
//            if (!response.ok) {
//                throw new Error(`Erro na solicitação: ${response.statusText}`);
//            }
//            return response.json();
//        })
//        .then((data) => {
//            // Manipular os dados do card aqui e atualizar o modal com as informações
//            const cardInfo = data; // Os dados do card estão em 'data'
//
//            // Atualizar o modal com as informações do card
//            document.getElementById('assuntoInfo').textContent = cardInfo.assunto;
//            document.getElementById('servicoInfo').textContent = `/  ${cardInfo.service}`;
//
//            document.getElementById('codCard').textContent = `N° ${cardInfo.idCard}`;
//            document.getElementById('sector').textContent = 'outracoisa'
//
//
//            // Exibir o modal
//            $('#processoModal').modal('show');
//        })
//        .catch((error) => {
//            console.error(error);
//            // Tratar erros aqui, por exemplo, exibindo uma mensagem de erro no modal
//        });
//}
//

function loadCardInfo(cardId) {
    // Realizar uma solicitação AJAX para obter os detalhes do card
    $.ajax({
        url: `/card_detl/${cardId}`,  // Substitua pela URL correta da sua view
        method: 'GET',
        dataType: 'json',
        success: function (data) {
            // Os dados do card serão retornados aqui em 'data'
            // Agora você pode preencher o modal com esses dados
            $("#assuntoInfo").text(data.assunto);
            $("#servicoInfo").text(` / ${data.service}`);
            $("#codInfo").text(`N° ${data.idCard}`);
            $("#sectorInfo").text(data.setor_nome);

            // Abra o modal
            $('#processoModal').modal('show');
        },
        error: function () {
            alert('Erro ao buscar os detalhes do card');
        }
    });
}