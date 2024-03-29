# myapp/context_processors.py
from ccis.models import dadosPessoais, enderecoContato
from ccis.forms import ModelFormMidia
from .models import Notification


def controle_button(request):
    log = request.user
    controle = log.groups.filter(name='gestao e controle').exists()
    return {'controle': controle}


def user_data(request):
    user_data = {}
    if request.user.is_authenticated:
        user_data = {
            'log': request.user,
            'log_id': request.user.id,
            'logName': request.user.first_name,
            'logLast': request.user.last_name,
            'logFoto': dadosPessoais.objects.get(usuario=request.user).foto,
            'logSexo': dadosPessoais.objects.get(usuario=request.user).sexo,
            'logEmail': enderecoContato.objects.get(usuario=request.user).emailCorporativo,
            'is_superadmin': request.user.is_superuser,
            'logGroup': request.user.groups.first().name if request.user.groups.first() else None,
            'id_do_grupo': request.user.groups.first().id if request.user.groups.first() else None,
        }

    return {'user_data': user_data}


def foto_profile(request):
    midia = ModelFormMidia()

    return {'midia': midia}


def ambiente_para_setor(request):
    # Mapeamento de ambiente para setor
    AMBIENTE_PARA_SETOR = {
        'Tecnologia': 1,
        # Adicione mais mapeamentos para outros ambientes, se necessário
    }
    return {'ambiente_para_setor': AMBIENTE_PARA_SETOR}


def exibir_notificacoes(request):
    try:
        if request.user.is_authenticated:
            notifications = Notification.objects.filter(
                recipient=request.user,
                is_read=False
            ).order_by('-date')
            return {'notifications': notifications}
    except:
        pass
    return {'notifications': []}  # Retorna uma lista vazia se não houver usuário logado ou houver algum erro
