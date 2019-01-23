#models.py File

from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=300)
	content = models.TextField(max_length=300)
	
	def __str__(self):
		return self.title, self.content
