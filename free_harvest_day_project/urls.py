#  Project urls
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    
    # url(r'^', include('apps.indiv_garden_info.urls')),
    url(r'^', include('apps.free_harvest_day_app.urls')), 
    url(r'^admin/', admin.site.urls),
]
