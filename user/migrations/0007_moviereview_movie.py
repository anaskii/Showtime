# Generated by Django 4.0.6 on 2022-08-14 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_rating'),
        ('user', '0006_remove_moviereview_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviereview',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movies'),
        ),
    ]
