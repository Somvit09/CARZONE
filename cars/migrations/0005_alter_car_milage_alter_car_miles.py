# Generated by Django 4.0 on 2022-04-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_body_style_alter_car_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.FloatField(),
        ),
    ]
