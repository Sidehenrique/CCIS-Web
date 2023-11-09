from django.db.models import Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from ccis.forms import ModelFormNotebook
from ..models import dadosPessoais, Card, MessageHistory, CardSetorHistory, Notebook, CustomGroupInfo, SectorButtons, \
    Notification
from ..forms import modelFormAcessosTI, modelFormEquipamentosTI, modelFormSevicosTI


# VIWER DO TI ----------------------------------------------------------------------------------------------------------
@login_required(login_url="/login")
def ti_home(request):
    user = request.user

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome='Tecnologia')

    except CustomGroupInfo.DOESNOTEXIST:
        dadosSetor = None

    setor = dadosSetor.nome
    print(setor)

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    superior = Group.objects.filter(id=2).first()

    nomes_equipe = []

    if superior is None:
        pass

    else:
        equipe = User.objects.filter(groups=superior)
        # Resto do código
        for usuario in equipe:
            first_nameA = usuario.first_name
            last_nameA = usuario.last_name
            sexo = usuario.dadosPessoais.sexo
            foto = usuario.dadosPessoais.foto
            cargo = usuario.profissional.first().cargo if usuario.profissional.first() else 'Não informado'
            nomes_equipe.append(
                {'id': usuario.id,
                 'foto': foto,
                 'first_name': first_nameA,
                 'last_name': last_nameA,
                 'sexo': sexo,
                 'cargo': cargo})

        # Ordenar a equipe com o supervisor no topo
        nomes_equipe = sorted(nomes_equipe, key=lambda x: (x['cargo'] != 'Supervisor(a)', x['cargo'] != 'Gerente de PA',
                                                           x['cargo'] != 'Encarregado(a)'))

    if request.method == 'GET':
        sector_buttons = SectorButtons.objects.filter(group=2)
        context = {
            'username': user, 'groupControle': groupControle, 'setor': setor,
            'group_gestao': group_gestao, 'sector_buttons': sector_buttons,
            'superior': superior, 'equipe': nomes_equipe, 'dadosSetor': dadosSetor,
        }

        return render(request, 'ccis/setor_home.html', context)


@login_required(login_url="/login")
def new_request_ti(request):
    acessos = modelFormAcessosTI()
    equipamentos = modelFormEquipamentosTI()
    servicos = modelFormSevicosTI()

    contexto = {'acessos': acessos, 'equipamentos': equipamentos, 'servicos': servicos}

    return render(request, 'ti/new_request.html', contexto)


@login_required(login_url="/login")
def request_acessos_ti(request):
    if request.method == 'POST':
        form = modelFormAcessosTI(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=2),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Tecnologia",  # Setor atual
            )
            history_entry.save()

            attachment = request.FILES.get('attachment')

            descricao = form.cleaned_data.get('descricao')
            if descricao:
                message_history = MessageHistory(
                    card=card,
                    remetente=request.user,
                    message=descricao,
                    attachment=attachment,
                )
                message_history.save()

                # Obtenha o histórico de setor mais recente para o cartão
                historico_setor = CardSetorHistory.objects.filter(card=card).latest('data_hora')

                # Obtenha o grupo associado ao histórico de setor
                grupo_setor = historico_setor.setor

                # Obtenha a URL do setor com base no grupo do responsável
                setor_link = CustomGroupInfo.objects.get(group=grupo_setor).url

                if card.responsavel is None:
                    # Se o responsável não existe, envie a mensagem para todos os membros do grupo
                    recipients = User.objects.filter(groups=grupo_setor)
                    for recipient in recipients:
                        if recipient != request.user:
                            notification = Notification(
                                author=request.user,
                                description="Você tem uma nova mensagem",
                                subject=card.assunto + f" N°: {card.idCard}",
                                recipient=recipient,
                                url=setor_link,
                            )
                            notification.save()
                elif card.responsavel == request.user:
                    # Se o remetente é o próprio responsável, envie a mensagem para o solicitante
                    notification = Notification(
                        author=request.user,
                        description="Você tem uma nova mensagem",
                        subject=card.assunto + f" N°: {card.idCard}",
                        recipient=card.solicitante,
                        url='processos_user',  # Defina a URL apropriada
                    )
                    notification.save()
                else:
                    # Se o remetente não é o responsável, envie a mensagem para o responsável
                    notification = Notification(
                        author=request.user,
                        description="Você tem uma nova mensagem",
                        subject=card.assunto + f" N°: {card.idCard}",
                        recipient=card.responsavel,
                        url=setor_link,
                    )
                    notification.save()

            return redirect('ti_home')

    else:
        form = modelFormAcessosTI()

    return render(request, 'ti/new_request.html', {'form': form})


@login_required(login_url="/login")
def request_equipamentos_ti(request):
    if request.method == 'POST':
        form = modelFormEquipamentosTI(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=1),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Tecnologia",  # Setor atual
            )
            history_entry.save()

            attachment = request.FILES.get('attachment')

            descricao = form.cleaned_data.get('descricao')
            if descricao:
                message_history = MessageHistory(
                    card=card,
                    remetente=request.user,
                    message=descricao,
                    attachment=attachment,
                )
                message_history.save()

            return redirect('ti_home')

    else:
        form = modelFormAcessosTI()

    return render(request, 'ti/new_request.html', {'form': form})


@login_required(login_url="/login")
def request_servicos_ti(request):
    if request.method == 'POST':
        form = modelFormSevicosTI(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=1),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Tecnologia",  # Setor atual
            )
            history_entry.save()

            attachment = request.FILES.get('attachment')

            descricao = form.cleaned_data.get('descricao')
            if descricao:
                message_history = MessageHistory(
                    card=card,
                    remetente=request.user,
                    message=descricao,
                    attachment=attachment,
                )
                message_history.save()

            return redirect('ti_home')
    else:
        form = modelFormAcessosTI()

    return render(request, 'ti/new_request.html', {'form': form})


@login_required(login_url="/login")
def processos_ti(request):

    if request.method == 'GET':
        cards = Card.objects.all().prefetch_related(Prefetch('cardsetorhistory_set',
            queryset=CardSetorHistory.objects.order_by('-data_hora'))
        )

        group = Group.objects.all()
        setor = 'Tecnologia'

        # Inicializa os contadores para cada estado
        card_count_triagem = 0
        card_count_atendimento = 0
        card_count_encaminhado = 0
        card_count_concluido = 0
        card_count_finalizado = 0

        for card in cards:
            cardsetorhistory = card.cardsetorhistory_set.first()
            if cardsetorhistory:
                if cardsetorhistory.setor_atual == setor:
                    if cardsetorhistory.status_atual == "Triagem":
                        card_count_triagem += 1
                    elif cardsetorhistory.status_atual == "Em Atendimento":
                        card_count_atendimento += 1
                    elif cardsetorhistory.status_atual == "Encaminhado":
                        card_count_encaminhado += 1
                    elif cardsetorhistory.status_atual == "Concluido":
                        card_count_concluido += 1
                    elif cardsetorhistory.status_atual == "Finalizado":
                        card_count_finalizado += 1

        context = {
            'cards': cards,
            'group': group,
            'setor': setor,
            'card_count_triagem': card_count_triagem,
            'card_count_atendimento': card_count_atendimento,
            'card_count_encaminhado': card_count_encaminhado,
            'card_count_concluido': card_count_concluido,
            'card_count_finalizado': card_count_finalizado,
        }

        return render(request, 'ccis/processo.html', context)


# ----------------------------------------------------------------------------------------------------------------------


def estoque(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    contexto = {
                'group_gestao': group_gestao, 'groupControle': groupControle}

    return render(request, 'ti/estoque.html', contexto)


@login_required(login_url="/login")
def notebook(request):
    dadosTable = Notebook.objects.all()
    form = ModelFormNotebook()

    if request.method == 'POST':
        form = ModelFormNotebook(request.POST)
        if form.is_valid():

            form.save()

            return redirect('notebook')

    return render(request, 'ti/estoque/notebook.html', {'form': form, 'dadosTable': dadosTable})
