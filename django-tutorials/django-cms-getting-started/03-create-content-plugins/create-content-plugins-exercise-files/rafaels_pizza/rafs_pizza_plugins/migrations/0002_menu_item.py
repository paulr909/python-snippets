# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('rafs_pizza_plugins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'menu_items')),
                ('price', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
