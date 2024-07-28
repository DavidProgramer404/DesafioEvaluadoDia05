from .models import Vehiculo, Chofer, RegistroContabilidad
from django.utils import timezone

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year)
    vehiculo.save()
    return vehiculo

def crear_chofer(rut, nombre, apellido):
    chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido)
    chofer.save()
    return chofer

def crear_registro_contable(fecha_compra, valor, vehiculo):
    registro = RegistroContabilidad(fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo)
    registro.save()
    return registro

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()
    return chofer

def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.chofer.activo = False
    vehiculo.save()
    return vehiculo

def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()
    return chofer

def habilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.chofer.activo = True
    vehiculo.save()
    return vehiculo

def obtener_vehiculo(patente):
    return Vehiculo.objects.get(patente=patente)

def obtener_chofer(rut):
    return Chofer.objects.get(rut=rut)

def asignar_chofer_a_vehiculo(rut, patente):
    chofer = Chofer.objects.get(rut=rut)
    vehiculo = Vehiculo.objects.get(patente=patente)
    chofer.vehiculo = vehiculo
    chofer.save()
    return chofer

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f'Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}')
