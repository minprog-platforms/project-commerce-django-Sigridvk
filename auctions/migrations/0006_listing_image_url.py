# Generated by Django 3.2.9 on 2022-05-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_url',
            field=models.URLField(default=None, max_length=400),
            preserve_default=False,
        ),
    ]