from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save

from usuarios.models import Usuario_Vendedor


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    vendedor = models.ForeignKey(
        Usuario_Vendedor,
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
    categoria = models.ForeignKey(
        'principal.Categoria', verbose_name='Categoria', on_delete=models.DO_NOTHING)
    descripcion = models.CharField(
        "Descripción",
        max_length=250,
        null=True,
        blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    vendedor = models.ForeignKey(
        User,
        verbose_name='Vendedor',
        on_delete=models.CASCADE, blank=False, null=False)
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
    categoria = models.ForeignKey(
        'principal.Categoria', verbose_name='Categoria', on_delete=models.DO_NOTHING)
