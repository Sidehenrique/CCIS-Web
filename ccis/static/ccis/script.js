
// Filtrar Campos tabela -------------------------------------------------------------------------------------
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



// Example starter JavaScript for disabling form submissions if there are invalid fields ---------------------
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



// Tratamento da view novo_user para esconder o display --------------------------------------------------------
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



// Tratamento da view novo_user para esconder o display --------------------------------------------------------
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



// Tratamento PAGINA TECNOLOGIA ---------------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {

    const menuInicial = document.getElementById("menu-inicial");
    const informativoTI = document.getElementById("informativoTI");
    const formularioAcessos = document.getElementById("formularioAcessos");
    const formularioEquipamentos = document.getElementById("formularioEquipamentos");
    const formularioDesenvolvimento = document.getElementById("formularioDesenvolvimento");
    const formularioServicos = document.getElementById("formularioServicos");
    const formularioCI = document.getElementById("formularioCI");
    const formularioApontamentos = document.getElementById("formularioApontamentos");

    //------------------------------------------------------------------------------------------------------------------


    //------------------------------------------------------------------------------------------------------------------
    document.getElementById("btnAcessos").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "block";
        formularioEquipamentos.style.display = "none";
        formularioServicos.style.display = "none";
        formularioDesenvolvimento.style.display = "none";
        formularioCI.style.display = "none";
        formularioApontamentos.style.display = "none";
    });


    document.getElementById("btnEquipamentos").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "none";
        formularioEquipamentos.style.display = "block";
        formularioServicos.style.display = "none";
        formularioDesenvolvimento.style.display = "none";
        formularioCI.style.display = "none";
        formularioApontamentos.style.display = "none";
    });

    document.getElementById("btnServicos").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "none";
        formularioEquipamentos.style.display = "none";
        formularioServicos.style.display = "block";
        formularioDesenvolvimento.style.display = "none";
        formularioCI.style.display = "none";
        formularioApontamentos.style.display = "none";
    });

    document.getElementById("btnDesenvolvimento").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "none";
        formularioEquipamentos.style.display = "none";
        formularioServicos.style.display = "none";
        formularioDesenvolvimento.style.display = "block";
        formularioCI.style.display = "none";
        formularioApontamentos.style.display = "none";
    });

    document.getElementById("btnCI").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "none";
        formularioEquipamentos.style.display = "none";
        formularioServicos.style.display = "none";
        formularioDesenvolvimento.style.display = "none";
        formularioCI.style.display = "block";
        formularioApontamentos.style.display = "none";
    });

    document.getElementById("btnApontamentos").addEventListener("click", function() {
        informativoTI.style.display = "none";
        formularioAcessos.style.display = "none";
        formularioEquipamentos.style.display = "none";
        formularioServicos.style.display = "none";
        formularioDesenvolvimento.style.display = "none";
        formularioCI.style.display = "none";
        formularioApontamentos.style.display = "block";
    });

    //------------------------------------------------------------------------------------------------------------------

});
//---------------------------------------------------------------------------------------------------------------


// Tratamento PAGINA DE REQUISIÇÕES SETORES ---------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {

    const menu_Inicial = document.getElementById("menu_inicial");
    const informativo = document.getElementById("informativo");

    const formulario1 = document.getElementById("formulario1");
    const formulario2 = document.getElementById("formulario2");
    const formulario3 = document.getElementById("formulario3");
    const formulario4 = document.getElementById("formulario4");
    const formulario5 = document.getElementById("formulario5");
    const formulario6 = document.getElementById("formulario6");

    //------------------------------------------------------------------------------------------------------------------


    //------------------------------------------------------------------------------------------------------------------
    document.getElementById("btn_request_1").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "block";
        formulario2.style.display = "none";
        formulario3.style.display = "none";
        formulario4.style.display = "none";
        formulario5.style.display = "none";
        formulario6.style.display = "none";
    });


    document.getElementById("btn_request_2").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "block";
        formulario3.style.display = "none";
        formulario4.style.display = "none";
        formulario5.style.display = "none";
        formulario6.style.display = "none";
    });


    document.getElementById("btn_request_3").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "block";
        formulario4.style.display = "none";
        formulario5.style.display = "none";
        formulario6.style.display = "none";
    });

    document.getElementById("btn_request_4").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "none";
        formulario4.style.display = "block";
        formulario5.style.display = "none";
        formulario6.style.display = "none";
    });

    document.getElementById("btn_request_5").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "none";
        formulario4.style.display = "none";
        formulario5.style.display = "block";
        formulario6.style.display = "none";
    });

    document.getElementById("btn_request_6").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "none";
        formulario4.style.display = "none";
        formulario5.style.display = "none";
        formulario6.style.display = "block";
    });

});
//---------------------------------------------------------------------------------------------------------------


// Tratamento do modal inativar_usuario da tabela da view usuário -----------------------------------------------
$('.btn-inativar').click(function() {
var modalId = $(this).data('bs-target');
var nomeUsuario = $(this).siblings('.modal-body').find('p').text().trim();
$(modalId).find('.modal-body p').text(nomeUsuario);
});


// Redefinição de Senha -----------------------------------------------------------------------------------------
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



// Configuração do scroll do mouse lateral -----------------------------------------------------------------------
function handleScroll(event) {
  const container = document.querySelector('.container-buttons');
  container.scrollLeft += event.deltaY; // Ajusta a posição de rolagem horizontal
  event.preventDefault(); // Impede o comportamento padrão do scroll do mouse
}


// Configure o cabeçalho CSRF para solicitações AJAX ---------------------------------------------------------
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
                // Use variáveis para armazenar os seletores dos elementos do modal
                const assuntoInfo = $("#assuntoInfo");
                const servicoInfo = $("#servicoInfo");
                const codInfo = $("#codInfo");
                const sectorInfo = $("#sectorInfo");
                const nomeSolicitante = $("#nomeSolicitante");
                const sexoSolicitante = $("#sexoSolicitante");
                const fotoSolicitante = $("#fotoSolicitante");
                const cpfSolicitante = $("#cpfSolicitante");
                const loginSolicitante = $("#loginSolicitante");
                const emailSolicitante = $("#emailSolicitante");
                const ramalSolicitante = $("#ramalSolicitante");
                const areaSolicitante = $("#areaSolicitante");
                const nomeResponsavel = $("#nomeResponsavel");
                const horarioAbertura = $("#horarioAbertura");

                // Preencha os campos relacionados ao card
                assuntoInfo.text(data.card.assunto);
                servicoInfo.text(` / ${data.card.service}`);
                codInfo.text(`N° ${data.card.idCard}`);


                // Preencha os campos relacionados ao solicitante ---------------------
                if (data.card.anonymous === false) {
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

                    // Verifique se a área do solicitante existe
                    if (data.card.solicitante_profissional.area) {
                        areaSolicitante.text(data.card.solicitante_profissional.area);
                    } else {
                        areaSolicitante.text("N/A");
                    }

                } else {
                    // Oculte a ul
                    $(".card-ul").hide();

                    // Adicione um elemento p com a mensagem "Solicitante Anônimo"
                    $(".card-body-custom").append("<p class='p-5'>Solicitante Anônimo</p>");
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

                // Exiba o horário de abertura do chamado personalizado
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


                atualizarListaMensagens(cardId);

                //--------------------------------------------------------------------------------------------





                //--------------------------------------------------------------------------------------------

                // Configurar o botão de resposta
                $("#enviarMensagemButton").click(function () {
                    const resposta = $("#resposta").val();
                    if (resposta) {
                        enviarResposta(cardId, resposta);
                    } else {
                        alert('Preencha o campo de resposta antes de enviar.');
                    }
                });


                // Função para enviar uma mensagem de resposta
                function enviarResposta(cardId, resposta) {
                const formData = new FormData();
                formData.append("resposta", resposta);

                // Selecione o input de arquivo por ID (substitua 'attachmentInput' pelo ID real do seu input)
                const attachmentInput = document.getElementById('attachmentInput');

                // Verifique se um arquivo foi selecionado
                if (attachmentInput.files.length > 0) {
                    // Adicione o arquivo ao FormData
                    formData.append('attachment', attachmentInput.files[0]);
                    }

                    $.ajax({
                        url: `/enviar_resposta/${cardId}`,
                        method: 'POST',
                        data: formData,
                        contentType: false,
                        processData: false,
                        success: function (response) {
                            // Limpe o campo de resposta após o envio
                            $("#resposta").val('');
                            // Atualize a lista de mensagens passando o cardId
                            atualizarListaMensagens(cardId);
                            // Limpe o campo de arquivo
                            attachmentInput.value = "";

                        },
                        error: function () {
                            alert('Erro ao enviar a resposta');
                        }
                    });
                }


                // Função para atualizar a lista de mensagens
                function atualizarListaMensagens(cardId) {
                    // Agora, vamos buscar as mensagens do solicitante
                    const messagesContainer = modal.find(".messages-container");
                    messagesContainer.empty(); // Limpa qualquer conteúdo anterior

                    $.ajax({
                        url: `/get_messages/${cardId}`,
                        method: 'GET',
                        dataType: 'json',
                        success: function (messages) {
                            if (messages && messages.length > 0) {
                                messages.forEach(function (message) {
                                    const dataHora = new Date(message.datetime);
                                    const dia = dataHora.getDate();
                                    const mes = dataHora.getMonth() + 1; // Os meses são indexados de 0 a 11
                                    const ano = dataHora.getFullYear();
                                    const hora = dataHora.getHours();
                                    const minuto = dataHora.getMinutes();

                                    const dataFormatada = `${dia}/${mes}/${ano}`;
                                    const horarioFormatado = `${hora}:${minuto}`;

                                    const rowElement = $("<div>").addClass("row pt-1").css({
                                        backgroundColor: "#d9d9d9",
                                        padding: "10px",
                                        borderRadius: "5px",
                                        margin: "0 0 10px 0",
                                    });

                                    const colElementEsquerda = $("<div>").addClass("col-auto me-auto");

                                    // Adicionar o nome completo do autor
                                    if (data.card.anonymous === false) {
                                        const nomeCompleto = `<h6>${message.remetente_first_name} ${message.remetente_last_name}</h6>`;
                                        colElementEsquerda.append(nomeCompleto);
                                    } else {
                                        const nomeCompleto = "<h6>Usuario Anônimo</h6>";
                                        colElementEsquerda.append(nomeCompleto);
                                    }''

                                    // Verificar se há anexo
                                    if (message.attachment) {
                                        // Obter o nome original do arquivo a partir do campo 'name' (se disponível)
                                        const attachmentName = message.attachment.name || message.attachment.split('/').pop();

                                        // Certificar-se de que o nome não é 'null' ou 'undefined'
                                        if (attachmentName && attachmentName !== 'null' && attachmentName !== 'undefined') {
                                            // Criar um link para download
                                            const attachmentLink = $("<a>")
                                                .attr("href", message.attachment)
                                                .attr("download", attachmentName)
                                                .html('<button title=" ' + attachmentName
                                                + ' "style="padding:2px 5px; border:none; border-radius:20px"><i class="fa-solid fa-circle-down"></i> '
                                                + attachmentName + '</button>');

                                            // Adicionar o link de anexo ao container
                                            colElementEsquerda.append(attachmentLink);
                                        } else {
                                            console.error("Não foi possível extrair o nome do arquivo.");
                                        }
                                    }

                                    const colElementDireita = $("<div>").addClass("col-auto");
                                    const dataElement = $(`<small>${dataFormatada} ${horarioFormatado}</small>`);
                                    const messageElement = $(`<p>${message.message}</p>`);

                                    // Adicionar os elementos à estrutura desejada
                                    colElementDireita.append(dataElement);

                                    rowElement.append(colElementEsquerda, colElementDireita);
                                    rowElement.append(messageElement);

                                    // Adicionar a rowElement ao seu container de mensagens
                                    messagesContainer.append(rowElement);
                                });
                            } else {
                                messagesContainer.append("<p>Nenhuma mensagem Informada.</p>");
                            }
                        },
                        error: function () {
                            alert('Erro ao buscar as mensagens do solicitante');
                        }
                    });

                }






                //---------------------------------------------------------------------------------------------


                if (data.card.setor_history && data.card.setor_history.length > 0) {
                    console.log(data.card.setor_history); // Adicione este log para verificar os dados do histórico de setores
                    const ultimaEntradaSetor = data.card.setor_history[data.card.setor_history.length - 1];
                    console.log(ultimaEntradaSetor); // Adicione este log para verificar a última entrada de setor
                    const setorAtual = ultimaEntradaSetor.setor_atual;
                    sectorInfo.text(setorAtual);
                } else {
                    sectorInfo.text("Setor não encontrado");
                }



                // Preencha o nome do responsável
                if (data.card.responsavel) {
                    const nomeResponsavelCompleto = `${data.card.responsavel.first_name} ${data.card.responsavel.last_name}`;
                    nomeResponsavel.text(nomeResponsavelCompleto);

                } else {
                    nomeResponsavel.text("Aguardando atendimento");
                }

                //---------------------------------------------------------------------------------------------


                // Ouvinte de evento para o botão "Atender"
                $("#registrarAtendimentoButton").click(function (event) {
                    event.preventDefault(); // Impede o link de navegar para outra página
                    registrarAtendimento(cardId); // Chama a função para registrar o atendimento
                });



                //---------------------------------------------------------------------------------------------

                // Ouvinte de evento para o botão "Encaminhar"
                $("#encaminharCardButton").click(function () {
                    // Ao clicar no botão "Encaminhar", exiba o segundo modal para seleção do setor
                    $('#modalSelecaoSetor').modal('show');
                });

                // Ouvinte de evento para o botão "Confirmar" no segundo modal
                $("#confirmarEncaminhamento").click(function () {
                    const selectedGroup = $("#seletorGrupo").val(); // Obtém o valor selecionado no <select>

                    // Verifique se o valor do grupo é válido
                    if (!selectedGroup) {
                        alert('Selecione um grupo válido.');
                        return;
                    }

                    // Construa um objeto com os dados do encaminhamento
                    const dadosEncaminhamento = {
                        cardId: cardId,
                        selectedGroup: selectedGroup,
                    };

                    // Envie uma solicitação AJAX para registrar o encaminhamento
                   $.ajax({
                        url: `/encaminhar_card/${cardId}`, // Substitua pela URL correta da sua view Django
                        method: 'POST',
                        data: dadosEncaminhamento,
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {
                                alert('Card encaminhado com sucesso.');
                                $('#modalSelecaoSetor').modal('hide');
                                $('#processoModal').modal('hide');
                            } else {
                                alert('ERRO: ' + data.message); // Exibe a mensagem de erro do servidor
                            }
                        },
                        error: function (xhr, status, error) {
                            alert('ERRO: ' + error); // Exibe informações de erro do AJAX
                        }
                    });

                });



                //---------------------------------------------------------------------------------------------


                // Ouvinte de evento para o botão "Transferir"
                $("#transferirCardButton").click(function () {
                    // Ao clicar no botão "Encaminhar", exiba o segundo modal para seleção do setor
                    $('#modalSelecaoSetorTrans').modal('show');
                });

                // Ouvinte de evento para o botão "Confirmar" no segundo modal
                $("#confirmarTransferencia").click(function () {
                    const selectedGroupTrans = $("#seletorGrupoTrans").val(); // Obtém o valor selecionado no <select>

                    // Verifique se o valor do grupo é válido
                    if (!selectedGroupTrans) {
                        alert('Selecione um grupo válido.');
                        return;
                    }

                    // Construa um objeto com os dados do encaminhamento
                    const dadosTransferencia = {
                        cardId: cardId,
                        selectedGroupTrans: selectedGroupTrans,
                    };

                    // Envie uma solicitação AJAX para registrar o encaminhamento
                   $.ajax({
                        url: `/transferir_card/${cardId}`, // Substitua pela URL correta da sua view Django
                        method: 'POST',
                        data: dadosTransferencia,
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {
                                alert('Card Transferido com sucesso.');
                                $('#modalSelecaoSetorTrans').modal('hide');
                                $('#processoModal').modal('hide');
                            } else {
                                alert('ERRO: ' + data.message); // Exibe a mensagem de erro do servidor
                            }
                        },
                        error: function (xhr, status, error) {
                            alert('ERRO: ' + error); // Exibe informações de erro do AJAX
                        }
                    });

                });


                // --------------------------------------------------------------------------------------------


                // Ouvinte de evento para o botão "Personalizar"
                $("#PersonalizarCard").click(function () {
                    // Ao clicar no botão "Encaminhar", exiba o segundo modal para seleção do setor
                    $('#modalSelecaoCor').modal('show');
                });

                // Ouvinte de evento para o botão "Confirmar" no segundo modal
                $("#confirmarCor").click(function () {
                    const selectedColor = $("#seletorCor").val(); // Obtém o valor selecionado no <select>

                    // Verifique se o valor do grupo é válido
                    if (!selectedColor) {
                        alert('Selecione uma cor válida.');
                        return;
                    }

                    // Construa um objeto com os dados do encaminhamento
                    const dadosPersonalisar = {
                        cardId: cardId,
                        selectedColor: selectedColor,
                    };

                    // Envie uma solicitação AJAX para registrar o encaminhamento
                   $.ajax({
                        url: `/presonalizar_card/${cardId}`, // Substitua pela URL correta da sua view Django
                        method: 'POST',
                        data: dadosPersonalisar,
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {
                                alert('Card Personalizado com sucesso.');
                                // Feche o segundo modal após o encaminhamento
                                $('#modalSelecaoCor').modal('hide');
                            } else {
                                alert('ERRO: ' + data.message); // Exibe a mensagem de erro do servidor
                            }
                        },
                        error: function (xhr, status, error) {
                            alert('ERRO: ' + error); // Exibe informações de erro do AJAX
                        }
                    });

                });



                //--------------------------------------------------------------------------------------------



                // Ouvinte de evento para o botão "Finalizar" no modal
                $("#ConcluirCardButton").click(function () {
                    $.ajax({
                        url: `/concluir_card/${cardId}`,
                        method: 'POST',
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {

                                alert('Card Concluido com sucesso.');
                                $('#processoModal').modal('hide');

                            } else {
                                alert('ERRO: ' + data.message);
                            }
                        },
                        error: function (xhr, status, error) {
                            alert('ERRO: ' + error);
                        }
                    });
                });


                //--------------------------------------------------------------------------------------------


                // Ouvinte de evento para o botão "Personalizar"
                $("#compartilharCardButton").click(function () {
                    // Ao clicar no botão "Encaminhar", exiba o segundo modal para seleção do setor
                    $('#modalSeletorUser').modal('show');
                });

                // Ouvinte de evento para o botão "Confirmar" no segundo modal
                $("#confirmarCompartilhamento").click(function () {
                    const selectedUser = $("#seletorUser").val(); // Obtém o valor selecionado no <select>

                    // Verifique se o valor do grupo é válido
                    if (!selectedUser) {
                        alert('Selecione um usuário válida.');
                        return;
                    }

                    // Construa um objeto com os dados do encaminhamento
                    const dadosUsuarios = {
                        cardId: cardId,
                        selectedUser: selectedUser,
                    };

                    // Envie uma solicitação AJAX para registrar o encaminhamento
                   $.ajax({
                        url: `/compartilhar_card/${cardId}`, // Substitua pela URL correta da sua view Django
                        method: 'POST',
                        data: dadosUsuarios,
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {
                                alert('Card Compartilhado com sucesso.');
                                // Feche o segundo modal após o encaminhamento
                                $('#modalSeletorUser').modal('hide');
                            } else {
                                alert('ERRO: ' + data.message); // Exibe a mensagem de erro do servidor
                            }
                        },
                        error: function (xhr, status, error) {
                            alert('ERRO: ' + error); // Exibe informações de erro do AJAX
                        }
                    });

                });



                //---------------------------------------------------------------------------------------------


                // Ouvinte de evento para o botão "Finalizar" no modal
                $("#FinalizarAtendimentoButton").click(function () {
                    $.ajax({
                        url: `/finalizar_card/${cardId}`,
                        method: 'POST',
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {

                                alert('Card Finalizado com sucesso.');
                                $('#processoModal').modal('hide');

                            } else {
                                alert('ERRO: ' + data.message);
                            }
                        },
                        error: function (xhr, status, error) {
                            alert('ERRO: ' + error);
                        }
                    });
                });


                //---------------------------------------------------------------------------------------------


                // Ouvinte de evento para o botão "Reabrir" no modal
                $("#reabrirChamadoButton").click(function () {
                    $.ajax({
                        url: `/reabrir_card/${cardId}`,
                        method: 'POST',
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {

                                alert('Requisição Reaberta com sucesso.');
                                $('#processoModal').modal('hide');

                            } else {
                                alert('ERRO: ' + data.message);
                            }
                        },
                        error: function (xhr, status, error) {
                            alert('ERRO: ' + error);
                        }
                    });
                });



                //---------------------------------------------------------------------------------------------



                // Realizar uma solicitação AJAX para obter as informações de avaliação do usuário logado para o cartão
                $.ajax({
                    url: `/get_user_rating/${cardId}`,  // Substitua pela URL correta da sua view
                    method: 'GET',
                    dataType: 'json',
                    success: function (userRatingData) {
                        const userHasRatedThisCard = userRatingData.user_has_rated;

                        // Habilitar ou desabilitar o botão "Finalizar" com base na avaliação do usuário
                        const finalizarButton = $("#FinalizarAtendimentoButton");
                        if (userHasRatedThisCard) {
                            finalizarButton.prop("disabled", false);
                        } else {
                            finalizarButton.prop("disabled", true);
                        }

                        // Restante do seu código...
                    },
                    error: function () {
                        alert('Erro ao buscar informações de avaliação do usuário');
                    }
                });


                //---------------------------------------------------------------------------------------------


                let selectedRating = 0; // Inicialmente, nenhuma estrela está selecionada

                // Ouvinte de evento para o clique nas estrelas
                $(".star-link").click(function () {
                    const rating = parseInt($(this).attr("name")); // Obtenha a classificação da estrela clicada como um número inteiro

                    // Adicione a classe filled-star para as estrelas até a classificação clicada
                    for (let i = 1; i <= rating; i++) {
                        $(`a[name="${i}"] i`).addClass('filled-star');

                    }

                    // Remova a classe filled-star das estrelas após a classificação clicada
                    for (let i = rating + 1; i <= 5; i++) {
                        $(`a[name="${i}"] i`).removeClass('filled-star');
                    }

                    selectedRating = rating;

                });


                // Ouvinte de evento para o botão "Avaliar Atendimento"
                $("#avaliarAtendimentoButton").click(function () {
                    if (selectedRating > 0) {
                        // Enviar a avaliação para o servidor se uma classificação estiver selecionada
                        enviarAvaliacao(cardId, selectedRating);
                    } else {
                        alert('Selecione uma classificação antes de avaliar.');
                    }
                });


                //------------------------------------------------------------------------------------------------------

                // Verifique o status do card
                if (data.card.setor_history.length > 0 && data.card.setor_history[data.card.setor_history.length - 1].status_atual === "Triagem") {
                    $("#compartilharCardButton").show();
                    $("#priorizarCardButton").show();
                    $("#enviarMensagemButton").show();
                    $("#starButtons").css("display", "none");
                    $("#reabrirChamado").css("display", "none");
                    $("#avaliarAtendimentoButton").hide();
                    $("#registrarAtendimentoButton").show();
                    $("#encaminharCardButton").hide();
                    $("#transferirCardButton").show();
                    $("#ConcluirCardButton").hide();
                }
//
//
                if (data.card.setor_history.length > 0 && data.card.setor_history[data.card.setor_history.length - 1].status_atual === "Em Atendimento") {

                    $("#compartilharCardButton").show();
                    $("#priorizarCardButton").show();
                    $("#enviarMensagemButton").show();
                    $("#starButtons").css("display", "none");
                    $("#reabrirChamado").css("display", "none");
                    $("#avaliarAtendimentoButton").hide();
                    $("#registrarAtendimentoButton").hide();
                    $("#encaminharCardButton").show();
                    $("#transferirCardButton").hide();
                    $("#ConcluirCardButton").show();

                }
//
//
                if (data.card.setor_history.length > 0 && data.card.setor_history[data.card.setor_history.length - 1].status_atual === "Emcaminhado") {

                    $("#compartilharCardButton").show();
                    $("#priorizarCardButton").show();
                    $("#enviarMensagemButton").show();
                    $("#starButtons").css("display", "none");
                    $("#reabrirChamado").css("display", "none");
                    $("#avaliarAtendimentoButton").hide();
                    $("#registrarAtendimentoButton").show();
                    $("#encaminharCardButton").show();
                    $("#transferirCardButton").show();
                    $("#ConcluirCardButton").hide();

                }
//
//
                if (data.card.setor_history.length > 0 && data.card.setor_history[data.card.setor_history.length - 1].status_atual === "Concluido") {

                    $("#compartilharCardButton").show();
                    $("#priorizarCardButton").hide();
                    $("#enviarMensagemButton").show();
                    $("#starButtons").css("display", "block");
                    $("#reabrirChamado").css("display", "none");
                    $("#avaliarAtendimentoButton").show();
                    $("#registrarAtendimentoButton").hide();
                    $("#encaminharCardButton").show();
                    $("#transferirCardButton").hide();
                    $("#ConcluirCardButton").hide();

                }


                // Verifique o status do card
                if (data.card.setor_history.length > 0 && data.card.setor_history[data.card.setor_history.length - 1].status_atual === "Finalizado") {
                    // Ocultar botões quando o card estiver em "Finalizado"
                    $("#compartilharCardButton").hide();
                    $("#priorizarCardButton").hide();
                    $("#enviarMensagemButton").hide();
                    $("#starButtons").css("display", "none");
                    $("#reabrirChamado").css("display", "block");
                    $("#avaliarAtendimentoButton").hide();
                    $("#registrarAtendimentoButton").hide();
                    $("#encaminharCardButton").hide();
                    $("#transferirCardButton").hide();
                    $("#ConcluirCardButton").hide();

                }


                //------------------------------------------------------------------------------------------------------


                // Abra o modal
                modal.modal('show');

                // Adicione um ouvinte de evento para o evento de ocultação do modal
                modal.on("hidden.bs.modal", function () {
                    // Atualize a página
                    location.reload();
                });

            } else {
                alert('Dados do card não encontrados.');
            }

        },
        error: function () {
            alert('Erro ao buscar os detalhes do card');
        }
    });
}


function registrarAtendimento(cardId) {
    console.log("ID do card:", cardId);

    // Construa um objeto com os dados do atendimento
    const dadosAtendimento = {
        cardId: cardId,
    };

    // Envie uma solicitação AJAX para atualizar o status do card
    $.ajax({
        url: `/registrar_atendimento/${cardId}`,  // Substitua pela URL correta da sua view
        method: 'POST',
        dataType: 'json',
        data: dadosAtendimento,

        success: function (data) {
            if (data.success) {
                location.reload();

                // Exibir um alerta de sucesso
                alert(data.message);
            } else {
                // Exibir um alerta de erro
                alert(data.message);
            }
        },

        error: function () {
            // Exibir um alerta de erro genérico
            alert('Erro ao registrar atendimento.');
        }
    });
}


function enviarAvaliacao(cardId, rating) {
    // Envie a avaliação para o servidor por meio de uma solicitação AJAX
    $.ajax({
        url: `/avaliar_card/${cardId}`,
        method: 'POST',
        data: { rating: rating }, // Envie a classificação selecionada
        dataType: 'json',
        success: function (data) {
            if (data.success) {
                // A avaliação foi registrada com sucesso, você pode atualizar o modal ou executar outras ações necessárias
                alert('Avaliado e Finalizado com sucesso.');
                $('#processoModal').modal('hide');
                location.reload();

            } else {
                alert('Erro ao registrar a avaliação: ' + data.message);
            }
        },
        error: function () {
            alert('Erro ao enviar a avaliação');
        }
    });
}


// Tratamento de Notificações
$('.marcar-lida-notificacao').click(function() {
    var notificationId = $(this).data('notification-id');
    $.ajax({
        url: `/notificacao_lida/${notificationId}`,
        method: 'POST',
        success: function(data) {
            if (data.success) {
//                location.reload();
                // Atualize a interface do usuário para refletir que a notificação foi marcada como lida.
            } else {
                alert('Erro ao registrar a avaliação: ' + data.message);
            }
        }
    });
});


//Menu -----------------------------
$(document).ready(function () {
    // Verifica se há um estado salvo no localStorage
    var menuState = localStorage.getItem('menuState');

    if (menuState === 'active') {
      $('#menu_lateral').addClass('active');
      $('#toggleMenu i').addClass('fa-times');
      $('#menu_lateral a').addClass('menu-toggle');
    }

    $('#toggleMenu').on('click', function () {
      $('#menu_lateral').toggleClass('active');
      // Alterna a classe do ícone conforme o estado do menu
      $(this).find('i').toggleClass('fa-bars fa-times');
      // Adiciona ou remove a classe menu-toggle aos itens do menu lateral
      $('#menu_lateral a').toggleClass('menu-toggle');

      // Salva o estado no localStorage
      var currentState = $('#menu_lateral').hasClass('active') ? 'active' : 'inactive';
      localStorage.setItem('menuState', currentState);
    });
  });


$(document).ready(function() {
        $('#calendario').fullCalendar({
            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'month,agendaWeek,agendaDay'
            },

            locale: 'pt-br',

            // Adicione seus eventos ao calendário
            events: [
                {
                    title: 'Férias do João',
                    start: '2023-11-01',
                    end: '2023-11-05'
                },

                {
                    title: 'Férias do Henrique',
                    start: '2023-11-01',
                    end: '2023-11-15'
                },
            ]
        });
    });


// Função para criar o gráfico
function criarGrafico(data) {
    // Obtenha o contexto do canvas
    var ctx = document.getElementById('feriasChart').getContext('2d');

    // Configurações do gráfico
    var options = {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    };

    // Crie o gráfico de área
    var myChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });

    // Calcular a média e exibi-la
    var media = data.datasets[0].data.reduce((a, b) => a + b, 0) / data.datasets[0].data.length;
    document.getElementById('mediaFerias').innerText = media.toFixed(2); // Exibe a média com 2 casas decimais
}


// Dados do gráfico de rosquinha
function criarGraficoDeRosquinha() {
    // Parte config ---------------------
    var config = {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [10, 20, 30],
                backgroundColor: ['red', 'green', 'blue']
            }],
            labels: ['Red', 'Green', 'Blue']
        },

        options: {
            responsive: true,
               plugins: {
                  legend: {
                    position: 'left',
                  }
               },

            title: {
                display: false,
                text: 'Doughnut Chart'
            },

            animation: {
                animateScale: true,
                animateRotate: true
            }
        }
    };

    // Parte setup --------------------------
    document.addEventListener('DOMContentLoaded', function() {
        var ctx = document.getElementById('myChart').getContext('2d');
        window.myDoughnut = new Chart(ctx, config);
    });

    // Parte actions -----------------------
    document.getElementById('randomizeData').addEventListener('click', function() {
        config.data.datasets.forEach(function(dataset) {
            dataset.data = dataset.data.map(function() {
                return randomScalingFactor();
            });
        });

        window.myDoughnut.update();
    });

    var colorNames = Object.keys(window.chartColors);
    document.getElementById('addDataset').addEventListener('click', function() {
        var newDataset = {
            backgroundColor: [],
            data: [],
            label: 'New dataset ' + config.data.datasets.length,
        };

        for (var index = 0; index < config.data.labels.length; ++index) {
            newDataset.data.push(randomScalingFactor());

            var colorName = colorNames[index % colorNames.length];
            var newColor = window.chartColors[colorName];
            newDataset.backgroundColor.push(newColor);
        }

        config.data.datasets.push(newDataset);
        window.myDoughnut.update();
    });
}

// Chame a função para criar o gráfico ao carregar a
criarGraficoDeRosquinha();


// script.js
function criarGraficoDeBarraComBordasArredondadas() {
    // Parte config
    var config = {
        type: 'bar',
        data: {
            labels: ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4'],
            datasets: [{
                label: 'Valores',
                data: [15, 25, 10, 30],
                backgroundColor: 'rgba(75, 192, 192, 0.7)', // Cor de fundo das barras
                borderColor: 'rgba(75, 192, 192, 1)', // Cor da borda das barras
                borderWidth: 2, // Largura da borda das barras
                borderRadius: 10 // Raio da borda para torná-la arredondada
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    grid: {
                        display: false
                    }
                },
                y: {
                    beginAtZero: true
                }
            },
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    bottom: 10
                }
            }
        }
    };

    // Parte setup
    document.addEventListener('DOMContentLoaded', function() {
        var ctx = document.getElementById('myBarChart').getContext('2d');
        window.myBarChart = new Chart(ctx, config);
    });
}
criarGraficoDeBarraComBordasArredondadas();




function GraficoBarra() {
    // Parte config
    var config = {
        type: 'bar',
        data: {
            labels: ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4'],
            datasets: [{
                label: 'Valores',
                data: [15, 25, 10, 30],
                backgroundColor: 'rgba(75, 192, 192, 0.7)', // Cor de fundo das barras
                borderColor: 'rgba(75, 192, 192, 1)', // Cor da borda das barras
                borderWidth: 2, // Largura da borda das barras
                borderRadius: 10 // Raio da borda para torná-la arredondada
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    grid: {
                        display: false
                    }
                },
                y: {
                    beginAtZero: true
                }
            },
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    bottom: 10
                }
            }
        }
    };

    // Parte setup
    document.addEventListener('DOMContentLoaded', function() {
        var ctx = document.getElementById('Grafico_barras').getContext('2d');
        window.myBarChart = new Chart(ctx, config);
    });
}
GraficoBarra();









//history request

const itemActions = document.querySelectorAll('.item-action');

itemActions.forEach(item => {
    item.addEventListener('click', function(event) {
        event.preventDefault();

        const cardId = item.getAttribute('data-card-id');

        if (cardId) {
            fetch(`/get_message_history/${cardId}`)
                .then(response => response.json())
                .then(data => {
                    // ... seu código existente para detalhesAssunto

                    let detalhesMensagens = '';
                    if (data && data.length > 0) {
                        // Iterar sobre as mensagens para adicionar ao detalhesMensagens
                        detalhesMensagens = data.map(msg => msg.message).join('<br>');
                    } else {
                        detalhesMensagens = 'Nenhuma mensagem encontrada';
                    }

                    // Restante do seu código para criar o HTML para exibir no campo de visualização

                    // Atualizar o campo de visualização com as mensagens
                    document.getElementById('detalhes-mensagens').innerHTML = detalhesMensagens;
                })

                .catch(error => {
                    console.error('Erro:', error);
                });
        } else {
            console.error('ID do card não encontrado.');
        }
    });
});



