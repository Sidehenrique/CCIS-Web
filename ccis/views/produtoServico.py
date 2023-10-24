from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from ..models import dadosPessoais, CardSetorHistory, MessageHistory, CustomGroupInfo
from ..forms import ModelFormPS


@login_required(login_url="/login")
def produtoServico_home(request):
    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome='Produto e Serviço')

    except CustomGroupInfo.DOESNOTEXIST:
        dadosSetor = None

    setor = dadosSetor.nome
    print(setor)

    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

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
        context = {
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'username': user, 'groupControle': groupControle, 'setor': setor,
            'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
            'superior': superior, 'equipe': nomes_equipe, 'dadosSetor': dadosSetor,
        }

        return render(request, 'ccis/setor_home.html', context)


def request_produto_servico(request):
    form = ModelFormPS()
    context = {'form': form, }

    return render(request, "produtoServico/request_produto_servico.html", context)


def salvar_malote_PS(request):
    if request.method == 'POST':

        request.POST = request.POST.copy()  # Crie uma cópia do dicionário para modificação
        request.POST['assunto'] = 'Malote'

        form = ModelFormPS(request.POST, request.FILES)

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
                setor_atual="ProdutoServico",  # Setor atual
            )
            history_entry.save()

            texto2 = request.POST["descricao"]

            attachment = request.FILES.get('attachment')

            # Coletar as seleções dos checkboxes e montar a descrição
            itens_selecionados = []
            for item in ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10',
                         'item11', 'item12', 'item13', 'item14', 'item15', 'item16', 'item17', 'item18',
                         'item19','item20','item21', 'item22', 'item23', 'item24', 'item25', 'item26', 'item27',
                         'item28','item29','item30', 'item31']:
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

            return redirect('produtoServico_home')

    else:
        form = ModelFormPS()

    return render(request, 'produtoServico/request_produto_servico.html', {'form': form})
