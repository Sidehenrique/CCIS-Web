from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import dadosPessoais, dependentes, enderecoContato, escolaridade, certificacao, profissional, \
    dadosBancarios, outros, CustomGroupInfo, SectorButtons
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


@admin.register(SectorButtons)
class CustomButtonsSectorAdmin(admin.ModelAdmin):
    list_display = ('group', 'text1', 'text2', 'cor', 'url', 'icon', 'permissao')
    list_filter = ('cor', 'permissao')
    search_fields = ('group__name', 'text1', 'text2')


class CustomGroupInline(admin.TabularInline):
    model = CustomGroupInfo
    can_delete = False
    verbose_name = 'Custom Group'
    verbose_name_plural = 'Custom Groups'


class CustomUserAdmin(UserAdmin):
    inlines = (dadosPessoaisInline, enderecoContatoInline, profissionalInline,)


class CustomGroupAdmin(GroupAdmin):
    inlines = [CustomGroupInline]


# Registre o modelo DadosPessoais com o admin personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
