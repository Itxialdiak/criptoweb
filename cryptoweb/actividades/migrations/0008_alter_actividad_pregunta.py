# Generated by Django 5.1.4 on 2025-01-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0007_actividad_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='Pregunta',
            field=models.TextField(),
        ),
    ]
