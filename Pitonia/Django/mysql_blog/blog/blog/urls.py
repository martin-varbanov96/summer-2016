from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	# url(r'^$', include('about_page.urls')),
	url(r'^', include('about_page.urls')),
	url(r'^', include('blog_app.urls')),
	url(r'^', include('contacts.urls')),
    url(r'^admin/', admin.site.urls),
]