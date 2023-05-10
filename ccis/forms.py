from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import dadosPessoais, dependentes, enderecoContato, escolaridade, certificacao, profissional, \
    dadosBancarios, outros
from crispy_forms.layout import Layout, Submit, Row, Column


class modelFormDadosPessoais(forms.ModelForm):
    class Meta:
        model = dadosPessoais
        fields = ('nomeCompleto', 'sexo', 'estadoCivil', 'corRaca', 'dataNascimento', 'naturalidade', 'tipoSanguineo',
                  'nomePai', 'nomeMae', 'cpf', 'rg', 'expedidor', 'cnh', 'validadeCnh', 'categoria', 'tituloEleitor',
                  'zona', 'secao', 'ctps', 'serieCTPS', 'dataCTPS', 'reservista', 'ra', 'serieReservista', 'pis', 'cns',
                  'pcd', 'foto', 'canvas')

        widgets = {
            'nomeCompleto': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'estadoCivil': forms.Select(attrs={'class': 'form-select'}),
            'corRaca': forms.Select(attrs={'class': 'form-select'}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoSanguineo': forms.Select(attrs={'class': 'form-select'}),
            'nomePai': forms.TextInput(attrs={'class': 'form-control'}),
            'nomeMae': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.NumberInput(attrs={'class': 'form-control'}),
            'rg': forms.NumberInput(attrs={'class': 'form-control'}),
            'expedidor': forms.TextInput(attrs={'class': 'form-control'}),
            'cnh': forms.TextInput(attrs={'class': 'form-control'}),
            'validadeCnh': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
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

        }


class modelFormDependentes(forms.ModelForm):
    class Meta:
        model = dependentes
        fields = ('nomeCompleto', 'cpf', 'dataNascimento', 'relacao', 'email', 'contato')

        widgets = {'nomeCompleto': forms.TextInput(attrs={'class': 'form-control'}),
                   'cpf': forms.NumberInput(attrs={'class': 'form-control'}),
                   'dataNascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'relacao': forms.Select(attrs={'class': 'form-select'}),
                   'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
                   'contato': forms.NumberInput(attrs={'class': 'form-control'})
                   }


class modelFormEnderecoContato(forms.ModelForm):
    class Meta:
        model = enderecoContato
        fields = ('endereco', 'bairro', 'cidade', 'estado', 'cep', 'emailCorporativo', 'telefonePessoal',
                  'telefoneCorporativo', 'celularCorporativo', 'celularPessoal', 'ramal', 'emailPessoal',
                  'relacao', 'telefoneDeEmergencia', 'celularDeEmergencia')

        widgets = {'endereco': forms.TextInput(attrs={'class': 'form-control'}),
                   'bairro': forms.TextInput(attrs={'class': 'form-control'}),
                   'cidade': forms.TextInput(attrs={'class': 'form-control'}),
                   'estado': forms.Select(attrs={'class': 'form-select'}),
                   'cep': forms.NumberInput(attrs={'class': 'form-control'}),
                   'emailCorporativo': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
                   'telefonePessoal': forms.NumberInput(attrs={'class': 'form-control'}),
                   'telefoneCorporativo': forms.NumberInput(attrs={'class': 'form-control'}),
                   'celularCorporativo': forms.NumberInput(attrs={'class': 'form-control'}),
                   'celularPessoal': forms.NumberInput(attrs={'class': 'form-control'}),
                   'ramal': forms.NumberInput(attrs={'class': 'form-control'}),
                   'emailPessoal': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
                   'relacao': forms.Select(attrs={'class': 'form-control'}),
                   'telefoneDeEmergencia': forms.NumberInput(attrs={'class': 'form-control'}),
                   'celularDeEmergencia': forms.NumberInput(attrs={'class': 'form-control'})
                   }


class modelFormEscolaridade(forms.ModelForm):
    class Meta:
        model = escolaridade
        fields = (
            'entidadeDeEnsino', 'curso', 'grau', 'dataConclusao', 'idiomaPrimario', 'nivelPrimario', 'idiomaSecundario',
            'nivelSecundario')

        widgets = {'entidadeDeEnsino': forms.TextInput(attrs={'class': 'form-control'}),
                   'curso': forms.TextInput(attrs={'class': 'form-control'}),
                   'grau': forms.Select(attrs={'class': 'form-select'}),
                   'dataConclusao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'idiomaPrimario': forms.TextInput(attrs={'class': 'form-control'}),
                   'nivelPrimario': forms.Select(attrs={'class': 'form-control'}),
                   'idiomaSecundario': forms.TextInput(attrs={'class': 'form-control'}),
                   'nivelSecundario': forms.Select(attrs={'class': 'form-select'})
                   }


class modelFormCertificacao(forms.ModelForm):
    class Meta:
        model = certificacao
        fields = ('nome', 'organizacaoEmissora', 'dataEmissao', 'dataExpiracao')

        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'}),
                   'organizacaoEmissora': forms.TextInput(attrs={'class': 'form-control'}),
                   'dataEmissao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'dataExpiracao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
                   }


class modelFormProfissional(forms.ModelForm):
    class Meta:
        model = profissional
        fields = (
            'cargo', 'area', 'paUnidade', 'colaborador', 'centroDeCusto', 'matricula', 'empregador', 'superiorImediato',
            'folhaDePagamento', 'admissao', 'desligamento', 'situacao', 'horarioEntrada', 'horarioSaida')

        widgets = {'cargo': forms.TextInput(attrs={'class': 'form-control'}),
                   'area': forms.TextInput(attrs={'class': 'form-control'}),
                   'paUnidade': forms.Select(attrs={'class': 'form-select'}),
                   'colaborador': forms.Select(attrs={'class': 'form-select'}),
                   'centroDeCusto': forms.TextInput(attrs={'class': 'form-control'}),
                   'matricula': forms.TextInput(attrs={'class': 'form-control'}),
                   'empregador': forms.Select(attrs={'class': 'form-select'}),
                   'superiorImediato': forms.TextInput(attrs={'class': 'form-control'}),
                   'folhaDePagamento': forms.TextInput(attrs={'class': 'form-control'}),
                   'admissao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'desligamento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'situacao': forms.Select(attrs={'class': 'form-select'}),
                   'horarioEntrada': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
                   'horarioSaida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
                   }


class modelFormDadosBancarios(forms.ModelForm):
    class Meta:
        model = dadosBancarios
        fields = ('conta', 'digito', 'banco', 'agencia', 'tipoDeConta', 'modalidade', 'chavePix')

        widgets = {'conta': forms.TextInput(attrs={'class': 'form-control'}),
                   'digito': forms.TextInput(attrs={'class': 'form-control'}),
                   'banco': forms.TextInput(attrs={'class': 'form-control'}),
                   'agencia': forms.TextInput(attrs={'class': 'form-control'}),
                   'tipoDeConta': forms.Select(attrs={'class': 'form-select'}),
                   'modalidade': forms.TextInput(attrs={'class': 'form-control'}),
                   'chavePix': forms.TextInput(attrs={'class': 'form-control'}),
                   }


class ModelFormMidia(forms.ModelForm):
    class Meta:
        model = dadosPessoais
        fields = ('foto', 'canvas')

        widgets = {'foto': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   'canvas': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'})
                   }


class ModelFormOutros(forms.ModelForm):
    class Meta:
        model = outros
        fields = ('camiseta',)
        widgets = {'camiseta': forms.Select(attrs={'class': 'form-select'}),
                   }


class modelFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
               'password': forms.PasswordInput(attrs={'class': 'form-control'}),
               'email': forms.EmailInput(attrs={'class': 'form-control'}),
               'first_name': forms.TextInput(attrs={'class': 'form-control'}),
               'last_name': forms.TextInput(attrs={'class': 'form-control'})
                   }


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
