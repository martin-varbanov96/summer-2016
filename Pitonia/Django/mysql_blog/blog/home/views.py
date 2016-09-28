from django.shortcuts import render
from home.models import Topic
from django.http import HttpResponse


def index(request):
	all_objects = Topic.objects.all()
	output = dict()
	output["title"]=list()
	output["text"]=list()
	output["date"]=list()
	for i in all_objects:
		output["title"].append(i.topic_title)

	return render(request, "home/home_page.html", output)