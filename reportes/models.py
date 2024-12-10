from django.db import models
from compra.models import Compra
from django.utils import timezone

# Create your models here.

class Factura(models.Model):
    """El modelo factura que representa un gasto por registro"""
    total = models.DecimalField(max_digits=10, decimal_places=0) #El total de la factura
    fecha = models.DateField(auto_now_add=True) #La fecha de la factura

    def __str__(self):
        return f"Factura {self.id} - {self.fecha}"


class Reporte(models.Model):
    """El modelo reporte que representa el estado de ganancias de la empresa por día"""
    fecha = models.DateField(default=timezone.now, unique=True) #La fecha del reporte
    ingresos = models.DecimalField(max_digits=10, decimal_places=0, default=0) #Los ingresos de la empresa por día
    gastos = models.DecimalField(max_digits=10, decimal_places=0, default=0) #Los gastos de la empresa por día
    ganancia = models.DecimalField(max_digits=10, decimal_places=0, default=0) #La ganancia de la empresa por día

    def actualizar_ganancias(self):
        """Actualiza los ingresos, gastos y ganancia de la empresa por día"""
        self.ingresos = sum(Compra.objects.filter(estado=False, order_date__date=timezone.now().date()).values_list('total', flat=True))
        self.gastos = sum(Factura.objects.filter(fecha=timezone.now().date()).values_list('total', flat=True))
        self.ganancia = self.ingresos - self.gastos
        self.save()