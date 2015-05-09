# encoding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import *

# Create your views here.

def login(request):
	errors = False
	if request.POST:
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			if user.is_active:
				return HttpResponseRedirect('/home')
			else:
				return HttpResponse("Esta cuenta de usuario aún no ha sido activada")
		else:
			errors = True
			return render(request, 'vinculapp/login.html', locals())

	return render(request, 'vinculapp/login.html', locals())

def index(request):
	
	return render(request, 'vinculapp/master.html', locals())