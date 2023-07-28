from django.contrib import admin
from .models import dadosPessoais
from .forms import modelFormDadosPessoais


class DadosPessoaisAdmin(admin.ModelAdmin):
    form = modelFormDadosPessoais

    # Adicione o campo 'user' na lista de campos para exibição no admin
    list_display = ('usuario', 'nomeCompleto', 'sexo', 'dataNascimento')

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)


# Registre o modelo DadosPessoais com o admin personalizado
admin.site.register(dadosPessoais, DadosPessoaisAdmin)
