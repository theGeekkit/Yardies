# Generated by Django 4.2.6 on 2023-10-17 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yardiesSales', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sale_location',
            new_name='SaleLocation',
        ),
        migrations.RenameModel(
            old_name='sale_schedule',
            new_name='SaleSchedule',
        ),
    ]
