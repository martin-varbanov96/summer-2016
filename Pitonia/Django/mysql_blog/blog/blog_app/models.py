from django.db import models

class Post(models.Model):
	topic_title = models.CharField(max_length=50)
	topic_text = models.TextField()
	pub_date = models.DateTimeField('date published')
	topic_resume = models.TextField()

	def __str__(self):
		return "Post " + self.topic_title + " with resume: " + self.topic_resume + " has been published on: "