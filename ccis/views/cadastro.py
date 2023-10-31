from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from ..models import CardSetorHistory, MessageHistory, CustomGroupInfo, SectorButtons, Card
from ..forms import ModelFormCadastroMalotes


@login_required(login_url="/login")
def cadastro_home(request):
    user = request.user

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome='Cadastro')

    except CustomGroupInfo.DOESNOTEXIST:
        dadosSetor = None

    setor = dadosSetor.nome
    print(setor)

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    superior = Group.objects.filter(id=7).first()

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
        sector_buttons = SectorButtons.objects.filter(group=7)

        context = {
            'username': user, 'groupControle': groupControle, 'setor': setor,
            'group_gestao': group_gestao, 'sector_buttons': sector_buttons,
            'superior': superior, 'equipe': nomes_equipe, 'dadosSetor': dadosSetor,
        }

        return render(request, 'ccis/setor_home.html', context)

def new_request_cadastro(request):
    form = ModelFormCadastroMalotes()
    context = {'form': form, }

    return render(request, "cadastro/new_request_cadastro.html", context)


def salvar_malote_cadastro(request):
    if request.method == 'POST':

        request.POST = request.POST.copy()  # Crie uma cópia do dicionário para modificação
        request.POST['assunto'] = 'Malote'

        form = ModelFormCadastroMalotes(request.POST, request.FILES)

        if form.is_valid():
            card = form.save(commit=False)
            card.solicitante = request.user
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=7),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Cadastro",  # Setor atual
            )
            history_entry.save()

            texto2 = request.POST["descricao"]

            attachment = request.FILES.get('attachment')

            # Coletar as seleções dos checkboxes e montar a descrição
            itens_selecionados = []
            for item in ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10',
                         'item11']:
                if request.POST.get(item):
                    itens_selecionados.append(request.POST.get(item))

            if (itens_selecionados or texto2):
                descricao = "Este Malote contém:<br> " + "<br>".join(itens_selecionados)

                if texto2:
                    descricao += "<br><br>"
                    descricao += "Descrição:<br>" + texto2

                # Salvar a descrição no campo message do MessageHistory
                message_history = MessageHistory(
                    card=card,
                    remetente=request.user,
                    message=descricao,
                    attachment=attachment,
                )
                message_history.save()

            return redirect('cadastro_home')

    else:
        form = ModelFormCadastroMalotes()

    return render(request, 'cadastro/new_request_cadastro.html', {'form': form})


@login_required(login_url="/login")
def processos_cadastro(request):

    if request.method == 'GET':
        cards = Card.objects.all().prefetch_related(Prefetch('cardsetorhistory_set',
            queryset=CardSetorHistory.objects.order_by('-data_hora'))
        )

        group = Group.objects.all()
        setor = 'Cadastro'

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
