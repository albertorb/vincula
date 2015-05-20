# encoding : utf8
from .models import Folder,Card
import os

def create_vin(request):
	directory = "media/series"
	root = Folder.create('ULTIMO',request.user.profile,None)
	root.save()
	for serie in os.listdir(directory):
		if not serie.startswith('.'):
			s = Folder.create(serie,request.user.profile,root)
			s.save()
			for season in os.listdir(directory+'/'+serie):
				if not season.startswith('.'):
					ss = Folder.create(season,request.user.profile,s)
					ss.pic='tv.png'
					ss.save()
					for episode in os.listdir(directory+'/'+serie+'/'+season+'/'):
						if not episode.startswith('.'):
							url = open(directory+'/'+serie+'/'+season+'/'+episode,'r').readline()
							if url.__len__ > 0:
								c = Card.create(episode,url,ss)
								c.save()










