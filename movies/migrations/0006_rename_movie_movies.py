# Generated by Django 5.1.4 on 2024-12-10 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_delete_movies'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='Movies',
        ),
    ]
