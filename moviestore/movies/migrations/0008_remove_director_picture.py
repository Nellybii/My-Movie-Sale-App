# Generated by Django 5.0.6 on 2024-05-29 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_director_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='picture',
        ),
    ]