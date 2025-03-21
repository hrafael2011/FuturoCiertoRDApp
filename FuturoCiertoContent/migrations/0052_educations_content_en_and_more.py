# Generated by Django 4.2 on 2024-12-21 19:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FuturoCiertoContent', '0051_educations_title_en_historicaleducations_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='educations',
            name='Content_en',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='historicaleducations',
            name='Content_en',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='educations',
            name='Content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='historicaleducations',
            name='Content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
