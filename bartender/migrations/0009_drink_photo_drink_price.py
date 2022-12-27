# Generated by Django 4.1.4 on 2022-12-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0008_remove_drink_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='drink',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
    ]
