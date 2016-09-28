from django.db import models

class Post(models.Model):
	topic_title = models.CharField(max_length=50)
	topic_text = models.TextField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return "Post " + self.topic_title + " with txt: " + self.topic_text + " has been published on: "