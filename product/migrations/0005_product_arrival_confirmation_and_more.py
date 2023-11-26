# Generated by Django 4.2.6 on 2023-11-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_id_alter_product_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='arrival_confirmation',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_confirmation',
            field=models.BooleanField(default=True),
        ),
    ]