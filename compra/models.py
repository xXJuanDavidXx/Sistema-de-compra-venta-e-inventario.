from django.db import models   
from app.models import Producto #Se debe importar para los detalles de la orden.
from django.contrib.auth.models import User

# Create your models here.     

class Compra(models.Model):     
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #La relación ForeignKey indica que cada compra está asociada a un solo usuario, pero un usuario puede tener varias compras.
    order_date = models.DateTimeField(auto_now_add=True) #Se crea con la fecha actual
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.BooleanField(default=True) #True si la compra está activa, False si está cerrada.


    def __str__(self):         
        return f"Compra {self.id} - {self.order_date}" 

    def actualizar_total(self): #Este método suma el total de los detalles de la compra (los productos y sus cantidades) y actualiza el campo total.
        self.total = sum(detalle.subtotal for detalle in self.detalleproducto_set.all())#self.detallesdecompra_set.all() accede a todos los objetos relacionados con la compra a través de la relación ForeignKey de DetallesDeCompra. Luego, calcula el subtotal para cada detalle y lo suma.
        self.save()

    def cerrar_compra(self): #este metodo finaliza la compra actual.
        self.estado = False
        self.save()




class DetalleProducto(models.Model):
    """
    En esta clase se guardan todos los items de la orden.
    """
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE) #Relacion con la compra
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT) #Relacion con el producto
    cantidad = models.PositiveIntegerField() #Cantidad del producto
    
    def __str__(self):
        return f"Detalle de compra {self.id} - {self.compra}"
    
    @property
    def subtotal(self): #Este metodo calcula el subtotal de cada producto por su cantidad
        return self.cantidad * self.producto.precio_final
