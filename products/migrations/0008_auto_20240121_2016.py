# Generated by Django 3.2.21 on 2024-01-21 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20240121_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='description',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='rating',
        ),
        migrations.AddField(
            model_name='rate',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]