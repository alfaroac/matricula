# coding: utf-8
from django.db import models
from apps.perfiles.models import Alumno, Profesor


class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=4)
    descripcion = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor)

    def __str__(self):
        return "%s | %s" % (self.nombre, self.profesor.nombres)
    
class Matricula(models.Model):

    # codigo=models.CharField(max_length=10)
    fec_reserva = models.DateTimeField(auto_now_add=True)
    pago = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    fec_confirma = models.DateTimeField()
    alumno = models.ForeignKey(Alumno)
    curso = models.ForeignKey(Curso)
    
