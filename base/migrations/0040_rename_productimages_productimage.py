# Generated by Django 5.0.3 on 2024-05-22 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_remove_product_images_productimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
    ]
