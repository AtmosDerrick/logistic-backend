# Generated by Django 4.2.6 on 2023-12-13 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_user_profile_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='admin',
            new_name='User',
        ),
    ]
