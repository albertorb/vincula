# vinculapp urls

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/', views.index, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^addfolder/', views.addfolder, name='addfolder'),
    url(r'^$', views._login, name='login'),
]