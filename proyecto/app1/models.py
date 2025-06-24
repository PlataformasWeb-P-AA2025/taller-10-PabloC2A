from django.db import models

class Parroquia(models.Model):
    UBICACION_CHOICES = [
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    ]

    TIPO_CHOICES = [
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
    ]

    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=10, choices=UBICACION_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.PositiveIntegerField()
    numero_parques = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 7)])
    numero_edificios_residenciales = models.PositiveIntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    def __str__(self):
        return self.nombre
