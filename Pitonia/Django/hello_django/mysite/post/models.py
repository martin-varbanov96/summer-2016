from django.db import models
from django.db import models

class Thread(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	votes =models.IntegerField(default=0)

class Page(models.Model):
	text = models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
	page_number=models.IntegerField(default=0)
