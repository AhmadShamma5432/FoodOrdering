# Generated by Django 5.0.3 on 2024-08-16 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0050_rename_prodcut_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
    ]
