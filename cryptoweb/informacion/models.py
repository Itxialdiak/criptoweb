from django.db import models

class PeriodoHistoria(models.Model):
    nombre = models.CharField(max_length=100)
    orden = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class HistoriaEp(models.Model):
    priodo = models.ForeignKey(PeriodoHistoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    orden = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='images/historia', null=True, blank=True)

    def __str__(self):
        return self.titulo

class TecnicaCriptografica(models.Model):
    nombre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    descripcion = models.TextField()
    detalles = models.TextField()
    imagen = models.ImageField(upload_to='images/tecnicas', null=True, blank=True)

    def __str__(self):
        return self.nombre
