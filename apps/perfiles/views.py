from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from .models import Alumno, Encargado, Profesor
from .forms import AlumnoForm, EncargadoForm, ProfesorForm


#@login_required
def alumno(request):
	lista=Alumno.objects.all()
	numreg=lista.count()
	return render(request,'perfiles/alumno.html',{'lista':lista,'cantidad':numreg})

def addAlumno(request):
	if request.method=='POST':
		objform=AlumnoForm(request.POST, request.FILES)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:alumno'))
	else:
		objform=AlumnoForm()
	return render(request,'perfiles/addAlumno.html', {'form':objform})	

def encargado(request):
	lista=Encargado.objects.all()
	numreg=lista.count()
	return render(request,'perfiles/encargado.html',{'lista':lista,'cantidad':numreg})

def addEncargado(request):
	if request.method=='POST':
		objform=EncargadoForm(request.POST, request.FILES)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:encargado'))
	else:
		objform=EncargadoForm()
	return render(request,'perfiles/addEncargado.html', {'form':objform})	

def profesor(request):
	lista=Profesor.objects.all()
	numreg=lista.count()
	return render(request, 'perfiles/profesor.html', {'lista':lista, 'cantidad':numreg})

def addProfesor(request):
	if request.method=='POST':
		objform=ProfesorForm(request.POST, request.FILES)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:profesor'))
	else:
		objform=ProfesorForm()
	return render(request,'perfiles/addProfesor.html', {'form':objform})
	