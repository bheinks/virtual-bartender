# Generated by Django 4.2.7 on 2024-01-24 21:09

import bartender.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patron',
            name='photo',
            field=models.ImageField(blank=True, upload_to=bartender.models.get_upload_path),
        ),
    ]
