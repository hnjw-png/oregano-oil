# Generated by Django 3.2.21 on 2024-01-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_auto_20240108_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='title',
            field=models.CharField(default='testimonial', max_length=255),
        ),
    ]
