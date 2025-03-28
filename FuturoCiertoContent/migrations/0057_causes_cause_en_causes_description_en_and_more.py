# Generated by Django 4.2 on 2024-12-22 11:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuturoCiertoContent', '0056_event_address_en_event_event_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='causes',
            name='Cause_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Cause'),
        ),
        migrations.AddField(
            model_name='causes',
            name='Description_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='causes',
            name='Title_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='historicalcauses',
            name='Cause_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Cause'),
        ),
        migrations.AddField(
            model_name='historicalcauses',
            name='Description_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='historicalcauses',
            name='Title_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='historicalreflectionbyjose',
            name='Comment1_en',
            field=ckeditor.fields.RichTextField(blank=True, max_length=450, verbose_name='Donator Comment 1'),
        ),
        migrations.AddField(
            model_name='historicalreflectionbyjose',
            name='Comment2_en',
            field=ckeditor.fields.RichTextField(blank=True, max_length=450, verbose_name='Donator Comment 2'),
        ),
        migrations.AddField(
            model_name='historicalreflectionbyjose',
            name='Comment3_en',
            field=ckeditor.fields.RichTextField(blank=True, max_length=450, verbose_name='Donator Comment 3'),
        ),
        migrations.AddField(
            model_name='reflectionbyjose',
            name='Comment1_en',
            field=ckeditor.fields.RichTextField(blank=True, max_length=450, verbose_name='Donator Comment 1'),
        ),
        migrations.AddField(
            model_name='reflectionbyjose',
            name='Comment2_en',
            field=ckeditor.fields.RichTextField(blank=True, max_length=450, verbose_name='Donator Comment 2'),
        ),
        migrations.AddField(
            model_name='reflectionbyjose',
            name='Comment3_en',
            field=ckeditor.fields.RichTextField(blank=True, max_length=450, verbose_name='Donator Comment 3'),
        ),
        migrations.AlterField(
            model_name='educations',
            name='Content_en',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='educations',
            name='Title_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='event',
            name='Address_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Event Address'),
        ),
        migrations.AlterField(
            model_name='event',
            name='Event_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Event Title'),
        ),
        migrations.AlterField(
            model_name='historicaleducations',
            name='Content_en',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='historicaleducations',
            name='Title_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='historicalevent',
            name='Address_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Event Address'),
        ),
        migrations.AlterField(
            model_name='historicalevent',
            name='Event_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Event Title'),
        ),
        migrations.AlterField(
            model_name='historicalmissionvalues',
            name='Content_mission_en',
            field=models.TextField(blank=True, verbose_name='Mission Content'),
        ),
        migrations.AlterField(
            model_name='historicalmissionvalues',
            name='Content_objetive',
            field=models.TextField(verbose_name='Contenido Objetivo'),
        ),
        migrations.AlterField(
            model_name='historicalmissionvalues',
            name='Content_objetive_en',
            field=models.TextField(blank=True, verbose_name='Objetive Content'),
        ),
        migrations.AlterField(
            model_name='historicalmissionvalues',
            name='Title_mission_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Mission Title'),
        ),
        migrations.AlterField(
            model_name='historicalmissionvalues',
            name='Title_motivation_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Motivation Title'),
        ),
        migrations.AlterField(
            model_name='historicalmissionvalues',
            name='Title_objetive_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Objetive Title'),
        ),
        migrations.AlterField(
            model_name='historicalnavigation',
            name='PageName',
            field=models.CharField(blank=True, max_length=255, verbose_name='Pagína'),
        ),
        migrations.AlterField(
            model_name='historicalnavigation',
            name='PageName_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='page'),
        ),
        migrations.AlterField(
            model_name='historicalnews',
            name='Content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='historicalnews',
            name='Content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='historicalnews',
            name='Title',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='historicalnews',
            name='Title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='historicalwhoweare',
            name='Content_en',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='historicalwhoweare',
            name='Title_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='missionvalues',
            name='Content_mission_en',
            field=models.TextField(blank=True, verbose_name='Mission Content'),
        ),
        migrations.AlterField(
            model_name='missionvalues',
            name='Content_objetive',
            field=models.TextField(verbose_name='Contenido Objetivo'),
        ),
        migrations.AlterField(
            model_name='missionvalues',
            name='Content_objetive_en',
            field=models.TextField(blank=True, verbose_name='Objetive Content'),
        ),
        migrations.AlterField(
            model_name='missionvalues',
            name='Title_mission_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Mission Title'),
        ),
        migrations.AlterField(
            model_name='missionvalues',
            name='Title_motivation_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Motivation Title'),
        ),
        migrations.AlterField(
            model_name='missionvalues',
            name='Title_objetive_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Objetive Title'),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='PageName',
            field=models.CharField(blank=True, max_length=255, verbose_name='Pagína'),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='PageName_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='page'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Title',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='whoweare',
            name='Content_en',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='whoweare',
            name='Title_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
    ]
