# Generated by Django 2.1.5 on 2019-01-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(verbose_name='idade'),
        ),
    ]