# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Calendar, Person, Place, Thing, Event, EventRelation

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ("id", "name","description", "baseCalendar", "calendarOffset")

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name","description")

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name","description")

@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = ("id", "name","description")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "calendar", "person", "place", "thing", "description")

@admin.register(EventRelation)
class EventRelationAdmin(admin.ModelAdmin):
    list_display = ("id", "firstEvent", "secondEvent", "intervalMin", "intervalMax")


# Register your models here.
