# Generated by Django 5.1.1 on 2024-10-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='detallesdecompra',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
