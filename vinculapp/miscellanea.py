# encoding : utf8
from .models import Folder,Card
import os

def create_vin(request):
	directory = "media/series"
	root = Folder.create('SERIES',request.user.profile,None,'/media/example_folder.png')
	root.save()
	for serie in os.listdir(directory):
		if not serie.startswith('.'):
			s = Folder.create(serie,request.user.profile,root,None)
			s.pic = None #TODO revisar codigo inutil
			for season in os.listdir(directory+'/'+serie):
				if not season.startswith('.'):
					pic = '/'+directory+'/'+serie+'/'+season+'/season.jpeg'
					if s.pic == None:
						s.pic = pic
						s.save()
					ss = Folder.create(season,request.user.profile,s,pic)
					ss.save()
					for episode in os.listdir(directory+'/'+serie+'/'+season+'/'):
						if not episode.startswith('.') and episode != 'season.jpeg':
							url = open(directory+'/'+serie+'/'+season+'/'+episode,'r').readline()
							if url.__len__ > 0:
								c = Card.create(episode,url,ss)							
								c.save()

def slugfy(string):
	return string.replace(" ", "-")










