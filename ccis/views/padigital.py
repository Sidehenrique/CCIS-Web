from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from ..models import dadosPessoais, CardSetorHistory, MessageHistory, CustomGroupInfo
@login_required(login_url="/login")
def paDigital_home(request):
    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    try:
        dadosSetor = CustomGroupInfo.objects.get(nome='PA Digital')

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