from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from ccis.forms import ModelFormNotebook
from .. models import dadosPessoais, Card, MessageHistory, CardSetorHistory, Notebook
from .. forms import modelFormAcessosTI, modelFormEquipamentosTI, modelFormSevicosTI

import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# VIWER DO TI ----------------------------------------------------------------------------------------------------------
@login_required(login_url="/login")
def ti_home(request):
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
        context = {
            'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
            'dados': dados, 'username': user, 'first_name': first_name, 'groupControle': groupControle,
            'last_name': last_name, 'group_gestao': group_gestao, 'is_superadmin': is_superadmin,
            'superior': superior, 'equipe': nomes_equipe
        }

        return render(request, 'ccis/setor_home.html', context)


@login_required(login_url="/login")
def new_request(request):


    acessos = modelFormAcessosTI()
    equipamentos = modelFormEquipamentosTI()
    servicos = modelFormSevicosTI()

    contexto = {'acessos': acessos, 'equipamentos':equipamentos, 'servicos':servicos}

    return render(request, 'ti/new_request.html', contexto)


@login_required(login_url="/login")
def request_acessos_ti(request):

    if request.method == 'POST':
        form = modelFormAcessosTI(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=1),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Tecnologia",  # Setor atual
            )
            history_entry.save()

            attachment = request.FILES.get('attachment')

            descricao = form.cleaned_data.get('descricao')
            if descricao:
                message_history = MessageHistory(
                    card=card,
                    remetente=request.user,
                    message=descricao,
                    attachment=attachment,
                )
                message_history.save()

            return redirect('ti_home')

    else:
        form = modelFormAcessosTI()

    return render(request, 'ti/new_request.html', {'form': form})


@login_required(login_url="/login")
def request_equipamentos_ti(request):

    if request.method == 'POST':
        form = modelFormEquipamentosTI(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=1),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Tecnologia",  # Setor atual
            )
            history_entry.save()

            attachment = request.FILES.get('attachment')

            descricao = form.cleaned_data.get('descricao')
            if descricao:
                message_history = MessageHistory(
                    card=card,
                    remetente=request.user,
                    message=descricao,
                    attachment=attachment,
                )
                message_history.save()

            return redirect('ti_home')

    else:
        form = modelFormAcessosTI()

    return render(request, 'ti/new_request.html', {'form': form})


@login_required(login_url="/login")
def request_servicos_ti(request):

    if request.method == 'POST':
        form = modelFormSevicosTI(request.POST, request.FILES)
        if form.is_valid():

            card = form.save(commit=False)
            card.solicitante = request.user
            card.save()

            # Crie um novo registro em CardSetorHistory para rastrear a criação do card
            history_entry = CardSetorHistory(
                card=card,
                setor=get_object_or_404(Group, id=1),
                status_anterior="",  # Status anterior (vazio, pois é a criação do card)
                status_atual="Triagem",  # Status atual
                setor_anterior="",  # Setor anterior (vazio, pois é a criação do card)
                setor_atual="Tecnologia",  # Setor atual
            )
            history_entry.save()

            attachment = request.FILES.get('attachment')

            descricao = form.cleaned_data.get('descricao')
            if descricao:
                message_history = MessageHistory(
                    card=card,
                    remetente=request.user,
                    message=descricao,
                    attachment=attachment,
                )
                message_history.save()

            return redirect('ti_home')
    else:
        form = modelFormAcessosTI()

    return render(request, 'ti/new_request.html', {'form': form})

# ----------------------------------------------------------------------------------------------------------------------


def estoque(request):
    log = request.user
    log_id = request.user.id
    logName = request.user.first_name
    logLast = request.user.last_name
    logFoto = dadosPessoais.objects.get(usuario=request.user).foto
    is_superadmin = log.is_superuser
    group_gestao = log.groups.filter(id=3).exists()
    groupControle = log.groups.filter(id=28).exists()

    contexto = {'log_id': log_id, 'logName': logName, 'logLast': logLast, 'logFoto': logFoto,
                'group_gestao': group_gestao, 'is_superadmin': is_superadmin, 'groupControle': groupControle}

    return render(request, 'ti/estoque.html', contexto)


@login_required(login_url="/login")
def solicit(request):

    return render(request, 'ti/solicit.html')


@login_required(login_url="/login")
def notebook(request):
    dadosTable = Notebook.objects.all()
    form = ModelFormNotebook()

    if request.method == 'POST':
        form = ModelFormNotebook(request.POST)
        if form.is_valid():
            logging.debug("Formulário é válido")
            form.save()
            logging.debug("Formulário salvo com sucesso")
            return redirect('notebook')
        else:
            logging.debug("Formulário não é válido. Erros: %s", form.errors)
    return render(request, 'ti/estoque/notebook.html', {'form': form, 'dadosTable': dadosTable})


