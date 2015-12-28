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

def updAlumno(request, id):
	obj_edit=Alumno.objects.get(pk=id)
	if request.method=='POST':
		objform=AlumnoForm(request.POST, instance=obj_edit) #oojo
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:alumno'))
	else:
		objform=AlumnoForm(instance=obj_edit)
	return render(request, 'perfiles/updAlumno.html', {'form': objform}, context_instance=RequestContext(request))

def delAlumno(request, id, template_name='perfiles/delAlumno.html'):
	objdel=Alumno.objects.get(pk=id)
	if request.method=='POST':
		objdel.delete()
		return redirect(reverse('perfiles_app:alumno'))	
	return render(request, template_name,{'object':objdel})


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

#@login_required
def updEncargado(request, id):
	obj_edit=Encargado.objects.get(pk=id)
	if request.method=='POST':
		formulario=EncargadoForm(request.POST, instance=obj_edit)
		if formulario.is_valid():
			formulario.save()
			return redirect(reverse('perfiles_app:encargado'))
	else:
		formulario=EncargadoForm(instance=obj_edit)
	return render(request,'perfiles/updEncargado.html', {'form':formulario},context_instance = RequestContext(request))

#@login_required	
def delEncargado(request, id, template_name='perfiles/delEncargado.html'):
    obj_delete = Encargado.objects.get(pk=id)    
    if request.method=='POST':
        obj_delete.delete()
        return redirect(reverse('perfiles_app:encargado'))
    return render(request, template_name, {'object':obj_delete})

def profesor(request):
	lista=Profesor.objects.all()
	numreg=lista.count()
	return render(request,'perfiles/profesor.html',{'lista':lista,'cantidad':numreg})

def addProfesor(request):
	if request.method=='POST':
		objform=ProfesorForm(request.POST, request.FILES)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:profesor'))
	else:
		objform=ProfesorForm()
	return render(request,'perfiles/addProfesor.html', {'form':objform})
	
def updProfesor(request, id):
	obj_edit=Profesor.objects.get(pk=id)
	if request.method=='POST':
		formulario=ProfesorForm(request.POST, instance=obj_edit)
		if formulario.is_valid():
			formulario.save()
			return redirect(reverse('perfiles_app:profesor'))
	else:
		formulario=ProfesorForm(instance=obj_edit)
	return render(request,'perfiles/updProfesor.html', {'form':formulario},context_instance = RequestContext(request))

def delProfesor(request, id, template_name='perfiles/delProfesor.html'):
    obj_delete = Profesor.objects.get(pk=id)    
    if request.method=='POST':
        obj_delete.delete()
        return redirect(reverse('perfiles_app:profesor'))
    return render(request, template_name, {'object':obj_delete})