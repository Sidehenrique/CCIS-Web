from django import forms
from django.forms import FileInput
from .models import dadosPessoais, dependentes, enderecoContato, escolaridade, certificacao, profissional, \
    dadosBancarios, outros, User, docRg, docCnh, docCpf, docReservista, docTitulo, docClt, docResidencia, \
    docCertidao, docAdmissional, docPeriodico, docCursos, Card, Notebook

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
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
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
        fields = (
            'nome', 'organizacaoEmissora', 'dataEmissao', 'dataExpiracao', 'docCertificado', 'certiAnbima',
            'anexoAnbima')

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


class GroupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        excluded_groups = kwargs.pop('excluded_groups', ['Lixo', 'governanca', 'gestao e controle'])  # Obtenha os grupos para excluir

        # Atualize as opções do campo 'group', excluindo grupos indesejados
        self.fields['group'].queryset = Group.objects.exclude(name__in=excluded_groups)

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )


# CHAMADOS TI  -------------------------------------------------------------->
class modelFormAcessosTI(forms.ModelForm):
    CHOICES_ServicoAcessos = [
        ('', ''),
        ('Criação', 'Criação'),
        ('Alteração', 'Alteração'),
        ('Redefinição', 'Redefinição'),
        ('Exclusão', 'Exclusão'),
        ('Liberação Celular', 'Liberação Celular'),
    ]

    CHOICES_AssuntoAcessos = [
        ('', ''),
        ('Sisbr', 'Sisbr'),
        ('VPN', 'VPN'),
        ('Email', 'Email'),
        ('Intranet', 'Intranet'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_AssuntoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_ServicoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormEquipamentosTI(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Instalação', 'Instalação'),
        ('Manutenção', 'Manutenção'),
        ('Substituição', 'Substituição'),

    ]

    CHOICES_Assunto = [
        ('', ''),
        ('Software', 'Software'),
        ('Equipamento', 'Equipamento'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormDesenvolvimentoTI(forms.ModelForm):
    CHOICES_Servico = [
        ('Intranet', 'Intranet'),
        ('Bot', 'Bot'),
    ]

    CHOICES_Assunto = [
        ('Desenvolvimento', 'Desenvolvimento'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormSevicosTI(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Intranet', 'Intranet'),
        ('Visita Técnica', 'Visita Técnica'),
        ('Manutenção CPD', 'Manutenção CPD'),
        ('Agendamento', 'Agendamento'),
        ('Outros', 'Outros'),

    ]

    CHOICES_Assunto = [
        ('Serviço', 'Serviço'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


# new request gestao de risco ------------------------------------------------------------------------------------------

class modelFormCI(forms.ModelForm):
    CHOICES_Servico = [
        ('Controle Interno', 'Controle Interno'),
        ('Auditoria CNAC', 'Auditoria CNAC'),
        ('Risco Operacional', 'Risco Operacional'),

    ]

    CHOICES_Assunto = [
        ('CI/CNAC/R.O', 'CI/CNAC/R.O'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormApontamentos(forms.ModelForm):
    CHOICES_Servico = [
        ('Controle Interno', 'Controle Interno'),
        ('Auditoria CNAC', 'Auditoria CNAC'),
        ('Risco Operacional', 'Risco Operacional'),

    ]

    CHOICES_Assunto = [
        ('Apontamentos', 'Apontamentos'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


# Performace Corporativa  ----------------------------------------------------------------------------------------------->

class modelFormPowerPC(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Criação de Painel', 'Criação de Painel'),
        ('Ajuste/Erros', 'Ajuste/Erros'),
        ('Sugestões', 'Sugestões'),
        ('Dashboard de Crédito', 'Dashboard de Crédito'),
        ('Dashboard de Captações', 'Dashboard de Captações'),
        ('Dashboard de Capital', 'Dashboard de Capital'),
        ('Gestão de Capital ', 'Gestão de Capital '),
        ('Contabilidade ', 'Contabilidade '),
    ]

    CHOICES_Assunto = [
        ('Painéis', 'Painéis'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormPropensoPC(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cheque Especial', 'Cheque Especial'),
        ('Conta Garantida', 'Conta Garantida'),
        ('Seguros Consórcio', 'Seguros Consórcio'),
        ('Crédito Comercial', 'Crédito Comercial'),
        ('Crédito Rural Sipag', 'Crédito Rural Sipag'),
        ('Cobrança Consignado', 'Cobrança Consignado'),
        ('Tarifas', 'Tarifas'),
    ]

    CHOICES_Assunto = [
        ('Lista de Propensos', 'Lista de Propensos'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormRelatorioPC(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Criação de Relatório', 'Criação de Relatório'),
        ('Ajuste', 'Ajuste'),
        ('Erros', 'Erros'),
        ('Sugestões', 'Sugestões'),
    ]

    CHOICES_Assunto = [
        ('Relatórios', 'Relatórios'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormEstudoPC(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Estudo de Viabilidade de Região', 'Estudo de Viabilidade de Região'),
        ('Estudo de Rentabilidade de Produto ou Serviço', 'Estudo de Rentabilidade de Produto ou Serviço'),
        ('Pesquisa de Mercado', 'Pesquisa de Mercado'),
    ]

    CHOICES_Assunto = [
        ('Estudo/Pesquisa', 'Estudo/Pesquisa'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


# ESTOQUE Marketing  -------------------------------------------------------------->

class modelFormAcessoriaMK(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Apoio em roteiro para vídeo', 'Apoio em roteiro para vídeo'),
        ('Cobertura de eventos (apoio)', 'Cobertura de eventos (apoio)'),
        ('Cobertura fotográfica', 'Cobertura fotográfica'),
        ('Criação de release', 'Criação de release'),
    ]

    CHOICES_Assunto = [
        ('Acessoria', 'Acessoria'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)
    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormDigitalMK(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Anúncio nas redes sociais', 'Anúncio nas redes sociais'),
        ('Criação de artes e textos para posts', 'Criação de artes e textos para posts'),
        ('Envio de e-mail marketing', 'Envio de e-mail marketing'),
    ]

    CHOICES_Assunto = [
        ('Comunicação Digital', 'Comunicação Digital'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormGraficaMK(forms.ModelForm):
    CHOICES_Servico = [
        ('', ''),
        ('Adaptação de peças', 'Adaptação de peças'),
        ('Criação de campanhas', 'Criação de campanhas'),
        ('Apresentação de power point', 'Apresentação de power point'),
    ]

    CHOICES_Assunto = [
        ('Criação gráfica', 'Criação gráfica'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Servico, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')



# ESTOQUE TI  -------------------------------------------------------------->

class ModelFormNotebook(forms.ModelForm):


    MEMORIA_RAM_CHOICES = [
        ('', ''),
        ('4GB', '4GB'),
        ('8GB', '8GB'),
        ('12GB', '12GB'),
        ('16GB', '16GB'),
    ]

    PROCESSADOR_CHOICES = [
        ('', ''),
        ('I3', 'I3'),
        ('I5', 'I5'),
        ('Ryzen 5', 'Ryzen 5'),
        ('Ryzen 7', 'Ryzen 7'),
    ]

    ARMAZENAMENTO_CHOICES = [
        ('', ''),
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
    ]

    GB_CHOICES = [
        ('', ''),
        ('120GB', '120GB'),
        ('240GB', '240GB'),
        ('256GB', '256GB'),
        ('480GB', '480GB'),
        ('512GB', '512GB'),
        ('1TB)', '1TB'),
    ]

    ANTIVIRUS_CHOICES = [
        ('', ''),
        ('Ativado', 'Ativado'),
        ('Desativado', 'Desativado'),
    ]

    STATUS_CHOICES = [
        ('', ''),
        ('ÓTIMO', 'ÓTIMO'),
        ('MUITO BOM', 'MUITO BOM'),
        ('BOM', 'BOM'),
        ('MEDIANO', 'MEDIANO'),
        ('RUIM', 'RUIM'),
        ('MUITO RUIM', 'MUITO RUIM'),
    ]

    memoria_ram = forms.ChoiceField(choices=MEMORIA_RAM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    processador = forms.ChoiceField(choices=PROCESSADOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    armazenamento = forms.ChoiceField(choices=ARMAZENAMENTO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    gb = forms.ChoiceField(choices=GB_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    antiVirus = forms.ChoiceField(choices=ANTIVIRUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    usuario = forms.ModelChoiceField(queryset=User.objects.all().order_by('username'), label='Usuário', widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = Notebook
        fields = (
            'modelo', 'marca', 'processador', 'geracao', 'memoria_ram', 'armazenamento', 'gb', 'usuario', 'setor',
            'unidade', 'serviceTag', 'antiVirus', 'chaveWin', 'chaveOffice', 'status', )


        widgets = {'modelo': forms.TextInput(attrs={'class': 'form-control'}),
                   'marca': forms.TextInput(attrs={'class': 'form-control'}),
                   'processador': forms.Select(attrs={'class': 'form-control'}),
                   'geracao': forms.TextInput(attrs={'class': 'form-control'}),
                   'memoria_ram': forms.Select(attrs={'class': 'form-control'}),
                   'armazenamento': forms.Select(attrs={'class': 'form-control'}),
                   'gb': forms.Select(attrs={'class': 'form-control'}),
                   'status': forms.Select(attrs={'class': 'form-control'}),
                   'usuario': forms.Select(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'setor': forms.TextInput(attrs={'class': 'form-control'}),
                   'unidade': forms.TextInput(attrs={'class': 'form-control'}),
                   'serviceTag': forms.TextInput(attrs={'class': 'form-control'}),
                   'antiVirus': forms.TextInput(attrs={'class': 'form-control'}),
                   'chaveWin': forms.TextInput(attrs={'class': 'form-control'}),
                   'chaveOffice': forms.TextInput(attrs={'class': 'form-control'}),

                   }

    def __init__(self, *args, **kwargs):
        super(ModelFormNotebook, self).__init__(*args, **kwargs)

        # Tornar os campos não obrigatórios
        self.fields['serviceTag'].required = False

        self.fields['chaveWin'].required = False
        self.fields['chaveOffice'].required = False


class ModelFormMalotes(forms.ModelForm):

    assunto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
        required=True
    )
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormPS(forms.ModelForm):

    assunto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


# -------RH---------------------------------------------------------------------------------------------------------

class ModelFormRhEtica(forms.ModelForm):


    CHOICES_Assunto = [
        ('Violações ao Pacto de Ética', 'Violações ao Pacto de Ética'),
    ]

    CHOICES_Service = [
        ('', ''),
        ('Descumprimento de leis, políticas, normas ou definições estratégicas', 'Descumprimento de leis, políticas, normas ou definições estratégicas'),
        ('Destruição, danos ou mau uso do patrimônio da empresa', 'Destruição, danos ou mau uso do patrimônio da empresa'),
        ('Desvio de conduta ou comportamento', 'Desvio de conduta ou comportamento'),
        ('Home office', 'Home office'),
        ('Ocorrências de fraudes', 'Ocorrências de fraudes'),
        ('Outras ocorrências', 'Outras ocorrências'),
        ('Promoções, benefícios dos empregados e horas-extras', 'Promoções, benefícios dos empregados e horas-extras'),
        ('recebimento de brindes, favorecimentos ou conflito de interesses', 'recebimento de brindes, favorecimentos ou conflito de interesses'),
        ('Uso ou tráfico de substâncias proibidas', 'Uso ou tráfico de substâncias proibidas'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_Service, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class modelFormRhFerias(forms.ModelForm):

    CHOICES_Assunto = [
        ('Férias', 'Férias'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service =forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}),
        required=False
    )
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)
    class Meta:
        model = Card
        fields = ('assunto', 'service', 'date', 'descricao', 'attachment',)

# -------Secretaria---------------------------------------------------------------------------------------------------------


class ModelFormGestaoRisco(forms.ModelForm):



    CHOICES_Assunto = [
        ('Análise de PLD/FT', 'Análise de PLD/FT'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormAcessosGR(forms.ModelForm):
    CHOICES_ServicoAcessos = [
        ('', ''),
        ('Portifólio de crédito', 'Portifólio de crédito'),
    ]

    CHOICES_AssuntoAcessos = [
        ('', ''),
        ('Dúvidas em geral', 'Dúvidas em geral'),
        ('Inclusão de linhas', 'Inclusão de linhas'),
        ('Alteração nas linhas', 'Alteração nas linhas'),
        ('Sugestões', 'Sugestões'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_AssuntoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_ServicoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormBasileiaGR(forms.ModelForm):
    CHOICES_ServicoAcessos = [
        ('', ''),
        ('Dúvidas em geral', 'Dúvidas em geral'),
        ('Inclusão de modalidade', 'Inclusão de modalidade'),
        ('Alteração nas taxas', 'Alteração nas taxas'),
        ('Sugestões', 'Sugestões'),
    ]

    CHOICES_AssuntoAcessos = [
        ('', ''),
        ('Portifólio de Investimentos', 'Portifólio de Investimentos '),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_AssuntoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_ServicoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormRiscoGR(forms.ModelForm):
    CHOICES_ServicoAcessos = [
        ('', ''),
        ('Dúvidas em geral', 'Dúvidas em geral'),
        ('Estudos a cerca dos impactos', 'Estudos a cerca dos impactos'),
        ('Sugestões', 'Sugestões'),
    ]

    CHOICES_AssuntoAcessos = [
        ('', ''),
        ('Planilha de Monitoramento do Risco', 'Planilha de Monitoramento do Risco'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_AssuntoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_ServicoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormContabilidadeGR(forms.ModelForm):
    CHOICES_ServicoAcessos = [
        ('', ''),
        ('Dúvidas acerca do resultado contábil', 'Dúvidas acerca do resultado contábil'),
        ('Sugestões', 'Sugestões'),
    ]

    CHOICES_AssuntoAcessos = [
        ('', ''),
        ('Plano de Metas', 'Plano de Metas'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_AssuntoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_ServicoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    attachment = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment')


class modelFormClock(forms.ModelForm):

    CHOICES_ServicoAcessos = [
        ('', ''),
        ('30MIN', '30MIN'),
        ('1H', '1H'),
        ('1:30H', '1:30H'),
        ('2H', '2H'),
        ('3H', '3H'),
        ('5D', '5D'),
    ]

    CHOICES_AssuntoAcessos = [
        ('', ''),
        ('30MIN', '30MIN'),
        ('1H', '1H'),
        ('1:30H', '1:30H'),
        ('2H', '2H'),
        ('3H', '3H'),
        ('5D', '5D'),
    ]

    CHOICES_ProcessoEnd = [
        ('', ''),
        ('30MIN', '30MIN'),
        ('1H', '1H'),
        ('1:30H', '1:30H'),
        ('2H', '2H'),
        ('3H', '3H'),
        ('5D', '5D'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_AssuntoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.ChoiceField(choices=CHOICES_ServicoAcessos, widget=forms.Select(attrs={'class': 'form-select'}))
    finalizados = forms.ChoiceField(choices=CHOICES_ProcessoEnd, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Card
        fields = ('assunto', 'service')


