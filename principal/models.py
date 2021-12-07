from django.db import models


class Producto(models.Model):
    vendedor = models.ForeignKey(
        'usuarios.Usuario_Vendedor',
        verbose_name='Vendedor',
        on_delete=models.CASCADE, blank=False, null=False)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    imagen = models.ImageField(
        "Imagen",
        upload_to='principal',
        blank=True,
        null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(
        "Descripción",
        max_length=250,
        null=True,
        blank=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    vendedor = models.ForeignKey(
        'usuarios.Usuario',
        verbose_name='Vendedor',
        on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    imagen = models.ImageField(
        "Imagen",
        upload_to='principal',
        blank=True,
        null=True)
    descripcion = models.TextField(
        "Descripción",
        max_length=250,
        null=True,
        blank=True)
    categoria = models.CharField(max_length=50, blank=False, null=False)
