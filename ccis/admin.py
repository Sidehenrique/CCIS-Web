from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import dadosPessoais, dependentes, enderecoContato, escolaridade, certificacao, profissional, \
    dadosBancarios, outros
from django.contrib.auth.models import User


# INSERÇÃO DE TABELAS NO CADASTRO DE USUARIO NO ADMIN ------------------------------------------------------------------
class dadosPessoaisInline(admin.StackedInline):
    model = dadosPessoais
    fields = ['nomeCompleto', 'sexo', 'cpf']
    can_delete = False


class enderecoContatoInline(admin.StackedInline):
    model = enderecoContato
    fields = ['emailCorporativo']
    can_delete = False


class profissionalInline(admin.StackedInline):
    model = profissional
    fields = ['cargo', 'area', 'situacao']
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (dadosPessoaisInline, enderecoContatoInline, profissionalInline)


# Registre o modelo DadosPessoais com o admin personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
