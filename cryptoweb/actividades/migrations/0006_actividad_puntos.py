# Generated by Django 5.1.4 on 2025-01-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0005_remove_actividad_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='puntos',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
