from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.conf import settings



class Usuario(User):
    # estado = ForeignKey("usuarios.Estado",verbose_name="Estado",on_delete=CASCADE)
    # municipio = ForeignKey("usuarios.Municipio",verbose_name="Municipio",on_delete=CASCADE)
    foto = models.ImageField("Foto de Perfil", upload_to= "perfil", blank = True, null=True)
    password2 = models.CharField("Verfica tu contraseña", blank=False, null=False, max_length = 62, default = "")
    puede_vender = models.BooleanField(default=False)
    
    
class Usuario_Vendedor(User):    
    # estado = ForeignKey("usuarios.Estado", verbose_name = "Estado", on_delete=CASCADE)
    # municipio = ForeignKey("usuarios.Municipio", verbose_name="Municipio", on_delete=CASCADE)
    foto = models.ImageField("Foto de Perfil", upload_to= "perfil", blank=True, null=True)
    direccion = models.CharField("Direccion", max_length=255, null=False, blank=False, default="")
    telefono = models.CharField("Telefono", max_length=10, null = False, blank=False, default="")
    password_rev = models.CharField("Verifica tu contraseña", blank=False, null=False, max_length= 62, default="")
    descripcion = models.CharField("Descripcion", max_length=255, null = True, blank = True)
    
        
class consulta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    Questions = models.TextField()
                        
class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey(
        'usuarios.Estado', verbose_name="Estado", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# class Permisos_Grupos(models.Model):
#     class Meta:
#         permissions = (('permiso_vendedores','Permiso creado para los vendedores'))
