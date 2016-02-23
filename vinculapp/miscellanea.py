# encoding : utf8
from .models import Folder,Card
import os
import json

def import_data(request, parent, data):
	"""
	Transform json file into vincula objects
	Every key of the json input will be transformed to a folder, and every
	value to links (Even arrays).
	Maximum depth allowed is 1, for security reasons, at the moment.
	"""
	# if not isinstance(data, dict):
	# 	data = json.loads(data)
	for folder, cards in data.iteritems():
		f_parent = Folder.create(folder, request.user.profile, parent, '/media/example_folder.png')
		f_parent.save()
		for name, url in cards.iteritems():
			card = Card.create(name, url, f_parent)
			card.save()
	return True

def create_vin(request):
	topics = ['NBA']
	for fld in topics:
		directory = "media/%s" % fld
		root = Folder.create(fld,request.user.profile,None,'/media/example_folder.png')
		root.save()
		for serie in os.listdir(directory):
			if not serie.startswith('.'):
				s = Folder.create(serie,request.user.profile,root,None)
				s.pic = None #TODO revisar codigo inutil
				for season in os.listdir(directory+'/'+serie):
					if not season.startswith('.'):
						if fld == 'NBA':
							pic = '/media/example_folder.png'
						else:
							pic = '/'+directory+'/'+serie+'/'+season+'/season.jpeg'
						if s.pic == None:
							s.pic = pic
							s.save()
						ss = Folder.create(season,request.user.profile,s,pic)
						ss.save()
						for episode in os.listdir(directory+'/'+serie+'/'+season+'/'):
							if not episode.startswith('.') and '.jpeg' not in episode:
								# if fld == 'NBA':
								# 	pic = '/media/example_folder.png'
								# else:
								# 	pic = '/'+directory+'/'+serie+'/'+season+'/season.jpeg'
								url = open(directory+'/'+serie+'/'+season+'/'+episode,'r').readline()
								if url.__len__ > 0:
									c = Card.create(episode,url,ss)
									if fld == 'NBA':
										c.pic = '/%s/%s/%s/%s' %(directory, serie, season, episode+'.jpeg')
									c.save()

def slugfy(string):
	return string.replace(" ", "-")
