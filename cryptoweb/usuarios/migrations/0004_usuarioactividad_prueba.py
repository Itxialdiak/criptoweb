# Generated by Django 5.1.4 on 2025-01-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuarioactividad_perfil_actividades_resueltas'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioactividad',
            name='prueba',
            field=models.BooleanField(default=False),
        ),
    ]
