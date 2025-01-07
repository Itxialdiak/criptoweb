from django.db import models
from django.contrib.auth.models import User

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
    # Otros campos relevantes, como progreso, etc.

    def __str__(self):
        return f"{self.user.username} - {self.nivel}"
