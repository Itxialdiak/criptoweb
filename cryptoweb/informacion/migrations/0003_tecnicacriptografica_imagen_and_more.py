# Generated by Django 5.1.4 on 2025-01-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacion', '0002_periodohistoria_historiaep_imagen_historiaep_priodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tecnicacriptografica',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/tecnicas'),
        ),
        migrations.AddField(
            model_name='tecnicacriptografica',
            name='type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
