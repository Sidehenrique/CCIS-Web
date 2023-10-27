from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Prefetch, F, Subquery, OuterRef
from django.shortcuts import render, redirect, get_object_or_404
from ..models import dadosPessoais, CardSetorHistory, MessageHistory, CustomGroupInfo, SectorButtons, Card
from ..forms import ModelFormAdmMalotes
from django.db.models import Max


@login_required(login_url="/login")
def adm_home(request):
    user = request.user

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome = 'Administrativo')

    except CustomGroupInfo.DOESNOTEXIST: dadosSetor = None

    setor = dadosSetor.nome

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    superior = Group.objects.filter(id=30).first()

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
        sector_buttons = SectorButtons.objects.filter(group=30)


        context = {

            'username': user, 'groupControle': groupControle, 'setor': setor,
            'group_gestao': group_gestao, 'sector_buttons': sector_buttons,
            'superior': superior, 'equipe': nomes_equipe, 'dadosSetor': dadosSetor,
        }

        return render(request, 'ccis/setor_home.html', context)


def new_request_adm(request):
    form = ModelFormAdmMalotes()
    context = {'form': form, }

    return render(request, "adm/new_request_adm.html", context)


def salvar_malote_adm(request):
    if request.method == 'POST':

        request.POST = request.POST.copy()  # Crie uma cópia do dicionário para modificação
        request.POST['assunto'] = 'Malote'

        form = ModelFormAdmMalotes(request.POST, request.FILES)

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
                setor_atual="Administrativo",  # Setor atual
            )
            history_entry.save()

            texto2 = request.POST["descricao"]

            attachment = request.FILES.get('attachment')

            # Coletar as seleções dos checkboxes e montar a descrição
            itens_selecionados = []
            for item in ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']:
                if request.POST.get(item):
                    itens_selecionados.append(request.POST.get(item))

            if (itens_selecionados or texto2):
                descricao = "<h6>Este Malote contém:</h6><br>" + ", ".join(itens_selecionados)

                if texto2:
                    descricao += f"<br>DESCRIÇÃO: {texto2}"

                # Salvar a descrição no campo message do MessageHistory
                message_history = MessageHistory(
                    card=card,
                    remetente=request.user,
                    message=descricao,
                    attachment=attachment,
                )
                message_history.save()

            return redirect('adm_home')

    else:
        form = ModelFormAdmMalotes()

    return render(request, 'adm/new_request_adm.html', {'form': form})


@login_required(login_url="/login")
def processos_adm(request):
    cards = Card.objects.all().prefetch_related(Prefetch('cardsetorhistory_set',
        queryset=CardSetorHistory.objects.order_by('-data_hora'))
    )

    # Inicializa o contador
    card_count = 0


    q_triagem = CardSetorHistory.objects.filter(
        status_atual="Triagem",
        setor_atual="Administrativo"
    ).count()

    q_atendimento = CardSetorHistory.objects.filter(
        status_atual="Em Atendimento",
        setor_atual="Administrativo"
    ).count()

    q_encaminhado = CardSetorHistory.objects.filter(
        status_atual="Encaminhado",
        setor_atual="Administrativo"
    ).count()

    q_concluido = CardSetorHistory.objects.filter(
        status_atual="Concluido",
        setor_atual="Administrativo"
    ).count()

    q_finalizado = CardSetorHistory.objects.filter(
        status_atual="Finalizado",
        setor_atual="Administrativo"
    ).count()

    group = Group.objects.all()
    setor = 'Administrativo'

    # Agora, você pode exibir card_count onde quiser no seu código, por exemplo:
    print(f"Total de cards em Triagem no setor {setor}: {card_count}")

    if request.method == 'GET':
        context = {
            'cards': cards,
            'group': group,
            'setor': setor,
            'q_triagem': q_triagem, 'q_atendimento': q_atendimento,
            'q_encaminhado': q_encaminhado, 'q_concluido': q_concluido,
            'q_finalizado':q_finalizado,


        }

        return render(request, 'ccis/processo.html', context)
