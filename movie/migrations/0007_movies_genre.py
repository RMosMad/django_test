# Generated by Django 5.0.4 on 2024-04-09 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_movies_options_movies_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.genre'),
        ),
    ]