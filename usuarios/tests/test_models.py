from django.contrib.auth.models import User
from django.test import TestCase

from usuarios.models import Usuario, Estado, Municipio
from django.core.exceptions import ValidationError


class TestModels(TestCase):
    def setUp(self, nombre='Usuario de pruebas', nombreusaurio='usuaario_prueba2',
              password='prueba123', saldo='100', password2='pruebas123',
              correo='erickoalex070@gmail.com', estado='Zacatecas', municipio='Villa Gonzalez', ):


        self.estado = Estado(
           nombre = estado
           
        )
        self.estado.save()
        
       
        self.municipio = Municipio(
            nombre = municipio,
            estado = self.estado
        )
        self.municipio.save()
   
        self.data_nuevo = {
            'username': nombreusaurio,
            'contra': password
        }
        self.usuario = Usuario(
            first_name=nombre,
            username = nombreusaurio,
            password=password,
            password2 = password2,
            email = correo,
            estado = self.estado,
            municipio = self.municipio
        )
        
      

    def test_prueba_humo(self):
        self.assertEqual(2 + 2, 4)

    def test_return_object_usuario(self):
        self.usuario.full_clean()
        self.usuario.save()
        self.assertEqual(User.objects.first().username, self.usuario.__str__())
    
    def test_nombre_es_requerido(self):
        usuario = Usuario(
            username='pyro',
            password='Contraseña12345'
        )
        with self.assertRaises(ValidationError):
            usuario.full_clean()
"""


"""