# Generated by Django 3.2.8 on 2022-05-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0002_auto_20220307_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleorden',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productoordenado',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
