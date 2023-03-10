# Generated by Django 4.0.2 on 2023-03-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivoatestadoadmissional',
            fields=[
                ('idarquivoatestadoadmissional', models.AutoField(db_column='idArquivoAtestadoAdmissional', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivoatestadoadmissional',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivoatestadoperiodico',
            fields=[
                ('idarquivoatestadoperiodico', models.AutoField(db_column='idArquivoAtestadoPeriodico', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivoatestadoperiodico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivocarteiradetrabalho',
            fields=[
                ('idarquivocarteiradetrabalho', models.AutoField(db_column='idArquivoCarteiraDeTrabalho', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivocarteiradetrabalho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivocertidao',
            fields=[
                ('idarquivocertidao', models.AutoField(db_column='idArquivoCertidao', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivocertidao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivocnh',
            fields=[
                ('idarquivocnh', models.AutoField(db_column='idArquivoCnh', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivocnh',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivocomprovanteresidencia',
            fields=[
                ('idarquivocomprovanteresidencia', models.AutoField(db_column='idArquivoComprovanteResidencia', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivocomprovanteresidencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivocpf',
            fields=[
                ('idarquivocpf', models.AutoField(db_column='idArquivoCpf', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivocpf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivoreservista',
            fields=[
                ('idarquivoreservista', models.AutoField(db_column='idArquivoReservista', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivoreservista',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivorg',
            fields=[
                ('idarquivorg', models.AutoField(db_column='idArquivoRg', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivorg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivotitulodeeleitor',
            fields=[
                ('idarquivotitulodeeleitor', models.AutoField(db_column='idArquivoTituloDeEleitor', primary_key=True, serialize=False)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('arquivo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arquivotitulodeeleitor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Certificacao',
            fields=[
                ('idcertificacao', models.AutoField(db_column='idCertificacao', primary_key=True, serialize=False)),
                ('certificacao', models.CharField(blank=True, max_length=45, null=True)),
                ('dataconclusao', models.CharField(blank=True, db_column='dataConclusao', max_length=45, null=True)),
                ('cargahoraria', models.CharField(blank=True, db_column='cargaHoraria', max_length=45, null=True)),
            ],
            options={
                'db_table': 'certificacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dadosbancarios',
            fields=[
                ('iddadosbancarios', models.AutoField(db_column='idDadosBancarios', primary_key=True, serialize=False)),
                ('banco', models.CharField(blank=True, max_length=45, null=True)),
                ('tipodeconta', models.CharField(blank=True, db_column='tipoDeConta', max_length=45, null=True)),
                ('modalidade', models.CharField(blank=True, max_length=45, null=True)),
                ('agencia', models.CharField(blank=True, max_length=45, null=True)),
                ('conta', models.CharField(blank=True, max_length=45, null=True)),
                ('digitodaconta', models.CharField(blank=True, db_column='digitoDaConta', max_length=45, null=True)),
                ('chavepix', models.CharField(blank=True, db_column='chavePix', max_length=45, null=True)),
            ],
            options={
                'db_table': 'dadosbancarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dadospessoais',
            fields=[
                ('iddadospessoais', models.AutoField(db_column='idDadosPessoais', primary_key=True, serialize=False)),
                ('nomecompleto', models.CharField(blank=True, db_column='nomeCompleto', max_length=60, null=True)),
                ('cpf', models.CharField(blank=True, max_length=45, null=True)),
                ('rg', models.CharField(blank=True, max_length=45, null=True)),
                ('expedidor', models.CharField(blank=True, max_length=45, null=True)),
                ('sexo', models.CharField(blank=True, max_length=45, null=True)),
                ('datanascimento', models.CharField(blank=True, db_column='dataNascimento', max_length=45, null=True)),
                ('idade', models.CharField(blank=True, max_length=45, null=True)),
                ('estadocivil', models.CharField(blank=True, db_column='estadoCivil', max_length=45, null=True)),
                ('nomepai', models.CharField(blank=True, db_column='nomePai', max_length=60, null=True)),
                ('nomemae', models.CharField(blank=True, db_column='nomeMae', max_length=60, null=True)),
                ('ctps', models.CharField(blank=True, max_length=45, null=True)),
                ('datactps', models.CharField(blank=True, db_column='dataCTPS', max_length=45, null=True)),
                ('seriectps', models.CharField(blank=True, db_column='serieCTPS', max_length=45, null=True)),
                ('corraca', models.CharField(blank=True, db_column='corRaca', max_length=45, null=True)),
                ('tiposanguineo', models.CharField(blank=True, db_column='tipoSanguineo', max_length=45, null=True)),
                ('naturalidade', models.CharField(blank=True, max_length=45, null=True)),
                ('cnh', models.CharField(blank=True, max_length=45, null=True)),
                ('categoria', models.CharField(blank=True, max_length=45, null=True)),
                ('validadecnh', models.CharField(blank=True, db_column='validadeCnh', max_length=45, null=True)),
                ('titulodeeleitor', models.CharField(blank=True, db_column='tituloDeEleitor', max_length=45, null=True)),
                ('zona', models.CharField(blank=True, max_length=45, null=True)),
                ('secao', models.CharField(blank=True, max_length=45, null=True)),
                ('pis', models.CharField(blank=True, max_length=45, null=True)),
                ('reservista', models.CharField(blank=True, max_length=45, null=True)),
                ('seriereservista', models.CharField(blank=True, db_column='serieReservista', max_length=45, null=True)),
                ('carteiranacionaldesaude', models.CharField(blank=True, db_column='carteiraNacionalDeSaude', max_length=45, null=True)),
                ('pessoacomdeficiencia', models.CharField(blank=True, db_column='pessoaComDeficiencia', max_length=45, null=True)),
            ],
            options={
                'db_table': 'dadospessoais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dependentes',
            fields=[
                ('iddependentes', models.AutoField(db_column='idDependentes', primary_key=True, serialize=False)),
                ('nomecompleto', models.CharField(blank=True, db_column='nomeCompleto', max_length=45, null=True)),
                ('relacao', models.CharField(blank=True, max_length=45, null=True)),
                ('datanascimento', models.CharField(blank=True, db_column='dataNascimento', max_length=45, null=True)),
                ('cpf', models.CharField(blank=True, max_length=45, null=True)),
                ('nomemae', models.CharField(blank=True, db_column='nomeMae', max_length=45, null=True)),
                ('contato', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'dependentes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enderecoecontato',
            fields=[
                ('idenderecoecontato', models.AutoField(db_column='idEnderecoEContato', primary_key=True, serialize=False)),
                ('endereco', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(blank=True, max_length=45, null=True)),
                ('cidade', models.CharField(blank=True, max_length=45, null=True)),
                ('estado', models.CharField(blank=True, max_length=45, null=True)),
                ('cep', models.CharField(blank=True, max_length=45, null=True)),
                ('emailcorporativo', models.CharField(blank=True, db_column='emailCorporativo', max_length=45, null=True)),
                ('telefonepessoal', models.CharField(blank=True, db_column='telefonePessoal', max_length=45, null=True)),
                ('telefonecorporativo', models.CharField(blank=True, db_column='telefoneCorporativo', max_length=45, null=True)),
                ('celularcorporativo', models.CharField(blank=True, db_column='celularCorporativo', max_length=45, null=True)),
                ('celularpessoal', models.CharField(blank=True, db_column='celularPessoal', max_length=45, null=True)),
                ('ramal', models.CharField(blank=True, max_length=45, null=True)),
                ('emailpessoal', models.CharField(blank=True, db_column='emailPessoal', max_length=45, null=True)),
                ('contatodeemergencia', models.CharField(blank=True, db_column='contatoDeEmergencia', max_length=45, null=True)),
                ('relacao', models.CharField(blank=True, max_length=45, null=True)),
                ('telefonedeemergencia', models.CharField(blank=True, db_column='telefoneDeEmergencia', max_length=45, null=True)),
                ('celulardeemergencia', models.CharField(blank=True, db_column='celularDeEmergencia', max_length=45, null=True)),
            ],
            options={
                'db_table': 'enderecoecontato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('idescolaridade', models.AutoField(db_column='idEscolaridade', primary_key=True, serialize=False)),
                ('escolaridade', models.CharField(blank=True, max_length=45, null=True)),
                ('entidadedeensino', models.CharField(blank=True, db_column='entidadeDeEnsino', max_length=45, null=True)),
                ('areadeensino', models.CharField(blank=True, db_column='areaDeEnsino', max_length=45, null=True)),
                ('dataconclusao', models.CharField(blank=True, db_column='dataConclusao', max_length=45, null=True)),
                ('idiomaprimario', models.CharField(blank=True, db_column='idiomaPrimario', max_length=45, null=True)),
                ('idiomasecundario', models.CharField(blank=True, db_column='idiomaSecundario', max_length=45, null=True)),
                ('nivelprimario', models.CharField(blank=True, db_column='nivelPrimario', max_length=45, null=True)),
                ('nivelsecundario', models.CharField(blank=True, db_column='nivelSecundario', max_length=45, null=True)),
            ],
            options={
                'db_table': 'escolaridade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Outros',
            fields=[
                ('idoutros', models.AutoField(db_column='idOutros', primary_key=True, serialize=False)),
                ('camiseta', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'outros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('idprofissional', models.AutoField(db_column='idProfissional', primary_key=True, serialize=False)),
                ('cargo', models.CharField(blank=True, max_length=45, null=True)),
                ('area', models.CharField(blank=True, max_length=45, null=True)),
                ('paunidade', models.CharField(blank=True, db_column='paUnidade', max_length=45, null=True)),
                ('colaborador', models.CharField(blank=True, max_length=60, null=True)),
                ('centrodecusto', models.CharField(blank=True, db_column='centroDeCusto', max_length=45, null=True)),
                ('matricula', models.CharField(blank=True, max_length=45, null=True)),
                ('empregador', models.CharField(blank=True, max_length=45, null=True)),
                ('superiorimediato', models.CharField(blank=True, db_column='superiorImediato', max_length=45, null=True)),
                ('folhadepagamento', models.CharField(blank=True, db_column='folhaDePagamento', max_length=45, null=True)),
                ('admissao', models.CharField(blank=True, max_length=45, null=True)),
                ('desligamento', models.CharField(blank=True, max_length=45, null=True)),
                ('situacao', models.CharField(blank=True, max_length=45, null=True)),
                ('horarioentrada', models.CharField(blank=True, db_column='horarioEntrada', max_length=45, null=True)),
                ('horariosaida', models.CharField(blank=True, db_column='horarioSaida', max_length=45, null=True)),
                ('dataatesadmissional', models.CharField(blank=True, db_column='dataAtesAdmissional', max_length=45, null=True)),
                ('dataatesperiodico', models.CharField(blank=True, db_column='dataAtesPeriodico', max_length=45, null=True)),
            ],
            options={
                'db_table': 'profissional',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.AutoField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('user', models.CharField(blank=True, max_length=45, null=True)),
                ('senha', models.CharField(blank=True, max_length=45, null=True)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('data', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
