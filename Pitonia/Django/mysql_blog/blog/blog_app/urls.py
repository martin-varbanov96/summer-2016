from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
from .models import Post

urlpatterns=[
	url(r'^$', views.IndexView.as_view()),
	url(r'^blog$', views.IndexView.as_view()),
	url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="blog_app/blog_post.html"))
]