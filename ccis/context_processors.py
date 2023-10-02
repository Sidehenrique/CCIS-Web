# myapp/context_processors.py

def governanca_button(request):
    log = request.user
    is_in_governanca_group = log.groups.filter(name='governanca').exists()
    return {'is_in_governanca_group': is_in_governanca_group}
