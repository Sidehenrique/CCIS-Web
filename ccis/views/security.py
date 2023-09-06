from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from .. models import dadosPessoais, profissional


# SEGURANÇA ------------------------------------------------------------------------------------------------------------
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
                return redirect('profile', user_id=request.user.id)

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
        return redirect('profile', user_id=request.user.id)

    return redirect('login')


@login_required(login_url="/login")
def inativar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)

    pro = get_object_or_404(profissional, usuario=user)

    # Atualize o status para inativo
    pro.situacao = 'Inativo'
    pro.save()

    return redirect('usuario')


def password_reset(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        cpf = request.POST.get('cpf')

        try:
            user = User.objects.get(username=username)
            dados_pessoais = dadosPessoais.objects.get(usuario=user)

            if cpf == dados_pessoais.cpf:
                nova_senha = request.POST.get('novaSenha')
                confirma_senha = request.POST.get('confSenha')

                if nova_senha == confirma_senha:
                    user.set_password(nova_senha)
                    user.save()
                    return redirect('password_done')
                else:
                    return render(request, 'security/password_reset.html', {'error': 'As senhas não conferem'})

            else:
                return render(request, 'security/password_reset.html', {'error': 'CPF não confere'})

        except User.DoesNotExist or dadosPessoais.DoesNotExist:
            return render(request, 'security/password_reset.html', {'error': 'Nome de usuário ou CPF não encontrado.'})

    return render(request, 'security/password_reset.html')


def password_done(request):
    return render(request, 'security/password_done.html')

# ----------------------------------------------------------------------------------------------------------------------

