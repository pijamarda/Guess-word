from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = [	
	url(r'^$', views.index),
	url(r'^check_guess/', views.check_guess),
	url(r'^resultado/', views.resultado),
	url(r'^save/(?P<intentos>[0-9]+)/(?P<palabra>[a-z]+)/', views.save),
	url(r'^merindo/(?P<intentos>[0-9]+)/(?P<palabra>[a-z]+)/', views.merindo),
	url(r'^reportar/(?P<palabra>[a-z]+)/', views.reportar),
]