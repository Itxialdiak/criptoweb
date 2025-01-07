from django.db import models

class HistoriaEp(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    orden = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class TecnicaCriptografica(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    detalles = models.TextField()

    def __str__(self):
        return self.nombre
