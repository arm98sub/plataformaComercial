from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class Usuario(User):
    estado = ForeignKey("usuarios.Estado",verbose_name="Estado",on_delete=CASCADE)
    municipio = ForeignKey("usuarios.Municipio",verbose_name="Municipio",on_delete=CASCADE)
    foto = models.ImageField("Foto de Perfil", upload_to= "perfiles", blank = True, null=True)
    puede_vender = models.BooleanField(default=False)
                        
    
class Estado(models.Model):
    nombre= models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
    nombre= models.CharField(max_length=50)
    estado = models.ForeignKey('usuarios.Estado',verbose_name="Estado",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre