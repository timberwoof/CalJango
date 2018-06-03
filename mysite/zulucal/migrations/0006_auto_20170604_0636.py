# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zulucal', '0005_auto_20170604_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='panoculus',
            field=models.URLField(default='https://library.panocul.us/mw/index.php?title=Main_Page'),
        ),
        migrations.AddField(
            model_name='person',
            name='panoculus',
            field=models.URLField(default='https://library.panocul.us/mw/index.php?title=Main_Page'),
        ),
        migrations.AddField(
            model_name='place',
            name='panoculus',
            field=models.URLField(default='https://library.panocul.us/mw/index.php?title=Main_Page'),
        ),
    ]