from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Alumno, Encargado, Profesor


class AlumnoForm(forms.ModelForm):
	class Meta:
		model=Alumno
		exclude=()
		widgets={
		#'usuario':forms.TextInput(attrs={'class':'form-control'}),
		'nombres':forms.TextInput(attrs={'class':'form-control'}),
		'apellidos':forms.TextInput(attrs={'class':'form-control'}),
		'dni':forms.TextInput(attrs={'class':'form-control'}),
		'lugar_nac':forms.TextInput(attrs={'class':'form-control'}),
		'direccion':forms.TextInput(attrs={'class':'form-control'}),
		'ciudad':forms.TextInput(attrs={'class':'form-control'}),
		'provincia':forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.TextInput(attrs={'class':'form-control'}),
		#'imagen':forms.FileInput(attrs={'class':'btn btn-warning'}),
		}
		
class EncargadoForm(forms.ModelForm):
	class Meta:
		model=Encargado
		exclude=()
		widgets={
		'nombres':forms.TextInput(attrs={'class':'form-control'}),
		'apellidos':forms.TextInput(attrs={'class':'form-control'}),
		'dni':forms.TextInput(attrs={'class':'form-control'}),
		'direccion':forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.EmailInput(attrs={'class':'form-control'}),
		'ocupacion':forms.TextInput(attrs={'class':'form-control'}),
		}
		
class ProfesorForm(forms.ModelForm):
	class Meta:
		model=Profesor
		exclude=()
		
	