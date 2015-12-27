from django.conf.urls import url


urlpatterns = [
  	url(r'^$', 'apps.perfiles.views.alumno', name='alumno'),   	
   	url(r'^addAlumno$', 'apps.perfiles.views.addAlumno', name='addAlumno'),
   	url(r'^encargado$', 'apps.perfiles.views.encargado', name='encargado'),
   	url(r'^encargado/add$','apps.perfiles.views.addEncargado', name='addEncargado'),
   	url(r'^profesor$','apps.perfiles.views.profesor',name='profesor'),
   	url(r'^profesor/add$', 'apps.perfiles.views.addProfesor', name='addProfesor'),
]
