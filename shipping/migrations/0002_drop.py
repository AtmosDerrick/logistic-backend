# Generated by Django 4.2.6 on 2023-11-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drop',
            fields=[
                ('drop_id', models.AutoField(primary_key=True, serialize=False)),
                ('drop_code', models.CharField(max_length=8)),
                ('region', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('drop_datetime', models.DateTimeField(auto_now=True)),
                ('manager', models.CharField(max_length=200)),
            ],
        ),
    ]
