# Generated by Django 4.2 on 2024-03-22 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ccis', '0016_ferias_card_notification_authorfirst_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferias',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ferias', to=settings.AUTH_USER_MODEL),
        ),
    ]
