from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
#from django.contrib.auth.decorators import login_required
from .forms import AlumnoForm, EncargadoForm, MatriculaForm, CursoForm
from .models import Matricula, Curso


#@login_required
def main(request):
	return render(request, 'main/main.html')

#@login_required
#def matricula(request):
#	return render(request, 'matricula/matricula.html')
def matricula(request):
	lista=Matricula.objects.all()
	numreg=lista.count()
	return render(request,'matricula/matricula.html',{'lista':lista,'cantidad':numreg})

def addMatricula(request):
	if request.method=='POST':
		objform=MatriculaForm(request.POST)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('matricula_app:matricula'))
	else:
		objform=MatriculaForm()		
	return render(request, 'matricula/addMatricula.html',{'form':objform})

def curso(request):
	lista=Curso.objects.all()
	numreg=lista.count()
	return render(request, 'matricula/cursos.html', {'lista':lista, 'cantidad':numreg})

def addCurso(request):
	if request.method=='POST':
		objform=CursoForm(request.POST, request.FILES)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('matricula_app:curso'))
	else:
		objform=CursoForm()
	return render (request, 'matricula/addCurso.html', {'form':objform})