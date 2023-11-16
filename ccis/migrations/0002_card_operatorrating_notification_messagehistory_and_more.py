# Generated by Django 4.2 on 2023-11-14 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('anonymous', models.BooleanField(default=False)),
                ('cor', models.CharField(max_length=20, null=True)),
                ('compartilhar', models.ManyToManyField(blank=True, related_name='cards_compartilhados', to=settings.AUTH_USER_MODEL)),
                ('responsavel', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chamados_responsaveis', to=settings.AUTH_USER_MODEL)),
                ('solicitante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='chamados_solicitados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OperatorRating',
            fields=[
                ('idOperatorRating', models.AutoField(db_column='idOperatorRating', primary_key=True, serialize=False)),
                ('rating', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('anonymous', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avaliador_anonimo', to=settings.AUTH_USER_MODEL)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ccis.card')),
                ('operador', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avaliacao_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='authorNotification', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_received', to=settings.AUTH_USER_MODEL)),
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
            name='CardSetorHistory',
            fields=[
                ('idCardSetorHistory', models.AutoField(db_column='idCardSetorHistory', primary_key=True, serialize=False)),
                ('status_anterior', models.CharField(blank=True, max_length=20, null=True)),
                ('status_atual', models.CharField(max_length=20)),
                ('setor_anterior', models.CharField(blank=True, max_length=20, null=True)),
                ('setor_atual', models.CharField(max_length=20)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ccis.card')),
                ('operador', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operador_history', to=settings.AUTH_USER_MODEL)),
                ('setor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]