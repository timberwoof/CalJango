# -*- coding: utf-8 -*-
# zulucal/models.py
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Calendar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    baseCalendar = models.ForeignKey('self', on_delete=models.PROTECT, default=1)
    calendarOffset = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    panoculus = models.URLField(default='https://library.panocul.us/mw/index.php/People')
    def __str__(self):
        return self.name

class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    panoculus = models.URLField(default='https://library.panocul.us/mw/index.php/Geography')
    def __str__(self):
        return self.name

class Thing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    panoculus = models.URLField(default='https://library.panocul.us/mw/index.php/Technology_and_Materials')
    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.PROTECT, default=1)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    thing = models.ForeignKey(Thing, on_delete=models.PROTECT)
    description = models.CharField(max_length=200)
    panoculus = models.URLField(default='https://library.panocul.us/mw/index.php/History')
    earliest = models.IntegerField(default=0)
    latest = models.IntegerField(default=0)
    pinned = models.BooleanField(default=0)
    def __str__(self):
        description = ''
        if self.person.name != 'NOBODY':
            description = self.person.name
        description = description + ' ' + self.description
        if self.place.name != 'NOWHERE':
            description = description + ' at ' + self.place.name
        if self.thing.name != 'NOTHING':
            description = description + ' with ' + self.thing.name
        return description

class EventRelation(models.Model):
    id = models.AutoField(primary_key=True)
    firstEvent = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='+')
    secondEvent = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='+')
    intervalMin = models.IntegerField(default=0)
    intervalMax = models.IntegerField(default=0)
    def __str__(self):
        description = ''
        if self.firstEvent.person.name != 'NOBODY':
            description = self.firstEvent.person.name
        description = description + ' ' + self.firstEvent.description
        if self.firstEvent.place.name != 'NOWHERE':
            description = description + ' at ' + self.firstEvent.place.name
        if self.firstEvent.thing.name != 'NOTHING':
            description = description + ' with ' + self.firstEvent.thing.name
        
        description = description + ' to '

        if self.secondEvent.person.name != 'NOBODY':
            description =  description + self.secondEvent.person.name
        description = description + ' ' + self.secondEvent.description
        if self.secondEvent.place.name != 'NOWHERE':
            description = description + ' at ' + self.secondEvent.place.name
        if self.secondEvent.thing.name != 'NOTHING':
            description = description + ' with ' + self.secondEvent.thing.name

        return description
