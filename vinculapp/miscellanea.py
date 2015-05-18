# encoding : utf8
from .models import Folder,Card

def create_vinc(input):
	res_folder = []
	res_card = []
	content = open(input,'r')
	#TODO verificar contenido para evitar errores
	for line in content.readlines():
		subs = line.split(' ', 1)
		path = subs[0]
		url = subs[1]
	folders = path.split('/')
	Folder f = Folder.create(folders.pop(0))
	res_folder.append(f)
	for folder in folders:
		Folder aux = Folder.create(folder)
		aux.parent = res_folder[-1]
		res_folder.append(aux)
	cards = url.split(' ')
	for cards in cards:
		Card c = Card.create('Capitulo '+ str(res_card.__len__), url, res_folder[-1])
		res_card.append(c)
	return res_folder, res_card





