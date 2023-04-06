from django import forms
from .models import dadosPessoais


class modelFormDadosPessoais(forms.ModelForm):
    class Meta:
        model = dadosPessoais
        fields = ('nomeCompleto', 'sexo', 'estadoCivil', 'corRaca', 'dataNascimento', 'naturalidade', 'tipoSanguineo',
                  'nomePai', 'nomeMae', 'cpf', 'rg', 'expedidor', 'cnh', 'validadeCnh', 'categoria', 'tituloEleitor',
                  'zona', 'secao', 'ctps', 'serieCTPS', 'dataCTPS', 'reservista', 'ra', 'serieReservista', 'pis', 'cns',
                  'pcd', 'foto', 'canvas')

        widgets = {
            'nomeCompleto': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoCivil': forms.TextInput(attrs={'class': 'form-control'}),
            'corRaca': forms.TextInput(attrs={'class': 'form-control'}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoSanguineo': forms.TextInput(attrs={'class': 'form-control'}),
            'nomePai': forms.TextInput(attrs={'class': 'form-control'}),
            'nomeMae': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.NumberInput(attrs={'class': 'form-control'}),
            'rg': forms.NumberInput(attrs={'class': 'form-control'}),
            'expedidor': forms.TextInput(attrs={'class': 'form-control'}),
            'cnh': forms.TextInput(attrs={'class': 'form-control'}),
            'validadeCnh': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'tituloEleitor': forms.NumberInput(attrs={'class': 'form-control'}),
            'zona': forms.NumberInput(attrs={'class': 'form-control'}),
            'secao': forms.NumberInput(attrs={'class': 'form-control'}),
            'ctps': forms.NumberInput(attrs={'class': 'form-control'}),
            'serieCTPS': forms.NumberInput(attrs={'class': 'form-control'}),
            'dataCTPS': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reservista': forms.NumberInput(attrs={'class': 'form-control'}),
            'ra': forms.NumberInput(attrs={'class': 'form-control'}),
            'serieReservista': forms.TextInput(attrs={'class': 'form-control'}),
            'pis': forms.NumberInput(attrs={'class': 'form-control'}),
            'cns': forms.NumberInput(attrs={'class': 'form-control'}),
            'pcd': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            # 'foto': forms.Im(attrs={'class': 'form-control'}),
            # 'canvas': forms.TextInput(attrs={'class': 'form-control'}),













                   }

