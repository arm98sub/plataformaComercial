# Generated by Django 3.2.8 on 2021-12-08 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordenes', '0001_initial'),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleorden',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.producto', verbose_name='Producto'),
        ),
    ]
