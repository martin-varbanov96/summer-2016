from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns=[
	url(r'^about', views.about_index  , name="about_index")
]