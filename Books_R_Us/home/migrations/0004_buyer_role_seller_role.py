# Generated by Django 4.2.11 on 2024-04-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='role',
            field=models.CharField(default='buyer', max_length=50),
        ),
        migrations.AddField(
            model_name='seller',
            name='role',
            field=models.CharField(default='seller', max_length=50),
        ),
    ]
