# Generated by Django 2.2.4 on 2019-08-29 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190828_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='start',
            field=models.DateField(default=datetime.datetime(2019, 8, 29, 12, 44, 50, 209478)),
        ),
    ]