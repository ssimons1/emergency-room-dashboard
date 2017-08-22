from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.dashboard, name='index'),
    url(r'^login/$', login, name="login"),
    url(r'^restricted/$', views.restricted, name="restricted"),
    url(r'^logout/$', views.logout),
]