# Generated by Django 5.1.4 on 2025-01-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0008_alter_actividad_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='clave',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
