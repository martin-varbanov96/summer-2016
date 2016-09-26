from django.http import HttpResponse

from .models import Thread,Page


def index(request):
	latest_question_list = Thread.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.title for q in latest_question_list])
	return HttpResponse(output)