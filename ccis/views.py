import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import dadosPessoais, dependentes, enderecoContato, outros, escolaridade, certificacao, \
    profissional, dadosBancarios

from .forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios


def loginPage(request):
    return render(request, 'ccis/login.html')


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

    data = datetime.datetime.now()

    context = {'form': dp, 'dependentes': de, 'contatoEndereco': conEnd,
               'escolaridade': esc, 'certificacao': cert, 'profissional': prof,
               'dadosBancarios': db, 'outros': out, 'midia': mid, 'data': data}

    if request.method == 'GET':
        return render(request, 'ccis/conta.html', context)

    if request.method == 'POST':
        dpForm = modelFormDadosPessoais(request.POST, instance=pk_dados)
        deForm = modelFormDependentes(request.POST, instance=pk_dependentes)
        conEndForm = modelFormEnderecoContato(request.POST, instance=pk_contato)
        escForm = modelFormEscolaridade(request.POST, instance=pk_escolaridade)
        certForm = modelFormCertificacao(request.POST, instance=pk_certificacao)
        profForm = modelFormProfissional(request.POST, instance=pk_profi)
        dbForm = modelFormDadosBancarios(request.POST, instance=pk_bancario)
        outForm = ModelFormOutros(request.POST, instance=pk_outros)

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

        else:
            cor = 'red'
            messages.add_message(request=request,
                                 message='ERRO ao validar o formulário, Por favor verifique se todos os'
                                         ' campos foram preenchidos corretamente', level=messages.ERROR)
            return render(request, 'ccis/conta.html', {'form': context, 'data': data, 'cor': cor})


def usuario(request):
    return render(request, 'ccis/usuario.html')


def solicitacao(request):
    return render(request, 'ccis/solicitacao.html')


def profile(request):
    return render(request, 'ccis/profile.html')


def base(request):
    return render(request, 'ccis/base.html')


def formLogin(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('senha')

        statusName = 'is-valid'
        statusSenha = 'is-valid'

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('conta')

        else:

            statusName = 'is-invalid'
            statusSenha = 'is-invalid'

            context = {
                'username': username,
                'password': password,
                'statusName': statusName,
                'statusSenha': statusSenha

            }
            messages.add_message(request=request, message='Usuario ou senha incorretos', level=messages.ERROR)
            return render(request, 'ccis/login.html', context)
    return render(request, 'ccis/login.html')


def dev(request):
    form = ModelFormMidia()

    if request.method == 'POST':

        form = ModelFormMidia(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("Salvo com sucesso")

        else:
            return HttpResponse("não passou")

    elif request.method == 'GET':
        return render(request, 'ccis/dev.html', {'form': form})
