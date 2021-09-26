# Generated by Django 2.2.20 on 2021-09-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20210926_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(db_index=True, related_name='owned_by', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
