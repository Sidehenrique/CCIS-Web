
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
    const formulario7 = document.getElementById("formulario7");

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
        formulario7.style.display = "none";
    });


    document.getElementById("btn_request_2").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "block";
        formulario3.style.display = "none";
        formulario4.style.display = "none";
        formulario5.style.display = "none";
        formulario6.style.display = "none";
        formulario7.style.display = "none";
    });


    document.getElementById("btn_request_3").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "block";
        formulario4.style.display = "none";
        formulario5.style.display = "none";
        formulario6.style.display = "none";
        formulario7.style.display = "none";
    });

    document.getElementById("btn_request_4").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "none";
        formulario4.style.display = "block";
        formulario5.style.display = "none";
        formulario6.style.display = "none";
        formulario7.style.display = "none";
    });

    document.getElementById("btn_request_5").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "none";
        formulario4.style.display = "none";
        formulario5.style.display = "block";
        formulario6.style.display = "none";
        formulario7.style.display = "none";
    });

    document.getElementById("btn_request_6").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "none";
        formulario4.style.display = "none";
        formulario5.style.display = "none";
        formulario6.style.display = "block";
        formulario7.style.display = "none";
    });

    document.getElementById("btn_request_7").addEventListener("click", function() {
        informativo.style.display = "none";
        formulario1.style.display = "none";
        formulario2.style.display = "none";
        formulario3.style.display = "none";
        formulario4.style.display = "none";
        formulario5.style.display = "none";
        formulario6.style.display = "none";
        formulario7.style.display = "block";
    });

});
//---------------------------------------------------------------------------------------------------------------


// Tratamento PAGINA CONFIGURAÇÕES ------------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {
    const menu_config = document.getElementById("menu_config");

    const config_1 = document.getElementById("config_1");
    const config_2 = document.getElementById("config_2");
    const config_3 = document.getElementById("config_3");
    const config_4 = document.getElementById("config_4");

    // Exibindo a página de Temas por padrão
    config_1.style.display = "block";
    config_2.style.display = "none";
    config_3.style.display = "none";
    config_4.style.display = "none";

    // Função para remover a classe 'active' de todos os botões
    function removeAllActiveClasses() {
        const buttons = menu_config.querySelectorAll('.li-link-kanban');
        buttons.forEach(button => {
            button.classList.remove('active');
        });
    }

    // Adicionando eventos aos botões do menu
    document.getElementById("btn-config_1").addEventListener("click", function() {
        removeAllActiveClasses();
        this.classList.add('active');

        config_1.style.display = "block";
        config_2.style.display = "none";
        config_3.style.display = "none";
        config_4.style.display = "none";
    });

    document.getElementById("btn_config_2").addEventListener("click", function() {
        removeAllActiveClasses();
        this.classList.add('active');

        config_1.style.display = "none";
        config_2.style.display = "block";
        config_3.style.display = "none";
        config_4.style.display = "none";
    });

    document.getElementById("btn_config_3").addEventListener("click", function() {
        removeAllActiveClasses();
        this.classList.add('active');

        config_1.style.display = "none";
        config_2.style.display = "none";
        config_3.style.display = "block";
        config_4.style.display = "none";
    });

    document.getElementById("btn_config_4").addEventListener("click", function() {
        removeAllActiveClasses();
        this.classList.add('active');

        config_1.style.display = "none";
        config_2.style.display = "none";
        config_3.style.display = "none";
        config_4.style.display = "block";
    });

    // Se estiver utilizando Bootstrap, você pode tentar atualizar o modal após as alterações
    $('#temasModal').modal('handleUpdate');
});
//---------------------------------------------------------------------------------------------------------------


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


//=========================================== CARDS ==================================================

// Função para recolher ou exibir o conteúdo ao clicar no header do card
$(document).on('click', '[id^="toggleBtn-"]', function () {
    const cardId = this.id.split('-').pop();
    const cardContent = $(`#cardContent-${cardId}`);

    // Adicione um teste para verificar se o elemento foi encontrado
    if (cardContent.length) {
        cardContent.slideToggle();

        // Atualize o estado de recolhimento do card no cookie
        const collapsedCards = JSON.parse(getCookieCards('collapsedCards')) || {};
        collapsedCards[cardId] = !collapsedCards[cardId];
        document.cookie = `collapsedCards=${JSON.stringify(collapsedCards)}; expires=Thu, 01 Jan 2030 00:00:00 UTC; path=/`;
    } else {
        console.error('Elemento não encontrado:', `#cardContent-${cardId}`);
    }
});


// Adicione um manipulador de evento para detectar cliques nos itens da lista
$('.dropdown-item-group').click(function () {
    var grupoSelecionado = $(this).data('value');
    clearKanbanBodies()
    fetchCards(grupoSelecionado);
});


// Função para buscar cards com base na opção selecionada
async function fetchCards(grupoSelecionado) {

    // Verificar se o elemento exclusivo do Kanban está presente na página
    const kanbanElement = $('#area-trabalho-kanban');
    if (kanbanElement.length === 0) {
        // Se o elemento não estiver presente, sair da função
        return;
    }

    const userId = getLoggedInUserId();

    // Atualize o texto do elemento h5 com base no grupo selecionado
    const areaTrabalhoElement = document.getElementById('area-trabalho-kanban');
    areaTrabalhoElement.innerText = grupoSelecionado;

//    // Salve a área de trabalho no cookie
//    saveWorkspaceToCookie(grupoSelecionado);

    try {
        // Faça uma solicitação AJAX para o backend
        const data = await $.ajax({
            url: `/cards_kanban_api/?option=${grupoSelecionado}&userId=${userId}`,
            type: 'GET',
            dataType: 'json'
        });

        // Recupere o estado de recolhimento do card do cookie
        const collapsedCards = JSON.parse(getCookieCards('collapsedCards')) || {};


        // Aqui, data conterá os cards retornados pelo backend
        // Atualize o kanban com os dados recebidos do backend
        updateKanban(data, collapsedCards);
    } catch (error) {
        areaTrabalhoElement.innerText = "Selecione uma Área de Trabalho";
        customToast(error.responseText || error.statusText, "errorSoong.mp3")
        console.error('Erro ao buscar cards:', error.responseText || error.statusText);
    }
}


//// Verificar se o elemento único do Kanban está presente na página
//if ($('#area-trabalho-kanban').length > 0) {
//    // Configurar o setInterval apenas se o elemento do Kanban estiver presente
//    const kanbanInterval = setInterval(() => {
//        const grupoSelecionado = $('#area-trabalho-kanban').text().trim();
//        fetchCards(grupoSelecionado);
//    }, 60000);
//
//    // Opcional: Limpar o intervalo se o usuário sair da página
//    // Exemplo usando o evento beforeunload
//    $(window).on('beforeunload', function() {
//        clearInterval(kanbanInterval);
//    });
//}


// Função para atualizar o kanban com os dados recebidos do backend
function updateKanban(cards, collapsedCards) {
    // Limpe os corpos do kanban
    clearKanbanBodies();

    // Atualize cada coluna do kanban com os novos cards
    cards.forEach(card => {
        // Use o valor do status para formar o ID da coluna
        const columnId = card.status.toLowerCase();
        // Adicione o card ao corpo da coluna correspondente
        const kanbanBody = $(`#kanban-body-${columnId}`);
        kanbanBody.append(createCardElement(card, collapsedCards[card.idCard]));
    });
}


// Função para criar um elemento de card HTML com base nas informações do card
function createCardElement(card, isCollapsed) {
    const cardId = `${card.idCard}`;

    // Função para formatar a data
    function formatarData(dataString) {
        const data = new Date(dataString);
        const dia = data.getDate();
        const mes = data.getMonth() + 1; // Os meses são indexados de 0 a 11
        const ano = data.getFullYear();
        return `${dia}/${mes}/${ano}`;
    }

    // Função para formatar o horário
    function formatarHorario(dataString) {
        const data = new Date(dataString);
        const hora = data.getHours();
        const minuto = data.getMinutes();
        return `${hora}:${minuto}`;
    }


    // Crie a estrutura HTML do card
    const cardElement = `
        <div class="kanban-card m-2 ${isCollapsed ? 'collapsed' : ''}" id="${cardId}">
            <!-- header do card --------->
            <a id="toggleBtn-${cardId}" type="button" class="d-grid kanban-card-header toggle-button">
                <div class="row">
                    <div class="col-auto me-auto">
                        <h5 class="card-titulo mt-1">${card.assunto}</h5>
                    </div>
                    <div class="col-auto mb-1">
                        <span class="card-setor processo-tag-setor">N° ${card.idCard}</span>
                        <span class="card-setor processo-tag-setor">${card.setor_history.length > 0 ? card.setor_history[card.setor_history.length - 1].setor_atual : 'N/A'}</span>
                    </div>
                </div>
            </a>
            <!-- header do card --------->

            <!-- conteúdo card --------->
            <div id="cardContent-${cardId}" class="kanban-card-content card-container" ${isCollapsed ? 'style="display: none;"' : ''}>
                <hr style="color:#C4C0C0; margin:0px;">

                <a class="d-grid kanban-card-header card-filter"
                   type="button"
                   data-bs-toggle="modal"
                   data-bs-target="#processoModal"
                   data-card-id="${card.idCard}"
                   onclick="loadCardInfo(${card.idCard})">
                    <!-- Adicione outros detalhes do card conforme necessário -->

                    <div class="col-auto">
                       <p class="card-responsavel" style="color:#818181;">
                            <img class="foto_card" src="${card.solicitante_dados_pessoais.foto}" alt="" width="25" height="25">
                            ${card.solicitante.first_name} ${card.solicitante.last_name}
                        </p>
                    </div>

                    <div style="color:#818181; font-size:13px;">
                        <p class="card-servico mb-1"><i class="fa-regular fa-circle-dot"></i> ${card.service}</p>
                    </div>
                    <div class="card-data row" style="color:#818181; font-size:13px">
                        <div class="col-auto me-auto">
                            <i class="fa-solid fa-calendar-days"></i> ${formatarData(card.dataCriacao)}
                        </div>
                        <div class="col-auto">
                            <i class="fa-solid fa-clock"></i> ${formatarHorario(card.dataCriacao)}
                        </div>
                    </div>
                </a>
            </div>
            <!-- conteúdo card --------->
        </div>
        <!-- Card ----------------->

    `;

    // Retorne o elemento do card
    return cardElement;
}


// Função para limpar os corpos do kanban
function clearKanbanBodies() {
    // Adapte isso conforme a estrutura real do seu HTML
    $('#kanban-body-triagem').empty();
    $('#kanban-body-atendimento').empty();
    $('#kanban-body-encaminhado').empty();
    $('#kanban-body-concluido').empty();
    $('#kanban-body-finalizado').empty();
}


// Função para obter o ID do usuário logado
function getLoggedInUserId() {
    return userData.userId
}


// Função para obter o nome do grupo do usuário logado
function getLoggedInUserGroup() {
    return userData.userGroupId;
}


function getCookieCards(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}


//function saveWorkspaceToCookie(workspace) {
//    // Defina o cookie 'workspace' com o valor fornecido
//    setCookie('workspace', workspace, 30); // Ajuste conforme necessário
//}


function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
}


document.addEventListener('DOMContentLoaded', function () {
    const workspace = getCookieCards('workspace');
    if (workspace) {
        // Faça algo com a área de trabalho, se necessário
        // Por exemplo, você pode configurar a área de trabalho na interface do usuário
        fetchCards(workspace); // Se necessário, atualize os cards com base na área de trabalho salva
    }
});


function filterProcesses() {
    const searchText = document.getElementById('inputUser').value.toLowerCase();
    const cards = document.querySelectorAll('.kanban-card');

    cards.forEach(card => {
        const assunto = card.querySelector('.card-titulo').innerText.toLowerCase();
        const servico = card.querySelector('.card-servico').innerText.toLowerCase();
        const nomeSolicitante = card.querySelector('.card-responsavel').innerText.toLowerCase();
        const cardId = card.id.toLowerCase(); // Obter o ID do card em minúsculas

        if (
            assunto.includes(searchText) ||
            servico.includes(searchText) ||
            nomeSolicitante.includes(searchText) ||
            cardId.includes(searchText) // Adicionar verificação pelo ID do card
        ) {
            card.style.display = 'block'; // Mostrar o card
            card.classList.add('flash'); // Adicionar a classe de animação
        } else {
            card.style.display = 'none'; // Esconder o card
            card.classList.remove('flash'); // Remover a classe de animação
        }
    });

    // Remover a classe de animação caso a caixa de pesquisa esteja vazia
    if (searchText === '') {
        cards.forEach(card => {
            card.classList.remove('flash');
        });
    }
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

                // -------------------------------------------------------------------------------
                // Remova eventos antigos
                $("#enviarMensagemButton").off("click");
                $("#registrarAtendimentoButton").off("click");
                $("#encaminharCardButton").off("click");
                $("#transferirCardButton").off("click");
                $("#PersonalizarCard").off("click");
                $("#ConcluirCardButton").off("click");
                $("#compartilharCardButton").off("click");
                $("#FinalizarAtendimentoButton").off("click");
                $("#reabrirChamadoButton").off("click");
                $("#avaliarAtendimentoButton").off("click");

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
                    messagesContainer.empty();

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
                                    }

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
                                    const messageElement = $(`<div>${message.message.replace(/\n/g, '<br>')}</div>`);

                                    // Adicionar os elementos à estrutura desejada
                                    colElementDireita.append(dataElement);

                                    rowElement.append(colElementEsquerda, colElementDireita, messageElement);

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
                    const ultimaEntradaSetor = data.card.setor_history[data.card.setor_history.length - 1];
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


                // AÇÕES ------------------------------------------------------------------------

                // Ouvinte de evento para o botão "Atender" no modal
                $("#registrarAtendimentoButton").off("click").on("click",function () {
                    $.ajax({
                        url: `/registrar_atendimento/${cardId}`,
                        method: 'POST',
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {

                                customToast(data.message, "notificationSong4.mp3");
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

                // Ouvinte de evento para o botão "Encaminhar"
                $("#encaminharCardButton").off("click").on("click",function () {
                    // Ao clicar no botão "Encaminhar", exiba o segundo modal para seleção do setor
                    $('#modalSelecaoSetor').modal('show');
                });

                // Ouvinte de evento para o botão "Confirmar" no segundo modal
                $("#confirmarEncaminhamento").off("click").on("click",function () {
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

                                customToast(data.message, "notificationSong4.mp3");
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
                $("#transferirCardButton").off("click").on("click",function () {
                    // Ao clicar no botão "Encaminhar", exiba o segundo modal para seleção do setor
                    $('#modalSelecaoSetorTrans').modal('show');
                });

                // Ouvinte de evento para o botão "Confirmar" no segundo modal
                $("#confirmarTransferencia").off("click").on("click",function () {
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

                                customToast(data.message, "notificationSong4.mp3");
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
                $("#PersonalizarCard").off("click").on("click",function () {
                    // Ao clicar no botão "Encaminhar", exiba o segundo modal para seleção do setor
                    $('#modalSelecaoCor').modal('show');
                });

                // Ouvinte de evento para o botão "Confirmar" no segundo modal
                $("#confirmarCor").off("click").on("click",function () {
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

                                customToast(data.message);
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
                $("#ConcluirCardButton").off("click").on("click",function () {
                    $.ajax({
                        url: `/concluir_card/${cardId}`,
                        method: 'POST',
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {

                                customToast(data.message, "successSong.mp3");
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
                $("#compartilharCardButton").off("click").on("click",function () {
                    // Ao clicar no botão "Encaminhar", exiba o segundo modal para seleção do setor
                    $('#modalSeletorUser').modal('show');
                });

                // Ouvinte de evento para o botão "Confirmar" no segundo modal
                $("#confirmarCompartilhamento").off("click").on("click",function () {
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

                                customToast(data.message, "notificationSong4.mp3");
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
                $("#FinalizarAtendimentoButton").off("click").on("click",function () {
                    $.ajax({
                        url: `/finalizar_card/${cardId}`,
                        method: 'POST',
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {

                                customToast(data.message, "notificationSong4.mp3");
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
                $("#reabrirChamadoButton").off("click").on("click",function () {
                    $.ajax({
                        url: `/reabrir_card/${cardId}`,
                        method: 'POST',
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {

                                customToast(data.message, "normalSong.mp3");
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
                $("#avaliarAtendimentoButton").off("click").on("click",function () {
                    if (selectedRating > 0) {
                        // Enviar a avaliação para o servidor se uma classificação estiver selecionada
                        enviarAvaliacao(cardId, selectedRating);
                    } else {
                        alert('Selecione uma classificação antes de avaliar.');
                    }
                });


// ------------- TRATAMENTO DOS BOTÕES DE AÇÃO -------------------------------------------------------

                // Obter o ID do usuário logado e o ID do grupo do usuário logado
                const userId = getLoggedInUserId();
                const userGroupId = getLoggedInUserGroup();

                // Verificar se o usuário logado é o solicitante
                const isSolicitante = userId === data.card.solicitante.id;

                // Verificar se o usuário é do setor ao qual o card foi criado
                const isDoSetor = parseInt(userGroupId) === parseInt(data.card.setor);

                // Verificar se a área de trabalho selecionada é "Minhas Solicitações"
                const grupoSelecionado = $('#area-trabalho-kanban').text().trim();
                const isInMinhasSolicitacoes = grupoSelecionado === "Minhas Solicitações";

                // Função para exibir bloco de botões específico e ocultar a mensagem do espectador
                function showButtonsAndHideMessage(buttons) {
                    // Oculta todos os botões e mensagem do espectador
                    $(".modal-processo-link, #starButtons, #reabrirChamado, #avaliarAtendimentoButton, #mensagemEspectador").addClass("hidden");

                    // Exibe os botões específicos
                    buttons.forEach(buttonId => {
                        $(`#${buttonId}`).removeClass("hidden");
                    });
                }

                // Adicione a classe "hidden" para ocultar inicialmente os botões e a mensagem do espectador
                $(".modal-processo-link, #starButtons, #reabrirChamado, #avaliarAtendimentoButton, #mensagemEspectador").addClass("hidden");


                //Verifique o status do card
                const statusAtual = data.card.status;

                // Verificar condições e exibir os botões apropriados
                if (isInMinhasSolicitacoes) {

                    resetStarRating();

                    // Se o usuário está em "Minhas Solicitações"
                    switch (statusAtual) {
                        case "Triagem":
                        case "Atendimento":
                        case "Encaminhado":
                            showButtonsAndHideMessage(["compartilharCardButton", "enviarMensagemButton"]);
                            break;
                        case "Concluido":
                            showButtonsAndHideMessage(["compartilharCardButton", "enviarMensagemButton", "starButtons", "avaliarAtendimentoButton"]);
                            break;
                        case "Finalizado":
                            showButtonsAndHideMessage(["compartilharCardButton", "reabrirChamadoButton"]);
                            break;
                        default:
                            // Lógica para outros status, se necessário
                            break;
                    }
                } else if (isDoSetor) {
                    // Se o usuário é do mesmo setor
                    switch (statusAtual) {
                        case "Triagem":
                            showButtonsAndHideMessage(["registrarAtendimentoButton", "transferirCardButton"]);
                            break;
                        case "Atendimento":
                            showButtonsAndHideMessage(["encaminharCardButton", "enviarMensagemButton", "ConcluirCardButton"]);
                            break;
                        case "Encaminhado":
                            showButtonsAndHideMessage(["registrarAtendimentoButton", "transferirCardButton"]);
                            break;
                        // Adicione outras condições conforme necessário
                        default:
                            // Lógica para outros status, se necessário
                            break;
                    }
                } else {
                    // Se nenhuma condição acima for atendida, exibir a imagem e a mensagem do espectador
                    $("#mensagemEspectador").removeClass("hidden");
                }


                //------------------------------------------------------------------------------------------------------


                // Adicione um ouvinte de evento para o evento de ocultação do modal
                modal.on("hidden.bs.modal", function () {
                    const grupoSelecionado = $('#area-trabalho-kanban').text().trim();
                    fetchCards(grupoSelecionado);
                });

                // Abra o modal
                resetStarRating();
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


function enviarAvaliacao(cardId, rating) {
    // Envie a avaliação para o servidor por meio de uma solicitação AJAX
    $.ajax({
        url: `/avaliar_card/${cardId}`,
        method: 'POST',
        data: { rating: rating }, // Envie a classificação selecionada
        dataType: 'json',
        success: function (data) {
            if (data.success) {

                customToast(data.message, "finishSong.mp3");
                $('#processoModal').modal('hide');

            } else {
                alert('Erro ao registrar a avaliação: ' + data.message);
            }
        },
        error: function () {
            alert('Erro ao enviar a avaliação');
        }
    });
}


// Função para redefinir as estrelas para a cor original
function resetStarRating() {
    // Remover a classe 'filled-star' de todas as estrelas
    $(".star-link i").removeClass('filled-star');

    // Resetar a classificação selecionada para 0
    selectedRating = 0;
}

//====================================================================================================




//========================================= NOTIFICAÇÕES =============================================

// Variável que armazena a opção de notificações ativas ou inativas
let notificacoesAtivas = false;


// Função para salvar a escolha do usuário no localStorage
function saveNotificationPreferenceToLocalStorage() {
    const localStorageValue = notificacoesAtivas ? 'ativas' : 'inativas';
    localStorage.setItem('notificationPreference', localStorageValue);
}


// Ouvinte de evento para o botão de alternância de notificações
$("#toggleNotificationButton").on("change", function () {
    notificacoesAtivas = this.checked;
    saveNotificationPreferenceToLocalStorage();
    fetchAndRenderNotifications();
    customToast(notificacoesAtivas ? "Som de Notificações ativado" : "Som de Notificações desativado", "notificationSong.mp3");
});


// Função para obter a preferência de notificações do localStorage ao carregar a página
document.addEventListener('DOMContentLoaded', function () {
    const localStorageValue = localStorage.getItem('notificationPreference');
    if (localStorageValue === 'ativas') {
        notificacoesAtivas = true;
        $("#toggleNotificationButton").prop('checked', true);
    } else {
        notificacoesAtivas = false;
        $("#toggleNotificationButton").prop('checked', false);
    }
    fetchAndRenderNotifications(); // Atualiza as notificações com a preferência armazenada
});


// Função para buscar notificações
function fetchAndRenderNotifications() {
    // Função para buscar notificações
    function fetchNotifications() {
        $.ajax({
            url: '/api/notifications/',  // URL da sua API de notificações
            method: 'GET',
            success: function (data) {
                // Limpar a lista de notificações existente
                $('#listaNotificacoes').empty();

                // Atualizar o contador de notificações
                const notificationCount = data.length;
                updateNotificationBadge(notificationCount);

                // Selecionar a imagem com a classe 'img_msg'
                const $noNotificationImage = $(".img_msg");


                // Obter o número anterior de notificações
                const previousNotificationCount = parseInt(localStorage.getItem('previousNotificationCount')) || 0;

                // Verificar se há notificações não lidas
                if (notificationCount > 0) {
                    // Iterar sobre as notificações e criar elementos HTML
                    $.each(data, function (index, notification) {
                        const notificationUrl = buildNotificationUrl(notification);
                        const formattedDate = moment(notification.date).format('DD/MM/YYYY HH:mm');

                        const $notificationElement = $(`
                            <a href="${notificationUrl}"
                                class="marcar-lida-notificacao list-group-item list-group-item-action"
                                data-notification-id="${notification.id}" aria-current="true">
                                <div class="d-flex w-100 justify-content-between">
                                    <h6 class="mb-1">${notification.authorFirst} ${notification.authorLast}</h6>
                                    <small>${formattedDate}</small>
                                </div>
                                <p class="mb-1">${notification.description}</p>
                                <small>Assunto: ${notification.subject}</small>
                            </a>
                        `);

                        // Adicionar um ouvinte de evento para marcar como lida e redirecionar
                        $notificationElement.click(function (event) {
                            event.preventDefault();
                            markNotificationAsRead(notification.id, notificationUrl);
                        });

                        // Adicionar o elemento ao container
                        $('#listaNotificacoes').append($notificationElement);
                    });

                    // Ocultar a imagem se houver notificações
                    $noNotificationImage.hide();


                    // Verificar se há novas notificações
                    if (notificationCount > previousNotificationCount) {
                        // Chamar customToast se houver novas notificações
                        notifcationToast("Você tem uma nova notificação", "notificationSong.mp3");

                        // Atualizar o número anterior de notificações no localStorage
                        localStorage.setItem('previousNotificationCount', notificationCount);
                    }


                } else {
                    // Mostrar a imagem se não houver notificações
                    $noNotificationImage.show();
                }
            },
            error: function () {
                console.error('Erro ao buscar notificações.');
            }
        });
    }

    // Função para construir a URL da notificação
    function buildNotificationUrl(notification) {
        const urlPrefix = window.location.pathname.includes('/kanban/') ? '' : '/kanban/';
        return `${urlPrefix}`;
    }

    // Função para marcar uma notificação como lida e redirecionar
    function markNotificationAsRead(notificationId, notificationUrl) {
        $.ajax({
            url: `/notificacao_lida/${notificationId}/`,
            method: 'POST',
            success: function (data) {
                if (data.success) {
                    // Atualize a interface do usuário para refletir que a notificação foi marcada como lida
                    fetchNotifications();

                    // Redirecione para a página de referência
                    window.location.href = notificationUrl;

                } else {
                    alert('Erro ao marcar a notificação como lida: ' + data.message);
                }
            },
            error: function () {
                console.error('Erro ao marcar a notificação como lida.');
            }
        });
    }

    // Função para atualizar o contador de notificações
    function updateNotificationBadge(count) {
        const $notificationBadge = $('.notification-badge');
        if (count > 0) {
            $notificationBadge.text(count).show();
        } else {
            $notificationBadge.hide();
        }
    }

    // Chamar a função de buscar notificações ao carregar a página
    fetchNotifications();
}


// Função para exibir o Toast personalizado
function notifcationToast(mensagem, somNome) {
    const notifcationToast = $("#customToast");
    const toastBody = $("#toastBody");
    const audioElement = new Audio(`/static/songs/${somNome}`);

    // Atualiza o conteúdo do Toast com a mensagem desejada
    toastBody.html(mensagem);

    // Exibe o Toast
    notifcationToast.toast("show");

    if (notificacoesAtivas) {
        audioElement.play();
    }


    // Esconde o Toast após 3 segundos (3000 milissegundos)
    setTimeout(function() {
        notifcationToast.toast("hide");
    }, 40000);
}



// Iniciar a função ao carregar a página
$(document).ready(function () {
    fetchAndRenderNotifications();

    // Adicione a função para buscar notificações a cada minuto
    setInterval(fetchAndRenderNotifications, 60000);  // 60000 milissegundos = 1 minuto
});



// Ouvinte de evento para o clique no botão "Limpar tudo"
$("#limparTudoLink").on("click", function (event) {
    event.preventDefault();

    // Chama a função para marcar todas as notificações como lidas
    marcarTodasNotificacoesComoLidas();
});

// Função para marcar todas as notificações como lidas
function marcarTodasNotificacoesComoLidas() {
    $.ajax({
        url: '/limpar_todas_notificacoes/',  // Atualize com a URL correta da sua API
        method: 'POST',
        success: function (data) {
            if (data.success) {
                // Atualize a interface do usuário para refletir que todas as notificações foram marcadas como lidas
                fetchAndRenderNotifications();

                // Zere a constante previousNotificationCount
                localStorage.setItem('previousNotificationCount', 0);
            } else {
                alert('Erro ao marcar todas as notificações como lidas: ' + data.message);
            }
        },
        error: function () {
            console.error('Erro ao marcar todas as notificações como lidas.');
        }
    });
}

//====================================================================================================




//============================================== SOM =================================================

// Variavel que armazena a opção de som ativo ou inativo
let somAtivo = false;


// Função para salvar a escolha do usuário no cookie
    function saveSoundPreferenceToCookie() {
        const cookieValue = somAtivo ? 'ativo' : 'inativo';
        setCookie('soundPreference', cookieValue, 365);  // Ajuste conforme necessário
    }

// Ouvinte de evento para o botão de alternância
$("#toggleSoundButton").on("change", function () {
    somAtivo = this.checked;
    saveSoundPreferenceToCookie();
    customToast(somAtivo ? "Som ativado" : "Som desativado", "normalSong.mp3");
});

// Função para definir um cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
}

// Função para obter um cookie
function getCookieSound(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

// Verificar o cookie ao carregar a página
document.addEventListener('DOMContentLoaded', function () {
    const cookieValue = getCookieSound('soundPreference');
    if (cookieValue === 'ativo') {
        somAtivo = true;
        $("#toggleSoundButton").prop('checked', true);
    } else {
        somAtivo = false;
        $("#toggleSoundButton").prop('checked', false);
    }
});

// Função para exibir o Toast personalizado
function customToast(mensagem, somNome) {
    const customToast = $("#customToast");
    const toastBody = $("#toastBody");
    const audioElement = new Audio(`/static/songs/${somNome}`);

    // Atualiza o conteúdo do Toast com a mensagem desejada
    toastBody.html(mensagem);

    // Exibe o Toast
    customToast.toast("show");

    // Toca o se o som estive ativado
    if (somAtivo) {
        audioElement.play();
    }

    // Esconde o Toast após 3 segundos (3000 milissegundos)
    setTimeout(function() {
        customToast.toast("hide");
    }, 40000);
}


//====================================================================================================



//============================================== MENU ================================================

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

//====================================================================================================



//=========================================== CALENDARIO =============================================

$(document).ready(function() {
        $('#calendario').fullCalendar({
            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'month,agendaWeek,agendaDay'
            },
            locale: 'pt-br',
            selectable: true, // Adiciona a opção para selecionar datas
            // Adicione seus eventos ao calendário
            events: [
                {
                    title: 'Férias do Arthur',
                    start: '2024-03-01',
                    color: '#00A094' // Define a cor do evento
                },
                {
                    title: 'Férias do Henrique',
                    start: '2024-03-01',
                    color: '#00A094' // Define a mesma cor para este evento
                }
            ]
        });

        $('#calendario').on('mouseover', '.fc-event', function(e) {
            var title = $(this).find('.fc-title').text();
            $('<div class="event-tooltip">' + title + '</div>').appendTo('body').css({
                top: e.pageY + 10,
                left: e.pageX + 10
            });
        }).on('mouseleave', '.fc-event', function() {
            $('.event-tooltip').remove();
        });
    });

//====================================================================================================


// time line ---------------------------------------------------------------------------------------------
$(document).ready(function(){
var $animation_elements = $('.anim');
var $window = $(window);

function check_if_in_view() {
var window_height = $window.height();
var window_top_position = $window.scrollTop();
var window_bottom_position = (window_top_position + window_height);

$.each($animation_elements, function() {
var $element = $(this);
var element_height = $element.outerHeight();
var element_top_position = $element.offset().top;
var element_bottom_position = (element_top_position + element_height);

if ((element_bottom_position >= window_top_position) &&
(element_top_position <= window_bottom_position)) {
$element.addClass('animated');
} else {
$element.removeClass('animated');
}
});
}

$window.on('scroll resize', check_if_in_view);
$window.trigger('scroll');
});


$(document).ready(function(){
    $(" .debits").hover(function(){
        $(" .center-right").css("background-color", "#4997cd");
        }, function(){
        $(" .center-right").css("background-color", "#fff");
    });
});


$(document).ready(function(){
    $(".credits").hover(function(){
        $(".center-left").css("background-color", "#4997cd");
        }, function(){
        $(".center-left").css("background-color", "#fff");
    });
});


// History request
const itemActions = document.querySelectorAll('.item-action');


// Função para buscar e exibir detalhes do cartão
function showCardDetails(cardId) {
    fetch(`/get_card_details/${cardId}`)
        .then(response => response.json())
        .then(data => {
            const detalhesAssunto = document.getElementById('detalhes-assunto');
            const detalhesService = document.getElementById('detalhes-service');

            // Verifica se os elementos HTML existem
            if (detalhesAssunto && detalhesService) {
                detalhesAssunto.textContent = `Assunto: ${data.assunto}`;
                detalhesService.textContent = `Serviço: ${data.service}`;
                // Adicione outros detalhes do cartão conforme necessário
            } else {
                console.error('Elementos de detalhes não encontrados.');
            }
        })
        .catch(error => {
            console.error('Erro ao obter detalhes do cartão:', error);
        });
}


// Iterar sobre os elementos e adicionar um event listener para cada um
itemActions.forEach(item => {
    item.addEventListener('click', function(event) {
        event.preventDefault();

        const cardId = item.getAttribute('data-card-id');

        if (cardId) {
            showCardDetails(cardId);
        } else {
            console.error('ID do cartão não encontrado.');
        }
    });
});


// Temas --------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    // Referenciar os elementos relevantes
    var backgroundImage = document.getElementById("backgroundImage");
    var padraoBtn = document.getElementById("padraoBtn");
    var cinzaBtn = document.getElementById("cinzaBtn");

    function setTema(tema) {
        console.log("Salvando tema: " + tema);
        localStorage.setItem("tema", tema);
    }

    // Função para obter o tema do localStorage
    function getTema() {
        // Obter o tema do localStorage, se não estiver definido, usar um valor padrão
        return localStorage.getItem("tema") || "/static/ccis/backgroundPro.png";
    }

    // Função para verificar se é o primeiro login
    function isFirstLogin() {
        return localStorage.getItem("firstLogin") === null;
    }

    function markFirstLogin() {
        localStorage.setItem("firstLogin", "false");
    }

    function aplicarTema() {
        var temaSalvo = getTema();
        console.log("Aplicando tema: " + temaSalvo);
        backgroundImage.src = temaSalvo;
    }

    // Adicione um evento ao botão padrão para verificar o primeiro login
    padraoBtn.addEventListener("click", function() {
        // Verificar se é o primeiro login antes de definir o tema
        if (isFirstLogin()) {
            markFirstLogin();
            setTema("/static/ccis/backgroundPro.png");
        } else {
            setTema("/static/ccis/backgroundPro.png");
        }
        aplicarTema();
    });

    padraoBtn.addEventListener("click", function() {
        setTema("/static/ccis/backgroundPro.png");
        aplicarTema();
    });

    cinzaBtn.addEventListener("click", function() {
        setTema("/static/ccis/backgroundCinza.png");
        aplicarTema();
    });

    // Aplicar o tema ao carregar a página
    aplicarTema();
});


// Férias --------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    // Configuração para o primeiro gráfico (pizzaPA)
    const ctx1 = document.getElementById('barPa').getContext('2d');
    const data1 = {
        labels: [
            'BRZ',
            'FSA',
            'DIG',
            'PAD',
            'PLA',
            'SJA',
            'SSB',
            'SIA',
            'VIP',
        ],
        datasets: [{
            label: 'PAs',
            data: [3, 5, 1, 1, 2, 2, 1, 9, 1], // Adicione mais valores conforme necessário
            backgroundColor: ['#00A094'],
            hoverOffset: 4
        }]
    };
    const config1 = {
        type: 'bar',
        data: data1,
    };
    new Chart(ctx1, config1);

    // Configuração para o segundo gráfico (pizzaSetor)
    const ctx2 = document.getElementById('barAdm').getContext('2d');
    const data2 = {
        labels: [
            'ADM',
            'CAD',
            'FIN',
            'RH',
            'REC',
            'RISC',
            'MKT',
            'PC',
            'RET',
            'SEC',
            'TEC'
        ],
        datasets: [{
            label: 'Administrativo',
            data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            backgroundColor: ['#00A094'],
            hoverOffset: 4
        }]
    };
    const config2 = {
        type: 'bar',
        data: data2,
    };
    new Chart(ctx2, config2);

    // Configuração para o segundo gráfico (pizzaSetor)
    const ctx3 = document.getElementById('barOpe').getContext('2d');
    const data3 = {
        labels: [
            'CAD',
            'CRÉ',
            'PS',
            'REC',
        ],
        datasets: [{
            label: 'Operacional',
            data: [1, 2, 3, 4],
            backgroundColor: ['#00A094'],
            hoverOffset: 4
        }]
    };
    const config3 = {
        type: 'bar',
        data: data3,
    };
    new Chart(ctx3, config3);

    const charts = [
        document.getElementById('chart1'),
        document.getElementById('chart2'),
        document.getElementById('chart3')
    ];
    let currentChartIndex = 0;

    const changeChartNextButton = document.getElementById('changeChartNext');
    const changeChartBackButton = document.getElementById('changeChartBack');

    function showChart(index) {
        charts.forEach((chart, i) => {
            if (i === index) {
                chart.style.display = 'block';
            } else {
                chart.style.display = 'none';
            }
        });
    }

    function showNextChart() {
        currentChartIndex = (currentChartIndex + 1) % charts.length;
        showChart(currentChartIndex);
    }

    function showPreviousChart() {
        currentChartIndex = (currentChartIndex - 1 + charts.length) % charts.length;
        showChart(currentChartIndex);
    }

    // Adicione ouvintes de evento aos botões de Next e Back
    changeChartNextButton.addEventListener('click', showNextChart);
    changeChartBackButton.addEventListener('click', showPreviousChart);

    // Mostrar o primeiro gráfico inicialmente
    showChart(currentChartIndex);;
});