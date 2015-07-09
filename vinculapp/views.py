# encoding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
from django.contrib.auth.models import User
from .miscellanea import create_vin
import json
from django.core import serializers

# Create your views here.

def register(request):
	if request.POST:
		form = UserForm(request.POST)
		form2 = ProfileForm(request.POST)
		if form.is_valid() and form2.is_valid():
			django = form.save()
			django.set_password(request.POST['password'])
			django.save()
			profile = form2.save(commit=False)
			profile.user = django
			if request.FILES:
				profile.pic = request.FILES['pic']
			profile.save()
			return HttpResponseRedirect('/')
		else:
			print(form.errors)
	else:
		form = UserForm()
		form2 = ProfileForm()

	return render(request, 'vinculapp/register.html', locals())

def _login(request):
	errors = False
	if request.POST:
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/home')
			else:
				return HttpResponse("Esta cuenta de usuario aún no ha sido activada")
		else:
			errors = True
			return render(request, 'vinculapp/login.html', locals())

	return render(request, 'vinculapp/login.html', locals())

@login_required(login_url='/')
def index(request):
	folders = Folder.objects.filter(profile = request.user.profile, parent = None)
	if len(folders) == 0:
		create_vin(request)
	return render(request, 'vinculapp/home.html', locals())

@login_required(login_url='/')
def content(request):
	folder = Folder.objects.get(id = request.POST['folder'])
	folders = Folder.objects.filter(profile=request.user.profile, parent=folder).order_by('name')
	cards = Card.objects.filter(folder=folder.id).order_by('name')
	return render(request, 'vinculapp/content.html', locals())

@login_required(login_url='/')
def search_content(request):
	if request.POST:
		name_filter = request.POST['search_param_name']
		print(name_filter)
		folder = Folder.objects.get(id = request.POST['folder'])
		folders = Folder.objects.filter(profile=request.user.profile, parent=folder, name__icontains=name_filter)
		cards = Card.objects.filter(folder=folder.id,  name__icontains=name_filter)
	return render(request, 'vinculapp/content.html', locals())


@login_required(login_url='/')
def addfolder(request):
	if request.POST:
		form = FolderForm(request.POST)
		if form.is_valid():
			folder = form.save(commit = False)
			folder.profile = request.user.profile
			folder.save()
			return HttpResponseRedirect('/home')
		else:
			print(form.errors)
			return HttpResponse(form.errors)

# API METHODS #

@csrf_exempt
def api_login(request):
	response_data = {}
	if request.method == 'POST':
		data = json.loads(request.body)
		user = authenticate(username = data['username'], password = data['password'])
		if user is not None:
			if user.is_active:
				#login(request,user)
				response_data['result'] = 'OK'
			else:
				response_data['result'] = 'NOT_ACTIVE'
		else:
			response_data['result'] = 'INVALID_CREDENTIALS'

	return HttpResponse(json.dumps(response_data), content_type='application/json')

@csrf_exempt
def api_register(request):
	response_data = {}
	if request.method == 'POST':
		data = json.loads(request.body)
		user = User(username=data['username'], email=data['email'], password=data['password'])
		user.set_password(data['password'])
		user.save()
		user = User.objects.get(username=data['username'])
		profile = Profile()
		profile.user = user
		profile.save()
		response_data['result'] = 'OK'
	return HttpResponse(json.dumps(response_data), content_type='application/json')

@csrf_exempt
def api_folders(request):
	response_data = {}
	if request.method == 'GET':
		print request.GET['username']
		data = request.GET['username']
		user = User.objects.get(username=data)
		profile = Profile.objects.get(user=user)
		if request.GET['parent']:
			data_parent = request.GET['parent']
			folders = Folders.objects.filter(profile = profile, parent = data_parent)
		else:
			folders = Folder.objects.filter(profile = profile, parent = None)
		serialized = serializers.serialize('python', folders)
		folder_serialized = [f['fields'] for f in serialized]
		if len(folders) == 0:
			create_vin(request)
		return HttpResponse(json.dumps(folder_serialized), content_type='application/json')

@csrf_exempt
def api_folder(request):
	response_data = {}
	if request.method = 'GET':
		data = request.GET['username']
		user = User.objects.get(username=data)
		profile = Profile.objects.get(user=user)
		parent = request.GET['parent']
		folder = Folder.objects.get(profile=profile, name=parent)
		folders = Folder.objects.filter(profile=profile, parent=folder).order_by('name')
		cards = Card.objects.filter(folder=folder.id).order_by('name')
		serialized = serializers.serialize('python', folders)
		serialized2 = serializers.serialize('python', cards)
		data_serialized = [f['fields'] for f in serialized]
		data_serialized.extend([f['fields'] for f in serialized2])
		return HttpResponse(json.dumps(data_serialized), content_type='application/json')

@csrf_exempt
def addfolder(request):
	if request.method == 'POST':
		data = request.loads(request.body)
		data_username = data['username']
		user = User.objects.get(username=data_username)
		profile = Profile.objects.get(user=user)
		folder = Folder(name=data['name'], parent = data['parent'], profile = profile)
		folder.save()
		response_data['result'] = 'OK'
		return HttpResponse(json.dumps(response_data), content_type='application/json')









	

		








