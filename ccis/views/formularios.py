from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .. models import dadosPessoais, dependentes, enderecoContato, outros, escolaridade, certificacao, \
    dadosBancarios, docRg, docCnh, docCpf, docReservista, docTitulo, docClt, docResidencia, \
    docCertidao, docAdmissional, docPeriodico, docCursos, profissional, setor

from .. forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios, \
    modelFormRg, modelFormCnh, modelFormCpf, modelFormReservista, modelFormTitulo, modelFormClt, modelFormSetor, \
    modelFormResidencia, modelFormCertidao, modelFormAdmissional, modelFormPeriodico, modelFormCurso, \
    CustomUserCreationForm


# FORMULARIOS DADOS PESSOAIS ---------------------------------------------------------------------------------
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
            return redirect('conta', user_id=request.user.id)

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
            return redirect('profile', user_id=request.user.id)

        else:
            print('deu erro')
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Escolaridade'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('profile', user_id=request.user.id)

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
            return redirect('profile', user_id=request.user.id)

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente do formulário Certificação'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('profile', user_id=request.user.id)

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
            return redirect('conta')

        else:
            mensagem = 'Por favor verifique se todos os campos foram preenchidos corretamente'
            messages.add_message(request=request, message=mensagem, level=messages.ERROR)
            return redirect('conta')
# ----------------------------------------------------------------------------------------------------------------------


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
            return redirect('documentos', user_id=request.user.id)

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
            return redirect('documentos', user_id=request.user.id)

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
            return redirect('documentos', user_id=request.user.id)

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

