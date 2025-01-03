# Generated by Django 5.1.1 on 2024-10-24 18:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now, unique=True)),
                ('ingresos', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('gastos', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('ganancia', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
    ]
