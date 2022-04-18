from django.db import models
from django.conf import settings

from principal.models import Producto


class ProductoOrdenado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE)
    ordenado = models.BooleanField(default= False)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    
    def __str__(self):
        return f"{self.cantidad} of {self.producto.nombre}"
    
    
    def get_subtotal(self):
        return self.cantidad * self.producto.precio
        

class Orden(models.Model):
    fecha_compra = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE)
    productos = models.ManyToManyField(ProductoOrdenado)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_orden = models.DateTimeField()
    ordenado = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.user.usuario.nombre
    
    def get_total(self):
        total = 0
        for prod_ordenado in self.productos.all():
            total += prod_ordenado.get_subtotal()
        return total


class DetalleOrden(models.Model):
    producto = models.ForeignKey(
        "principal.Producto",
        verbose_name="Producto",
        on_delete=models.CASCADE)
    orden = models.ForeignKey(
        "ordenes.Orden",
        verbose_name="Orden",
        on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad")
    precio = models.FloatField("Precio unitario")
