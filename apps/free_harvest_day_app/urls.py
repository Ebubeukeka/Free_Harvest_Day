from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^gardens$', views.gardens),
    url(r'^register$', views.register),
    url(r'^process_register$', views.process_register),
    url(r'^process_login$', views.process_login),
    url(r'^welcome$', views.welcome),
    url(r'^logout$', views.logout),
]
