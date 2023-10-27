from django.utils import timezone
from dateutil.relativedelta import relativedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .. models import dadosPessoais, profissional, CardSetorHistory, MessageHistory, CustomGroupInfo, SectorButtons
from ..forms import ModelFormRhMalotes


# VIWER DO RH ----------------------------------------------------------------------------------------------------------
@login_required(login_url="/login")
def rh_home(request):
    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome='Gestão de Pessoas')

    except CustomGroupInfo.DOESNOTEXIST:
        dadosSetor = None

    setor = dadosSetor.nome
    print(setor)

    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

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
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'username': user, 'groupControle': groupControle, 'setor': setor,
            'group_gestao': group_gestao, 'is_superadmin': is_superadmin, 'sector_buttons': sector_buttons,
            'superior': superior, 'equipe': nomes_equipe, 'dadosSetor': dadosSetor,
        }

        return render(request, 'ccis/setor_home.html', context)


@login_required(login_url="/login")
def rh_dash(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

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
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
        }

        return render(request, 'rh/dashboard.html', context)


@login_required(login_url="/login")
def pro_seletivo(request):
    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser
    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    contexto = {'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
                'groupControle':groupControle, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin
                }

    return render(request, 'rh/processo-seletivo.html', contexto)


@login_required(login_url="/login")
def ferias(request):
    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser
    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    contexto = {'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
                'groupControle': groupControle, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin
                }
    return render(request, 'rh/ferias.html', contexto)


@login_required(login_url="/login")
def anbima(request):
    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser
    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    contexto = {'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
                'groupControle': groupControle, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin
                }
    return render(request, 'rh/certificacoes-anbima.html', contexto)


@login_required(login_url="/login")
def colaboradores(request):
    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser
    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    contexto = {'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
                'groupControle': groupControle, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin
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
                setor_atual="Rh",  # Setor atual
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

            return redirect('rh_home')

    else:
        form = ModelFormRhMalotes()

    return render(request, 'rh/new_request_rh.html', {'form': form})