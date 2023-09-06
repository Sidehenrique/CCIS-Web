from django import forms
from django.forms import FileInput

from .models import dadosPessoais, dependentes, enderecoContato, escolaridade, certificacao, profissional, \
    dadosBancarios, outros, User, docRg, docCnh, docCpf, docReservista, docTitulo, docClt, docResidencia, \
    docCertidao, docAdmissional, docPeriodico, docCursos, setor, acessoM1, acessoM2

from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm


# FORMULÁRIOS -------------------------------------------------------------------->
class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('group',)

        widgets = {
            'group': forms.Select(attrs={'class': 'form-select'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class modelFormDadosPessoais(forms.ModelForm):
    class Meta:
        model = dadosPessoais
        fields = ('nomeCompleto', 'sexo', 'estadoCivil', 'corRaca', 'dataNascimento', 'naturalidade', 'tipoSanguineo',
                  'nomePai', 'nomeMae', 'cpf', 'rg', 'expedidor', 'cnh', 'validadeCnh', 'categoria', 'tituloEleitor',
                  'zona', 'secao', 'ctps', 'serieCTPS', 'dataCTPS', 'reservista', 'ra', 'serieReservista', 'pis', 'cns',
                  'pcd')

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

    def calcular_porcentagem_dp(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


class modelFormDependentes(forms.ModelForm):
    class Meta:
        model = dependentes
        fields = ('nomeCompleto', 'cpf', 'dataNascimento', 'relacao', 'email', 'contato', 'declaracao')

        widgets = {'nomeCompleto': forms.TextInput(attrs={'class': 'form-control'}),
                   'cpf': forms.NumberInput(attrs={'class': 'form-control'}),
                   'dataNascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'relacao': forms.Select(attrs={'class': 'form-select'}),
                   'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
                   'contato': forms.NumberInput(attrs={'class': 'form-control'}),
                   'declaracao': forms.Select(attrs={'class': 'form-select'}),
                   }

    def calcular_porcentagem_dep(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


class modelFormEnderecoContato(forms.ModelForm):
    class Meta:
        model = enderecoContato
        fields = ('endereco', 'bairro', 'cidade', 'estado', 'cep', 'emailCorporativo', 'telefonePessoal',
                  'telefoneCorporativo', 'celularCorporativo', 'celularPessoal', 'ramal', 'emailPessoal',
                  'nomeCompleto', 'relacao', 'telefoneDeEmergencia', 'celularDeEmergencia')

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
                   'nomeCompleto': forms.TextInput(attrs={'class': 'form-control'}),
                   'relacao': forms.Select(attrs={'class': 'form-select'}),
                   'telefoneDeEmergencia': forms.NumberInput(attrs={'class': 'form-control'}),
                   'celularDeEmergencia': forms.NumberInput(attrs={'class': 'form-control'})
                   }

    def calcular_porcentagem_end(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


class modelFormEscolaridade(forms.ModelForm):
    class Meta:
        model = escolaridade
        fields = (
            'entidadeDeEnsino', 'curso', 'grau', 'dataInicio', 'dataConclusao', 'idiomaSecundario', 'nivelSecundario',
            'docEscolaridade',)

        widgets = {'entidadeDeEnsino': forms.TextInput(attrs={'class': 'form-control'}),
                   'curso': forms.TextInput(attrs={'class': 'form-control'}),
                   'grau': forms.Select(attrs={'class': 'form-select'}),
                   'dataInicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'dataConclusao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'idiomaSecundario': forms.TextInput(attrs={'class': 'form-control'}),
                   'nivelSecundario': forms.Select(attrs={'class': 'form-select'}),
                   'docEscolaridade': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }

    def calcular_porcentagem_esc(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


class modelFormCertificacao(forms.ModelForm):
    class Meta:
        model = certificacao
        fields = ('nome', 'organizacaoEmissora', 'dataEmissao', 'dataExpiracao', 'docCertificado','certiAnbima','anexoAnbima')

        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'}),
                   'organizacaoEmissora': forms.TextInput(attrs={'class': 'form-control'}),
                   'dataEmissao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'dataExpiracao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'docCertificado': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   'certiAnbima': forms.Select(attrs={'class': 'form-select'}),
                   'anexoAnbima': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }

    def calcular_porcentagem_cer(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


class modelFormProfissional(forms.ModelForm):
    class Meta:
        model = profissional
        fields = (
            'cargo', 'area', 'paUnidade', 'colaborador', 'centroDeCusto', 'matricula', 'empregador', 'superiorImediato',
            'folhaDePagamento', 'admissao', 'desligamento', 'situacao', 'horarioEntrada', 'horarioSaida',
        )

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

    def calcular_porcentagem_pro(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


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

    def calcular_porcentagem_db(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


class ModelFormMidia(forms.ModelForm):
    class Meta:
        model = dadosPessoais
        fields = ('foto', 'canvas')

        widgets = {'foto': FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   'canvas': FileInput(attrs={'type': 'file', 'class': 'form-control'})
                   }

    def calcular_porcentagem_mid(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


class ModelFormOutros(forms.ModelForm):
    class Meta:
        model = outros
        fields = ('camiseta',)
        widgets = {'camiseta': forms.Select(attrs={'class': 'form-select'}),
                   }

    def calcular_porcentagem_out(self):
        total_campos = len(self.Meta.fields)
        preenchidos = 0

        for campo in self.Meta.fields:
            if getattr(self.instance, campo):
                preenchidos += 1

        return (preenchidos / total_campos) * 100


# DOCUMENTOS -------------------------------------------------------------------->

class modelFormRg(forms.ModelForm):
    class Meta:
        model = docRg
        fields = ('documentoRg',)
        widgets = {'documentoRg': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormCnh(forms.ModelForm):
    class Meta:
        model = docCnh
        fields = ('documentoCnh',)
        widgets = {'documentoCnh': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormCpf(forms.ModelForm):
    class Meta:
        model = docCpf
        fields = ('documentoCpf',)
        widgets = {'documentoCpf': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormReservista(forms.ModelForm):
    class Meta:
        model = docReservista
        fields = ('documentoReservista',)
        widgets = {'documentoReservista': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormTitulo(forms.ModelForm):
    class Meta:
        model = docTitulo
        fields = ('documentoTitulo',)
        widgets = {'documentoTitulo': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormClt(forms.ModelForm):
    class Meta:
        model = docClt
        fields = ('documentoClt',)
        widgets = {'documentoClt': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormResidencia(forms.ModelForm):
    class Meta:
        model = docResidencia
        fields = ('documentoResidencia',)
        widgets = {'documentoResidencia': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormCertidao(forms.ModelForm):
    class Meta:
        model = docCertidao
        fields = ('documentoCertidao',)
        widgets = {'documentoCertidao': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormAdmissional(forms.ModelForm):
    class Meta:
        model = docAdmissional
        fields = ('documentoAdmissional',)
        widgets = {'documentoAdmissional': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormPeriodico(forms.ModelForm):
    class Meta:
        model = docPeriodico
        fields = ('documentoPeriodico',)
        widgets = {'documentoPeriodico': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                   }


class modelFormCurso(forms.ModelForm):
    class Meta:
        model = docCursos
        fields = ('curso', 'data', 'certiCurso')
        widgets = {
            'certiCurso': forms.ClearableFileInput(attrs={'type': 'file', 'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Cadastro setor -------------------------------------------------------------->
class modelFormSetor(forms.ModelForm):
    class Meta:
        model = setor
        fields = ('sigla', 'nome', 'cor', 'email', 'contato', 'ramal', 'unidade', 'responsavel', 'atribuicoes', 'canvas')

        widgets = {'siglas': forms.TextInput(attrs={'class': 'form-control'}),
                   'nome': forms.TextInput(attrs={'class': 'form-control'}),
                   'cor': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
                   'contato': forms.NumberInput(attrs={'class': 'form-control'}),
                   'ramal': forms.NumberInput(attrs={'class': 'form-control'}),
                   'unidade': forms.TextInput(attrs={'class': 'form-control'}),
                   'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
                   'atribuicoes': forms.TextInput(attrs={'class': 'form-control'}),
                   'canvas': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'})

                   }


# GRUPOS -------------------------------------------------------------------->

class GroupForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all())


# Cadastro request -------------------------------------------------------------->
class modelFormAcessosM1(forms.ModelForm):
    class Meta:
        model = acessoM1
        fields = ('assunto', 'descricao', 'arquivo')

        widgets = {'assunto': forms.Select(attrs={'class': 'form-select'}),
                   'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}),
                   'arquivo': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'})
                   }

