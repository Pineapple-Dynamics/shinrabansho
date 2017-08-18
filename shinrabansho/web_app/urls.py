#!coding:utf-8
from django.conf.urls import url, include
from web_app import views

urlpatterns = [
        url(r'^$', views.show, name='show'),
        url(r'^edit/$', views.edit, name='edit'),
               ]
