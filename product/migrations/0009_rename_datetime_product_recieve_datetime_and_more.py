# Generated by Django 4.2.6 on 2023-11-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_reciever_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='datetime',
            new_name='recieve_datetime',
        ),
        migrations.AddField(
            model_name='product',
            name='arrival_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='delivered_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]