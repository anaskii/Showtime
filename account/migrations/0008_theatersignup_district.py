# Generated by Django 4.0.6 on 2022-08-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_theatersignup_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='theatersignup',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
