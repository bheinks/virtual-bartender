# Generated by Django 5.0.1 on 2024-03-16 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0010_drinkcategory_drink_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drinkcategory',
            options={'verbose_name_plural': 'drink categories'},
        ),
    ]
