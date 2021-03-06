# Generated by Django 4.0 on 2022-04-27 20:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_style',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Sport', 'Sport'), ('SUV', 'SUV'), ('Mini Van', 'Mini Van'), ('Classic', 'Classic'), ('Royal', 'Royal')], max_length=32),
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Excellent', 'Excellent'), ('Out standing', 'Out standing'), ('New', 'New'), ('Used', 'Used')], max_length=31),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=9),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')], max_length=22),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('CVT', 'CVT')], max_length=20),
        ),
    ]
