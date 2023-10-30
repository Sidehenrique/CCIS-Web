# Generated by Django 4.2 on 2023-10-26 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ccis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorButtons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(blank=True, max_length=45, null=True)),
                ('text2', models.CharField(blank=True, max_length=45, null=True)),
                ('cor', models.CharField(blank=True, max_length=45, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=45, null=True)),
                ('permissao', models.CharField(blank=True, max_length=45, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]