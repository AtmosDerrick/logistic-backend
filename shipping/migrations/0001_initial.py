# Generated by Django 4.2.6 on 2023-11-28 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ships',
            fields=[
                ('driver', models.TextField(max_length=150)),
                ('shipping_id', models.AutoField(primary_key=True, serialize=False)),
                ('shipping_datetime', models.DateTimeField(auto_now=True)),
                ('delivered_datetime', models.DateTimeField(null=True)),
                ('attendant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]