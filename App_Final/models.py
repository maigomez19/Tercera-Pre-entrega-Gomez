from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    detalle = models.TextField()
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    seccion_rostro = models.CharField(max_length=40)

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    clave = models.CharField(max_length=20)
    rol = models.IntegerField()

class Articulo(models.Model):
    titulo = models.CharField(max_length=40)
    detalle = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    autor = models.CharField(max_length=40)
    clasificacion = models.CharField(max_length=40)