from django.contrib import admin

from .models import Usuario, Estado, Municipio

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Estado)
admin.site.register(Municipio)
