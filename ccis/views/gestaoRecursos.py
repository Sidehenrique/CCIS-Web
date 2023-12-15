from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from ..models import CardSetorHistory, MessageHistory, CustomGroupInfo, SectorButtons, Card, Notification
from ..forms import modelFormCI, modelFormApontamentos, modelFormAcessosGR, modelFormBasileiaGR, modelFormRiscoGR, \
    modelFormContabilidadeGR


@login_required(login_url="/login")
def gestaoRecurso_home(request):
    user = request.user

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome='Gestão de Recursos')

    except CustomGroupInfo.DOESNOTEXIST:
        dadosSetor = None

    setor = dadosSetor.nome
    print(setor)

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    superior = Group.objects.filter(id=43).first()

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
        sector_buttons = SectorButtons.objects.filter(group=43)
        context = {
            'username': user, 'groupControle': groupControle, 'setor': setor,
            'group_gestao': group_gestao, 'sector_buttons': sector_buttons,
            'superior': superior, 'equipe': nomes_equipe, 'dadosSetor': dadosSetor,
        }

        return render(request, 'ccis/setor_home.html', context)


@login_required(login_url="/login")
def new_request_recurso(request):
    apontamentos = modelFormApontamentos()
    ci = modelFormCI()
    portifolio = modelFormAcessosGR()
    basileia = modelFormBasileiaGR()
    risco = modelFormRiscoGR()
    contabilidade = modelFormContabilidadeGR()

    context = {'apontamentos': apontamentos, 'ci': ci, 'portifolio': portifolio, 'basileia': basileia, 'risco': risco,
               'contabilidade': contabilidade}

    return render(request, "gestaoRecursos/new_request_GR.html", context)


@login_required(login_url="/login")
def request_portifolios(request):
    if request.method == 'POST':
        form = modelFormAcessosGR(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.setor = get_object_or_404(Group, id=43)
            card.status = 'Triagem'
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=43),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Gestão de Recursos",  # Setor atual
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

                recipients = User.objects.filter(groups=grupo_setor)
                for recipient in recipients:
                    if recipient != request.user:
                        notification = Notification(
                            author=request.user,
                            description=f"{card.solicitante} Abri uma nova Solicitação",
                            subject=card.assunto + f" N°: {card.idCard}",
                            recipient=recipient,
                            url=setor_link,
                        )
                        notification.save()

            return redirect('gestaoRecurso_home')

    else:
        form = modelFormAcessosGR()

    return render(request, 'gestaoRecursos/new_request_recurso.html', {'form': form})


@login_required(login_url="/login")
def request_basileia(request):
    if request.method == 'POST':
        form = modelFormBasileiaGR(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.setor = get_object_or_404(Group, id=43)
            card.status = 'Triagem'
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=43),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Gestão de Recursos",  # Setor atual
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

                recipients = User.objects.filter(groups=grupo_setor)
                for recipient in recipients:
                    if recipient != request.user:
                        notification = Notification(
                            author=request.user,
                            description=f"{card.solicitante} Abri uma nova Solicitação",
                            subject=card.assunto + f" N°: {card.idCard}",
                            recipient=recipient,
                            url=setor_link,
                        )
                        notification.save()

            return redirect('gestaoRecurso_home')

    else:
        form = modelFormBasileiaGR()

    return render(request, 'gestaoRecursos/new_request_recurso.html', {'form': form})


@login_required(login_url="/login")
def request_risco(request):
    if request.method == 'POST':
        form = modelFormRiscoGR(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.setor = get_object_or_404(Group, id=43)
            card.status = 'Triagem'
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=43),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Gestão de Recursos",  # Setor atual
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

                recipients = User.objects.filter(groups=grupo_setor)
                for recipient in recipients:
                    if recipient != request.user:
                        notification = Notification(
                            author=request.user,
                            description=f"{card.solicitante} Abri uma nova Solicitação",
                            subject=card.assunto + f" N°: {card.idCard}",
                            recipient=recipient,
                            url=setor_link,
                        )
                        notification.save()

            return redirect('gestaoRecurso_home')

    else:
        form = modelFormRiscoGR()

    return render(request, 'gestaoRecursos/new_request_recurso.html', {'form': form})


@login_required(login_url="/login")
def request_contabilidade(request):
    if request.method == 'POST':
        form = modelFormContabilidadeGR(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.setor = get_object_or_404(Group, id=43)
            card.status = 'Triagem'
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=43),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Gestão de Recursos",  # Setor atual
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

                recipients = User.objects.filter(groups=grupo_setor)
                for recipient in recipients:
                    if recipient != request.user:
                        notification = Notification(
                            author=request.user,
                            description=f"{card.solicitante} Abri uma nova Solicitação",
                            subject=card.assunto + f" N°: {card.idCard}",
                            recipient=recipient,
                            url=setor_link,
                        )
                        notification.save()

            return redirect('gestaoRecurso_home')

    else:
        form = modelFormContabilidadeGR()

    return render(request, 'gestaoRecursos/new_request_recurso.html', {'form': form})


@login_required(login_url="/login")
def request_ci_recurso(request):
    if request.method == 'POST':

        request.POST = request.POST.copy()
        request.POST['assunto'] = 'CI/CNAC/R.O'

        form = modelFormCI(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.setor = get_object_or_404(Group, id=43)
            card.status = 'Triagem'
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=43),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Gestão de Recursos",  # Setor atual
            )
            history_entry.save()

            attachment = request.FILES.get('attachment')
            descricao = form.cleaned_data.get('descricao')
            assunto = request.POST.get('assunto-input')

            if (assunto):
                descricao = f"<strong>Assunto:</strong> {assunto} <br><br>" + descricao

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

                recipients = User.objects.filter(groups=grupo_setor)
                for recipient in recipients:
                    if recipient != request.user:
                        notification = Notification(
                            author=request.user,
                            description=f"{card.solicitante} Abriu uma nova solicitação",
                            subject=card.assunto + f" N°: {card.idCard}",
                            recipient=recipient,
                            url=setor_link,
                        )
                        notification.save()

            return redirect('gestaoRecurso_home')
    else:
        form = modelFormCI()

    return render(request, 'gestaoRecursos/new_request_GR', {'form': form})


@login_required(login_url="/login")
def request_apontamentos_recurso(request):
    descricao = ""
    if request.method == 'POST':

        request.POST = request.POST.copy()
        request.POST['assunto'] = 'Apontamentos'

        form = modelFormApontamentos(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.setor = get_object_or_404(Group, id=43)
            card.status = 'Triagem'
            card.cor = "#FFCECE"
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=43),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Gestão de Recursos",  # Setor atual
            )
            history_entry.save()

            attachment = request.FILES.get('attachment')
            assunto = request.POST.get('input')

            reincidente = request.POST.get('reincidente')

            reagendamentos_selecionados = []

            for i in range(1, 5):  # Altere o range para o número correto de checkboxes
                checkbox_name = f'reagendamento{i}'
                if checkbox_name in request.POST:
                    reagendamentos_selecionados.append(request.POST.get(checkbox_name))

            if assunto or reincidente is not None or reagendamentos_selecionados or form.cleaned_data.get('descricao'):

                if assunto:
                    descricao += f"<strong>Assunto:</strong> {assunto}<br>"

                if reincidente is not None:
                    descricao += f"Reincidente: {reincidente}<br>"

                if reagendamentos_selecionados:
                    descricao += f"Reagendamentos: {', '.join(reagendamentos_selecionados)}<br>"

                if form.cleaned_data.get('descricao'):
                    descricao += f"Descrição: {form.cleaned_data.get('descricao')}<br>"

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

                recipients = User.objects.filter(groups=grupo_setor)
                for recipient in recipients:
                    if recipient != request.user:
                        notification = Notification(
                            author=request.user,
                            description=f"{card.solicitante} Abriu uma nova solicitação",
                            subject=card.assunto + f" N°: {card.idCard}",
                            recipient=recipient,
                            url=setor_link,
                        )
                        notification.save()

            return redirect('gestaoRecurso_home')
    else:
        form = modelFormApontamentos()

    return render(request, 'gestaoRecursos/new_request_GR.html', {'form': form, 'is_apontamento': True})


@login_required(login_url="/login")
def processos_recurso(request):
    if request.method == 'GET':
        cards = Card.objects.all().prefetch_related(Prefetch('cardsetorhistory_set',
                                                             queryset=CardSetorHistory.objects.order_by('-data_hora'))
                                                    )

        group = Group.objects.all()
        setor = 'Gestão de Recursos'

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
