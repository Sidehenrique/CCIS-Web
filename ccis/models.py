from django.db import models
import os


class dadosPessoais(models.Model):
    idDadosPessoais = models.AutoField(db_column='idDadosPessoais', primary_key=True)
    nomeCompleto = models.CharField(db_column='nomeCompleto', max_length=60, blank=True, null=True)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    estadoCivil = models.CharField(db_column='estadoCivil', max_length=45, blank=True, null=True)
    corRaca = models.CharField(db_column='corRaca', max_length=45, blank=True, null=True)
    dataNascimento = models.DateField(db_column='dataNascimento', blank=True, null=True)
    naturalidade = models.CharField(max_length=45, blank=True, null=True)
    tipoSanguineo = models.CharField(db_column='tipoSanguineo', max_length=45, blank=True, null=True)

    nomePai = models.CharField(db_column='nomePai', max_length=60, blank=True, null=True)
    nomeMae = models.CharField(db_column='nomeMae', max_length=60, blank=True, null=True)

    cpf = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    expedidor = models.CharField(max_length=45, blank=True, null=True)
    cnh = models.CharField(max_length=45, blank=True, null=True)
    validadeCnh = models.DateField(db_column='validadeCnh', blank=True, null=True)
    categoria = models.CharField(max_length=45, blank=True, null=True)
    tituloEleitor = models.CharField(db_column='tituloEleitor', max_length=45, blank=True, null=True)
    zona = models.CharField(max_length=45, blank=True, null=True)
    secao = models.CharField(max_length=45, blank=True, null=True)
    ctps = models.CharField(max_length=45, blank=True, null=True)
    serieCTPS = models.CharField(db_column='serieCTPS', max_length=45, blank=True, null=True)
    dataCTPS = models.DateField(db_column='dataCTPS', blank=True, null=True)
    reservista = models.CharField(max_length=45, blank=True, null=True)
    ra = models.CharField(db_column='RA', max_length=45, blank=True, null=True)
    serieReservista = models.CharField(db_column='serieReservista', max_length=45, blank=True, null=True)
    pis = models.CharField(max_length=45, blank=True, null=True)
    cns = models.CharField(db_column='CNS', max_length=45, blank=True, null=True)
    pcd = models.CharField(db_column='PCD', max_length=45, blank=True, null=True)

    foto = models.ImageField(null=True, blank=True)
    canvas = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.idDadosPessoais

