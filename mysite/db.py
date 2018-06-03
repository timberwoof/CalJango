# -*- coding: utf-8 -*-
# zulucal/models.py
from __future__ import unicode_literals
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

from zulucal.models import Calendar, Person, Place, Thing, Event, EventRelation
allEvents = Event.objects.all()
# snot working