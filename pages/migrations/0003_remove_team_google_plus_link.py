# Generated by Django 4.0 on 2022-04-27 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200625_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='google_plus_link',
        ),
    ]
