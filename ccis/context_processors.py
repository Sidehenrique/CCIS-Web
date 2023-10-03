# myapp/context_processors.py

def controle_button(request):
    log = request.user
    controle = log.groups.filter(name='gestao e controle').exists()
    return {'controle': controle}
