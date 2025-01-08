from django.db import models
from django.contrib.auth.models import User

class Nivel(models.Model):
    nombre = models.CharField(max_length=20, choices=[
        ('Básico', 'Básico'),
        ('Fácil', 'Fácil'),
        ('Medio', 'Medio'),
        ('Avanzado', 'Avanzado'),
        ('Experto', 'Experto'),
    ])

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    Pregunta = models.TextField()
    pista = models.TextField()
    nivel_requerido = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    solucion = models.TextField()
    puntos = models.PositiveIntegerField()
    clave = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.titulo
    
class Pregunta(models.Model):
    texto = models.CharField(max_length=255)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    opcion1 = models.CharField(max_length=100)
    opcion2 = models.CharField(max_length=100)
    opcion3 = models.CharField(max_length=100)
    respuesta_correcta = models.CharField(max_length=100)

    def __str__(self):
        return self.texto

