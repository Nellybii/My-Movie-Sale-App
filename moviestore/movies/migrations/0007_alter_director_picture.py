# Generated by Django 5.0.6 on 2024-05-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_movie_rating_remove_movie_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]