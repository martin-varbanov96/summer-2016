from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from .models import Post

class IndexView(ListView):
	template_name = 'blog_app/blog_app.html'
	queryset = Post.objects.all()

	def get_queryset(self):
		"""Return the last five published questions."""
		return Post.objects.order_by('-pub_date')