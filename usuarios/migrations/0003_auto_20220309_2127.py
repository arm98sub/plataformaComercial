# Generated by Django 2.2.14 on 2022-03-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perfil', verbose_name='Foto de Perfil'),
        ),
    ]