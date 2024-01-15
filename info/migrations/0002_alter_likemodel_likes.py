# Generated by Django 3.2.21 on 2024-01-11 17:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likemodel',
            name='likes',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]