from django.db import models
from django.contrib import admin
from django.urls import reverse

# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=250)
    dpi = models.IntegerField()
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Predio(models.Model):
    largo = models.FloatField()
    ancho = models.FloatField()
    nomenclatura = models.CharField(max_length=10)
    def __str__(self):
        return self.nomenclatura
    
class Reservation(models.Model):
    titular = models.CharField(max_length=250)
    espacios = models.IntegerField()
    niveles = models.IntegerField()
    ornato = models.BooleanField()
    cancelado = models.BooleanField()
    inspeccion = models.BooleanField()
    fecha = models.DateField()
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)

    def __str__(self):
        return 'Titular: '+ self.titular + 'Espacios: '+ str(self.espacios)

    def get_absolute_url(self):
        return reverse("nichos:show-reservation", kwargs={"id":self.id})





    