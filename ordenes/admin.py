from django.contrib import admin
from .models import Orden, DetalleOrden
# Register your models here.

admin.site.register(Orden)
admin.site.register(DetalleOrden)
