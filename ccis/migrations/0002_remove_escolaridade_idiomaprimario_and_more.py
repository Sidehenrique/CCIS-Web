# Generated by Django 4.2 on 2023-05-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escolaridade',
            name='idiomaPrimario',
        ),
        migrations.RemoveField(
            model_name='escolaridade',
            name='nivelPrimario',
        ),
        migrations.AlterField(
            model_name='enderecocontato',
            name='nomeCompleto',
            field=models.CharField(blank=True, db_column='nomeCompleto', max_length=45, null=True),
        ),
    ]