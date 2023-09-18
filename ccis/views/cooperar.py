
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .. models import dadosPessoais


# VIWER DO COOPERAR ----------------------------------------------------------------------------------------------------
@login_required(login_url="/login")
def coopera(request):
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

    return render(request, 'coopera/home.html', context)


@login_required(login_url="/login")
def relacionamento(request):
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

    return render(request, 'coopera/relacionamento.html', context)


@login_required(login_url="/login")
def simulador(request):
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

    return render(request, 'coopera/simulador.html', context)


@login_required(login_url="/login")
def tabela(request):
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

    return render(request, 'coopera/tabela.html', context)


@login_required(login_url="/login")
def india(request):
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

    return render(request, 'coopera/india.html', context)


@login_required(login_url="/login")
def portifolio(request):
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

    return render(request, 'coopera/portifolio.html', context)


@login_required(login_url="/login")
def capital(request):
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

    return render(request, 'coopera/capital.html', context)


def dadosConsolidados(request):
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

    return render(request, 'coopera/dados.html', context)
# ----------------------------------------------------------------------------------------------------------------------
