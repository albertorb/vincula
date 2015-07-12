# vinculapp urls

from django.conf.urls import url, patterns
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^home/', views.index, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^addfolder/', views.addfolder, name='addfolder'),
    url(r'^content/', views.content, name='content'),
    url(r'^search/', views.search_content, name='search'),
    url(r'^api/login/', views.api_login, name='apilogin'),
    url(r'^api/register/', views.api_register, name='apiregister'),
    url(r'^api/folders/', views.api_folders, name='apifolders'),
    url(r'^api/folder/', views.api_folder, name='apifolder'),
    url(r'^api/add/folder/', views.addfolder, name='apiaddfolder'),
    url(r'^api/add/card/', views.addcard, name='apiaddcard'),
    url(r'^$', views._login, name='login'),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)