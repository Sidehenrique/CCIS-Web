import pymysql
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ccis.models import Usuario
from django.contrib import messages


# Create your views here.


def loginPage(request):
   return render(request, 'ccis/login.html')


def conta(request):
   return render(request, 'ccis/conta.html')


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








