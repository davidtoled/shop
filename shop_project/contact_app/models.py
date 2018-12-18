from django.db import models

class Contact(models.Model):
	subject = models.CharField(max_length=52)
	email = models.EmailField(max_length=264)
	text = models.TextField()

	def __str__(self):
		return self.email

	def __repr__(self):
		return "<Contact {}>".format(self.email)

