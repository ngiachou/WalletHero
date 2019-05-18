from django.db import models

class User(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=15)

	def __str__(self):
		return self.name