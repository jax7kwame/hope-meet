# Generated by Django 5.0.4 on 2024-05-09 13:34

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='intro',
            field=tinymce.models.HTMLField(),
        ),
    ]
