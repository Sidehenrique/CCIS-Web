import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import modelformset_factory

from .models import dadosPessoais, dependentes, enderecoContato, outros, escolaridade, certificacao, \
    profissional, dadosBancarios,User,docRg,docCnh,docCpf,docReservista,docTitulo,docClt,docResidencia,\
    docCertidao,docAdmissional,docPeriodico,docCursos

from .forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios,\
    modelFormUser,modelFormRg,modelFormCnh, modelFormCpf,modelFormReservista,modelFormTitulo,modelFormClt,\
    modelFormResidencia,modelFormCertidao,modelFormAdmissional,modelFormPeriodico, modelFormCurso

from django.forms import inlineformset_factory


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

    pk_user = User.objects.get(pk=2)
    pk_dados = dadosPessoais.objects.get(pk=2)
    pk_dependentes = dependentes.objects.get(pk=2)
    pk_contato = enderecoContato.objects.get(pk=2)
    pk_escolaridade = escolaridade.objects.get(pk=2)
    #pk_certificacao = certificacao.objects.get(pk=2)
    pk_profi = profissional.objects.get(pk=2)
    pk_bancario = dadosBancarios.objects.get(pk=2)
    pk_outros = outros.objects.get(pk=2)
    print(pk_user,pk_outros,pk_bancario,pk_contato,pk_dados,pk_dependentes,pk_escolaridade,pk_profi)#pk_certificacao)

    dp = modelFormDadosPessoais(instance=pk_dados)
    de = modelFormDependentes(instance=pk_dependentes)
    conEnd = modelFormEnderecoContato(instance=pk_contato)
    esc = modelFormEscolaridade(instance=pk_escolaridade)
    #cert = modelFormCertificacao(instance=pk_certificacao)
    prof = modelFormProfissional(instance=pk_profi)
    db = modelFormDadosBancarios(instance=pk_bancario)
    out = ModelFormOutros(instance=pk_outros)
    mid = ModelFormMidia(instance=pk_dados)

    data = datAT()

    context = {'form': dp, 'dependentes': de, 'contatoEndereco': conEnd,
               'escolaridade': esc,  'profissional': prof,
               'dadosBancarios': db, 'outros': out, 'midia': mid, 'data': data} #'certificacao': cert, }

    if request.method == 'GET':
        return render(request, 'ccis/conta.html', context)

    if request.method == 'POST':
        dpForm = modelFormDadosPessoais(request.POST or None, instance=pk_dados)
        deForm = modelFormDependentes(request.POST or None, instance=pk_dependentes)
        conEndForm = modelFormEnderecoContato(request.POST or None, instance=pk_contato)
        escForm = modelFormEscolaridade(request.POST or None, instance=pk_escolaridade)
        #certForm = modelFormCertificacao(request.POST or None, instance=pk_certificacao)
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

        # elif certForm.is_valid():
        #     cor = 'green'
        #     certForm.save()
        #     messages.add_message(request=request,
        #                          message='SUCCESS: O Formulário foi validade e salvo com sucesso.',
        #                          level=messages.SUCCESS)

        #     return redirect('conta')

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


# INCLUIR NOVO USUARIO NO BANCO

def dev(request):
    
    form = UserCreationForm()
    dados_formset = inlineformset_factory(User,dadosPessoais,modelFormDadosPessoais,extra=1,can_delete=False)
    endereco_formset = inlineformset_factory(User, enderecoContato,modelFormEnderecoContato, extra=1,
                                               can_delete=False)
    dependentes_formset = inlineformset_factory(User, dependentes,modelFormDependentes, extra=1, 
                                                can_delete=False)
    escolaridade_formset = inlineformset_factory(User, escolaridade,modelFormEscolaridade, extra=1,
                                                can_delete=False)
    certificacao_formset = inlineformset_factory(User, certificacao,modelFormCertificacao, extra=1,
                                                can_delete=False)
    profissional_formset = inlineformset_factory(User, profissional,modelFormProfissional, extra=1,
                                                can_delete=False)
    dadosBancarios_formset = inlineformset_factory(User, dadosBancarios,modelFormDadosBancarios, extra=1,
                                                can_delete=False)
    outros_formset = inlineformset_factory(User, outros,ModelFormOutros, extra=1, can_delete=False)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        dados_form = dados_formset(request.POST)
        endereco_form = endereco_formset(request.POST)
        dependentes_form = dependentes_formset(request.POST) 
        escolaridade_form = escolaridade_formset (request.POST)
        certificacao_form = certificacao_formset (request.POST)
        profissional_form = profissional_formset (request.POST)
        dadosBancarios_form = dadosBancarios_formset (request.POST)
        outros_form = outros_formset(request.POST)


        if form.is_valid() and dados_form.is_valid() and endereco_form.is_valid() and dependentes_form.is_valid() and escolaridade_form.is_valid() and certificacao_form.is_valid() and profissional_form.is_valid() and dadosBancarios_form.is_valid() and outros_form.is_valid():
            novo_usuario = form.save()
            dados_form = dados_formset(request.POST, instance=novo_usuario)
            endereco_form = endereco_formset(request.POST, instance=novo_usuario)
            dependentes_form = dependentes_formset(request.POST, instance=novo_usuario)
            escolaridade_form = escolaridade_formset(request.POST, instance=novo_usuario)
            certificacao_form = certificacao_formset (request.POST, instance=novo_usuario)
            profissional_form = profissional_formset (request.POST, instance=novo_usuario)
            dadosBancarios_form = dadosBancarios_formset(request.POST, instance=novo_usuario)
            outros_form = outros_formset(request.POST, instance=novo_usuario)
            dados_form.save()
            endereco_form.save()
            dependentes_form.save()
            escolaridade_form.save()
            certificacao_form.save()
            profissional_form.save()
            dadosBancarios_form.save()
            outros_form.save()

        return HttpResponse('Salvo')


    else:
        form = UserCreationForm()
        dados_form = dados_formset()
        endereco_form = endereco_formset()
        dependentes_form = dependentes_formset() 
        escolaridade_form = escolaridade_formset ()
        certificacao_form = certificacao_formset ()
        profissional_form = profissional_formset ()
        dadosBancarios_form = dadosBancarios_formset ()
        outros_form = outros_formset()
       

    context = {
       
        'user': form,
        'dados': dados_form,
        'end':endereco_form,
        'dependentes_form': dependentes_form,
        'escolaridade_form': escolaridade_form,
        'certificacao_form': certificacao_form,
        'profissional_form': profissional_form,
        'dadosBancarios_form': dadosBancarios_form,
        'outros_form': outros_form}

    return render(request, 'ccis/dev.html', context)


#RETORNAR OS DADOS DO USUARIO NO FORMULARIO
# def dev(request):
#     usuario = request.user
#     dados = dadosPessoais.objects.filter(usuario=usuario).first()

#     if request.method == 'POST':
#         form = modelFormDadosPessoais(request.POST, instance=dados)
#         if form.is_valid():
#             form.save()
#     else:
#         form = modelFormDadosPessoais(instance=dados)
    
#     return render(request, 'ccis/dev.html', {'dados': dados,'form': form})

#RECEBER OS DOCUMENTOS POR USUARIO
def documentos(request):
    usuario = request.user
    doc = docRg.objects.filter(usuario=usuario).first()
    doc_cnh = docCnh.objects.filter(usuario=usuario).first()
    doc_cpf = docCpf.objects.filter(usuario=usuario).first()
    doc_reservista = docReservista.objects.filter(usuario=usuario).first()
    doc_titulo = docTitulo.objects.filter(usuario=usuario).first()
    doc_clt= docClt.objects.filter(usuario=usuario).first()
    doc_residencia = docResidencia.objects.filter(usuario=usuario).first()
    doc_certidao = docCertidao.objects.filter(usuario=usuario).first()
    doc_admissional = docAdmissional.objects.filter(usuario=usuario).first()
    doc_periodico = docPeriodico.objects.filter(usuario=usuario).first()


    if request.method == 'POST':
        form = modelFormRg(request.POST,request.FILES, instance=doc)
        cnh_form = modelFormCnh(request.POST,request.FILES, instance=doc_cnh)
        cpf_form = modelFormCpf(request.POST,request.FILES, instance=doc_cpf)
        reservista_form = modelFormReservista(request.POST,request.FILES, instance=doc_reservista)
        titulo_form = modelFormTitulo(request.POST,request.FILES, instance=doc_titulo)
        clt_form = modelFormClt(request.POST,request.FILES, instance=doc_clt)
        residencia_form = modelFormResidencia(request.POST,request.FILES, instance=doc_residencia)
        certidao_form = modelFormCertidao(request.POST,request.FILES, instance=doc_certidao)
        admissional_form = modelFormAdmissional(request.POST,request.FILES, instance=doc_admissional)
        periodico_form = modelFormPeriodico(request.POST,request.FILES, instance=doc_periodico)
        
        if form.is_valid and cnh_form.is_valid() and cpf_form.is_valid() and reservista_form.is_valid() and titulo_form.is_valid() and clt_form.is_valid() and residencia_form.is_valid() and certidao_form.is_valid() and admissional_form.is_valid() and periodico_form.is_valid():
            obj = form.save(commit=False)
            cnh_obj = cnh_form.save(commit=False)
            cpf_obj = cpf_form.save(commit=False)
            reservista_obj = reservista_form.save(commit=False)
            titulo_obj = titulo_form.save(commit=False)
            clt_obj = clt_form.save(commit=False)
            residencia_obj = residencia_form.save(commit=False)
            certidao_obj = certidao_form.save(commit=False)
            admissional_obj = admissional_form.save(commit=False)
            periodico_obj = periodico_form.save(commit=False)

            obj.usuario = usuario
            cnh_obj.usuario = usuario
            cpf_obj.usuario = usuario
            reservista_obj.usuario = usuario
            titulo_obj.usuario = usuario
            clt_obj.usuario = usuario
            residencia_obj.usuario = usuario
            certidao_obj.usuario = usuario
            admissional_obj.usuario = usuario
            periodico_obj.usuario = usuario

            obj.save()
            cnh_obj.save()
            cpf_obj.save()
            reservista_obj.save()
            titulo_obj.save()
            clt_obj.save()
            residencia_obj.save()
            certidao_obj.save()
            admissional_obj.save()
            periodico_obj.save()

            form.save()
            cnh_form.save()
            cpf_form.save()
            reservista_form.save()
            titulo_form.save()
            clt_form.save()
            residencia_form.save()
            certidao_form.save()
            admissional_form.save()
            periodico_form.save()

            return HttpResponse('Salvo')
    else:
        form = modelFormRg(instance=doc)
        cnh_form = modelFormCnh(instance=doc_cnh)
        cpf_form = modelFormCpf(instance=doc_cpf)
        reservista_form = modelFormReservista(instance=doc_reservista)
        titulo_form = modelFormTitulo(instance=doc_titulo)
        clt_form = modelFormClt(instance=doc_clt)
        residencia_form = modelFormResidencia(instance=doc_residencia)
        certidao_form = modelFormCertidao(instance=doc_certidao)
        admissional_form = modelFormAdmissional(instance=doc_admissional)
        periodico_form = modelFormPeriodico(instance=doc_periodico)

    context ={
        'form': form,
        'cnh_form':cnh_form,
        'cpf_form':cpf_form,
        'reservista_form':reservista_form,
        'titulo_form': titulo_form,
        'clt_form': clt_form,
        'residencia_form':residencia_form,
        'certidao_form': certidao_form,
        'admissional_form': admissional_form,
        'periodico_form': periodico_form,
    }

    return render(request, 'ccis/documentos.html', context)

# RECEBE OS CERTIFICADOS DO CURSO DO SICOOB UNIVERSIDADE
def cursos(request):
    if request.method == 'POST':
        curso_form = modelFormCurso(request.POST,request.FILES)
        if curso_form.is_valid():
            
            obj = curso_form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            curso_form.save()
        return HttpResponse('Salvo')
    else:
        curso_form = modelFormCurso(request.POST,request.FILES)
    return render(request, 'ccis/cursos.html', {'curso_form': curso_form})