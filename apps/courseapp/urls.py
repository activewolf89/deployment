from django.conf.urls import url
# from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^post$', views.posts),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^decision/(?P<id>\d+)$', views.decision),
    url(r'^return$', views.resultreturn)
]
