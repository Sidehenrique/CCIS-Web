# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import os


class Arquivoatestadoadmissional(models.Model):
    idarquivoatestadoadmissional = models.AutoField(db_column='idArquivoAtestadoAdmissional', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivoatestadoadmissional'


class Arquivoatestadoperiodico(models.Model):
    idarquivoatestadoperiodico = models.AutoField(db_column='idArquivoAtestadoPeriodico', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivoatestadoperiodico'


class Arquivocarteiradetrabalho(models.Model):
    idarquivocarteiradetrabalho = models.AutoField(db_column='idArquivoCarteiraDeTrabalho', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivocarteiradetrabalho'


class Arquivocertidao(models.Model):
    idarquivocertidao = models.AutoField(db_column='idArquivoCertidao', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivocertidao'


class Arquivocnh(models.Model):
    idarquivocnh = models.AutoField(db_column='idArquivoCnh', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivocnh'


class Arquivocomprovanteresidencia(models.Model):
    idarquivocomprovanteresidencia = models.AutoField(db_column='idArquivoComprovanteResidencia', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivocomprovanteresidencia'


class Arquivocpf(models.Model):
    idarquivocpf = models.AutoField(db_column='idArquivoCpf', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivocpf'


class Arquivoreservista(models.Model):
    idarquivoreservista = models.AutoField(db_column='idArquivoReservista', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivoreservista'


class Arquivorg(models.Model):
    idarquivorg = models.AutoField(db_column='idArquivoRg', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivorg'


class Arquivotitulodeeleitor(models.Model):
    idarquivotitulodeeleitor = models.AutoField(db_column='idArquivoTituloDeEleitor', primary_key=True)  # Field name made lowercase.
    data = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivotitulodeeleitor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Certificacao(models.Model):
    idcertificacao = models.AutoField(db_column='idCertificacao', primary_key=True)  # Field name made lowercase.
    certificacao = models.CharField(max_length=45, blank=True, null=True)
    dataconclusao = models.CharField(db_column='dataConclusao', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cargahoraria = models.CharField(db_column='cargaHoraria', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificacao'


class Dadosbancarios(models.Model):
    iddadosbancarios = models.AutoField(db_column='idDadosBancarios', primary_key=True)  # Field name made lowercase.
    banco = models.CharField(max_length=45, blank=True, null=True)
    tipodeconta = models.CharField(db_column='tipoDeConta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    modalidade = models.CharField(max_length=45, blank=True, null=True)
    agencia = models.CharField(max_length=45, blank=True, null=True)
    conta = models.CharField(max_length=45, blank=True, null=True)
    digitodaconta = models.CharField(db_column='digitoDaConta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    chavepix = models.CharField(db_column='chavePix', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dadosbancarios'


class Dadospessoais(models.Model):
    iddadospessoais = models.AutoField(db_column='idDadosPessoais', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(db_column='nomeCompleto', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    expedidor = models.CharField(max_length=45, blank=True, null=True)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    datanascimento = models.CharField(db_column='dataNascimento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idade = models.CharField(max_length=45, blank=True, null=True)
    estadocivil = models.CharField(db_column='estadoCivil', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nomepai = models.CharField(db_column='nomePai', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nomemae = models.CharField(db_column='nomeMae', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ctps = models.CharField(max_length=45, blank=True, null=True)
    datactps = models.CharField(db_column='dataCTPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    seriectps = models.CharField(db_column='serieCTPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    corraca = models.CharField(db_column='corRaca', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tiposanguineo = models.CharField(db_column='tipoSanguineo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    naturalidade = models.CharField(max_length=45, blank=True, null=True)
    cnh = models.CharField(max_length=45, blank=True, null=True)
    categoria = models.CharField(max_length=45, blank=True, null=True)
    validadecnh = models.CharField(db_column='validadeCnh', max_length=45, blank=True, null=True)  # Field name made lowercase.
    titulodeeleitor = models.CharField(db_column='tituloDeEleitor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(max_length=45, blank=True, null=True)
    secao = models.CharField(max_length=45, blank=True, null=True)
    pis = models.CharField(max_length=45, blank=True, null=True)
    reservista = models.CharField(max_length=45, blank=True, null=True)
    seriereservista = models.CharField(db_column='serieReservista', max_length=45, blank=True, null=True)  # Field name made lowercase.
    carteiranacionaldesaude = models.CharField(db_column='carteiraNacionalDeSaude', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pessoacomdeficiencia = models.CharField(db_column='pessoaComDeficiencia', max_length=45, blank=True, null=True)  # Field name made lowercase.
    avatar = models.ImageField(upload_to='ccis/midia/', null=True, blank=True)
    canvas = models.ImageField(upload_to='ccis/midia/', null=True, blank=True)
    escolaridade_idescolaridade = models.ForeignKey('Escolaridade', models.DO_NOTHING, db_column='escolaridade_idEscolaridade', blank=True, null=True)  # Field name made lowercase.
    profissional_idprofissional = models.ForeignKey('Profissional', models.DO_NOTHING, db_column='profissional_idProfissional', blank=True, null=True)  # Field name made lowercase.
    outros_idoutros = models.ForeignKey('Outros', models.DO_NOTHING, db_column='outros_idOutros', blank=True, null=True)  # Field name made lowercase.
    certificacao_idcertificacao = models.ForeignKey(Certificacao, models.DO_NOTHING, db_column='certificacao_idCertificacao', blank=True, null=True)  # Field name made lowercase.
    arquivoatestadoadmissional_idarquivoatestadoadmissional = models.ForeignKey(Arquivoatestadoadmissional, models.DO_NOTHING, db_column='arquivoAtestadoAdmissional_idArquivoAtestadoAdmissional', blank=True, null=True)  # Field name made lowercase.
    arquivocomprovanteresidencia_idarquivocomprovanteresidencia = models.ForeignKey(Arquivocomprovanteresidencia, models.DO_NOTHING, db_column='arquivoComprovanteResidencia_idArquivoComprovanteResidencia', blank=True, null=True)  # Field name made lowercase.
    arquivotitulodeeleitor_idarquivotitulodeeleitor = models.ForeignKey(Arquivotitulodeeleitor, models.DO_NOTHING, db_column='arquivoTituloDeEleitor_idArquivoTituloDeEleitor', blank=True, null=True)  # Field name made lowercase.
    arquivocnh_idarquivocnh = models.ForeignKey(Arquivocnh, models.DO_NOTHING, db_column='arquivoCnh_idArquivoCnh', blank=True, null=True)  # Field name made lowercase.
    arquivorg_idarquivorg = models.ForeignKey(Arquivorg, models.DO_NOTHING, db_column='arquivoRg_idArquivoRg', blank=True, null=True)  # Field name made lowercase.
    arquivocpf_idarquivocpf = models.ForeignKey(Arquivocpf, models.DO_NOTHING, db_column='arquivoCpf_idArquivoCpf', blank=True, null=True)  # Field name made lowercase.
    dadosbancarios_iddadosbancarios = models.ForeignKey(Dadosbancarios, models.DO_NOTHING, db_column='dadosBancarios_idDadosBancarios', blank=True, null=True)  # Field name made lowercase.
    dependentes_iddependentes = models.ForeignKey('Dependentes', models.DO_NOTHING, db_column='dependentes_idDependentes', blank=True, null=True)  # Field name made lowercase.
    enderecoecontato_idenderecoecontato = models.ForeignKey('Enderecoecontato', models.DO_NOTHING, db_column='enderecoEContato_idEnderecoEContato', blank=True, null=True)  # Field name made lowercase.
    arquivoatestadoperiodico_idarquivoatestadoperiodico = models.ForeignKey(Arquivoatestadoperiodico, models.DO_NOTHING, db_column='arquivoAtestadoPeriodico_idArquivoAtestadoPeriodico', blank=True, null=True)  # Field name made lowercase.
    arquivocertidao_idarquivocertidao = models.ForeignKey(Arquivocertidao, models.DO_NOTHING, db_column='arquivoCertidao_idArquivoCertidao', blank=True, null=True)  # Field name made lowercase.
    arquivocarteiradetrabalho_idarquivocarteiradetrabalho = models.ForeignKey(Arquivocarteiradetrabalho, models.DO_NOTHING, db_column='arquivoCarteiraDeTrabalho_idArquivoCarteiraDeTrabalho', blank=True, null=True)  # Field name made lowercase.
    arquivoreservista_idarquivoreservista = models.ForeignKey(Arquivoreservista, models.DO_NOTHING, db_column='arquivoReservista_idArquivoReservista', blank=True, null=True)  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_idUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dadospessoais'


class Dependentes(models.Model):
    iddependentes = models.AutoField(db_column='idDependentes', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(db_column='nomeCompleto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    relacao = models.CharField(max_length=45, blank=True, null=True)
    datanascimento = models.CharField(db_column='dataNascimento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(max_length=45, blank=True, null=True)
    nomemae = models.CharField(db_column='nomeMae', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependentes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enderecoecontato(models.Model):
    idenderecoecontato = models.AutoField(db_column='idEnderecoEContato', primary_key=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=45, blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    cep = models.CharField(max_length=45, blank=True, null=True)
    emailcorporativo = models.CharField(db_column='emailCorporativo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefonepessoal = models.CharField(db_column='telefonePessoal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefonecorporativo = models.CharField(db_column='telefoneCorporativo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celularcorporativo = models.CharField(db_column='celularCorporativo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celularpessoal = models.CharField(db_column='celularPessoal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ramal = models.CharField(max_length=45, blank=True, null=True)
    emailpessoal = models.CharField(db_column='emailPessoal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contatodeemergencia = models.CharField(db_column='contatoDeEmergencia', max_length=45, blank=True, null=True)  # Field name made lowercase.
    relacao = models.CharField(max_length=45, blank=True, null=True)
    telefonedeemergencia = models.CharField(db_column='telefoneDeEmergencia', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celulardeemergencia = models.CharField(db_column='celularDeEmergencia', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enderecoecontato'


class Escolaridade(models.Model):
    idescolaridade = models.AutoField(db_column='idEscolaridade', primary_key=True)  # Field name made lowercase.
    escolaridade = models.CharField(max_length=45, blank=True, null=True)
    entidadedeensino = models.CharField(db_column='entidadeDeEnsino', max_length=45, blank=True, null=True)  # Field name made lowercase.
    areadeensino = models.CharField(db_column='areaDeEnsino', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dataconclusao = models.CharField(db_column='dataConclusao', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idiomaprimario = models.CharField(db_column='idiomaPrimario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idiomasecundario = models.CharField(db_column='idiomaSecundario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nivelprimario = models.CharField(db_column='nivelPrimario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nivelsecundario = models.CharField(db_column='nivelSecundario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'escolaridade'


class Outros(models.Model):
    idoutros = models.AutoField(db_column='idOutros', primary_key=True)  # Field name made lowercase.
    camiseta = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outros'


class Profissional(models.Model):
    idprofissional = models.AutoField(db_column='idProfissional', primary_key=True)  # Field name made lowercase.
    cargo = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    paunidade = models.CharField(db_column='paUnidade', max_length=45, blank=True, null=True)  # Field name made lowercase.
    colaborador = models.CharField(max_length=60, blank=True, null=True)
    centrodecusto = models.CharField(db_column='centroDeCusto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    matricula = models.CharField(max_length=45, blank=True, null=True)
    empregador = models.CharField(max_length=45, blank=True, null=True)
    superiorimediato = models.CharField(db_column='superiorImediato', max_length=45, blank=True, null=True)  # Field name made lowercase.
    folhadepagamento = models.CharField(db_column='folhaDePagamento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    admissao = models.CharField(max_length=45, blank=True, null=True)
    desligamento = models.CharField(max_length=45, blank=True, null=True)
    situacao = models.CharField(max_length=45, blank=True, null=True)
    horarioentrada = models.CharField(db_column='horarioEntrada', max_length=45, blank=True, null=True)  # Field name made lowercase.
    horariosaida = models.CharField(db_column='horarioSaida', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dataatesadmissional = models.CharField(db_column='dataAtesAdmissional', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dataatesperiodico = models.CharField(db_column='dataAtesPeriodico', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profissional'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    user = models.CharField(max_length=45, blank=True, null=True)
    senha = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    data = models.CharField(max_length=45, blank=True, null=True)
    foto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
