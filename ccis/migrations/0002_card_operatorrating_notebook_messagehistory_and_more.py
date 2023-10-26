# Generated by Django 4.2 on 2023-10-24 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ccis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('idCard', models.AutoField(db_column='idCard', primary_key=True, serialize=False)),
                ('assunto', models.CharField(max_length=45, null=True)),
                ('service', models.CharField(max_length=255, null=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('responsavel', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chamados_responsaveis', to=settings.AUTH_USER_MODEL)),
                ('solicitante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='chamados_solicitados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OperatorRating',
            fields=[
                ('idOperatorRating', models.AutoField(db_column='idOperatorRating', primary_key=True, serialize=False)),
                ('rating', models.PositiveIntegerField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas')])),
                ('comment', models.TextField(blank=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('anonymous', models.BooleanField(default=False)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ccis.card')),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('processador', models.CharField(max_length=100)),
                ('geracao', models.CharField(max_length=100)),
                ('memoria_ram', models.CharField(max_length=100)),
                ('armazenamento', models.CharField(max_length=100)),
                ('gb', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('setor', models.CharField(max_length=100)),
                ('unidade', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('serviceTag', models.CharField(max_length=100)),
                ('antiVirus', models.CharField(max_length=100)),
                ('chaveWin', models.CharField(max_length=100)),
                ('chaveOffice', models.CharField(max_length=100)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Notebook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MessageHistory',
            fields=[
                ('idMessageHistory', models.AutoField(db_column='idMessageHistory', primary_key=True, serialize=False)),
                ('message', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='chat/')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ccis.card')),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomGroupInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(blank=True, max_length=45, null=True)),
                ('nome', models.CharField(blank=True, max_length=45, null=True)),
                ('cor', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.EmailField(blank=True, max_length=45, null=True)),
                ('ramal', models.CharField(blank=True, max_length=45, null=True)),
                ('contato', models.CharField(blank=True, max_length=45, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='group/')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='CardSetorHistory',
            fields=[
                ('idCardSetorHistory', models.AutoField(db_column='idCardSetorHistory', primary_key=True, serialize=False)),
                ('status_anterior', models.CharField(blank=True, max_length=20, null=True)),
                ('status_atual', models.CharField(max_length=20)),
                ('setor_anterior', models.CharField(blank=True, max_length=20, null=True)),
                ('setor_atual', models.CharField(max_length=20)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ccis.card')),
                ('setor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]
