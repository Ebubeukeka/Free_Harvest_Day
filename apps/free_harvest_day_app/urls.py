from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^process_register$', views.process_register),
    url(r'^process_login$', views.process_login),
    url(r'^welcome$', views.welcome),
    url(r'^logout$', views.logout),
    url(r'^garden_volunteer$',views.garden_volunteer),
    url(r'^garden_registration$',views.garden_registration),
    # url(r'^volunteer_registration/(?P<garden_id>\d+)$',views.volunteer_registration)
    url(r'^volunteer_registration$',views.volunteer_registration),
    # url(r'^add_volunteer$',views.add_volunteer),
]
