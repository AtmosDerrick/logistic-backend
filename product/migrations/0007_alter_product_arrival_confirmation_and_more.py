# Generated by Django 4.2.6 on 2023-11-26 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_arrival_confirmation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='arrival_confirmation',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_cancel',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='shipping_confirmation',
            field=models.BooleanField(null=True),
        ),
    ]