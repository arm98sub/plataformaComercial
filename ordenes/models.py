from django.db import models
from django.conf import settings

from principal.models import Producto
from usuarios.models import Usuario_Vendedor


class ProductoOrdenado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    ordenado = models.BooleanField(default=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} of {self.producto.nombre}"

    def get_subtotal(self):
        return self.cantidad * self.producto.precio


class Orden(models.Model):
    fecha_compra = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    productos = models.ManyToManyField(ProductoOrdenado)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_orden = models.DateTimeField()
    ordenado = models.BooleanField(default=False)

    def __str__(self):
        return self.user.usuario.nombre

    def get_total(self):
        total = 0
        for prod_ordenado in self.productos.all():
            total += prod_ordenado.get_subtotal()
        return total

    def get_total_vendedor(self, vendedor):
        total = 0
        prod_vendedor = filter(lambda p: p.producto.vendedor == vendedor, self.productos.all())
        for p in prod_vendedor:
            total += p.get_subtotal()
        print(total)

    def get_pagos(self):
        vendedores = list()
        for prod in self.productos.all():
            if not vendedores.__contains__(prod.producto.vendedor):
                vendedores.append(prod.producto.vendedor)
        for vend in vendedores:
            self.get_total_vendedor(vend)
        return vendedores

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
