# Generated by Django 5.0.3 on 2024-03-26 20:04

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collectApp', '0002_individualprofile_address_individualprofile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='organizationprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]