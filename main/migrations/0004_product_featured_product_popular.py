# Generated by Django 4.2 on 2023-04-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_img_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]