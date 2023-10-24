from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import dadosPessoais, dependentes, enderecoContato, escolaridade, certificacao, profissional, \
    dadosBancarios, outros, CustomGroupInfo
from django.contrib.auth.models import User, Group


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


class CustomGroupInline(admin.TabularInline):  # Use TabularInline ou StackedInline, dependendo da aparência desejada
    model = CustomGroupInfo
    can_delete = False
    verbose_name = 'Custom Group'  # Nome da seção no admin
    verbose_name_plural = 'Custom Groups'


class CustomUserAdmin(UserAdmin):
    inlines = (dadosPessoaisInline, enderecoContatoInline, profissionalInline)


class CustomGroupAdmin(GroupAdmin):
    inlines = [CustomGroupInline]


# Registre o modelo DadosPessoais com o admin personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
