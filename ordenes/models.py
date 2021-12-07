from django.db import models


class Orden(models.Model):
    fecha_compra = models.DateField(auto_now_add=True)
    usuario = models.CharField(max_length=150)


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
