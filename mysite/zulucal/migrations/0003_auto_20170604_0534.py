# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zulucal', '0002_auto_20170603_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='calendarId',
        ),
        migrations.RemoveField(
            model_name='event',
            name='personId',
        ),
        migrations.RemoveField(
            model_name='event',
            name='placeId',
        ),
        migrations.RemoveField(
            model_name='eventrelation',
            name='firstEventId',
        ),
        migrations.RemoveField(
            model_name='eventrelation',
            name='secondEventId',
        ),
        migrations.AddField(
            model_name='event',
            name='calendar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='zulucal.Calendar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='zulucal.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='zulucal.Place'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventrelation',
            name='firstEvent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='zulucal.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventrelation',
            name='secondEvent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='zulucal.Event'),
            preserve_default=False,
        ),
    ]
