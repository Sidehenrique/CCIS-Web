# Generated by Django 4.2 on 2023-11-06 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ccis', '0004_card_compartilhar'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatorRating',
            fields=[
                ('idOperatorRating', models.AutoField(db_column='idOperatorRating', primary_key=True, serialize=False)),
                ('rating', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('anonymous', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avaliador_anonimo', to=settings.AUTH_USER_MODEL)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ccis.card')),
                ('operador', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avaliacao_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
