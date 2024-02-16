from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from ..models import dadosPessoais


@login_required(login_url="/login")
def home(request):

    return render(request, 'gestaoNegocios/home.html')


@login_required(login_url="/login")
def gestaoMetas(request):

    return render(request, 'gestaoNegocios/gestaoMetas.html')
    

@login_required(login_url="/login")
def diaria(request):

    return render(request, 'gestaoNegocios/diaria.html')
    

@login_required(login_url="/login")
def listasPropensos(request):

    return render(request, 'gestaoNegocios/listasPropensos.html')
    

@login_required(login_url="/login")
def planoMetas(request):

    return render(request, 'gestaoNegocios/planoMetas.html')
    

@login_required(login_url="/login")
def pronampe(request):
    return render(request, 'gestaoNegocios/pronampe.html')
    

@login_required(login_url="/login")
def relatorioVisitas(request):
    return render(request, 'gestaoNegocios/relatorioVisitas.html')


@login_required(login_url="/login")
def lastro(request):
    return render(request, 'gestaoNegocios/lastro.html')


@login_required(login_url="/login")
def credito(request):

    return render(request, 'gestaoNegocios/credito.html')


@login_required(login_url="/login")
def operacoes_credito(request):
    return render(request, 'gestaoNegocios/operacoes_credito.html')


@login_required(login_url="/login")
def credito_liberacao(request):

    return render(request, 'gestaoNegocios/credito_liberacao.html')


@login_required(login_url="/login")
def calendario(request):

    return render(request, 'gestaoNegocios/calendario.html')


@login_required(login_url="/login")
def gestaoCarteira(request):

    return render(request, 'gestaoNegocios/gestaoCarteira.html')


@login_required(login_url="/login")
def carteiras(request):

    return render(request, 'gestaoNegocios/carteiras.html')


@login_required(login_url="/login")
def capitalRecorrente(request):

    return render(request, 'gestaoNegocios/resultadoCoop.html')


@login_required(login_url="/login")
def contasInativas(request):

    return render(request, 'gestaoNegocios/contasInativas.html')


@login_required(login_url="/login")
def resultadoCoop(request):
    return render(request, 'gestaoNegocios/resultadoCoop.html')


@login_required(login_url="/login")
def gestaoCapital(request):
    return render(request, 'gestaoNegocios/gestaoCapital.html')





