# Generated by Django 2.2.4 on 2019-10-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20191004_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistitem',
            name='added_to_cart',
            field=models.BooleanField(default=False),
        ),
    ]
