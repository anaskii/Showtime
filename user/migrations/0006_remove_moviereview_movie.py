# Generated by Django 4.0.6 on 2022-08-14 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_moviereview_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviereview',
            name='movie',
        ),
    ]
