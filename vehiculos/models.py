from django.db import models

# Create your models here.

# clases vehiculo
# patente
# marca
# modelo
# year

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6,primary_key=True)
    marca = models.CharField(max_length=20,null=False)
    modelo = models.CharField(max_length=20,null=False)
    year = models.IntegerField(null=False)

    def __str__(self):
        return self.patente
    
# Class chofer
# rut
# nombre
# apellido
# activo
# creacion_registro
# vehiculo - onatoonefield

class Chofer(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.rut
    
# class RegistroContabilidad

class RegistroContabilidad(models.Model):
    fecha_compra = models.DateTimeField(null=False)
    valor = models.FloatField(null=False)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.fecha_compra
    
        
    
