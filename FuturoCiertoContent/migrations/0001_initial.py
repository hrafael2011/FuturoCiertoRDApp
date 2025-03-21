# Generated by Django 5.1.1 on 2024-09-25 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='navigation',
            fields=[
                ('NavId', models.AutoField(primary_key=True, serialize=False)),
                ('PageName', models.CharField(blank=True, max_length=255)),
                ('Url', models.CharField(max_length=255)),
                ('CreateAt', models.DateTimeField(auto_now_add=True)),
                ('UpdateAt', models.DateTimeField(auto_now=True, null=True)),
                ('DeleteAt', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
