from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^community$', views.community),
    url(r'^about_us/dee$', views.about_dee),
    url(r'^about_us/qiana$', views.about_qiana),
    url(r'^about_us/kc$', views.about_kc),
    url(r'^contact_us$', views.contact_us),
    url(r'^process_register$', views.process_register),
    url(r'^process_login$', views.process_login),
    url(r'^process_contact$', views.process_contact),
    url(r'^welcome$', views.welcome),
    url(r'^logout$', views.logout),
]
