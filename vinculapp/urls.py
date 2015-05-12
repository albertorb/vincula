# vinculapp urls

from django.conf.urls import url, patterns
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^home/', views.index, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^addfolder/', views.addfolder, name='addfolder'),
    url(r'^content/', views.content, name='content'),
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