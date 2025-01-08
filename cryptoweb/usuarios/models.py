from django.db import models
from django.contrib.auth.models import User
from actividades.models import Actividad

class Perfil(models.Model):
    NIVEL_CHOICES = [
        ('Básico', 'Básico'),
        ('Fácil', 'Fácil'),
        ('Medio', 'Medio'),
        ('Avanzado', 'Avanzado'),
        ('Experto', 'Experto'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=10, choices=NIVEL_CHOICES, default='Básico')
    experiencia = models.PositiveIntegerField(default=0)
    actividades_resueltas = models.ManyToManyField(Actividad, through='UsuarioActividad')
    # Otros campos relevantes, como progreso, etc.

    def __str__(self):
        return f"{self.user.username} - {self.nivel}"

class UsuarioActividad(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)

    class Meta:
        unique_together = ('perfil', 'actividad')

    def __str__(self):
        return f"{self.usuario.username} - {self.actividad.titulo} - {'Resuelta' if self.estado else 'No Resuelta'}"