from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .. models import dadosPessoais


@login_required(login_url="/login")
def home(request):
    return render(request, 'gestaoControle/home.html')


@login_required(login_url="/login")
def contabilidade(request):
    return render(request, 'gestaoControle/painel/contabilidade.html')


@login_required(login_url="/login")
def relatorios(request):
    return render(request, 'gestaoControle/painel/relatorios.html')


@login_required(login_url="/login")
def estrategico(request):
    return render(request, 'gestaoControle/painel/estrategico.html')


@login_required(login_url="/login")
def inadimplencia(request):
    return render(request, 'gestaoControle/painel/inadimplencia.html')


@login_required(login_url="/login")
def qqs(request):
    return render(request, 'gestaoControle/painel/qqs.html')


@login_required(login_url="/login")
def pesquisa(request):
    return render(request, 'gestaoControle/painel/pesquisa.html')


@login_required(login_url="/login")
def gestaoRelatorios(request):
    return render(request, 'gestaoControle/submod/gestaoRelatorios.html')


@login_required(login_url="/login")
def rankingsicoob(request):
    return render(request, 'gestaoControle/painel/rankingsicoob.html')


