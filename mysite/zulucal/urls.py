from django.conf.urls import url
from .views import personList

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #/zulucal/

    #/zulucal/calendars/
    url(r'calendars/$', views.calendarList, name='calendarList'),
    #/zulucal/calendars/5/
    url(r'calendars/(?P<calendar>[0-9]+)/$', views.calendarDetail, name='calendarDetail'),

    #/zulucal/persons/
    url(r'persons/$', personList, name='personList'),
    #/zulucal/persons/5/
    url(r'persons/(?P<person>[0-9]+)/$', views.personDetail, name='personDetail'),

    #/zulucal/places/
    url(r'places/$', views.placeList, name='placeList'),
    #/zulucal/places/5/
    url(r'places/(?P<place>[0-9]+)/$', views.placeDetail, name='placeDetail'),

    #/zulucal/things/
    url(r'things/$', views.placeList, name='thingList'),
    #/zulucal/things/5/
    url(r'things/(?P<thing>[0-9]+)/$', views.thingDetail, name='thingDetail'),

    #/zulucal/events/
    url(r'events/$', views.eventList, name='eventList'),
    #/zulucal/events/5/
    url(r'events/(?P<event>[0-9]+)/$', views.eventDetail, name='eventDetail'),

    #/zulucal/relations/
    url(r'relations/$', views.eventRelationList, name='eventRelationList'),
    #/zulucal/relations/5/
    url(r'relations/(?P<eventRelation>[0-9]+)/$', views.eventRelationDetail, name='eventRelationDetail'),
    ]
