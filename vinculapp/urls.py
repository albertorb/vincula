# vinculapp urls

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/', views.index, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^$', views.login, name='login'),
]