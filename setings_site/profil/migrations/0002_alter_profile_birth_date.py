# Generated by Django 4.1.5 on 2023-01-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='День рожденья'),
        ),
    ]