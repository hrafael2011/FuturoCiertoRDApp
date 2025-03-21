# Generated by Django 4.2 on 2025-03-18 21:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuturoCiertoContent', '0059_alter_historicalwhatourdonorssay_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalwhoweare',
            name='Content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='historicalwhoweare',
            name='Content_en',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='whoweare',
            name='Content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='whoweare',
            name='Content_en',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
    ]
