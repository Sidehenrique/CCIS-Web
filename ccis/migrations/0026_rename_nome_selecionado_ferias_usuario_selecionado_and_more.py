# Generated by Django 4.2 on 2024-03-25 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccis', '0025_remove_ferias_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ferias',
            old_name='nome_selecionado',
            new_name='usuario_selecionado',
        ),
    ]