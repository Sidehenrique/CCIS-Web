# Generated by Django 4.2 on 2023-04-11 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ccis', '0007_outros'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosbancarios',
            name='dadosPessoa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ccis.dadospessoais'),
        ),
    ]
