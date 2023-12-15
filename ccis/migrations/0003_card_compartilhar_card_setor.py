# Generated by Django 4.2 on 2023-12-14 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ccis', '0002_card_operatorrating_notification_messagehistory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='compartilhar',
            field=models.ManyToManyField(blank=True, related_name='cards_compartilhados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
    ]