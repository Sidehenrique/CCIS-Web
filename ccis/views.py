import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import dadosPessoais, dependentes, enderecoContato, outros, escolaridade, certificacao, \
    profissional, dadosBancarios

from .forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios


def datAT():
    data = datetime.datetime.now()
    d = datetime.datetime.strftime(data, "%d-%m-%Y %H:%M")
    return d


def loginPage(request):
    if request.method == 'GET':
        return render(request, 'ccis/login.html')

    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('senha')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

        else:

            statusName = 'is-invalid'
            statusSenha = 'is-invalid'

            context = {
                'username': username,
                'password': password,
                'statusName': statusName,
                'statusSenha': statusSenha
            }

            messages.add_message(request=request,
                                 message='Usuário ou senha incorretos.',
                                 level=messages.ERROR)

            return render(request, 'ccis/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/login")
def conta(request):
    pk_dados = dadosPessoais.objects.get(pk=1)
    pk_dependentes = dependentes.objects.get(pk=1)
    pk_contato = enderecoContato.objects.get(pk=1)
    pk_escolaridade = escolaridade.objects.get(pk=1)
    pk_certificacao = certificacao.objects.get(pk=1)
    pk_profi = profissional.objects.get(pk=1)
    pk_bancario = dadosBancarios.objects.get(pk=1)
    pk_outros = outros.objects.get(pk=1)

    dp = modelFormDadosPessoais(instance=pk_dados)
    de = modelFormDependentes(instance=pk_dependentes)
    conEnd = modelFormEnderecoContato(instance=pk_contato)
    esc = modelFormEscolaridade(instance=pk_escolaridade)
    cert = modelFormCertificacao(instance=pk_certificacao)
    prof = modelFormProfissional(instance=pk_profi)
    db = modelFormDadosBancarios(instance=pk_bancario)
    out = ModelFormOutros(instance=pk_outros)
    mid = ModelFormMidia(instance=pk_dados)

    data = datAT()

    context = {'form': dp, 'dependentes': de, 'contatoEndereco': conEnd,
               'escolaridade': esc, 'certificacao': cert, 'profissional': prof,
               'dadosBancarios': db, 'outros': out, 'midia': mid, 'data': data}

    if request.method == 'GET':
        return render(request, 'ccis/conta.html', context)

    if request.method == 'POST':
        dpForm = modelFormDadosPessoais(request.POST or None, instance=pk_dados)
        deForm = modelFormDependentes(request.POST or None, instance=pk_dependentes)
        conEndForm = modelFormEnderecoContato(request.POST or None, instance=pk_contato)
        escForm = modelFormEscolaridade(request.POST or None, instance=pk_escolaridade)
        certForm = modelFormCertificacao(request.POST or None, instance=pk_certificacao)
        profForm = modelFormProfissional(request.POST or None, instance=pk_profi)
        dbForm = modelFormDadosBancarios(request.POST or None, instance=pk_bancario)
        outForm = ModelFormOutros(request.POST or None, instance=pk_outros)
        midForm = ModelFormMidia(request.POST, request.FILES, instance=pk_dados)

        if dpForm.is_valid():
            cor = 'green'
            dpForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        elif deForm.is_valid():
            cor = 'green'
            deForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        elif conEndForm.is_valid():
            cor = 'green'
            conEndForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        elif escForm.is_valid():
            cor = 'green'
            escForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        elif certForm.is_valid():
            cor = 'green'
            certForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        elif profForm.is_valid():
            cor = 'green'
            profForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        elif dbForm.is_valid():
            cor = 'green'
            dbForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        elif outForm.is_valid():
            cor = 'green'
            outForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        elif midForm.is_valid():
            cor = 'green'
            midForm.save()
            messages.add_message(request=request,
                                 message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
                                 level=messages.SUCCESS)

            return redirect('conta')

        else:
            cor = 'red'
            messages.add_message(request=request,
                                 message='ERRO ao validar o formulário, Por favor verifique se todos os'
                                         ' campos foram preenchidos corretamente', level=messages.ERROR)
            return redirect('conta')


@login_required(login_url="/login")
def solicitacao(request):
    return render(request, 'ccis/solicitacao.html')


@login_required(login_url="/login")
def profile(request):
    return render(request, 'ccis/profile.html')


def base(request):
    return render(request, 'ccis/base.html')


def home(request):
    return render(request, 'ccis/home.html')


@login_required(login_url="/login")
def usuario(request):

    dp = modelFormDadosPessoais()
    data = datAT()

    totalUsuarios = len(profissional.objects.filter(situacao='Ativo'))
    totalColaborador = len(profissional.objects.filter(colaborador='Funcionário(a)', situacao='Ativo'))
    totalEstagiarios = len(profissional.objects.filter(colaborador='Estagiário(a)', situacao='Ativo'))
    totalMenor = len(profissional.objects.filter(colaborador='Menor Aprendiz', situacao='Ativo'))

    totalAnual = len(profissional.objects.filter(situacao='Ativo', admissao__lte='2022-12-31 00:00:00'))
    totalAtual = len(profissional.objects.filter(situacao='Ativo', admissao__gte='2023-01-01 00:00:00'))
    totalMaster = (totalAtual + totalAnual) * 100 / totalAnual - 100
    totalMaster = str(totalMaster)[0:5]

    anual_F = len(profissional.objects.filter(situacao='Ativo', colaborador='Funcionário(a)',
                                              admissao__lte='2022-12-31 00:00:00'))
    atual_F = len(profissional.objects.filter(situacao='Ativo', colaborador='Funcionário(a)',
                                              admissao__gte='2023-01-01 00:00:00'))
    total_F = (anual_F + atual_F) * 100 / anual_F - 100
    porcentagem_F = str(total_F)[0:5]

    anual_E = len(profissional.objects.filter(situacao='Ativo', colaborador='Estagiário(a)',
                                              admissao__lte='2022-12-31 00:00:00'))
    atual_E = len(profissional.objects.filter(situacao='Ativo', colaborador='Estagiário(a)',
                                              admissao__gte='2023-01-01 00:00:00'))
    total_E = (anual_E + atual_E) * 100 / anual_E - 100
    porcentagem_E = str(total_E)[0:5]

    anual_M = len(profissional.objects.filter(situacao='Ativo', colaborador='Menor Aprendiz',
                                              admissao__lte='2022-12-31 00:00:00'))
    atual_M = len(profissional.objects.filter(situacao='Ativo', colaborador='Menor Aprendiz',
                                              admissao__gte='2023-01-01 00:00:00'))
    total_M = (anual_M + atual_M) * 100 / anual_M - 100
    porcentagem_M = str(total_M)[0:5]

    dados = dadosPessoais.objects.all()
    profi = profissional.objects.select_related('dadosPessoais').all()
    contatos = enderecoContato.objects.select_related('dadosPessoais').all()

    context = {'form': dp, 'data': data, 'totalUsuarios': totalUsuarios, 'totalColaborador': totalColaborador,
               'totalEstagiarios': totalEstagiarios, 'totalMenor': totalMenor, 'totalMaster': totalMaster,
               'totalUsuariosAnual': totalAnual, 'porcentagem_F': porcentagem_F, 'AnualFuncionarios': anual_F,
               'porcentagem_E': porcentagem_E, 'anualEstagiarios': anual_E, 'anualMenor': anual_M,
               'porcentagem_M': porcentagem_M, 'profissional': profi, 'dados': dados, 'enderecoContato': contatos}

    if request.method == 'GET':
        return render(request, 'ccis/usuario.html', context)

    # if request.method == 'POST':
    #     dpForm = modelFormDadosPessoais(request.POST)
    #
    #     if dpForm.is_valid():
    #         dpForm.save()
    #         messages.add_message(request=request,
    #                              message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
    #                              level=messages.SUCCESS)
    #
    #         return redirect('usuario')
    #
    #     else:
    #         messages.add_message(request=request,
    #                              message='ERRO ao validar o formulário, Por favor verifique se todos os'
    #                                      ' campos foram preenchidos corretamente', level=messages.ERROR)
    #         return redirect('usuario')


def dev(request):
    form = ModelFormMidia()

    dados = dadosPessoais.objects.get(pk=266)
    print(dados)

    if request.method == 'POST':
        form = ModelFormMidia(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("Salvo com sucesso")

    elif request.method == 'GET':
        return render(request, 'ccis/dev.html', {'form': form, 'dados': dados})
