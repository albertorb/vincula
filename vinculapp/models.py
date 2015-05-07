from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	pic = models.TextField(default = '/static/vinculapp/img/example_profile.png')

	def __unicode__(self):
		return self.user.get_username()

class Folder(models.Model):
	profile = models.ForeignKey(Profile, default = None)
	name = models.TextField(max_length=100)
	parent = models.ForeignKey('self', null = True, blank = True, default = None)

	def __unicode__(self):
		return self.name



class Card(models.Model):
	name = models.TextField(max_length=100)
	url = models.TextField()
	pic = models.TextField(blank=True, null=True, default = '/static/vinculapp/img/example_card.png')
	folder = models.ForeignKey(Folder)

	def __unicode__(self):
		return self.name


