# Generated by Django 4.2 on 2023-04-11 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccis', '0012_outros_dadospessoais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outros',
            name='dadosPessoais',
        ),
    ]
