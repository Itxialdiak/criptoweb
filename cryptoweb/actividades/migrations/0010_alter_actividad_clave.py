# Generated by Django 5.1.4 on 2025-01-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0009_actividad_clave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='clave',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
