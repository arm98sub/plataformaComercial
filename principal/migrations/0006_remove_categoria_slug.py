# Generated by Django 3.2.8 on 2022-05-29 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_merge_20220525_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='slug',
        ),
    ]
