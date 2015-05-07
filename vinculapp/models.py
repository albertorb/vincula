from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.ForeignKey(User, unique = True)
	pic = models.TextField(default = '/static/img/prof_defaultpic')

class Folder(models.Model):
	name = models.TextField(max_length=100)
	parent = models.ForeignKey(self, null = True, blank = True, default = None)

	def __unicode__(self):
		return self.name



class Card(models.Model):
	name = models.TextField(max_length=100)
	url = models.TextField()
	pic = models.TextField()
	folder = models.ForeignKey(Folder)

	def __unicode__(self):
		return self.name

