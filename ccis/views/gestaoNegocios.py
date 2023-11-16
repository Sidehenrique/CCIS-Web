from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from ..models import dadosPessoais


@login_required(login_url="/login")
def home(request):

    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    group_gestao = log.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = log.groups.filter(id=28).exists()

    context = {
        'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
        'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
    }

    return render(request, 'gestaoNegocios/home.html', context)



@login_required(login_url="/login")
def gestaoMetas(request):
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

    if request.method == 'GET':
        context = {
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
        }

        return render(request, 'gestaoNegocios/gestaoMetas.html', context)
    

@login_required(login_url="/login")
def diaria(request):
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

    if request.method == 'GET':
        context = {
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
        }

        return render(request, 'gestaoNegocios/diaria.html', context)
    

@login_required(login_url="/login")
def listasPropensos(request):
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

    if request.method == 'GET':
        context = {
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
        }

        return render(request, 'gestaoNegocios/listasPropensos.html', context)
    

@login_required(login_url="/login")
def planoMetas(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    if request.method == 'GET':
        context = {
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
            'last_name': last_name, 'group_gestao': group_gestao
        }

        return render(request, 'gestaoNegocios/planoMetas.html', context)
    

@login_required(login_url="/login")
def pronampe(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    if request.method == 'GET':
        context = {
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
            'last_name': last_name, 'group_gestao': group_gestao
        }

        return render(request, 'gestaoNegocios/pronampe.html', context)
    

@login_required(login_url="/login")
def relatorioVisitas(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user


    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    if request.method == 'GET':
        context = {
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
            'last_name': last_name, 'group_gestao': group_gestao
        }

        return render(request, 'gestaoNegocios/relatorioVisitas.html', context)

@login_required(login_url="/login")
def lastro(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = user.groups.filter(id=28).exists()

    context = {
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao
    }

    return render(request, 'gestaoNegocios/lastro.html', context)


@login_required(login_url="/login")
def credito(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = user.groups.filter(id=28).exists()

    context = {
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao,
    }

    return render(request, 'gestaoNegocios/credito.html', context)


@login_required(login_url="/login")
def operacoes_credito(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = user.groups.filter(id=28).exists()

    context = {
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao,
    }

    return render(request, 'gestaoNegocios/operacoes_credito.html', context)


@login_required(login_url="/login")
def credito_liberacao(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = user.groups.filter(id=28).exists()

    context = {
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao,
    }

    return render(request, 'gestaoNegocios/credito_liberacao.html', context)


@login_required(login_url="/login")
def calendario(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = user.groups.filter(id=28).exists()

    context = {
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao,
    }

    return render(request, 'gestaoNegocios/calendario.html', context)


@login_required(login_url="/login")
def gestaoCarteira(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = user.groups.filter(id=28).exists()

    context = {
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao,
    }

    return render(request, 'gestaoNegocios/gestaoCarteira.html', context)


@login_required(login_url="/login")
def carteiras(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = user.groups.filter(id=28).exists()

    context = {
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao,
    }

    return render(request, 'gestaoNegocios/carteiras.html', context)





