# myapp/context_processors.py
from ccis.models import dadosPessoais, enderecoContato
from ccis.forms import ModelFormMidia


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
        }

    return {'user_data': user_data}


def foto_profile(request):
    midia = ModelFormMidia()

    return {'midia': midia}

