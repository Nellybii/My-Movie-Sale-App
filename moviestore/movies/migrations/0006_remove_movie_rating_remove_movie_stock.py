# Generated by Django 5.0.6 on 2024-05-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_price_alter_movie_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='stock',
        ),
    ]
