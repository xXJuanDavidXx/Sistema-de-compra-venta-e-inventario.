# Generated by Django 5.1.1 on 2024-12-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte_anual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.DateField()),
                ('ingresos', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('gastos', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('ganancia', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte_mensual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.DateField()),
                ('ingresos', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('gastos', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('ganancia', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
    ]
