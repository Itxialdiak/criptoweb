# Generated by Django 5.1.4 on 2025-01-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0006_actividad_puntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
