# Generated by Django 5.0.3 on 2024-03-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_restaurant_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Rate',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
