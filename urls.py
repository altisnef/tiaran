from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='repos'),
    url(r'^update_settings', views.update_settings, name='repos'),
]


