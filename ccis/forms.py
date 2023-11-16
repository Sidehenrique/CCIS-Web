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
    group = forms.ModelChoiceField(queryset=Group.objects.all())


# CHAMADOS TI  -------------------------------------------------------------->
class modelFormAcessosTI(forms.ModelForm):
    CHOICES_ServicoAcessos = [
        ('', ''),
        ('Criação', 'Criação'),
        ('Alteração', 'Alteração'),
        ('Redefinição', 'Redefinição'),
        ('Exclusão', 'Exclusão'),
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
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
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
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
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
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
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


class ModelFormRetaguardaMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormPS(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormFinanceiroMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormCadastroMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormAdmMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormCobrancaMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormRhMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


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
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormSecretariaMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormCreditoMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)

class ModelFormFormosaMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormPlanaltinaMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormPADFMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormVicenteMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormSJMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormSaoSebasMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormMarketMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormPCMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormGestaoRiscoMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormPaDigitalMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)


class ModelFormSIAMalotes(forms.ModelForm):


    CHOICES_Assunto = [
        ('Malote', 'Malote'),
    ]

    assunto = forms.ChoiceField(choices=CHOICES_Assunto, widget=forms.Select(attrs={'class': 'form-select'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 50}),
                                required=False)
    attachment = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
                                 required=False)

    class Meta:
        model = Card
        fields = ('assunto', 'service', 'descricao', 'attachment',)

