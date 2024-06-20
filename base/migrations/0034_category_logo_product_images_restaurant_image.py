# Generated by Django 5.0.3 on 2024-05-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_remove_category_logo_remove_product_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='base/category_logos'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default='C:\\Users\\Ahmad_Shamma\\\\Desktop\\root.jpg', upload_to='base/product_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='C:\\Users\\Ahmad_Shamma\\\\Desktop\\root.jpg', upload_to='base/restaurant_images'),
            preserve_default=False,
        ),
    ]
