from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from .forms import AlumnoForm, EncargadoForm


#@login_required
def main(request):
	return render(request, 'main/main.html')

#@login_required
#def matricula(request):
#	return render(request, 'matricula/matricula.html')

def matricula(request):
	if request.method=='POST':
		objform=AlumnoForm(request.POST)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('matricula_app:matricula'))
	else:
		objform=AlumnoForm()
		objform1=EncargadoForm()
	return render(request, 'matricula/matricula.html',{'form':objform, 'form1':objform1})