# Generated by Django 4.2 on 2023-09-26 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccis', '0003_alter_card_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='attachment',
        ),
    ]