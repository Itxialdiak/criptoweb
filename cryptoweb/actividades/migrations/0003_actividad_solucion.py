# Generated by Django 5.1.4 on 2025-01-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='solucion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
