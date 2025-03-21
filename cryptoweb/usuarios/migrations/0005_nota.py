# Generated by Django 5.1.4 on 2025-01-08 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0011_remove_actividad_estado'),
        ('usuarios', '0004_usuarioactividad_prueba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.actividad')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.perfil')),
            ],
        ),
    ]
