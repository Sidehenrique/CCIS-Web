from django import forms
from .models import imagens


class formImagens(forms.ModelForm):
    class Meta:
        model = imagens
        fields = ('descricao', 'foto')


