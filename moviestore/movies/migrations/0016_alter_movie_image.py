# Generated by Django 5.0.6 on 2024-06-07 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, max_length=4000, null=True, upload_to=''),
        ),
    ]
