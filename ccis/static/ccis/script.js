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


//function loadCardInfo(cardId) {
//    const modal = $('#processoModal');
//    const modalBody = modal.find('.modal-body');
//
//    // Realizar uma solicitação AJAX para obter os detalhes do card
//    $.ajax({
//        url: `/card_detl/${cardId}`,  // Substitua pela URL correta da sua view
//        method: 'GET',
//        dataType: 'json',
//        success: function (data) {
//            if (data) {
//                // Os dados do card foram retornados com sucesso
//                // Preencha o modal com esses dados
//
//                // Use variáveis para armazenar os seletores dos elementos do modal
//                const assuntoInfo = $("#assuntoInfo");
//                const servicoInfo = $("#servicoInfo");
//                const codInfo = $("#codInfo");
//                const nomeSolicitante = $("#nomeSolicitante");
//                const sexoSolicitante = $("#sexoSolicitante");
//                const fotoSolicitante = $("#fotoSolicitante");
//                const cpfSolicitante = $("#cpfSolicitante");
//                const loginSolicitante = $("#loginSolicitante");
//                const emailSolicitante = $("#emailSolicitante");
//                const ramalSolicitante = $("#ramalSolicitante");
//                const areaSolicitante = $("#areaSolicitante");
//                const sectorInfo = $("#sectorInfo");
//                const statusHistory = $("#statusHistory"); // Adicione este seletor
//
//                // Preencha os campos relacionados ao card
//                assuntoInfo.text(data.card.assunto);
//                servicoInfo.text(` / ${data.card.service}`);
//                codInfo.text(`N° ${data.card.idCard}`);
//
//                // Preencha os campos relacionados ao solicitante
//                nomeSolicitante.text(data.card.solicitante_dados_pessoais.nomeCompleto);
//                sexoSolicitante.text(data.card.solicitante_dados_pessoais.sexo);
//                cpfSolicitante.text(data.card.solicitante_dados_pessoais.cpf);
//
//                // Verifique se a foto do solicitante existe
//                if (data.card.solicitante_dados_pessoais.foto) {
//                    fotoSolicitante.attr("src", data.card.solicitante_dados_pessoais.foto);
//                } else {
//                    // Caso não haja foto, defina um valor padrão ou oculte o elemento
//                    fotoSolicitante.attr("src", "caminho_para_foto_padrao.jpg");
//                    // Ou, se preferir, esconda o elemento completamente
//                    // fotoSolicitante.hide();
//                }
//
//                // Preencha os campos relacionados ao solicitante
//                loginSolicitante.text(data.card.solicitante.username);
//                emailSolicitante.text(data.card.solicitante.email);
//
//                // Verifique se o ramal do solicitante existe
//                if (data.card.solicitante_contato.ramal) {
//                    ramalSolicitante.text(data.card.solicitante_contato.ramal);
//                } else {
//                    ramalSolicitante.text("N/A");
//                }
//
//                if (data.card.solicitante_contato.ramal) {
//                    areaSolicitante.text(data.card.solicitante_profissional.area);
//                } else {
//                    areaSolicitante.text("N/A");
//                }
//
//                // Preencha o histórico de status
//                statusHistory.empty(); // Limpa qualquer conteúdo anterior
//
//                if (data.history && data.history.length > 0) {
//                    data.history.forEach(function (entry) {
//                        const li = $("<li>").text(entry.status_atual);
//                        statusHistory.append(li);
//                    });
//                } else {
//                    statusHistory.append("<li>Nenhum histórico de status disponível.</li>");
//                }
//
//                // Obtenha o setor_atual da tabela CardSetorHistory
//                if (data.card.setor_history && data.card.setor_history.length > 0) {
//                    const setorAtual = data.card.setor_history[0].setor_atual;
//                    sectorInfo.text(setorAtual);
//                } else {
//                    sectorInfo.text("Setor não encontrado");
//                }
//
//                // Abra o modal
//                modal.modal('show');
//            } else {
//                alert('Dados do card não encontrados.');
//            }
//        },
//        error: function () {
//            alert('Erro ao buscar os detalhes do card');
//        }
//    });
//}

// Configure o cabeçalho CSRF para solicitações AJAX
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        }
    }
});

function csrfSafeMethod(method) {
    // Esses métodos não exigem um token CSRF
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Procura o nome do cookie
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}





function loadCardInfo(cardId) {
    const modal = $('#processoModal');
    const modalBody = modal.find('.modal-body');

    // Realizar uma solicitação AJAX para obter os detalhes do card
    $.ajax({
        url: `/card_detl/${cardId}`,  // Substitua pela URL correta da sua view
        method: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data) {
                // Os dados do card foram retornados com sucesso
                // Preencha o modal com esses dados

                // Use variáveis para armazenar os seletores dos elementos do modal
                const assuntoInfo = $("#assuntoInfo");
                const servicoInfo = $("#servicoInfo");
                const codInfo = $("#codInfo");
                const nomeSolicitante = $("#nomeSolicitante");
                const sexoSolicitante = $("#sexoSolicitante");
                const fotoSolicitante = $("#fotoSolicitante");
                const cpfSolicitante = $("#cpfSolicitante");
                const loginSolicitante = $("#loginSolicitante");
                const emailSolicitante = $("#emailSolicitante");
                const ramalSolicitante = $("#ramalSolicitante");
                const areaSolicitante = $("#areaSolicitante");
                const sectorInfo = $("#sectorInfo");
                const nomeResponsavel = $("#nomeResponsavel");
                const horarioAbertura = $("#horarioAbertura");

                // Preencha os campos relacionados ao card
                assuntoInfo.text(data.card.assunto);
                servicoInfo.text(` / ${data.card.service}`);
                codInfo.text(`N° ${data.card.idCard}`);

                // Preencha os campos relacionados ao solicitante
                nomeSolicitante.text(data.card.solicitante_dados_pessoais.nomeCompleto);
                sexoSolicitante.text(data.card.solicitante_dados_pessoais.sexo);
                cpfSolicitante.text(data.card.solicitante_dados_pessoais.cpf);

                // Verifique se a foto do solicitante existe
                if (data.card.solicitante_dados_pessoais.foto) {
                    fotoSolicitante.attr("src", data.card.solicitante_dados_pessoais.foto);
                } else {
                    // Caso não haja foto, defina um valor padrão ou oculte o elemento
                    fotoSolicitante.attr("src", "caminho_para_foto_padrao.jpg");
                    // Ou, se preferir, esconda o elemento completamente
                    // fotoSolicitante.hide();
                }

                // Preencha os campos relacionados ao solicitante
                loginSolicitante.text(data.card.solicitante.username);
                emailSolicitante.text(data.card.solicitante.email);

                // Verifique se o ramal do solicitante existe
                if (data.card.solicitante_contato.ramal) {
                    ramalSolicitante.text(data.card.solicitante_contato.ramal);
                } else {
                    ramalSolicitante.text("N/A");
                }

                if (data.card.solicitante_contato.ramal) {
                    areaSolicitante.text(data.card.solicitante_profissional.area);
                } else {
                    areaSolicitante.text("N/A");
                }


                // Preencha o histórico de status
                const statusHistory = modalBody.find(".container-buttons");
                statusHistory.empty(); // Limpa qualquer conteúdo anterior

                if (data.history && data.history.length > 0) {
                    data.history.forEach(function (entry) {
                        // Crie um elemento HTML para representar cada entrada do histórico
                        const historyItem = $("<span>").addClass("processo-tag-historico");
                        historyItem.html(`<i class="fa-regular fa-compass"></i> ${entry.status_atual}`);

                        // Adicione o elemento ao histórico de status
                        statusHistory.append(historyItem);
                    });
                } else {
                    statusHistory.append("<span>Nenhum histórico de status disponível.</span>");
                }


                // Exiba o horário de abertura do chamado personalizado ------------------------------------------------
                const horarioAberturaCard = new Date(data.card.dataCriacao);
                const horarioAtual = new Date();
                const diferencaMilissegundos = horarioAtual - horarioAberturaCard;
                const diferencaMinutos = Math.floor(diferencaMilissegundos / (1000 * 60)); // Diferença em minutos
                const diferencaHoras = Math.floor(diferencaMilissegundos / (1000 * 60 * 60)); // Diferença em horas
                const diferencaDias = Math.floor(diferencaMilissegundos / (1000 * 60 * 60 * 24)); // Diferença em dias
                const diferencaMeses = Math.floor(diferencaMilissegundos / (1000 * 60 * 60 * 24 * 30.44)); // Diferença em meses aproximados

                let mensagemHorarioAbertura = "";

                if (diferencaMinutos < 60) {
                    mensagemHorarioAbertura = `Criado há ${diferencaMinutos} minuto(s)`;
                } else if (diferencaHoras < 24) {
                    mensagemHorarioAbertura = `Criado há ${diferencaHoras} hora(s)`;
                } else if (diferencaDias < 30) {
                    mensagemHorarioAbertura = `Criado há ${diferencaDias} dia(s)`;
                } else {
                    mensagemHorarioAbertura = `Criado há ${diferencaMeses} mês(es)`;
                }

                horarioAbertura.text(mensagemHorarioAbertura);



                // Dentro do loop que renderiza as mensagens do chat ---------------------------------------------------

                // Realizar uma solicitação AJAX para obter os detalhes do card
 // Ao clicar em "Enviar Resposta"
$('#enviarResposta').click(function () {
    const resposta = $('#resposta').val();

    // Verifique se a resposta não é nula ou vazia
    if (resposta.trim() !== '') {
        // Adicione a resposta à lista de mensagens como "pendente"
        const messageText = resposta;  // Substitua pelo campo correto da resposta
        const messageElement = $("<div>").addClass("mt-1 mensagem-pendente").css("background-color", "#d9d9d9");
        const messageTextElement = $("<div>").addClass("col").html(messageText);
        messageElement.append(messageTextElement);
        $("#messageContainer").append(messageElement);

        // Limpe o campo de resposta
        $('#resposta').val('');

        // Realize uma solicitação AJAX para enviar a resposta
        $.ajax({
            url: `/enviar_resposta/${cardId}`,
            method: 'POST',
            data: {
                resposta: resposta
            },
            dataType: 'json',
            success: function (data) {
                // Atualize a mensagem como "enviada com sucesso"
                messageElement.removeClass("mensagem-pendente");
                messageElement.css("background-color", "#dfffe7");

                // Limpe o campo de resposta
                $('#resposta').val('');
            },
            error: function () {
                // Exiba uma mensagem de erro
                alert('Erro ao enviar resposta');
            }
        });
    } else {
        alert('Por favor, insira uma resposta válida');
    }
});


                // -----------------------------------------------------------------------------------------------------




//                // Se alguém estiver atendendo, exiba o nome do atendente
//                if (data.card.responsavel) {
//                    const atendenteNome = data.card.responsavel.first_name + ' ' + data.card.responsavel.last_name;
//                    nomeResponsavel.text(atendenteNome);
//                }
//                } else {
//                    nomeResponsavel.text("Aguardando atendimento");
//                }



                // Obtenha o setor_atual da tabela CardSetorHistory
                if (data.card.setor_history && data.card.setor_history.length > 0) {
                    const setorAtual = data.card.setor_history[0].setor_atual;
                    sectorInfo.text(setorAtual);
                } else {
                    sectorInfo.text("Setor não encontrado");
                }

                // Abra o modal
                modal.modal('show');
            } else {
                alert('Dados do card não encontrados.');
            }
        },
        error: function () {
            alert('Erro ao buscar os detalhes do card');
        }
    });
}


//
//// Exiba o nome, sobrenome e data do remetente
//                const remetente = data.card.messages[0];
//                const nomeCompleto = `${remetente.remetente_first_name} ${remetente.remetente_last_name}`;
//                const dataHora = new Date(remetente.datetime);
//
//                $("#nomeRemetente").text(nomeCompleto);