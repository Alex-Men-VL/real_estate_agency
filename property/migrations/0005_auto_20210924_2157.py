# Generated by Django 3.2.6 on 2021-09-24 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20210924_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_text', models.TextField(verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.flat', verbose_name='Квартира, на которую пожаловались')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]
