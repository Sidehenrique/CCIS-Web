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
class DadosPessoaisAdmin(admin.ModelAdmin):
    form = modelFormDadosPessoais

    # Adicione o campo 'user' na lista de campos para exibição no admin
    list_display = ('usuario', 'nomeCompleto', 'sexo', 'dataNascimento')


class enderecoContatoAdmin(admin.ModelAdmin):
    form = modelFormEnderecoContato

    # Adicione o campo 'user' na lista de campos para exibição no admin
    list_display = ('endereco', 'cidade', 'emailCorporativo', 'celularPessoal')


class profissionalAdmin(admin.ModelAdmin):
    form = modelFormProfissional

    # Adicione o campo 'user' na lista de campos para exibição no admin
    list_display = ('cargo', 'colaborador', 'superiorImediato', 'situacao')


class setorAdmin(admin.ModelAdmin):
    form = modelFormSetor

    # Adicione o campo 'user' na lista de campos para exibição no admin
    list_display = ('sigla', 'nome', 'email', 'responsavel')


# Registre o modelo DadosPessoais com o admin personalizado
admin.site.register(dadosPessoais, DadosPessoaisAdmin)
admin.site.register(enderecoContato, enderecoContatoAdmin)
admin.site.register(profissional, profissionalAdmin)
admin.site.register(setor, setorAdmin)


# INSERÇÃO DE TABELAS NO CADASTRO DE USUARIO NO ADMIN ------------------------------------------------------------------
class dadosPessoaisInline(admin.StackedInline):
    model = dadosPessoais
    can_delete = False


class enderecoContatoInline(admin.StackedInline):
    model = enderecoContato
    can_delete = False


class profissionalInline(admin.StackedInline):
    model = profissional
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (dadosPessoaisInline, enderecoContatoInline, profissionalInline)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
