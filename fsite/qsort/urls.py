from django.conf.urls import url
from . import views


app_name = 'qsort'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sorted$', views.sort_it, name='sort_it'),
]