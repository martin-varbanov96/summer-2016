from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^contacts/$', views.contacts_index, name='contacts_index'),
]
