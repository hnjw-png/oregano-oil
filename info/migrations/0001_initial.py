# Generated by Django 3.2.21 on 2024-01-26 10:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dislikes', models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
