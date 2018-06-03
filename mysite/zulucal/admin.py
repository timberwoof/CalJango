# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Calendar, Person, Place, Thing, Event, EventRelation

admin.site.register(Calendar)
admin.site.register(Person)
admin.site.register(Place)
admin.site.register(Thing)
admin.site.register(Event)
admin.site.register(EventRelation)

# Register your models here.
