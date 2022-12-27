# Generated by Django 4.1.4 on 2022-12-22 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0011_alter_drink_photo_alter_drink_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='patron',
            name='photo',
            field=models.ImageField(blank=True, upload_to='patrons'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='photo',
            field=models.ImageField(blank=True, upload_to='drinks'),
        ),
    ]