# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Specials',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'daily_specials')),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Daily Special',
                'verbose_name_plural': 'Daily Specials',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
