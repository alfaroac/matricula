from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'index.html'}, name='login'),
    url(r'^matricula/', include('apps.matricula.urls')),
    #url(r'^lectores/', include('apps.lectores.urls')),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',name='logout'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
]
