import requests

from django.utils import timezone
from dateutil.relativedelta import relativedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.models import User, Group

from .. models import dadosPessoais, dependentes, enderecoContato, outros, escolaridade, certificacao, \
    dadosBancarios, docRg, docCnh, docCpf, docReservista, docTitulo, docClt, docResidencia, \
    docCertidao, docAdmissional, docPeriodico, docCursos, profissional, setor

from .. forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios, \
    modelFormRg, modelFormCnh, modelFormCpf, modelFormReservista, modelFormTitulo, modelFormClt, modelFormSetor, \
    modelFormResidencia, modelFormCertidao, modelFormAdmissional, modelFormPeriodico, modelFormCurso, \
    CustomUserCreationForm


# PAGINAS --------------------------------------------------------------------------------------------------------------
def infoClima():
    API_KEY = '65ea38b72e0784b11d03334985c5fac7'

    cidade_city = "brasília"

    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade_city}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requesicao_dic = requisicao.json()

    descricao = requesicao_dic['weather'][0]['description']
    temperatura = requesicao_dic['main']['temp'] - 273.15
    umidade = requesicao_dic['main']['humidity']
    minima = requesicao_dic['main']['temp_min'] - 273.15
    maxima = requesicao_dic['main']['temp_max'] - 273.15
    cidade = requesicao_dic['name']

    clima = {'descricao': descricao, 'temperatura': temperatura, 'umidade': umidade, 'minima': minima,
             'maxima': maxima, 'cidade': cidade}

    return clima


def base(request):

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    dados = dadosPessoais.objects.get(usuario=log)

    groupControle = log.groups.filter(id=28).exists()

    context = {
        'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
        'dados': dados, 'is_superadmin': is_superadmin, 'groupControle': groupControle,
        }

    return render(request, 'ccis/base.html', context)


def home(request):
    context = infoClima()
    return render(request, 'ccis/home.html', context)


@login_required(login_url="/login")
def new_login_page(request):
    if request.method == 'POST':

        first_name = request.POST.get('first-name').capitalize()
        last_name = request.POST.get('last-name').capitalize()

        # Obter o objeto User atual
        user = request.user

        print(first_name, last_name, user)

        # Atualizar os campos first_name e last_name do User
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        nova_senha = request.POST['Senha']
        user = request.user
        user.set_password(nova_senha)
        user.save()
        return redirect('profile', user_id=request.user.id)

    else:
        return render(request, 'ccis/new_login_page.html')


@login_required(login_url="/login")
def solicitacao(request):
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto

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
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto

    first_name = user.first_name if user.first_name else 'Não informado'
    last_name = user.last_name if user.last_name else ''

    dados = dadosPessoais.objects.filter(usuario=user).first()
    prof = profissional.objects.filter(usuario=user).first()
    contatos = enderecoContato.objects.filter(usuario=user).first()
    depen = dependentes.objects.filter(usuario=user).first()
    end = enderecoContato.objects.filter(usuario=user).first()
    esc = escolaridade.objects.filter(usuario=user).first()
    cert = certificacao.objects.filter(usuario=user).first()
    profi = profissional.objects.filter(usuario=user).first()
    db = dadosBancarios.objects.filter(usuario=user).first()
    out = outros.objects.filter(usuario=user).first()

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

    porcentagem_total = (
                                porcentagem_dados_pessoais + porcentagem_dados_dependentes + porcentagem_end + porcentagem_esc +
                                porcentagem_cert + porcentagem_profi + porcentagem_db + porcentagem_out + porcentagem_mid) / 9

    pf = str(round(porcentagem_total, 2))

    certiAn = certificacao.objects.filter(usuario=user)

    superior = Group.objects.filter(user=user).first()

    nomes_equipe = []
    if superior is None:
        pass

    else:
        equipe = User.objects.filter(groups=superior)
        # Resto do código
        for usuario in equipe:
            first_nameA = usuario.first_name
            last_nameA = usuario.last_name
            sexo = usuario.dadosPessoais.sexo
            foto = usuario.dadosPessoais.foto
            cargo = usuario.profissional.first().cargo if usuario.profissional.first() else 'Não informado'
            nomes_equipe.append(
                {'id': usuario.id,
                 'foto': foto,
                 'first_name': first_nameA,
                 'last_name': last_nameA,
                 'sexo': sexo,
                 'cargo': cargo})

        # Ordenar a equipe com o supervisor no topo
        nomes_equipe = sorted(nomes_equipe, key=lambda x: (x['cargo'] != 'Supervisor(a)', x['cargo'] != 'Gerente de PA',
                                                           x['cargo'] != 'Encarregado(a)'))

    escola = modelFormEscolaridade()
    certific = modelFormCertificacao()

    dados_cert = certificacao.objects.filter(usuario=user)

    log = request.user
    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()
    is_superadmin = log.is_superuser

    dadosCards_cert = []
    for item in dados_cert:
        nome = item.nome
        instituicao = item.organizacaoEmissora
        conclusao = item.dataEmissao

        dadosCards_cert.append({
            'id': log_id,
            'nome': nome,
            'instituicao': instituicao,
            'conclusao': conclusao,
        })

    dados_esc = escolaridade.objects.filter(usuario=user)

    dadosCards_esc = []
    for item in dados_esc:
        entidade = item.entidadeDeEnsino
        curso = item.curso
        graduacao = item.grau
        inicio = item.dataInicio
        conclusao = item.dataConclusao

        dadosCards_esc.append({
            'id': log_id,
            'entidade': entidade,
            'curso': curso,
            'graduacao': graduacao,
            'inicio': inicio,
            'conclusao': conclusao,
        })

    contexto = {'user': user_id, 'first_name': first_name, 'last_name': last_name, 'logName': logName,
                'logLast': logLast,
                'log_id': log_id, 'logFoto': logFoto, 'dados': dados, 'prof': prof, 'contato': contatos, 'mid': mid,
                'equipe': nomes_equipe, 'pf': pf, 'cert': certiAn, 'escolaridade': escola, 'certificacao': certific,
                'dadosCards_cert': dadosCards_cert, 'dadosCards_esc': dadosCards_esc, 'User': request.user,
                'is_superadmin': is_superadmin, 'group_gestao': group_gestao, 'groupControle': groupControle}

    if request.method == 'GET':
        return render(request, 'ccis/profile.html', contexto)


@login_required(login_url="/login")
def usuario(request):
    dados_formset = inlineformset_factory(User, dadosPessoais, modelFormDadosPessoais, extra=1, can_delete=False)
    endereco_formset = inlineformset_factory(User, enderecoContato, modelFormEnderecoContato, extra=1,
                                             can_delete=False)
    dependentes_formset = inlineformset_factory(User, dependentes, modelFormDependentes, extra=1,
                                                can_delete=False)
    profissional_formset = inlineformset_factory(User, profissional, modelFormProfissional, extra=1,
                                                 can_delete=False)
    dadosBancarios_formset = inlineformset_factory(User, dadosBancarios, modelFormDadosBancarios, extra=1,
                                                   can_delete=False)
    outros_formset = inlineformset_factory(User, outros, ModelFormOutros, extra=1, can_delete=False)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None)
        dados_form = dados_formset(request.POST)
        endereco_form = endereco_formset(request.POST)
        dependentes_form = dependentes_formset(request.POST)
        profissional_form = profissional_formset(request.POST)
        dadosBancarios_form = dadosBancarios_formset(request.POST)
        outros_form = outros_formset(request.POST)

        if form.is_valid() and dados_form.is_valid() and endereco_form.is_valid() and dependentes_form.is_valid() and \
                profissional_form.is_valid() and dadosBancarios_form.is_valid() and outros_form.is_valid():

            novo_usuario = form.save()
            grupo_selecionado = form.cleaned_data['group']
            novo_usuario.groups.set([grupo_selecionado])
            novo_usuario.save()

            dados_form = dados_formset(request.POST, instance=novo_usuario)
            endereco_form = endereco_formset(request.POST, instance=novo_usuario)
            dependentes_form = dependentes_formset(request.POST, instance=novo_usuario)
            profissional_form = profissional_formset(request.POST, instance=novo_usuario)
            dadosBancarios_form = dadosBancarios_formset(request.POST, instance=novo_usuario)
            outros_form = outros_formset(request.POST, instance=novo_usuario)

            dados_form.save()
            endereco_form.save()
            dependentes_form.save()
            profissional_form.save()
            dadosBancarios_form.save()
            outros_form.save()

            return redirect('usuario')

        else:

            messages.error(request, 'Ocorreu um erro no formulário. Verifique os campos.')
            return HttpResponse('Não passou na validação')

    else:
        dp = modelFormDadosPessoais()

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

        dados = User.objects.prefetch_related('dadosPessoais', 'profissional') \
            .values('id', 'dadosPessoais__nomeCompleto', 'dadosPessoais__foto', 'dadosPessoais__sexo',
                    'profissional__cargo', 'profissional__paUnidade', 'profissional__situacao',
                    'profissional__colaborador')

        dadosTable = []
        for item in dados:
            id = item['id']
            nomeCompleto = item['dadosPessoais__nomeCompleto']
            foto = item['dadosPessoais__foto']
            sexo = item['dadosPessoais__sexo']
            cargo = item['profissional__cargo']
            unidade = item['profissional__paUnidade']
            situacao = item['profissional__situacao']
            colaborador = item['profissional__colaborador']

            if nomeCompleto == None and foto == None and sexo == None:
                continue

            dadosTable.append({
                'id': id,
                'nomeCompleto': nomeCompleto,
                'foto': foto,
                'sexo': sexo,
                'cargo': cargo,
                'unidade': unidade,
                'situacao': situacao,
                'colaborador': colaborador,
            })

        form = CustomUserCreationForm()
        dados_form = dados_formset()
        endereco_form = endereco_formset()
        dependentes_form = dependentes_formset()
        profissional_form = profissional_formset()
        dadosBancarios_form = dadosBancarios_formset()
        outros_form = outros_formset()

        log = request.user
        log_id = request.user.id
        logName = request.user.first_name
        logLast = request.user.last_name
        logFoto = dadosPessoais.objects.get(usuario=request.user).foto
        group_gestao = log.groups.filter(id=3).exists()
        groupControle = log.groups.filter(id=28).exists()
        is_superadmin = log.is_superuser

        context = {'dados': dados, 'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
                   'form': dp, 'totalUsuarios': totalUsuarios, 'totalColaborador': totalColaborador,
                   'totalEstagiarios': totalEstagiarios, 'totalMenor': totalMenor, 'totalMaster': totalMaster,
                   'totalUsuariosAnual': totalAnual, 'porcentagem_F': porcentagem_F, 'AnualFuncionarios': anual_F,
                   'porcentagem_E': porcentagem_E, 'anualEstagiarios': anual_E, 'anualMenor': anual_M,
                   'porcentagem_M': porcentagem_M, 'userCreation': form, 'dadosTable': dadosTable,
                   'dadosP': dados_form, 'usuario': usuario, 'end': endereco_form, 'dependentes_form': dependentes_form,
                   'profissional_form': profissional_form, 'dadosBancarios_form': dadosBancarios_form,
                   'user': request.user, 'outros_form': outros_form, 'group_gestao': group_gestao, 'groupControle':groupControle,
                   'is_superadmin': is_superadmin}

        return render(request, 'rh/usuario.html', context)


@login_required(login_url="/login")
def conta(request):
    # user = get_object_or_404(User, id=user_id)
    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    pk_dados = dadosPessoais.objects.filter(usuario=user).first()
    pk_dependentes = dependentes.objects.filter(usuario=user).first()
    pk_contato = enderecoContato.objects.filter(usuario=user).first()
    pk_profi = profissional.objects.filter(usuario=user).first()
    pk_bancario = dadosBancarios.objects.filter(usuario=user).first()
    pk_outros = outros.objects.filter(usuario=user).first()

    dp = modelFormDadosPessoais(instance=pk_dados)
    de = modelFormDependentes(instance=pk_dependentes)
    conEnd = modelFormEnderecoContato(instance=pk_contato)
    prof = modelFormProfissional(instance=pk_profi)
    db = modelFormDadosBancarios(instance=pk_bancario)
    out = ModelFormOutros(instance=pk_outros)
    mid = ModelFormMidia(instance=pk_dados)

    context = {'dados': dados, 'first_name': first_name, 'last_name': last_name,
               'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
               'form': dp, 'dependentes': de, 'contatoEndereco': conEnd, 'group_gestao': group_gestao,
               'is_superadmin': is_superadmin, 'groupControle':groupControle,
               'profissional': prof, 'dadosBancarios': db, 'outros': out, 'midia': mid}

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
            return redirect('conta', user_id=request.user.id)


@login_required(login_url="/login")
def documentos(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    doc = docRg.objects.filter(usuario=user).first()
    doc_cnh = docCnh.objects.filter(usuario=user).first()
    doc_cpf = docCpf.objects.filter(usuario=user).first()
    doc_reservista = docReservista.objects.filter(usuario=user).first()
    doc_titulo = docTitulo.objects.filter(usuario=user).first()
    doc_clt = docClt.objects.filter(usuario=user).first()
    doc_residencia = docResidencia.objects.filter(usuario=user).first()
    doc_certidao = docCertidao.objects.filter(usuario=user).first()
    doc_admissional = docAdmissional.objects.filter(usuario=user).first()
    doc_periodico = docPeriodico.objects.filter(usuario=user).first()

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
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
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
            'statusPeriodico': statusPeriodico, 'dados': dados, 'username': user, 'first_name': first_name,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin, 'groupControle': groupControle
        }

        return render(request, 'ccis/documentos.html', context)


@login_required(login_url="/login")
def departamentos(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    if request.method == 'GET':
        context = {
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
        }

        return render(request, 'ccis/departamentos.html', context)


def utilitarios(request):
    context = infoClima()
    return render(request, 'ccis/utilitarios.html', context)


@login_required(login_url="/login")
def gestaoMetas(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user

    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser

    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    if request.method == 'GET':
        context = {
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle':groupControle,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
        }

        return render(request, 'ccis/gestaoMetas.html', context)


def dev(request):
    pass

# ----------------------------------------------------------------------------------------------------------------------
