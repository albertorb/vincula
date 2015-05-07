from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Folder)
admin.site.register(Card)
admin.site.register(Profile)