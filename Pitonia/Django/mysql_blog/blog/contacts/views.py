from django.shortcuts import render
from django.http import HttpResponse

def contacts_index(request):
	return render(request, "contacts/contacts.html")