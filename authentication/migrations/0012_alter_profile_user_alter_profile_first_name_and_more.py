# Generated by Django 4.2.6 on 2023-12-13 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_remove_profile_admin_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='User',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(default='', max_length=100),
        ),
    ]
