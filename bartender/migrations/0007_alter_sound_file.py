# Generated by Django 5.0.1 on 2024-01-27 19:27

import bartender.models
import bartender.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0006_alter_sound_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='file',
            field=models.FileField(validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])]),
        ),
    ]
