# Generated by Django 4.0.6 on 2022-08-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_theatersignup_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbackk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
    ]