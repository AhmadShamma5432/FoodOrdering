# Generated by Django 5.0.3 on 2024-03-07 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_remove_product_sizes_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
