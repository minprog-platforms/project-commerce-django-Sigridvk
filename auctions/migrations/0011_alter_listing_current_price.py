# Generated by Django 3.2.9 on 2022-05-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listing_current_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='current_price',
            field=models.IntegerField(default=models.IntegerField(), null=True),
        ),
    ]