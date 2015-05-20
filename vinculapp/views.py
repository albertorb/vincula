# encoding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .miscellanea import create_vin

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
			print(django)
			profile.user = django
			print(profile.user)
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
	if request.user.username == 'vincula':
		create_vin(request)
	return render(request, 'vinculapp/home.html', locals())

@login_required(login_url='/')
def content(request):
	folder = Folder.objects.get(id = request.POST['folder'])
	folders = Folder.objects.filter(profile=request.user.profile, parent=folder)
	cards = Card.objects.filter(folder=folder.id)
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
		








