import json

import requests
from rest_framework import status, generics, permissions
from django.db.models import Prefetch
from dateutil.parser import parse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from reportlab.pdfgen import canvas
from io import BytesIO

from ..serializers import CardSerializer, CardSetorHistorySerializer, MessageHistorySerializer
from django.http import JsonResponse, HttpResponseNotFound
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.models import User, Group
from collections import defaultdict

from ..models import dadosPessoais, dependentes, enderecoContato, outros, escolaridade, certificacao, \
    dadosBancarios, profissional, Card, CardSetorHistory, MessageHistory, OperatorRating, Notification, SectorButtons, \
    CustomGroupInfo, Cupons

from ..forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios, \
    CustomUserCreationForm, modelFormClock


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
    return render(request, 'ccis/base.html')


def home(request):
    context = infoClima()
    return render(request, 'ccis/home.html', context)


@login_required(login_url="/login")
def ccc(request):
    return render(request, "ccis/ccc.html")


def processa_cupons(request):
    cpf = request.GET.get('cpf')
    cupons = None

    if cpf:
        cupons = Cupons.objects.filter(cpf=cpf)
        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        p.drawString(100, 750, "Cooperar+ - Campanha de Capital Colaboradores")
        p.drawString(100, 700, f"Cupons para o CPF: {cpf}")

        if cupons:
            y_position = 650
            for cupom in cupons:
                p.drawString(100, y_position, f"Cupom: {cupom.numero_cupom}")
                y_position -= 20

        p.showPage()
        p.save()

        buffer.seek(0)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="cupons_{cpf}.pdf'
        response.write(buffer.read())

        return response  # Retorna o PDF como resposta

    context = {
        'cupons': cupons
    }

    return render(request, 'index.html', context)


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
        dadosPessoais = modelFormDadosPessoais()
        enderecoContato = modelFormEnderecoContato()
        profissional = modelFormProfissional()

        context={'dadosPessoais': dadosPessoais,
                 'enderecoContato': enderecoContato,
                 'profissional': profissional}

        return render(request, 'ccis/new_login_page.html', context)


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
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

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

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()
    is_superadmin = user.is_superuser

    dadosCards_cert = []
    for item in dados_cert:
        nome = item.nome
        instituicao = item.organizacaoEmissora
        conclusao = item.dataEmissao

        dadosCards_cert.append({
            'id': user_id,
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
            'id': user_id,
            'entidade': entidade,
            'curso': curso,
            'graduacao': graduacao,
            'inicio': inicio,
            'conclusao': conclusao,
        })

    contexto = {'user': user_id, 'first_name': first_name, 'last_name': last_name,
                 'dados': dados, 'prof': prof, 'contato': contatos, 'mid': mid,
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
                   'user': request.user, 'outros_form': outros_form, 'group_gestao': group_gestao,
                   'groupControle': groupControle,
                   'is_superadmin': is_superadmin}

        return render(request, 'rh/usuario.html', context)


@login_required(login_url="/login")
def conta(request):
    # user = get_object_or_404(User, id=user_id)
    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

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
               'form': dp, 'dependentes': de, 'contatoEndereco': conEnd, 'group_gestao': group_gestao,
                'groupControle': groupControle,
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
def departamentos(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    if request.method == 'GET':
        context = {
            'dados': dados, 'username': user, 'first_name': first_name, 'last_name': last_name,
        }

        return render(request, 'ccis/departamentos.html', context)


@login_required(login_url="/login")
def utilitariosCopy(request):
    # user = get_object_or_404(User, id=user_id)

    user = request.user

    group_gestao = user.groups.filter(id=3).exists()
    groupControle = user.groups.filter(id=28).exists()

    first_name = user.first_name
    last_name = user.last_name

    dados = dadosPessoais.objects.get(usuario=user)

    if request.method == 'GET':
        context = {
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
            'last_name': last_name, 'group_gestao': group_gestao,
        }

        return render(request, 'ccis/utilitariosCopy.html', context)


@login_required(login_url="/login")
def malotes(request):
    return render(request, 'ccis/malotes.html')


def utilitariosHome(request):
    return render(request, 'ccis/utilitariosHome.html')


def dev(request):

    superior = Group.objects.filter(id=2).first()

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

    if request.method == 'GET':
        sector_buttons = SectorButtons.objects.filter(group=2)

        print(sector_buttons)

        context = {
            'sector_buttons': sector_buttons,'superior': superior, 'equipe': nomes_equipe,
        }


        return render(request, 'ccis/dev.html', context)


@login_required(login_url="/login")
def processos_user(request):

    if request.method == 'GET':
        cards = Card.objects.all().prefetch_related(Prefetch('cardsetorhistory_set',
            queryset=CardSetorHistory.objects.order_by('-data_hora'))
        )

        usuarios = User.objects.all()
        solicitante = request.user.id

        status_counts = defaultdict(int)

        for card in cards:
            cardsetorhistory = card.cardsetorhistory_set.first()
            if card and card.solicitante.id == solicitante and cardsetorhistory:
                status_atual = cardsetorhistory.status_atual
                status_counts[status_atual] += 1

        card_count_triagem = status_counts["Triagem"]
        card_count_atendimento = status_counts["Em Atendimento"]
        card_count_encaminhado = status_counts["Encaminhado"]
        card_count_concluido = status_counts["Concluido"]
        card_count_finalizado = status_counts["Finalizado"]

        context = {
            'cards': cards,
            'usuarios': usuarios,
            'solicitante': solicitante,
            'card_count_triagem': card_count_triagem,
            'card_count_atendimento': card_count_atendimento,
            'card_count_encaminhado': card_count_encaminhado,
            'card_count_concluido': card_count_concluido,
            'card_count_finalizado': card_count_finalizado,
        }

        return render(request, 'ccis/processo_user.html', context)


@login_required(login_url="/login")
def kanban_view(request):
    usuarios = User.objects.all()
    group = Group.objects.all()
    clock = modelFormClock()

    try:
        id_setor = request.user.groups.first().id
        group_info = CustomGroupInfo.objects.get(group_id=id_setor)

        superior = Group.objects.filter(id=id_setor).first()

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
            nomes_equipe = sorted(nomes_equipe,
                                  key=lambda x: (x['cargo'] != 'Supervisor(a)', x['cargo'] != 'Gerente de PA',
                                                 x['cargo'] != 'Encarregado(a)'))

            context = {
                'clock': clock,
                'superior': superior,
                'equipe': nomes_equipe,
                'group_info': group_info,
                'usuarios': usuarios,
                'group': group
            }

            return render(request, 'ccis/kanban.html', context)


    except AttributeError:
        return HttpResponseNotFound('O usuário não esta logado ou não pertence a nenhum setor.')









@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def card_list_view(request):
    # Obtém o ID do usuário logado
    user_id = request.user.id

    # Obtém a opção da solicitação (processos ou minhas_solicitacoes)
    option = request.query_params.get('option', None)

    # Lógica para filtrar os cards com base na opção
    if option == 'processos':
        # Filtra os cards relacionados ao setor do usuário
        queryset = Card.objects.filter(setor__user=user_id)
    elif option == 'minhas_solicitacoes':
        # Filtra os cards criados pelo próprio usuário
        queryset = Card.objects.filter(solicitante__id=user_id)
    else:
        # Lógica adicional conforme necessário
        queryset = Card.objects.all()

    serializer = CardSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def card_detail_view(request, pk):

    try:
        card = Card.objects.get(pk=pk)

    except Card.DoesNotExist:
        return Response(status=404)

    serializer = CardSerializer(card)
    return Response(serializer.data)









@api_view(['GET'])
@login_required(login_url="/login")
def card_kanban_api(request):
    # Recuperar o setor do usuário logado
    user_setor = request.user.groups.first()

    # Filtrar os cards com base no setor do usuário
    cards = Card.objects.filter(setor=user_setor)

    # Serializar os dados dos cards
    serializer = CardSerializer(cards, many=True)

    # Organizar os cards por status
    kanban_data = {
        'Triagem': [],
        'Em Atendimento': [],
        'Encaminhado': [],
        'Concluido': [],
        'Finalizado': [],
    }

    for card in serializer.data:
        card_status = card['status']
        card['dataCriacao'] = parse(card['dataCriacao']).replace(tzinfo=None)

        # Adiciona o setor do usuário aos dados do card
        card['user_setor'] = str(user_setor)

        kanban_data[card_status].append(card)

    return Response(kanban_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required(login_url="/login")
def user_card_kanban_api(request):
    # Recuperar os cards abertos pelo usuário logado
    user_cards = Card.objects.filter(solicitante=request.user)

    # Serializar os dados dos cards
    serializer = CardSerializer(user_cards, many=True)

    # Organizar os cards por status
    kanban_data = {
        'Triagem': [],
        'Em Atendimento': [],
        'Encaminhado': [],
        'Concluido': [],
        'Finalizado': [],
    }

    for card in serializer.data:
        card_status = card['status']
        card['dataCriacao'] = parse(card['dataCriacao']).replace(tzinfo=None)
        kanban_data[card_status].append(card)

    return Response(kanban_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def card_detl(request, card_id):
    card = get_object_or_404(Card, idCard=card_id)

    # Busque o histórico de status para o card específico
    card_history = CardSetorHistory.objects.filter(card=card).order_by('data_hora')
    history_serializer = CardSetorHistorySerializer(card_history, many=True)

    # Serialize o card e o histórico de status
    card_serializer = CardSerializer(card)

    # Crie um dicionário que inclua os dados do card e o histórico de status
    response_data = {
        'card': card_serializer.data,
        'history': history_serializer.data,
    }

    return Response(response_data)


@api_view(['POST'])
def enviar_resposta(request, card_id):

    if request.method == 'POST':
        card = get_object_or_404(Card, idCard=card_id)
        descricao = request.data.get('resposta')
        attachment = request.data.get('attachment')
        remetente = request.user

        message_history = MessageHistory(
            card=card,
            remetente=remetente,
            message=descricao,
            attachment=attachment,
        )
        message_history.save()

        # Obtenha o histórico de setor mais recente para o cartão
        historico_setor = CardSetorHistory.objects.filter(card=card).latest('data_hora')

        # Obtenha o grupo associado ao histórico de setor
        grupo_setor = historico_setor.setor

        # Obtenha a URL do setor com base no grupo do responsável
        setor_link = CustomGroupInfo.objects.get(group=grupo_setor).url

        if card.responsavel is None:
            # Se o responsável não existe, envie a mensagem para todos os membros do grupo
            recipients = User.objects.filter(groups=grupo_setor)
            for recipient in recipients:
                if recipient != request.user:
                    notification = Notification(
                        author=request.user,
                        description="Você tem uma nova mensagem",
                        subject=card.assunto + f" N°: {card.idCard}",
                        recipient=recipient,
                        url=setor_link,
                    )
                    notification.save()

        elif card.responsavel == request.user:
            # Se o remetente é o próprio responsável, envie a mensagem para o solicitante
            notification = Notification(
                author=request.user,
                description="Você tem uma nova mensagem",
                subject=card.assunto + f" N°: {card.idCard}",
                recipient=card.solicitante,
                url='processos_user',  # Defina a URL apropriada
            )
            notification.save()
        else:
            # Se o remetente não é o responsável, envie a mensagem para o responsável
            notification = Notification(
                author=request.user,
                description="Você tem uma nova mensagem",
                subject=card.assunto + f" N°: {card.idCard}",
                recipient=card.responsavel,
                url=setor_link,
            )
            notification.save()

        data = {'status': 'Mensagem adicionada com sucesso'}
        return JsonResponse(data)


@api_view(['GET'])
def get_messages(request, card_id):
    messages = MessageHistory.objects.filter(card__idCard=card_id)
    message_serializer = MessageHistorySerializer(messages, many=True)

    return Response(message_serializer.data)


@login_required(login_url="/login")
def registrar_atendimento(request, card_id):
    card = get_object_or_404(Card, idCard=card_id)

    card.status = 'Em Atendimento'
    card.setor = request.user.groups.first()
    card.responsavel = request.user
    card.save()

    groups = request.user.groups.all()
    if groups:
        setor_atual = groups[0]  # Se o usuário estiver em apenas um grupo
    else:
        setor_atual = None

    historico = CardSetorHistory.objects.filter(card=card).order_by('-data_hora').last()

    # Registre o histórico de movimentação
    card_setor_history = CardSetorHistory(
        setor_id=setor_atual.id,
        card_id=card_id,
        status_anterior=historico.status_atual,
        status_atual="Em Atendimento",
        setor_anterior=historico.setor_atual,
        setor_atual=setor_atual.name,
        operador=request.user
    )

    card_setor_history.save()

    # Crie uma notificação para informar o usuário do atendimento registrado
    notification = Notification(
        author=request.user,
        description=f"Sua solicitação esta em Atendimento por {request.user.first_name} {request.user.last_name}",
        subject=card.assunto + f" N°: {card.idCard}",
        recipient=card.solicitante,  # O destinatário é o solicitante da questão
        url='processos_user',  # URL da página atual
    )
    notification.save()

    return JsonResponse({'success': True, 'message': 'Atendimento registrado com sucesso.'})


@login_required(login_url="/login")
def encaminhar_card(request, card_id):

    try:
        id_group = request.POST.get('selectedGroup')
        group = Group.objects.get(id=id_group)

        card = Card.objects.get(idCard=card_id)
        card.status = 'Encaminhado'
        card.setor = group
        card.responsavel = None
        card.save()

        historico = CardSetorHistory.objects.filter(card=card).order_by('-data_hora').last()

        # Registre o histórico de movimentação
        card_setor_history = CardSetorHistory(
            setor_id=group.id,
            card_id=card_id,
            status_anterior=historico.status_atual,
            status_atual="Encaminhado",
            setor_anterior=historico.setor_atual,
            setor_atual=group.name,
            operador=request.user
        )

        card_setor_history.save()

        historico_setor = CardSetorHistory.objects.filter(card=card).latest('data_hora')

        # Notificar o solicitante
        notification = Notification(
            author=request.user,
            description="Sua solicitação foi encaminhada para " + historico_setor.setor_atual,
            subject=card.assunto + f" N°: {card.idCard}",
            recipient=card.solicitante,
            url='processos_user',
        )
        notification.save()

        # Notificar os usuários compartilhados
        for user in card.compartilhar.all():
            if user != request.user:
                notification = Notification(
                    author=request.user,
                    description="Uma solicitação encaminhada para" + historico_setor.setor_atual,
                    subject=card.assunto + f" N°: {card.idCard}",
                    recipient=user,
                    url='processos_user',
                )
                notification.save()

        return JsonResponse({'success': True, 'message': 'Card encaminhado com sucesso.'})

    except Card.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Card não encontrado.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Erro ao encaminhar o card.'})


@login_required(login_url="/login")
def compartilhar_card(request, card_id):

    try:
        id_User = request.POST.get('selectedUser')
        user = User.objects.get(id=id_User)

        card = Card.objects.get(idCard=card_id)
        card.compartilhar.add(user)
        card.save()

        notification = Notification(
            author=request.user,
            description="Solicitação compartilhada com você",
            subject=card.assunto + f" N°: {card.idCard}",
            recipient=user,  # O destinatário é o solicitante da questão
            url='processos_user',  # URL da página atual
        )
        notification.save()

        return JsonResponse({'success': True, 'message': 'Card encaminhado com sucesso.'})

    except Card.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Card não encontrado.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Erro ao encaminhar o card.'})


@login_required(login_url="/login")
def transferir_card(request, card_id):

    try:
        id_group = request.POST.get('selectedGroupTrans')
        group = Group.objects.get(id=id_group)

        card = Card.objects.get(idCard=card_id)
        card.status = 'Triagem'
        card.setor = group
        card.responsavel = None
        card.save()

        historico = CardSetorHistory.objects.filter(card=card).order_by('-data_hora').last()

        # Registre o histórico de movimentação
        card_setor_history = CardSetorHistory(
            setor_id=group.id,
            card_id=card_id,
            status_anterior=historico.status_atual,
            status_atual="Triagem",
            setor_anterior=historico.setor_atual,
            setor_atual=group.name,
            operador=request.user,
        )

        card_setor_history.save()

        historico_setor = CardSetorHistory.objects.filter(card=card).latest('data_hora')

        # Notificar o solicitante
        notification = Notification(
            author=request.user,
            description="Sua solicitação foi Transferida para " + historico_setor.setor_atual,
            subject=card.assunto + f" N°: {card.idCard}",
            recipient=card.solicitante,
            url='processos_user',
        )
        notification.save()

        return JsonResponse({'success': True, 'message': 'Card Transferido com sucesso.'})

    except Card.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Card não encontrado.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Erro ao Transferir o card.'})


@login_required(login_url="/login")
def presonalizar_card(request, card_id):

    try:
        cor = request.POST.get('selectedColor')

        card = Card.objects.get(idCard=card_id)
        card.cor = cor
        card.save()

        return JsonResponse({'success': True, 'message': 'Card Presonalizado com sucesso.'})

    except Card.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Card não encontrado.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Erro ao Personalizar o card.'})


@login_required(login_url="/login")
def concluir_card(request, card_id):

    if request.method == 'POST':
        card = get_object_or_404(Card, idCard=card_id)

        try:
            card.status = 'Concluido'
            card.setor = request.user.groups.first()
            card.responsavel = request.user
            card.save()

            group = request.user.groups.first()

            historico = CardSetorHistory.objects.filter(card=card).order_by('-data_hora').last()

            # Registre o histórico de movimentação
            card_setor_history = CardSetorHistory(
                setor_id=group.id,
                card_id=card_id,
                status_anterior=historico.status_atual,
                status_atual="Concluido",
                setor_anterior=historico.setor_atual,
                setor_atual=group.name,
                operador=request.user,
            )

            notification = Notification(
                author=request.user,
                description="Eba! Sua solicitação foi concluida",
                subject=card.assunto + f" N°: {card.idCard}",
                recipient=card.solicitante,  # O destinatário é o solicitante da questão
                url='processos_user',  # URL da página atual
            )
            notification.save()

            card_setor_history.save()
            return JsonResponse({'success': True, 'message': 'Card finalizado com sucesso'})

        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Card não encontrado'})


@login_required(login_url="/login")
def get_user_rating(request, card_id):

    try:
        # Verifique se o usuário logado já avaliou o atendimento para o cartão
        user = request.user
        card = Card.objects.get(idCard=card_id)

        user_has_rated = OperatorRating.objects.filter(card=card, remetente=user).exists()

        return JsonResponse({'user_has_rated': user_has_rated})
    except Card.DoesNotExist:
        return JsonResponse({'error': 'Card não encontrado.'})
    except Exception as e:
        return JsonResponse({'error': 'Erro ao verificar a avaliação do usuário.'})


@login_required(login_url="/login")
def avaliar_card(request, card_id):

    card = Card.objects.get(idCard=card_id)

    try:
        card.status = 'Finalizado'
        card.save()

        group = request.user.groups.first()

        historico = CardSetorHistory.objects.filter(card=card).order_by('-data_hora').last()

        # Registre o histórico de movimentação
        card_setor_history = CardSetorHistory(
            setor_id=group.id,
            card_id=card_id,
            status_anterior=historico.status_atual,
            status_atual="Finalizado",
            setor_anterior=historico.setor_atual,
            setor_atual=group.name,
            operador=request.user,
        )
        card_setor_history.save()

        # Obtenha o histórico de setor mais recente para o cartão
        historico_setor = CardSetorHistory.objects.filter(card=card).latest('data_hora')

        # Obtenha o grupo associado ao histórico de setor
        grupo_setor = historico_setor.setor

        # Obtenha a URL do setor com base no grupo do responsável
        setor_link = CustomGroupInfo.objects.get(group=grupo_setor).url

        notification = Notification(
            author=request.user,
            description="Solicitação finalizada pelo solicitante",
            subject=card.assunto + f" N°: {card.idCard}",
            recipient=card.responsavel,  # O destinatário
            url=setor_link,  # URL da página atual
        )

        notification.save()

        avaliacao = request.POST.get('rating')

        rating = OperatorRating()
        rating.card = card
        rating.rating = avaliacao
        rating.operador = card.responsavel
        rating.anonymous = request.user
        rating.group = card.setor
        rating.save()

        return JsonResponse({'success': True})

    except Card.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Requisição inválida'})


@login_required(login_url="/login")
def finalizar_card(request, card_id):
    if request.method == 'POST':
        try:
            card = Card.objects.get(idCard=card_id)
            card.status = 'Finalizado'
            card.save()

            group = request.user.groups.first()

            historico = CardSetorHistory.objects.filter(card=card).order_by('-data_hora').last()

            # Registre o histórico de movimentação
            card_setor_history = CardSetorHistory(
                setor_id=group.id,
                card_id=card_id,
                status_anterior=historico.status_atual,
                status_atual="Finalizado",
                setor_anterior=historico.setor_atual,
                setor_atual=group.name,
                operador=request.user,
            )
            card_setor_history.save()

            # Obtenha o histórico de setor mais recente para o cartão
            historico_setor = CardSetorHistory.objects.filter(card=card).latest('data_hora')

            # Obtenha o grupo associado ao histórico de setor
            grupo_setor = historico_setor.setor

            # Obtenha a URL do setor com base no grupo do responsável
            setor_link = CustomGroupInfo.objects.get(group=grupo_setor).url

            notification = Notification(
                author=request.user,
                description="Solicitação finalizada pelo solicitante",
                subject=card.assunto,
                recipient=card.responsavel,  # O destinatário
                url=setor_link,  # URL da página atual
            )
            notification.save()

            return JsonResponse({'success': True, 'message': 'Card finalizado com sucesso'})

        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Card não encontrado'})
    else:
        return JsonResponse({'success': False, 'message': 'Requisição inválida'})


@login_required(login_url="/login")
def reabrir_card(request, card_id):
    if request.method == 'POST':
        try:
            card = Card.objects.get(idCard=card_id)
            card.status = 'Em Atendimento'
            card.save()

            group = request.user.groups.first()

            historico = CardSetorHistory.objects.filter(card=card).order_by('-data_hora').last()

            # Registre o histórico de movimentação
            card_setor_history = CardSetorHistory(
                setor_id=group.id,
                card_id=card_id,
                status_anterior=historico.status_atual,
                status_atual="Em Atendimento",
                setor_anterior=historico.setor_atual,
                setor_atual=group.name,
                operador=request.user,
            )
            card_setor_history.save()

            # Obtenha o histórico de setor mais recente para o cartão
            historico_setor = CardSetorHistory.objects.filter(card=card).latest('data_hora')

            # Obtenha o grupo associado ao histórico de setor
            grupo_setor = historico_setor.setor

            # Obtenha a URL do setor com base no grupo do responsável
            setor_link = CustomGroupInfo.objects.get(group=grupo_setor).url

            notification = Notification(
                author=request.user,
                description="Solicitação reaberta pelo usuário",
                subject=card.assunto,
                recipient=card.responsavel,  # O destinatário
                url=setor_link,  # URL da página atual
            )
            notification.save()
            return JsonResponse({'success': True, 'message': 'Card finalizado com sucesso'})

        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Card não encontrado'})
    else:
        return JsonResponse({'success': False, 'message': 'Requisição inválida'})


def history_request(request):
    cards = Card.objects.prefetch_related('messagehistory_set').all()

    context = {
        'cards': cards,
    }

    return render(request, 'ccis/history_request.html', context)


def get_message_history(request, card_id):
    if card_id:
        try:
            card_id = int(card_id)
            messages = MessageHistory.objects.filter(card_id=card_id).values('message')

            messages_list = [{'message': msg['message']} for msg in messages]
            return JsonResponse(messages_list, safe=False)

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': 'Invalid card ID'}, status=400)
    return JsonResponse({'error': 'Card ID not provided'}, status=400)


def get_card_details(request, card_id):
    try:
        card = Card.objects.get(id=card_id)
        # Obtenha os detalhes do card e retorne como JSON
        card_details = {
            "assunto": card.assunto,
            "service": card.service,
            # Adicione outros detalhes do card aqui
        }
        return JsonResponse(card_details)
    except Card.DoesNotExist:
        return JsonResponse({'error': 'Cartão não encontrado'}, status=404)


@login_required(login_url="/login")
def notificacao_lida(request, notification_id):
    try:
        notification = Notification.objects.get(pk=notification_id)

        if request.user == notification.recipient:
            notification.is_read = True
            notification.save()
            return JsonResponse({'success': True, 'message': 'Notificação marcada como lida.'})

        else:
            return JsonResponse({'success': False, 'message': 'Você não tem permissão para marcar esta notificação como lida.'})

    except Notification.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Notificação não encontrada.'})

        return JsonResponse({"error": "Card não encontrado"}, status=404)

