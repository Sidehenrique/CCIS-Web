from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin

CHOICES_sexo = [
    ('', ''),
    ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino'),
]

CHOICES_estadoCivil = [
    ('', ''),
    ('Solteiro(a)', 'Solteiro(a)'),
    ('Casado(a)', 'Casado(a)'),
    ('Divorciado(a)', 'Divorciado(a)'),
    ('Viúvo(a)', 'Viúvo(a)'),
    ('Separado(a)', 'Separado(a)'),
    ('União Estável', 'União Estável'),
]

CHOICES_corRaca = [
    ('', ''),
    ('Amarelo', 'Amarelo'),
    ('Branco', 'Branco'),
    ('Indígena', 'Indígena'),
    ('Pardo', 'Pardo'),
    ('Preto', 'Preto'),
]

CHOICES_tipoSanguineo = [
    ('', ''),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
]

CHOICES_categoria = [
    ('', ''),
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
]


class dadosPessoais(models.Model):
    idDadosPessoais = models.AutoField(db_column='idDadosPessoais', primary_key=True)
    nomeCompleto = models.CharField(db_column='nomeCompleto', max_length=60, blank=False, null=True)
    sexo = models.CharField(choices=CHOICES_sexo, max_length=45, blank=False, null=True)
    estadoCivil = models.CharField(choices=CHOICES_estadoCivil, db_column='estadoCivil', max_length=45, blank=True,
                                   null=True)
    corRaca = models.CharField(choices=CHOICES_corRaca, db_column='corRaca', max_length=45, blank=True, null=True)
    dataNascimento = models.CharField(max_length=45, blank=True, null=True)
    naturalidade = models.CharField(max_length=45, blank=True, null=True)
    tipoSanguineo = models.CharField(choices=CHOICES_tipoSanguineo, db_column='tipoSanguineo', max_length=45,
                                     blank=True, null=True)

    nomePai = models.CharField(db_column='nomePai', max_length=60, blank=True, null=True)
    nomeMae = models.CharField(db_column='nomeMae', max_length=60, blank=True, null=True)

    cpf = models.CharField(max_length=11, blank=False, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    expedidor = models.CharField(max_length=45, blank=True, null=True)
    cnh = models.CharField(max_length=45, blank=True, null=True)
    validadeCnh = models.CharField(max_length=45, blank=True, null=True)
    categoria = models.CharField(choices=CHOICES_categoria, max_length=45, blank=True, null=True)
    tituloEleitor = models.CharField(db_column='tituloEleitor', max_length=45, blank=True, null=True)
    zona = models.CharField(max_length=45, blank=True, null=True)
    secao = models.CharField(max_length=45, blank=True, null=True)
    ctps = models.CharField(max_length=45, blank=True, null=True)
    serieCTPS = models.CharField(db_column='serieCTPS', max_length=45, blank=True, null=True)
    dataCTPS = models.CharField(max_length=45, blank=True, null=True)
    reservista = models.CharField(max_length=45, blank=True, null=True)
    ra = models.CharField(db_column='RA', max_length=45, blank=True, null=True)
    serieReservista = models.CharField(db_column='serieReservista', max_length=45, blank=True, null=True)
    pis = models.CharField(max_length=45, blank=True, null=True)
    cns = models.CharField(db_column='CNS', max_length=45, blank=True, null=True)
    pcd = models.CharField(db_column='PCD', max_length=45, blank=True, null=True)

    foto = models.ImageField(upload_to='users', null=True, blank=True)
    canvas = models.ImageField(upload_to='canvas', null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='dadosPessoais')

    def __str__(self):
        return self.nomeCompleto


CHOICES_relacao = [
    ('', ''),
    ('Cônjuge', 'Cônjuge'),
    ('Filho(a)', 'Filho(a)'),
    ('Pais', 'Pais'),
    ('Outros', 'Outros'),
]

CHOICES_declaracao = [
    ('', ''),
    ('Sim', 'Sim'),
    ('Não', 'Não'),

]


class dependentes(models.Model):
    idDependentes = models.AutoField(db_column='idDependentes', primary_key=True)
    nomeCompleto = models.CharField(db_column='nomeCompleto', max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    dataNascimento = models.CharField(max_length=45, blank=True, null=True)
    relacao = models.CharField(choices=CHOICES_relacao, max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True, null=True)
    contato = models.CharField(max_length=45, blank=True, null=True)
    declaracao = models.CharField(choices=CHOICES_declaracao, max_length=45, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='dependentes')

    def __str__(self):
        return self.nomeCompleto


CHOICES_estado = [
    ('', ''),
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),

]


class enderecoContato(models.Model):
    idEndereCoecontato = models.AutoField(db_column='idEnderecoEContato', primary_key=True)
    endereco = models.CharField(db_column='endereco', max_length=100, blank=True, null=True)
    bairro = models.CharField(db_column='bairro', max_length=45, blank=True, null=True)
    cidade = models.CharField(db_column='cidade', max_length=45, blank=True, null=True)
    estado = models.CharField(choices=CHOICES_estado, db_column='estado', max_length=45, blank=True, null=True)
    cep = models.CharField(db_column='cep', max_length=45, blank=True, null=True)
    emailCorporativo = models.CharField(db_column='emailCorporativo', max_length=45, blank=True, null=True)
    telefonePessoal = models.CharField(db_column='telefonePessoal', max_length=45, blank=True, null=True)
    telefoneCorporativo = models.CharField(db_column='telefoneCorporativo', max_length=45, blank=True, null=True)
    celularCorporativo = models.CharField(db_column='celularCorporativo', max_length=45, blank=True, null=True)
    celularPessoal = models.CharField(db_column='celularPessoal', max_length=45, blank=True, null=True)
    ramal = models.CharField(db_column='ramal', max_length=45, blank=True, null=True)
    emailPessoal = models.EmailField(db_column='emailPessoal', max_length=45, blank=True, null=True)
    relacao = models.CharField(choices=CHOICES_relacao, max_length=45, blank=True, null=True)

    nomeCompleto = models.CharField(db_column='nomeCompleto', max_length=45, blank=True, null=True)
    telefoneDeEmergencia = models.CharField(db_column='telefoneDeEmergencia', max_length=45, blank=True, null=True)
    celularDeEmergencia = models.CharField(db_column='celularDeEmergencia', max_length=45, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='enderecoContato')

    def __str__(self):
        return self.emailCorporativo


CHOICES_nivelSecundario = [
    ('', ''),
    ('Básico', 'Básico'),
    ('Intermediário', 'Intermediário'),
    ('Avançado', 'Avançado'),
]

CHOICES_grau = [
    ('', ''),
    ('Graduação', 'Graduação'),
    ('Pós-Graduação', 'Pós-Graduação'),
    ('Mestrado', 'Mestrado'),
    ('Doutorado', 'Doutorado')
]


class escolaridade(models.Model):
    idEscolaridade = models.AutoField(db_column='idEscolaridade', primary_key=True)
    entidadeDeEnsino = models.CharField(db_column='entidadeDeEnsino', max_length=45, blank=True, null=True)
    curso = models.CharField(db_column='curso', max_length=45, blank=True, null=True)
    grau = models.CharField(choices=CHOICES_grau, db_column='grau', max_length=45, blank=True, null=True)
    dataInicio = models.CharField(max_length=45, blank=True, null=True)
    dataConclusao = models.CharField(max_length=45, blank=True, null=True)
    idiomaSecundario = models.CharField(db_column='idiomaSecundario', max_length=45, blank=True, null=True)
    nivelSecundario = models.CharField(choices=CHOICES_nivelSecundario, db_column='nivelSecundario', max_length=45,
                                       blank=True, null=True)
    docEscolaridade = models.FileField(upload_to='certificados', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='escolaridade')

    def __str__(self):
        return self.entidadeDeEnsino


CHOICES_anbima = [
    ('', ''),
    ('CPA-10', 'CPA-10'),
    ('CPA-20', 'CPA-20'),
    ('CEA', 'CEA'),
    ('Não possuo', 'Não possuo'),
]


class certificacao(models.Model):
    idCertificacao = models.AutoField(db_column='idCertificacao', primary_key=True)
    nome = models.CharField(db_column='nome', max_length=45, blank=True, null=True)
    organizacaoEmissora = models.CharField(db_column='organizacaoEmissora', max_length=45, blank=True, null=True)
    dataEmissao = models.CharField(max_length=45, blank=True, null=True)
    dataExpiracao = models.CharField(max_length=45, blank=True, null=True)
    docCertificado = models.FileField(upload_to='certificados', null=True, blank=True)
    certiAnbima = models.CharField(choices=CHOICES_anbima, max_length=45, blank=True, null=True)
    anexoAnbima = models.FileField(upload_to='certificados', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='certificacao')

    def __str__(self):
        return self.nome


CHOICES_paUnidade = [
    ('', ''),
    ('00-SIA', '00-SIA'),
    ('01-PADF', '01-PADF'),
    ('02-FSA', '02-FSA'),
    ('03-SJA', '03-SJA'),
    ('06-PLA', '06-PLA'),
    ('07-VIP', '07-VIP'),
    ('08-AGC', '08-AGC'),
    ('09-SSB', '09-SSB'),
    ('97-DIG', '97-DIG'),
    ('98-OPE', '98-OPE'),
    ('99-UAD', '99-UAD'),
]

CHOICES_colaborador = [
    ('', ''),
    ('Funcionário(a)', 'Funcionário(a)'),
    ('Tercerizado(a)', 'Tercerizado(a)'),
    ('Estagiário(a)', 'Estagiário(a)'),
    ('Menor Aprendiz', 'Menor Aprendiz'),
    ('Diretoria Executiva', 'Diretoria Executiva'),
    ('Diretoria Administrativa', 'Diretoria Administrativa'),
    ('Conselho Fiscal', 'Conselho Fiscal'),
    ('Conselho de Administração', 'Conselho de Administração'),
]

CHOICES_situacao = [
    ('', ''),
    ('Ativo', 'Ativo'),
    ('Inativo', 'Inativo'),
]

CHOICES_empregador = [
    ('', ''),
    ('Sicoob Credibrasília', 'Sicoob Credibrasília'),
    ('Life Defense', 'Life Defense'),
    ('BS Soares', 'BS Soares'),
]


class profissional(models.Model):
    idProfissional = models.AutoField(db_column='idProfissional', primary_key=True)
    cargo = models.CharField(max_length=45, blank=False, null=True)
    area = models.CharField(max_length=45, blank=False, null=True)
    paUnidade = models.CharField(choices=CHOICES_paUnidade, db_column='paUnidade', max_length=45, blank=True, null=True)
    colaborador = models.CharField(choices=CHOICES_colaborador, max_length=60, blank=True, null=True)
    centroDeCusto = models.CharField(db_column='centroDeCusto', max_length=45, blank=True, null=True)
    matricula = models.CharField(max_length=45, blank=True, null=True)
    empregador = models.CharField(choices=CHOICES_empregador, max_length=45, blank=True, null=True)
    superiorImediato = models.CharField(max_length=45, blank=True, null=True)
    folhaDePagamento = models.CharField(max_length=45, blank=True, null=True)
    admissao = models.CharField(max_length=45, blank=True, null=True)
    desligamento = models.CharField(max_length=45, blank=True, null=True)
    situacao = models.CharField(choices=CHOICES_situacao, max_length=45, blank=False, null=True)
    horarioEntrada = models.TimeField(db_column='horarioEntrada', max_length=45, blank=True, null=True)
    horarioSaida = models.TimeField(db_column='horarioSaida', max_length=45, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='profissional')

    def __str__(self):
        return self.cargo


CHOICES_tipoDeConta = [
    ('', ''),
    ('Conta Corrente', 'Conta Corrente'),
    ('Conta Poupança', 'Conta Poupança'),
    ('Conta Salário', 'Conta Salário'),
]


class dadosBancarios(models.Model):
    idDadosBancarios = models.AutoField(db_column='idDadosBancarios', primary_key=True)
    conta = models.CharField(max_length=45, blank=True, null=True)
    digito = models.CharField(db_column='digitoDaConta', max_length=45, blank=True, null=True)
    banco = models.CharField(max_length=45, blank=True, null=True)
    agencia = models.CharField(max_length=45, blank=True, null=True)
    tipoDeConta = models.CharField(choices=CHOICES_tipoDeConta, db_column='tipoDeConta', max_length=45, blank=True,
                                   null=True)
    modalidade = models.CharField(max_length=45, blank=True, null=True)
    chavePix = models.CharField(db_column='chavePix', max_length=45, blank=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='dadosBancarios')

    def __str__(self):
        return self.conta


CHOICES_tamanho = [
    ('', ''),
    ('PP', 'PP'),
    ('P', 'P'),
    ('M', 'M'),
    ('G', 'G'),
    ('GG', 'GG'),
    ('XG', 'XG'),
]


class outros(models.Model):
    idOutros = models.AutoField(db_column='idOutros', primary_key=True)
    camiseta = models.CharField(choices=CHOICES_tamanho, max_length=45, blank=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='outros')

    def __str__(self):
        return self.camiseta


# DOCUMENTOS----------------------------------------------------------
class docRg(models.Model):
    idRg = models.AutoField(db_column='idRg', primary_key=True)
    documentoRg = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docRg')

    def __str__(self):
        return self.documentoRg


class docCnh(models.Model):
    idCnh = models.AutoField(db_column='idCnh', primary_key=True)
    documentoCnh = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docCnh')

    def __str__(self):
        return self.documentoCnh


class docCpf(models.Model):
    idCpf = models.AutoField(db_column='idCpf', primary_key=True)
    documentoCpf = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docCpf')

    def __str__(self):
        return self.documentoCpf


class docReservista(models.Model):
    idReservista = models.AutoField(db_column='idReservista', primary_key=True)
    documentoReservista = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docReservista')

    def __str__(self):
        return self.documentoReservista


class docTitulo(models.Model):
    idTitulo = models.AutoField(db_column='idTitulo', primary_key=True)
    documentoTitulo = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docTitulo')

    def __str__(self):
        return self.documentoTitulo


class docClt(models.Model):
    idClt = models.AutoField(db_column='idClt', primary_key=True)
    documentoClt = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docClt')

    def __str__(self):
        return self.documentoClt


class docResidencia(models.Model):
    idResidencia = models.AutoField(db_column='idResidencia', primary_key=True)
    documentoResidencia = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docResidencia')

    def __str__(self):
        return self.documentoResidencia


class docCertidao(models.Model):
    idCertidao = models.AutoField(db_column='idCertidao', primary_key=True)
    documentoCertidao = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docCertidao')

    def __str__(self):
        return self.documentoCertidao


class docAdmissional(models.Model):
    idAdmissional = models.AutoField(db_column='idAdmissional', primary_key=True)
    documentoAdmissional = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docAdmissional')

    def __str__(self):
        return self.documentoAdmissional


class docPeriodico(models.Model):
    idPeriodico = models.AutoField(db_column='idPeriodico', primary_key=True)
    documentoPeriodico = models.FileField(upload_to='documents', null=True, blank=True)
    dataAtualizacao = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True, auto_now=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='docPeriodico')

    def __str__(self):
        return self.documentoPeriodico


class docCursos(models.Model):
    idCursos = models.AutoField(db_column='idCursos', primary_key=True)
    curso = models.CharField(max_length=45, blank=True, null=True)
    certiCurso = models.FileField(upload_to='cursos', null=True, blank=True)
    data = models.DateField(db_column='dataAtualizacao', max_length=45, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='docCursos')

    def __str__(self):
        return self.certiCurso


# ------------------- Botões ---------------------------------------------------------------------------
class SectorButtons(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    text1 = models.CharField(max_length=45, blank=True, null=True)
    text2 = models.CharField(max_length=45, blank=True, null=True)
    cor = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=45, blank=True, null=True)
    permissao = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.group.name


# ------------------- tabela Notificação -----------------------------------------------------------------

class Notification(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorNotification', default=None)
    description = models.TextField()
    subject = models.CharField(max_length=255)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_received')
    department = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.description


# ------------------- tabela Group ---------------------------------------------------------------------

class CustomGroupInfo(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    sigla = models.CharField(max_length=45, blank=True, null=True)
    nome = models.CharField(max_length=45, blank=True, null=True)
    cor = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True, null=True)
    ramal = models.CharField(max_length=45, blank=True, null=True)
    contato = models.CharField(max_length=45, blank=True, null=True)
    imagem = models.ImageField(upload_to='group/', blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    url_home = models.URLField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    periodo_arquivamento = models.IntegerField(default=10)

    def __str__(self):
        return self.group.name


# -------- Tabelas de Processo --------------------------------------------------------------------------
class Card(models.Model):
    idCard = models.AutoField(db_column='idCard', primary_key=True)
    assunto = models.CharField(max_length=45, blank=False, null=True)
    service = models.CharField(max_length=255, blank=False, null=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chamados_solicitados', default=None)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='chamados_responsaveis', default=None)
    setor = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, default='Triagem')
    compartilhar = models.ManyToManyField(User, related_name="cards_compartilhados", blank=True)
    anonymous = models.BooleanField(default=False)
    cor = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.assunto


class MessageHistory(models.Model):
    idMessageHistory = models.AutoField(db_column='idMessageHistory', primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    remetente = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    attachment = models.ImageField(upload_to='chat/', null=True, blank=True)  # Alterado para ImageField

    def __str__(self):
        return self.message


class CardSetorHistory(models.Model):
    idCardSetorHistory = models.AutoField(db_column='idCardSetorHistory', primary_key=True)
    setor = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    status_anterior = models.CharField(max_length=100, null=True, blank=True)
    status_atual = models.CharField(max_length=100)
    setor_anterior = models.CharField(max_length=100, null=True, blank=True)
    setor_atual = models.CharField(max_length=100)
    operador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name='operador_history', default=None)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.setor_atual


class OperatorRating(models.Model):
    idOperatorRating = models.AutoField(db_column='idOperatorRating', primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    rating = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    operador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='avaliacao_user', default=None)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    anonymous = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='avaliador_anonimo', default=None)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.operador


# -------- Estoque ------------------------------------------------------------------------------------------------------

class Notebook(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='Notebook')
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    processador = models.CharField(max_length=100)
    geracao = models.CharField(max_length=100)
    memoria_ram = models.CharField(max_length=100)
    armazenamento = models.CharField(max_length=100)
    gb = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    email = models.EmailField()
    serviceTag = models.CharField(max_length=100)
    antiVirus = models.CharField(max_length=100)
    chaveWin = models.CharField(max_length=100)
    chaveOffice = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo


#-------------------------------------------------------------------------------------

class Cupons(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de modificação', auto_now=True)
    cpf = models.CharField('CPF', max_length=14)
    numero_cupom = models.CharField('Numero Cupom', max_length=5, unique=True)

    def __str__(self):
        return self.cpf


#-------------------------------------------------------------------------------------

class KanbanGroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group.id} - {self.group.name}"


