# Generated by Django 4.2 on 2023-04-11 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccis', '0010_outros_dadospessoais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadosbancarios',
            name='dadosPessoais',
        ),
        migrations.RemoveField(
            model_name='outros',
            name='dadosPessoais',
        ),
    ]