from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .. models import dadosPessoais
# from .. forms import modelFormAcessosTI


# VIWER DO TI ----------------------------------------------------------------------------------------------------------
@login_required(login_url="/login")
def ti_home(request):
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
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
            'superior': superior, 'equipe': nomes_equipe
        }

        return render(request, 'ccis/setor_home.html', context)


def new_request(request):
    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser
    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    acessos = modelFormAcessosTI()
    equipamentos = modelFormEquipamentosTI()
    servicos = modelFormServicosTI()

    contexto = {'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
                'group_gestao': group_gestao, 'is_superadmin': is_superadmin, 'acessos': acessos,
                'equipamentos': equipamentos, 'servicos': servicos, 'groupControle': groupControle}

    return render(request, 'ti/new_request.html', contexto)

<<<<<<< HEAD

def estoque(request):
    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser
    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    acessos = modelFormAcessosTI()
    equipamentos = modelFormEquipamentosTI()
    servicos = modelFormServicosTI()

    contexto = {'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
                'group_gestao': group_gestao, 'is_superadmin': is_superadmin, 'acessos': acessos,
                'equipamentos': equipamentos, 'servicos': servicos, 'groupControle': groupControle}

    return render(request, 'ti/estoque.html', contexto)
# ----------- ----------------------------------------------------------------------------------------------------------
=======
# ----------------------------------------------------------------------------------------------------------------------
>>>>>>> 860fa90b4bf85d656ad0cf973070c3a42a0a10a3

