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

//$(document).ready(function () {
//    // Adicione um evento de clique aos botões dos cards para abrir o modal
//    $('.processo-link').on('click', function () {
//        // Obtenha o ID do card a partir do atributo data-card-id
//        var card_id = $(this).data('card-id');
//
//        // Faça uma solicitação AJAX para obter informações do card
//        $.ajax({
//            url: '/obter_informacoes_card/' + card_id + '/',
//            method: 'GET',
//            dataType: 'json',
//            success: function (data) {
//                // Preencha o modal com os dados obtidos
//
//                // Campos do modal relacionados ao card
//                $('#modal-assunto').text(data.assunto);
//                $('#modal-servico').text(data.servico);
//                $('#modal-setor').text(data.setor_do_card);
//                $('#modal-card-id').text(data.card_id);
//
//                // Campos relacionados ao solicitante
//                $('#modal-nome-completo').text(data.nomeCompleto);
//                $('#modal-cpf').text(data.cpf);
//                $('#modal-sexo').text(data.sexo);
//                $('#modal-foto').attr('src', data.foto);
//
//                // Campos relacionados ao profissional
//                $('#modal-area').text(data.area);
//
//                // Campos relacionados ao contato
//                $('#modal-email-corporativo').text(data.emailCorporativo);
//                $('#modal-ramal').text(data.ramal);
//
//                // Preencha o histórico
//                var historicoHtml = '';
//                for (var i = 0; i < data.historico.length; i++) {
//                    historicoHtml += '<div>' + data.historico[i].previous_status + ' -> ' + data.historico[i].current_status + '</div>';
//                }
//                $('#modal-historico').html(historicoHtml);
//
//                // Preencha o histórico de mensagens
//                var mensagemHtml = '';
//                for (var j = 0; j < data.message_history.length; j++) {
//                    mensagemHtml += '<div>';
//                    mensagemHtml += '<p>' + data.message_history[j].message + '</p>';
//                    mensagemHtml += '<p>Enviado por: ' + data.message_history[j].author_name + '</p>';
//                    mensagemHtml += '<p>Data e hora: ' + data.message_history[j].timestamp + '</p>';
//                    if (data.message_history[j].attachment) {
//                        mensagemHtml += '<p>Anexo: <a href="' + data.message_history[j].attachment + '">Download</a></p>';
//                    }
//                    mensagemHtml += '</div>';
//                }
//                $('#modal-message-history').html(mensagemHtml);
//
//                // Abra o modal
//                $('#processoModal').modal('show');
//            },
//            error: function () {
//                alert('Erro ao carregar informações do card.');
//            }
//        });
//    });
//});




// Função para carregar as informações do card no modal
function carregarInformacoesCard(card_id) {
    $.ajax({
        url: `/obter_informacoes_card/${card_id}/`,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // Preencha os campos do modal com as informações obtidas
            $('#assuntoInfo').text(data.assunto);
            $('#servicoInfo').text(data.servico);

            // Preencha os campos do solicitante
            $('#nomeCompleto').text(data.nomeCompleto);
            $('#cpf').text(data.cpf);
            $('#usuarioSisbr').text(data.usuario_sisbr);
            $('#email').text(data.email);
            $('#ramal').text(data.ramal);
            $('#setor').text(data.setor);

            // Preencha o histórico
            var historicoHtml = '';
            data.historico.forEach(function (historico) {
                historicoHtml += `<li>${historico.previous_status} &rarr; ${historico.current_status} em ${historico.datetime}</li>`;
            });
            $('#historicoList').html(historicoHtml);

            // Preencha as mensagens
            var mensagensHtml = '';
            data.message_history.forEach(function (mensagem) {
                mensagensHtml += `
                    <div class="mt-2 p-2" style="background-color:#d9d9d9">
                        <div class="row pt-2">
                            <div class="col-auto me-auto">
                                <h6>
                                    <img class="avatar-img" src="{% static 'ccis/avatar.jpg' %}" alt="" width="40" height="40">
                                    ${mensagem.author_name}
                                </h6>
                            </div>
                            <div class="col-auto">
                                <span>${mensagem.timestamp}</span>
                            </div>
                        </div>
                        <div class="p-2">
                            <p>${mensagem.message}</p>
                            ${mensagem.attachment ? `<a href="${mensagem.attachment}" download>Download Anexo</a>` : ''}
                        </div>
                    </div>
                `;
            });
            $('#mensagemList').html(mensagensHtml);

            // Abra o modal
            $('#processoModal').modal('show');
        },
        error: function () {
            alert('Erro muito errado ao carregar informações do card.');
        }
    });
}

// Quando o modal for mostrado, carregue as informações do card
$('#processoModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var card_id = button.data('card-id');
    carregarInformacoesCard(card_id);
});







