# Generated by Django 4.1.4 on 2022-12-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0004_alter_drink_name_alter_patron_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
