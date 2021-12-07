# Generated by Django 3.2.8 on 2021-10-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True,
                 upload_to='principal', verbose_name='Imagen')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('descripcion', models.CharField(blank=True,
                 max_length=250, null=True, verbose_name='Descripción')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True,
                 upload_to='principal', verbose_name='Imagen')),
                ('descripcion', models.CharField(blank=True,
                 max_length=250, null=True, verbose_name='Descripción')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
    ]
