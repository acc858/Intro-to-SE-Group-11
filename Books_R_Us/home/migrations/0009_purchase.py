# Generated by Django 4.2.11 on 2024-04-23 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_listing_image_alter_buyer_user_alter_seller_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.listing')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.buyer')),
            ],
        ),
    ]
