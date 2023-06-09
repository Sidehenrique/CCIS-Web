import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.forms import formset_factory, inlineformset_factory
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

from .models import dadosPessoais, dependentes, enderecoContato, outros, escolaridade, certificacao, \
    profissional, dadosBancarios, docRg, docCnh, docCpf, docReservista, docTitulo, docClt, docResidencia, \
    docCertidao, docAdmissional, docPeriodico, docCursos

from .forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios, \
    modelFormUser, modelFormRg, modelFormCnh, modelFormCpf, modelFormReservista, modelFormTitulo, modelFormClt, \
    modelFormResidencia, modelFormCertidao, modelFormAdmissional, modelFormPeriodico, modelFormCurso


# SEGURANÇA ------------------------------------------------------------------------------------------------------------
def datAT():
    data = datetime.datetime.now()
    d = datetime.datetime.strftime(data, "%d-%m-%Y")
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

            new_login = User.objects.get(username=request.user).first_name
            print('>>>>>>>>>', new_login)

            if new_login == "" or None:
                return redirect('new_login_page')

            else:
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
    return redirect('home')


@login_required(login_url="/login")
def redefinir_senha(request):
    if request.method == 'POST':
        nova_senha = request.POST['Senha']
        user = request.user
        user.set_password(nova_senha)
        user.save()
        return redirect('profile')

    return redirect('login')


# ----------------------------------------------------------------------------------------------------------------------


# PAGINAS --------------------------------------------------------------------------------------------------------------
def base(request):
    user = request.user.username
    dados = User.objects.filter(username=user).select_related('dadosPessoais, profissional').values \
        ('first_name', 'last_name', 'dadosPessoais__nomeCompleto', 'dadosPessoais__foto',
         'dadosPessoais__sexo', 'profissional__cargo')

    dados_user = []
    for d in dados:
        first_name = d['first_name']
        last_name = d['last_name']
        sexo = d['dadosPessoais__sexo']
        foto = d['dadosPessoais__foto']
        cargo = d['profissional__cargo']

        dados_user.append(
            {'sexo': sexo, 'foto': foto, 'first_name': first_name, 'last_name': last_name, 'cargo': cargo})

    print(dados_user)
    contexto = {'dados_user': dados_user}

    return render(request, 'ccis/base.html', contexto)


def home(request):
    return render(request, 'ccis/home.html')


@login_required(login_url="/login")
def new_login_page(request):
    if request.method == 'POST':

        first_name = request.POST.get('first-name').capitalize()
        last_name = request.POST.get('last-name').capitalize()
        supervisor_id = request.POST.get('supervisor')

        # Obter o objeto User atual
        user = request.user

        print(first_name, last_name, supervisor_id, user)

        # Atualizar os campos first_name e last_name do User
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Obter o objeto Profissional atual ou criar um novo se não existir
        pro = profissional.objects.get(usuario=user)

        print(pro)

        if supervisor_id is not "":
            # Atualizar o campo supervisor do Profissional
            pro.superiorImediato = supervisor_id
            print(pro)
            pro.save()

            # Redefine a Senha
            nova_senha = request.POST['Senha']
            user = request.user
            user.set_password(nova_senha)
            user.save()

            # Redirecionar para outra página ou retornar uma resposta adequada
            return redirect('profile')


        else:

            # Redefine a Senha
            nova_senha = request.POST['Senha']
            user = request.user
            user.set_password(nova_senha)
            user.save()
            return redirect('profile')


    else:

        return render(request, 'ccis/new_login_page.html')


@login_required(login_url="/login")
def solicitacao(request):
    user = request.user.username
    dados = User.objects.filter(username=user).select_related('dadosPessoais, profissional').values \
        ('first_name', 'last_name', 'dadosPessoais__nomeCompleto', 'dadosPessoais__foto',
         'dadosPessoais__sexo', 'profissional__cargo')

    dados_user = []
    for d in dados:
        first_name = d['first_name']
        last_name = d['last_name']
        sexo = d['dadosPessoais__sexo']
        foto = d['dadosPessoais__foto']
        cargo = d['profissional__cargo']

        dados_user.append(
            {'sexo': sexo, 'foto': foto, 'first_name': first_name, 'last_name': last_name, 'cargo': cargo})

    print(dados_user)

    return render(request, 'ccis/solicitacao.html')


@login_required(login_url="/login")
def profile(request):
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name

    dados = dadosPessoais.objects.get(usuario=request.user)
    prof = profissional.objects.get(usuario=request.user)
    contatos = enderecoContato.objects.get(usuario=request.user)
    depen = dependentes.objects.filter(usuario=request.user).first()
    end = enderecoContato.objects.filter(usuario=request.user).first()
    esc = escolaridade.objects.filter(usuario=request.user).first()
    cert = certificacao.objects.filter(usuario=request.user).first()
    profi = profissional.objects.filter(usuario=request.user).first()
    db = dadosBancarios.objects.filter(usuario=request.user).first()
    out = outros.objects.filter(usuario=request.user).first()

    mid = ModelFormMidia(instance=dados)

    dados_form = modelFormDadosPessoais(request.POST or None, instance=dados)
    depen_form = modelFormDependentes(request.POST or None, instance=depen)
    end_form = modelFormEnderecoContato(request.POST or None, instance=end)
    esc_form = modelFormEscolaridade(request.POST or None, instance=esc)
    cert_form = modelFormCertificacao(request.POST or None, instance=cert)
    profi_form = modelFormProfissional(request.POST or None, instance=profi)
    db_form = modelFormDadosBancarios(request.POST or None, instance=db)
    out_form = ModelFormOutros(request.POST or None, instance=out)
    mid_form = ModelFormMidia(request.POST or None, instance=dados)

    # porcentagem barra de progresso

    porcentagem_dados_pessoais = dados_form.calcular_porcentagem_dp()
    porcentagem_dados_dependentes = depen_form.calcular_porcentagem_dep()
    porcentagem_end = end_form.calcular_porcentagem_end()
    porcentagem_esc = esc_form.calcular_porcentagem_esc()
    porcentagem_cert = cert_form.calcular_porcentagem_cer()
    porcentagem_profi = profi_form.calcular_porcentagem_pro()
    porcentagem_db = db_form.calcular_porcentagem_db()
    porcentagem_out = out_form.calcular_porcentagem_out()
    porcentagem_mid = mid_form.calcular_porcentagem_mid()

    porcentagem_total = (porcentagem_dados_pessoais + porcentagem_dados_dependentes + porcentagem_end + porcentagem_esc +
                         porcentagem_cert + porcentagem_profi + porcentagem_db + porcentagem_out + porcentagem_mid) / 9

    pf = round(porcentagem_total, 2)
    pf = str(pf)

    superior = Group.objects.get(user=request.user)
    equipe = User.objects.filter(groups=superior).values('first_name', 'last_name', 'dadosPessoais__nomeCompleto',
                                                         'dadosPessoais__foto', 'dadosPessoais__sexo',
                                                         'profissional__cargo')

    nomes_equipe = []
    for usuario in equipe:
        first_nameA = usuario['first_name']
        last_nameA = usuario['last_name']
        sexo = usuario['dadosPessoais__sexo']
        foto = usuario['dadosPessoais__foto']
        cargo = usuario['profissional__cargo']
        nomes_equipe.append(
            {'foto': foto, 'first_name': first_nameA, 'last_name': last_nameA, 'sexo': sexo, 'cargo': cargo})

    # Ordenar a equipe com o supervisor no topo
    nomes_equipe = sorted(nomes_equipe, key=lambda x: (x['cargo'] != 'Supervisor(a)', x['cargo'] != 'Encarregado(a)'))

    contexto = {'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name,
                'dados': dados, 'prof': prof, 'contato': contatos, 'mid': mid, 'equipe': nomes_equipe, 'pf': pf}

    if request.method == 'GET':
        return render(request, 'ccis/profile.html', contexto)


@login_required(login_url="/login")
def usuario(request):
    dp = modelFormDadosPessoais()
    data = datAT()

    totalUsuarios = len(profissional.objects.filter(situacao='Ativo'))
    totalColaborador = len(profissional.objects.filter(colaborador='Funcionário(a)', situacao='Ativo'))
    totalEstagiarios = len(profissional.objects.filter(colaborador='Estagiário(a)', situacao='Ativo'))
    totalMenor = len(profissional.objects.filter(colaborador='Menor Aprendiz', situacao='Ativo'))

    totalAnual = len(profissional.objects.filter(situacao='Ativo', admissao__lte='2022-12-31'))
    totalAtual = len(profissional.objects.filter(situacao='Ativo', admissao__gte='2023-01-01'))
    totalMaster = (totalAtual + totalAnual) * 100 / totalAnual - 100
    totalMaster = str(totalMaster)[0:4]

    anual_F = len(profissional.objects.filter(situacao='Ativo', colaborador='Funcionário(a)',
                                              admissao__lte='2022-12-31'))
    atual_F = len(profissional.objects.filter(situacao='Ativo', colaborador='Funcionário(a)',
                                              admissao__gte='2023-01-01'))
    total_F = (anual_F + atual_F) * 100 / anual_F - 100
    porcentagem_F = str(total_F)[0:4]

    anual_E = len(profissional.objects.filter(situacao='Ativo', colaborador='Estagiário(a)',
                                              admissao__lte='2022-12-31'))
    atual_E = len(profissional.objects.filter(situacao='Ativo', colaborador='Estagiário(a)',
                                              admissao__gte='2023-01-01'))
    total_E = (anual_E + atual_E) * 100 / anual_E - 100
    porcentagem_E = str(total_E)[0:4]

    anual_M = len(profissional.objects.filter(situacao='Ativo', colaborador='Menor Aprendiz',
                                              admissao__lte='2022-12-31'))
    atual_M = len(profissional.objects.filter(situacao='Ativo', colaborador='Menor Aprendiz',
                                              admissao__gte='2023-01-01'))
    total_M = (anual_M + atual_M) * 100 / anual_M - 100
    porcentagem_M = str(total_M)[0:4]

    dados = User.objects.select_related('dadosPessoais', 'profissional').values('dadosPessoais__nomeCompleto',
                                                                                'dadosPessoais__foto',
                                                                                'dadosPessoais__sexo',
                                                                                'profissional__cargo',
                                                                                'profissional__paUnidade',
                                                                                'profissional__situacao',
                                                                                'profissional__colaborador')

    dadosTable = []
    for item in dados:
        nomeCompleto = item['dadosPessoais__nomeCompleto']
        foto = item['dadosPessoais__foto']
        sexo = item['dadosPessoais__sexo']
        cargo = item['profissional__cargo']
        unidade = item['profissional__paUnidade']
        situacao = item['profissional__situacao']
        colaborador = item['profissional__colaborador']

        if nomeCompleto == None and foto == None and sexo == None:
            continue

        else:
            dadosTable.append({'nomeCompleto': nomeCompleto, 'foto': foto, 'sexo': sexo, 'cargo': cargo,
                               'unidade': unidade, 'situacao': situacao, 'colaborador': colaborador})

    form = UserCreationForm()
    dados_formset = inlineformset_factory(User, dadosPessoais, modelFormDadosPessoais, extra=1, can_delete=False)
    endereco_formset = inlineformset_factory(User, enderecoContato, modelFormEnderecoContato, extra=1,
                                             can_delete=False)
    dependentes_formset = inlineformset_factory(User, dependentes, modelFormDependentes, extra=1,
                                                can_delete=False)
    escolaridade_formset = inlineformset_factory(User, escolaridade, modelFormEscolaridade, extra=1,
                                                 can_delete=False)
    profissional_formset = inlineformset_factory(User, profissional, modelFormProfissional, extra=1,
                                                 can_delete=False)
    dadosBancarios_formset = inlineformset_factory(User, dadosBancarios, modelFormDadosBancarios, extra=1,
                                                   can_delete=False)
    outros_formset = inlineformset_factory(User, outros, ModelFormOutros, extra=1, can_delete=False)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        dados_form = dados_formset(request.POST)
        endereco_form = endereco_formset(request.POST)
        dependentes_form = dependentes_formset(request.POST)
        escolaridade_form = escolaridade_formset(request.POST)
        profissional_form = profissional_formset(request.POST)
        dadosBancarios_form = dadosBancarios_formset(request.POST)
        outros_form = outros_formset(request.POST)

        if form.is_valid() and dados_form.is_valid() and endereco_form.is_valid() and dependentes_form.is_valid() and \
                escolaridade_form.is_valid() and profissional_form.is_valid() and dadosBancarios_form.is_valid() and \
                outros_form.is_valid():
            novo_usuario = form.save()
            dados_form = dados_formset(request.POST, instance=novo_usuario)
            endereco_form = endereco_formset(request.POST, instance=novo_usuario)
            dependentes_form = dependentes_formset(request.POST, instance=novo_usuario)
            escolaridade_form = escolaridade_formset(request.POST, instance=novo_usuario)
            profissional_form = profissional_formset(request.POST, instance=novo_usuario)
            dadosBancarios_form = dadosBancarios_formset(request.POST, instance=novo_usuario)
            outros_form = outros_formset(request.POST, instance=novo_usuario)
            dados_form.save()
            endereco_form.save()
            dependentes_form.save()
            escolaridade_form.save()
            profissional_form.save()
            dadosBancarios_form.save()
            outros_form.save()

            return redirect('usuario')

    else:
        form = UserCreationForm()
        dados_form = dados_formset()
        endereco_form = endereco_formset()
        dependentes_form = dependentes_formset()
        escolaridade_form = escolaridade_formset()
        profissional_form = profissional_formset()
        dadosBancarios_form = dadosBancarios_formset()
        outros_form = outros_formset()

        user = request.user.username
        email = request.user.email
        first_name = request.user.first_name if request.user.first_name else 'Nome de Usuário'
        last_name = request.user.last_name if request.user.last_name else 'Sobre Nome do Usuário'
        dados = dadosPessoais.objects.get(usuario=request.user)

        context = {'dados': dados, 'username': user, 'email': email, 'first_name': first_name, 'last_name': last_name,
                   'form': dp, 'data': data, 'totalUsuarios': totalUsuarios, 'totalColaborador': totalColaborador,
                   'totalEstagiarios': totalEstagiarios, 'totalMenor': totalMenor, 'totalMaster': totalMaster,
                   'totalUsuariosAnual': totalAnual, 'porcentagem_F': porcentagem_F, 'AnualFuncionarios': anual_F,
                   'porcentagem_E': porcentagem_E, 'anualEstagiarios': anual_E, 'anualMenor': anual_M,
                   'porcentagem_M': porcentagem_M, 'user': form, 'dadosTable': dadosTable,
                   'dadosP': dados_form, 'usuario': usuario, 'end': endereco_form, 'dependentes_form': dependentes_form,
                   'escolaridade_form': escolaridade_form, 'profissional_form': profissional_form,
                   'dadosBancarios_form': dadosBancarios_form,
                   'outros_form': outros_form}

        return render(request, 'ccis/usuario.html', context)


@login_required(login_url="/login")
def conta(request):
    user = request.user.username
    email = request.user.email
    first_name = request.user.first_name if request.user.first_name else 'Nome de Usuário'
    last_name = request.user.last_name if request.user.last_name else 'Sobre Nome do Usuário'
    dados = dadosPessoais.objects.get(usuario=request.user)

    usuario = request.user
    pk_dados = dadosPessoais.objects.filter(usuario=usuario).first()
    pk_dependentes = dependentes.objects.filter(usuario=usuario).first()
    pk_contato = enderecoContato.objects.filter(usuario=usuario).first()
    pk_escolaridade = escolaridade.objects.filter(usuario=usuario).first()
    pk_certificacao = certificacao.objects.filter(usuario=usuario).first()
    pk_profi = profissional.objects.filter(usuario=usuario).first()
    pk_bancario = dadosBancarios.objects.filter(usuario=usuario).first()
    pk_outros = outros.objects.filter(usuario=usuario).first()

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

    context = {'dados': dados, 'username': user, 'email': email, 'first_name': first_name, 'last_name': last_name,
               'form': dp, 'dependentes': de, 'contatoEndereco': conEnd, 'escolaridade': esc, 'certificacao': cert,
               'profissional': prof, 'dadosBancarios': db, 'outros': out, 'midia': mid, 'data': data}

    if request.method == 'GET':
        return render(request, 'ccis/conta.html', context)

    if request.method == 'POST':
        form = modelFormDadosPessoais(request.POST, instance=pk_dados)

        if form.is_valid():
            form.save()
            return redirect('conta')

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Dados Pessoais'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')


@login_required(login_url="/login")
def documentos(request):
    user = request.user.username
    email = request.user.email
    first_name = request.user.first_name if request.user.first_name else 'Nome de Usuário'
    last_name = request.user.last_name if request.user.last_name else 'Sobre Nome do Usuário'
    dados = dadosPessoais.objects.get(usuario=request.user)

    usuario = request.user
    doc = docRg.objects.filter(usuario=usuario).first()
    doc_cnh = docCnh.objects.filter(usuario=usuario).first()
    doc_cpf = docCpf.objects.filter(usuario=usuario).first()
    doc_reservista = docReservista.objects.filter(usuario=usuario).first()
    doc_titulo = docTitulo.objects.filter(usuario=usuario).first()
    doc_clt = docClt.objects.filter(usuario=usuario).first()
    doc_residencia = docResidencia.objects.filter(usuario=usuario).first()
    doc_certidao = docCertidao.objects.filter(usuario=usuario).first()
    doc_admissional = docAdmissional.objects.filter(usuario=usuario).first()
    doc_periodico = docPeriodico.objects.filter(usuario=usuario).first()

    status = 'Concluído' if doc != None else 'Pendente'
    statusCnh = 'Concluído' if doc_cnh != None else 'Pendente'
    statusCpf = 'Concluído' if doc_cpf != None else 'Pendente'
    statusReservista = 'Concluído' if doc_reservista != None else 'Pendente'
    statusTitulo = 'Concluído' if doc_titulo != None else 'Pendente'
    statusClt = 'Concluído' if doc_clt != None else 'Pendente'
    statusCertidao = 'Concluído' if doc_certidao != None else 'Pendente'
    statusAdmissional = 'Concluído' if doc_admissional != None else 'Pendente'

    if doc_residencia != None:
        statusResidencia = 'Concluído'
        if doc_residencia.dataAtualizacao + relativedelta(years=1) < timezone.now().date():
            statusResidencia = 'Expirado'
    else:
        statusResidencia = 'Pendente'

    if doc_periodico != None:
        statusPeriodico = 'Concluído'
        if doc_periodico.dataAtualizacao + relativedelta(years=2) < timezone.now().date():
            statusPeriodico = 'Expirado'
    else:
        statusPeriodico = 'Pendente'

    if request.method == 'GET':
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

        context = {
            'form': form, 'cnh_form': cnh_form, 'cpf_form': cpf_form, 'reservista_form': reservista_form,
            'titulo_form': titulo_form, 'clt_form': clt_form, 'residencia_form': residencia_form,
            'certidao_form': certidao_form, 'admissional_form': admissional_form, 'periodico_form': periodico_form,
            'doc': doc, 'doc_cnh': doc_cnh, 'doc_cpf': doc_cpf, 'doc_reservista': doc_reservista,
            'doc_titulo': doc_titulo,
            'doc_clt': doc_clt, 'doc_residencia': doc_residencia, 'doc_certidao': doc_certidao,
            'doc_admissional': doc_admissional,
            'doc_periodico': doc_periodico, 'status': status, 'statusCnh': statusCnh, 'statusCpf': statusCpf,
            'statusReservista': statusReservista, 'statusTitulo': statusTitulo, 'statusClt': statusClt,
            'statusResidencia': statusResidencia, 'statusCertidao': statusCertidao,
            'statusAdmissional': statusAdmissional,
            'statusPeriodico': statusPeriodico, 'dados': dados, 'username': user, 'email': email,
            'first_name': first_name,
            'last_name': last_name,
        }

        return render(request, 'ccis/documentos.html', context)


@login_required(login_url="/login")
def cursos(request):
    if request.method == 'POST':
        curso_form = modelFormCurso(request.POST, request.FILES)
        if curso_form.is_valid():
            obj = curso_form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            curso_form.save()
        return HttpResponse('Salvo')
    else:
        curso_form = modelFormCurso(request.POST, request.FILES)
    return render(request, 'ccis/cursos.html', {'curso_form': curso_form})


# ----------------------------------------------------------------------------------------------------------------------


# RECEBER OS DADOS PESSOAIS DO USUÁRIO ---------------------------------------------------------------------------------
@login_required(login_url="/login")
def formDep(request):
    user = request.user
    if request.method == 'POST':
        pk = dependentes.objects.filter(usuario=user).first()
        form = modelFormDependentes(request.POST, instance=pk)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('conta')

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Dependentes'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')

    else:
        return HttpResponse('não deu certo')


@login_required(login_url="/login")
def formEnd(request):
    user = request.user
    if request.method == 'POST':
        pk = enderecoContato.objects.filter(usuario=user).first()
        form = modelFormEnderecoContato(request.POST, instance=pk)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('conta')

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Endereço e Contatos'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')

    else:
        return HttpResponse('não deu certo')


@login_required(login_url="/login")
def formEsc(request):
    if request.method == 'POST':
        curso_esc = modelFormEscolaridade(request.POST, request.FILES)
        if curso_esc.is_valid():
            obj = curso_esc.save(commit=False)
            obj.usuario = request.user
            obj.save()
            curso_esc.save()
            return redirect('conta')

        else:
            print('deu erro')
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Escolaridade'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')

    else:
        return HttpResponse('não deu certo')


@login_required(login_url="/login")
def formCert(request):
    if request.method == 'POST':
        curso_esc = modelFormCertificacao(request.POST, request.FILES)

        if curso_esc.is_valid():
            obj = curso_esc.save(commit=False)
            obj.usuario = request.user
            obj.save()
            curso_esc.save()
            return redirect('conta')


        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Certificação'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')

    else:
        return HttpResponse('não deu certo')


@login_required(login_url="/login")
def formProf(request):
    user = request.user
    if request.method == 'POST':
        pk = profissional.objects.filter(usuario=user).first()
        form = modelFormProfissional(request.POST, instance=pk)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('conta')

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Profissional'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')

    else:
        return HttpResponse('não deu certo')


@login_required(login_url="/login")
def formBanc(request):
    user = request.user
    if request.method == 'POST':
        pk = dadosBancarios.objects.filter(usuario=user).first()
        form = modelFormDadosBancarios(request.POST, instance=pk)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('conta')

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Dados Bancários'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')

    else:
        return HttpResponse('não deu certo')


@login_required(login_url="/login")
def formOut(request):
    user = request.user
    if request.method == 'POST':
        pk = outros.objects.filter(usuario=user).first()
        form = ModelFormOutros(request.POST, instance=pk)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('conta')

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Outros'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')

    else:
        return HttpResponse('não deu certo')


@login_required(login_url="/login")
def formMidia(request):
    user = request.user
    if request.method == 'POST':
        pk_dados = dadosPessoais.objects.get(usuario=user)
        form = ModelFormMidia(request.POST, request.FILES, instance=pk_dados)

        if form.is_valid():
            form.save()
            return redirect('profile')

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('profile')


# -----------------------------------------------------------------------------------------------------------------------


# PROCESSAMENTO DE DOCUMENTOS -------------------------------------------------------------------------------------------
@login_required(login_url="/login")
def rg(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docRg.objects.filter(usuario=usuario).first()
        form = modelFormRg(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def cnh(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docCnh.objects.filter(usuario=usuario).first()
        form = modelFormCnh(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def cpf(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docCpf.objects.filter(usuario=usuario).first()
        form = modelFormCpf(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def reservista(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docReservista.objects.filter(usuario=usuario).first()
        form = modelFormReservista(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def titulo(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docTitulo.objects.filter(usuario=usuario).first()
        form = modelFormTitulo(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def clt(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docClt.objects.filter(usuario=usuario).first()
        form = modelFormClt(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def residencia(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docResidencia.objects.filter(usuario=usuario).first()
        form = modelFormResidencia(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def certidao(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docCertidao.objects.filter(usuario=usuario).first()
        form = modelFormCertidao(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def admissional(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docAdmissional.objects.filter(usuario=usuario).first()
        form = modelFormAdmissional(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


@login_required(login_url="/login")
def periodico(request):
    usuario = request.user

    if request.method == 'POST':
        doc = docPeriodico.objects.filter(usuario=usuario).first()
        form = modelFormPeriodico(request.POST, request.FILES, instance=doc)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            form.save()
            return redirect('documentos')

        return render(request, 'ccis/documentos.html')


# -----------------------------------------------------------------------------------------------------------------------


def dev(request):
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name if request.user.first_name else 'Nome de Usuário'
    last_name = request.user.last_name if request.user.last_name else 'Sobre Nome do Usuário'

    dados = dadosPessoais.objects.get(usuario=request.user)
    prof = profissional.objects.get(usuario=request.user)
    contatos = enderecoContato.objects.get(usuario=request.user)

    mid = ModelFormMidia(instance=dados)

    superior = profissional.objects.get(usuario=request.user, situacao='Ativo').superiorImediato
    equipe = User.objects.filter(profissional__superiorImediato=superior).select_related('dadosPessoais',
                                                                                         'profissional') \
        .values('first_name', 'last_name', 'dadosPessoais__nomeCompleto', 'dadosPessoais__foto', 'dadosPessoais__sexo',
                'profissional__cargo')

    chefe = dadosPessoais.objects.get(nomeCompleto=superior).usuario
    dd = User.objects.filter(username=chefe).select_related('dadosPessoais, profissional').values \
        ('first_name', 'last_name', 'dadosPessoais__nomeCompleto', 'dadosPessoais__foto',
         'dadosPessoais__sexo', 'profissional__cargo')

    dados_chefe = []
    for d in dd:
        first_name = d['first_name']
        last_name = d['last_name']
        sexo = d['dadosPessoais__sexo']
        foto = d['dadosPessoais__foto']
        cargo = d['profissional__cargo']

        dados_chefe.append(
            {'sexo': sexo, 'foto': foto, 'first_name': first_name, 'last_name': last_name, 'cargo': cargo})

    nomes_equipe = []
    for usuario in equipe:
        first_name = usuario['first_name']
        last_name = usuario['last_name']
        sexo = usuario['dadosPessoais__sexo']
        foto = usuario['dadosPessoais__foto']
        cargo = usuario['profissional__cargo']

        nomes_equipe.append(
            {'foto': foto, 'first_name': first_name, 'last_name': last_name, 'sexo': sexo, 'cargo': cargo})

    contexto = {'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name,
                'dados': dados, 'prof': prof, 'contato': contatos, 'mid': mid, 'equipe': nomes_equipe,
                'chefe': dados_chefe}

    if request.method == 'GET':
        return render(request, 'ccis/dev.html', contexto)
