# Generated by Django 5.0.4 on 2024-05-08 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_venuetype_venue_venue_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venuetype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='venue_types', to='events.venuetype'),
        ),
    ]
