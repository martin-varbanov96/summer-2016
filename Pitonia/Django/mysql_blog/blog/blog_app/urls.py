from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from .models import Post

urlpatterns=[
	url(r'^blog$', ListView.as_view(queryset=Post.objects.all(), template_name="blog_app/blog_app.html")),
	url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="blog_app/blog_post.html"))
]