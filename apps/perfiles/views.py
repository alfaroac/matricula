from django.shortcuts import render

#@login_required
def alumno(request):
	return render(request, 'perfiles/alumno.html')