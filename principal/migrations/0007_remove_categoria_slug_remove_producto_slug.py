# Generated by Django 4.1.3 on 2022-12-11 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_merge_20221211_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='slug',
        ),
    ]
