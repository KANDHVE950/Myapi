from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Data(models.Model):
	userId = models.IntegerField(default=0)
	title = models.CharField(max_length=2000)
	body = models.CharField(max_length=5000)

	def __str__(self):
		return self.title.split()[0]
