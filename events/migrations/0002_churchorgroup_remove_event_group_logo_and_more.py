# Generated by Django 5.0.4 on 2024-04-21 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchOrGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, upload_to='uploads/group_logos')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='group_logo',
        ),
        migrations.AlterField(
            model_name='event',
            name='church_or_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.churchorgroup'),
        ),
    ]
