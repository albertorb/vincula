from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def login(request):
	return render(request, 'vinculapp/login.html', locals())

def index(request):
	
	return render(request, 'vinculapp/master.html', locals())