from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .. models import dadosPessoais


@login_required(login_url="/login")
def home(request):
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)
    groupControle = user.groups.filter(id=28).exists()

    context = {
        'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
        'last_name': last_name, 'group_gestao': group_gestao,
    }

    return render(request, 'gestaoControle/home.html', context)


@login_required(login_url="/login")
def contabilidade(request):
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

    return render(request, 'gestaoControle/contabilidade.html', context)


@login_required(login_url="/login")
def relatorios(request):
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

    return render(request, 'gestaoControle/relatorios.html', context)


@login_required(login_url="/login")
def estrategico(request):
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

    return render(request, 'gestaoControle/estrategico.html', context)


@login_required(login_url="/login")
def inadimplencia(request):
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

    return render(request, 'gestaoControle/inadimplencia.html', context)


@login_required(login_url="/login")
def qqs(request):
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

    return render(request, 'gestaoControle/qqs.html', context)


@login_required(login_url="/login")
def pesquisa(request):
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

    return render(request, 'gestaoControle/pesquisa.html', context)


@login_required(login_url="/login")
def gestaoRelatorios(request):
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

    return render(request, 'gestaoControle/gestaoRelatorios.html', context)


@login_required(login_url="/login")
def rankingsicoob(request):
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

    return render(request, 'gestaoControle/rankingsicoob.html', context)


