# Generated by Django 5.0.1 on 2024-01-27 19:36

import bartender.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0008_alter_sound_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='photo',
            field=models.ImageField(blank=True, storage=bartender.storage.OverwriteStorage(), upload_to='images/drinks/'),
        ),
        migrations.AlterField(
            model_name='patron',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/patrons/'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='file',
            field=models.FileField(upload_to='sounds/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])]),
        ),
    ]
