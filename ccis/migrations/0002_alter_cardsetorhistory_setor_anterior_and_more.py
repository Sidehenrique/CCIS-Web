# Generated by Django 4.2 on 2023-10-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardsetorhistory',
            name='setor_anterior',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cardsetorhistory',
            name='status_anterior',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
