from django.contrib import admin
from .models import Producto, Servicio, Categoria

admin.site.register(Producto)
admin.site.register(Categoria)

admin.site.register(Servicio)
