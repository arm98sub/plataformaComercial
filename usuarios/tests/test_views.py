from django.contrib.auth.models import User
from django.test import TestCase
from usuarios.models import Usuario, Estado, Municipio


class TestViews(TestCase):
    def setUp(self, nombre='Usuario de pruebas', nombreusaurio='usuaario_prueba2',
              password='prueba123', saldo='100', password2='pruebas123',
              correo='erickoalex070@gmail.com', estado='Zacatecas', municipio='Villa Gonzalez', ):


        self.estado = Estado(
           nombre = estado
        )
       
        self.municipio = Municipio(
            nombre = municipio,
            estado = self.estado
        )
   
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
        
      

 

    # TEST DEL NOMBRE EN USUSRIO
    def test_no_agrega_sin_nombre_usuario(self):
        self.login_usuario()
        self.data_nuevo['username'] = ''
        response = self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_agrega_invalido_usuario(self):
        self.login_usuario()
        self.data_nuevo['username'] = 'un'
        response = self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_agrega_invalido_usuario_invalido(self):
        self.login_usuario()
        self.data_nuevo['username'] = 'un123'
        response = self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_agrega_invalido_usuario_invalido_2(self):
        self.login_usuario()
        self.data_nuevo['username'] = 'empresa'
        response = self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    # Funciones #

    def login_usuario(self):
        self.client.login(username='usuaario_prueba2', password='prueba123')

   