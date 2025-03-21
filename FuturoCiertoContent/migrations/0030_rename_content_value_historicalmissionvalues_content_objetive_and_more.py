# Generated by Django 5.1.1 on 2024-10-29 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuturoCiertoContent', '0029_banner_url_historicalbanner_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalmissionvalues',
            old_name='Content_value',
            new_name='Content_objetive',
        ),
        migrations.RenameField(
            model_name='historicalmissionvalues',
            old_name='Title_value',
            new_name='Title_objetive',
        ),
        migrations.RenameField(
            model_name='missionvalues',
            old_name='Content_value',
            new_name='Content_objetive',
        ),
        migrations.RenameField(
            model_name='missionvalues',
            old_name='Title_value',
            new_name='Title_objetive',
        ),
        migrations.AddField(
            model_name='historicalmissionvalues',
            name='Content_motivation',
            field=models.TextField(null=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='historicalmissionvalues',
            name='Title_motivation',
            field=models.CharField(max_length=255, null=True, verbose_name='Titulo'),
        ),
        migrations.AddField(
            model_name='missionvalues',
            name='Content_motivation',
            field=models.TextField(null=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='missionvalues',
            name='Title_motivation',
            field=models.CharField(max_length=255, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='Url',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='FuturoCiertoContent.navigation', verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='historicalbanner',
            name='Url',
            field=models.ForeignKey(blank=True, db_constraint=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='FuturoCiertoContent.navigation', verbose_name='URL'),
        ),
    ]
