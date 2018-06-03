# -*- coding: utf-8 -*-
# zulucal/views.py
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the zulucal index.")

# Create your views here.
def detail(request, question):
    return HttpResponse("You're looking at question %s." % question)

def calendarList(request):
    return HttpResponse("You're looking at calendar list")

def calendarDetail(request, calendar):
    return HttpResponse("You're looking at calendar %s." % calendar)

def personList(request):
    return HttpResponse("You're looking at person list")

def personDetail(request, person):
    return HttpResponse("You're looking at person %s." % person)

def placeList(request):
    return HttpResponse("You're looking at place list")

def placeDetail(request, place):
    return HttpResponse("You're looking at place %s." % place)

def thingList(request):
    return HttpResponse("You're looking at thing list")

def thingDetail(request, thing):
    return HttpResponse("You're looking at thing %s." % thing)

def eventList(request):
    return HttpResponse("You're looking at event list")

def eventDetail(request, event):
    return HttpResponse("You're looking at event %s." % event)

def eventRelationList(request):
    return HttpResponse("You're looking at event relation list")

def eventRelationDetail(request, eventRelation):
    return HttpResponse("You're looking at event relation %s." % eventRelation)

