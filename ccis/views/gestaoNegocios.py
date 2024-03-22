from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from ..models import dadosPessoais


@login_required(login_url="/login")
def home(request):

    return render(request, 'gestaoNegocios/home.html')


@login_required(login_url="/login")
def gestaoMetas(request):

    return render(request, 'gestaoNegocios/painel/gestaoMetas.html')
    

@login_required(login_url="/login")
def diaria(request):

    return render(request, 'gestaoNegocios/painel/diaria.html')
    

@login_required(login_url="/login")
def listasPropensos(request):

    return render(request, 'gestaoNegocios/painel/listasPropensos.html')
    

@login_required(login_url="/login")
def planoMetas(request):

    return render(request, 'gestaoNegocios/painel/planoMetas.html')
    

@login_required(login_url="/login")
def pronampe(request):
    return render(request, 'gestaoNegocios/painel/pronampe.html')
    

@login_required(login_url="/login")
def relatorioVisitas(request):
    return render(request, 'gestaoNegocios/painel/relatorioVisitas.html')


@login_required(login_url="/login")
def lastro(request):
    return render(request, 'gestaoNegocios/painel/lastro.html')


@login_required(login_url="/login")
def credito(request):

    return render(request, 'gestaoNegocios/submod/credito.html')


@login_required(login_url="/login")
def operacoes_credito(request):
    return render(request, 'gestaoNegocios/painel/operacoes_credito.html')


@login_required(login_url="/login")
def credito_liberacao(request):

    return render(request, 'gestaoNegocios/painel/credito_liberacao.html')


@login_required(login_url="/login")
def calendario(request):

    return render(request, 'gestaoNegocios/painel/calendario.html')


@login_required(login_url="/login")
def gestaoCarteira(request):

    return render(request, 'gestaoNegocios/submod/gestaoCarteira.html')


@login_required(login_url="/login")
def carteiras(request):

    return render(request, 'gestaoNegocios/painel/carteiras.html')


@login_required(login_url="/login")
def capitalRecorrente(request):

    return render(request, 'gestaoNegocios/painel/resultadoCoop.html')


@login_required(login_url="/login")
def contasInativas(request):

    return render(request, 'gestaoNegocios/painel/contasInativas.html')


@login_required(login_url="/login")
def resultadoCoop(request):
    return render(request, 'gestaoNegocios/painel/resultadoCoop.html')


@login_required(login_url="/login")
def campanhas(request):
    return render(request, 'gestaoNegocios/submod/campanhas.html')


@login_required(login_url="/login")
def integralize(request):
    return render(request, 'gestaoNegocios/painel/integralize.html')


@login_required(login_url="/login")
def gestaoCapital(request):
    return render(request, 'gestaoNegocios/gestaoCapital.html')


@login_required(login_url="/login")
def operacoes_vencer(request):
    return render(request, 'gestaoNegocios/operacoes_vencer.html')


@login_required(login_url="/login")
def sipag(request):
    return render(request, 'gestaoNegocios/sipag.html')





