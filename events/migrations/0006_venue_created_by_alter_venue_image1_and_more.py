# Generated by Django 5.0.4 on 2024-05-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_venue_image1_alter_venue_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='created_by',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/venue'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/venue'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/venue'),
        ),
    ]