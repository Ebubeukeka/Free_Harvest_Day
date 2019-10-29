#  Project urls
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.free_harvest_day_app.urls')), 
]