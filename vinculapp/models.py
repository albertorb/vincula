#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	pic = models.ImageField(upload_to = 'user-pic/', default = '/static/vinculapp/img/example_profile.png', max_length=255)

	def __unicode__(self):
		return self.user.get_username()

class Folder(models.Model):
	profile = models.ForeignKey(Profile, default = None)
	name = models.TextField(max_length=255)
	parent = models.ForeignKey('self', null = True, blank = True, default = None)
	pic = models.ImageField(upload_to = 'folders-pic/', default = 'example_folder.png', blank = True, null = True, max_length=255)

	@classmethod
	def create(cls,name,profile,parent,pic):
		folder = cls(name=name,profile=profile,parent=parent, pic=pic)
		return folder

	def __unicode__(self):
		return self.name



class Card(models.Model):
	name = models.TextField(max_length=255)
	url = models.TextField(max_length=255)
	pic = models.ImageField(upload_to = 'cards-pic/', blank=True, null=True, default = 'video.jpeg', max_length=255)
	folder = models.ForeignKey(Folder)

	@classmethod
	def create(cls,name,url,folder):
		card = cls(name=name,url=url,folder=folder)
		return card

	def __unicode__(self):
		return self.name


