# Generated by Django 5.0.3 on 2024-04-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_listing_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='whishlist',
            field=models.ManyToManyField(blank=True, related_name='marked', to='auctions.listing'),
        ),
    ]
