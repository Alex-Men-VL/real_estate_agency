# Generated by Django 2.2.20 on 2021-09-25 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_auto_20210924_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claim',
            name='owner',
        ),
        migrations.AddField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claims', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
