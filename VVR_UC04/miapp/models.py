from django.db import models

class estudiante(models.Model):
    codigo = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apepat = models.CharField(max_length=100)
    apemat = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    estado = models.BooleanField()
