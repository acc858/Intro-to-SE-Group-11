# Generated by Django 4.2.11 on 2024-04-23 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='Listing',
            new_name='listing',
        ),
    ]