from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from ..models import CardSetorHistory, MessageHistory, CustomGroupInfo, SectorButtons, Card
from ..forms import ModelFormMarketMalotes


@login_required(login_url="/login")
def marketing_home(request):
    user = request.user

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome='Marketing')

    except CustomGroupInfo.DOESNOTEXIST:
        dadosSetor = None

    setor = dadosSetor.nome
    print(setor)

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    superior = Group.objects.filter(id=41).first()

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
        sector_buttons = SectorButtons.objects.filter(group=41)
        context = {
            'username': user, 'groupControle': groupControle, 'setor': setor,
            'group_gestao': group_gestao, 'sector_buttons': sector_buttons,
            'superior': superior, 'equipe': nomes_equipe, 'dadosSetor': dadosSetor,
        }

        return render(request, 'ccis/setor_home.html', context)


@login_required(login_url="/login")
def new_request_market(request):
    form = ModelFormMarketMalotes()
    context = {'form': form, }

    return render(request, "marketing/new_request_market.html", context)


@login_required(login_url="/login")
def request_acessos_MK(request):
    if request.method == 'POST':
        form = ModelFormMarketMalotes(request.POST, request.FILES)
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
                setor_atual="Marketing",  # Setor atual
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

            return redirect('marketing_home')

    else:
        form = ModelFormMarketMalotes()

    return render(request, 'marketing/new_request_market.html', {'form': form})


@login_required(login_url="/login")
def processos_MK(request):

    if request.method == 'GET':
        cards = Card.objects.all().prefetch_related(Prefetch('cardsetorhistory_set',
            queryset=CardSetorHistory.objects.order_by('-data_hora'))
        )

        group = Group.objects.all()
        setor = 'Marketing'

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