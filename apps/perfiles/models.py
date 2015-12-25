# coding: utf-8
from django.db import models
#from django.contrib.auth.models import User


class Encargado(models.Model):

    ECV = [
        ('Soltero', 'Soltero(a)'),
        ('Casado', 'Casado(a)'),
        ('Viudo', 'Viudo(a)'),
    ]
    SEX = [
        ('M', 'Padre'),
        ('F', 'Madre'),
    ]
    nombres = models.CharField(max_length=50, unique=True)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=8, unique=True)
    sexo = models.CharField(choices=SEX, max_length=10,
                            blank=True, verbose_name='Encargado')
    direccion = models.CharField(max_length=100)
    estado_civil = models.CharField(choices=ECV, max_length=10, blank=True, verbose_name='Estado_civíl')
    telefono = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    ocupacion = models.CharField(max_length=40)

    def __str__(self):
        return u"%s %s" % (self.nombres, self.apellidos)


class Alumno(models.Model):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    #usuario = models.OneToOneField(User)
    nombres = models.CharField(max_length=50, unique=True)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=8, unique=True)
    sexo = models.CharField(choices=SEX, max_length=10,
                            blank=True, verbose_name='Género')
    fecha_nac = models.DateTimeField(auto_now=True)
    lugar_nac = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    imagen = models.ImageField(upload_to='alumnos')  # falta hacer algo
    encargado = models.ForeignKey(Encargado)

    # def __unicode__(self):
    #     return self.nombres
    def __str__(self):
        return u"%s %s" % (self.nombres, self.apellidos)


class Profesor(models.Model):

    nombres = models.CharField(max_length=50, unique=True)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=8, unique=True)
    direccion = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=13)
    fecha_nac = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='profesores')  # falta hacer algo

    def __str__(self):
        return u"%s %s" % (self.nombres, self.apellidos)
