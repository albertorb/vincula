from django import forms
from django.contrib.auth.models import User
from models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('pic',)

class CardForm(forms.ModelForm):
	class Meta:
		model = Card
		fields = '__all__'
