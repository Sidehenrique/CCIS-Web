from django.contrib import admin
from .forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios, \
    modelFormRg, modelFormCnh, modelFormCpf, modelFormReservista, modelFormTitulo, modelFormClt, modelFormSetor,\
    modelFormResidencia, modelFormCertidao, modelFormAdmissional, modelFormPeriodico, modelFormCurso, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import dadosPessoais, dependentes, enderecoContato, escolaridade, certificacao, profissional, \
    dadosBancarios, outros, setor
from django.contrib.auth.models import User


# VISUALIZAÇÃO DE TABELAS PERSONALIZADAS -------------------------------------------------------------------------------
class setorAdmin(admin.ModelAdmin):
    form = modelFormSetor

    # Adicione o campo 'user' na lista de campos para exibição no admin
    list_display = ('sigla', 'nome', 'email', 'responsavel')


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

admin.site.register(setor, setorAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
