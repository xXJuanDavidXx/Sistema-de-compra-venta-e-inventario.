# Generated by Django 5.1.1 on 2024-12-13 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0002_reporte_anual_reporte_mensual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte_anual',
            name='año',
            field=models.IntegerField(),
        ),
    ]
