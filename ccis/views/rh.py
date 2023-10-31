from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from .. models import dadosPessoais, profissional, CardSetorHistory, MessageHistory, CustomGroupInfo, SectorButtons, Card
from ..forms import ModelFormRhMalotes


# VIWER DO RH ----------------------------------------------------------------------------------------------------------
@login_required(login_url="/login")
def rh_home(request):
    user = request.user

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome='Gestão de Pessoas')

    except CustomGroupInfo.DOESNOTEXIST:
        dadosSetor = None

    setor = dadosSetor.nome
    print(setor)

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    superior = Group.objects.filter(id=3).first()

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
        sector_buttons = SectorButtons.objects.filter(group=3)
        context = {

            'username': user, 'groupControle': groupControle, 'setor': setor,
            'group_gestao': group_gestao, 'sector_buttons': sector_buttons,
            'superior': superior, 'equipe': nomes_equipe, 'dadosSetor': dadosSetor,
        }

        return render(request, 'ccis/setor_home.html', context)


@login_required(login_url="/login")
def rh_dash(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    totalUsuarios = len(profissional.objects.filter(situacao='Ativo'))
    totalColaborador = len(profissional.objects.filter(colaborador='Funcionário(a)', situacao='Ativo'))
    totalEstagiarios = len(profissional.objects.filter(colaborador='Estagiário(a)', situacao='Ativo'))
    totalMenor = len(profissional.objects.filter(colaborador='Menor Aprendiz', situacao='Ativo'))

    if request.method == 'GET':
        context = {
            'totalUsuarios': totalUsuarios, 'totalColaborador': totalColaborador,
            'totalEstagiarios': totalEstagiarios, 'totalMenor': totalMenor,
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
            'last_name': last_name, 'group_gestao': group_gestao,
        }

        return render(request, 'rh/dashboard.html', context)


@login_required(login_url="/login")
def pro_seletivo(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    contexto = {
                'groupControle':groupControle, 'group_gestao': group_gestao,
                }

    return render(request, 'rh/processo-seletivo.html', contexto)


@login_required(login_url="/login")
def ferias(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    contexto = {
                'groupControle': groupControle, 'group_gestao': group_gestao,
                }
    return render(request, 'rh/ferias.html', contexto)


@login_required(login_url="/login")
def anbima(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    contexto = {
                'groupControle': groupControle, 'group_gestao': group_gestao,
                }
    return render(request, 'rh/certificacoes-anbima.html', contexto)


@login_required(login_url="/login")
def colaboradores(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    contexto = {
                'groupControle': groupControle, 'group_gestao': group_gestao,
                }
    return render(request, 'rh/colaboradores.html', contexto)
# ----------------------------------------------------------------------------------------------------------------------

def new_request_rh(request):
    form = ModelFormRhMalotes()
    context = {'form': form, }

    return render(request, "rh/new_request_rh.html", context)


def salvar_malote_rh(request):
    if request.method == 'POST':

        request.POST = request.POST.copy()  # Crie uma cópia do dicionário para modificação
        request.POST['assunto'] = 'Malote'

        form = ModelFormRhMalotes(request.POST, request.FILES)

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
                setor_atual="Gestão de Pessoas",  # Setor atual
            )
            history_entry.save()

            texto2 = request.POST["descricao"]

            attachment = request.FILES.get('attachment')

            # Coletar as seleções dos checkboxes e montar a descrição
            itens_selecionados = []
            for item in ['item1', 'item2', 'item3', 'item4']:
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

            return redirect('rh_home')

    else:
        form = ModelFormRhMalotes()

    return render(request, 'rh/new_request_rh.html', {'form': form})


@login_required(login_url="/login")
def processos_rh(request):

    if request.method == 'GET':
        cards = Card.objects.all().prefetch_related(Prefetch('cardsetorhistory_set',
            queryset=CardSetorHistory.objects.order_by('-data_hora'))
        )

        group = Group.objects.all()
        setor = 'Gestão de Pessoas'

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
