from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^click_test$',views.click_test),
    url(r'^gardens$',views.gardens),
    url(r'^garden_registration$',views.garden_registration),
    url(r'^garden_request$',views.garden_request),
    # url(r'^garden_map_search$',views.garden_map_search)
]