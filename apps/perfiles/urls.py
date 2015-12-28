from django.conf.urls import url


urlpatterns = [
  	url(r'^$', 'apps.perfiles.views.alumno', name='alumno'),   	
   	url(r'^addAlumno$', 'apps.perfiles.views.addAlumno', name='addAlumno'),
   	url(r'^alumno/upd/(?P<id>\d+)$', 'apps.perfiles.views.updAlumno', name='updAlumno'),
    url(r'^alumno/del/(?P<id>\d+)$', 'apps.perfiles.views.delAlumno', name='delAlumno'),

   	url(r'^profesor$','apps.perfiles.views.profesor',name='profesor'),
   	url(r'^profesor/add$', 'apps.perfiles.views.addProfesor', name='addProfesor'),
    url(r'^profesor/upd/(?P<id>\d+)$', 'apps.perfiles.views.updProfesor', name='updProfesor'),    
    url(r'^profesor/del/(?P<id>\d+)$', 'apps.perfiles.views.delProfesor', name='delProfesor'),
   	
   	url(r'^encargado$', 'apps.perfiles.views.encargado', name='encargado'),
   	url(r'^encargado/add$','apps.perfiles.views.addEncargado', name='addEncargado'),
   	url(r'^encargado/upd/(?P<id>\d+)$', 'apps.perfiles.views.updEncargado', name='updEncargado'),     
    url(r'^encargado/del/(?P<id>\d+)$', 'apps.perfiles.views.delEncargado', name='delEncargado'),


]
