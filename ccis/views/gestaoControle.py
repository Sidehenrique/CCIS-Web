from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .. models import dadosPessoais


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

    return render(request, 'gestaoControle/home.html', context)


@login_required(login_url="/login")
def contabilidade(request):
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
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
    }

    return render(request, 'gestaoControle/contabilidade.html', context)


@login_required(login_url="/login")
def comissionamento(request):
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
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
    }

    return render(request, 'gestaoControle/comissionamento.html', context)


@login_required(login_url="/login")
def estrategico(request):
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
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
    }

    return render(request, 'gestaoControle/estrategico.html', context)


@login_required(login_url="/login")
def inadimplencia(request):
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
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
    }

    return render(request, 'gestaoControle/inadimplencia.html', context)


@login_required(login_url="/login")
def lastro(request):
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
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
    }

    return render(request, 'gestaoControle/lastro.html', context)


@login_required(login_url="/login")
def qqs(request):
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
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
    }

    return render(request, 'gestaoControle/qqs.html', context)


@login_required(login_url="/login")
def pesquisa(request):
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
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
        'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
    }

    return render(request, 'gestaoControle/pesquisa.html', context)