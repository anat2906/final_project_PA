# chat/urls.py
from django.urls import path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('chat/mentor/', views.index, name='index'),
]
