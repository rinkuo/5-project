# Generated by Django 5.1.4 on 2024-12-10 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_director_movie_direction_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='Movies',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='realizer_year',
            new_name='release_year',
        ),
    ]