# Generated by Django 4.2 on 2024-03-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccis', '0026_rename_nome_selecionado_ferias_usuario_selecionado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferias',
            name='status_ferias',
            field=models.CharField(max_length=100),
        ),
    ]