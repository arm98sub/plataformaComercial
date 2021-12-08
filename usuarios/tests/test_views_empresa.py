from django.test import TestCase
from usuarios.models import Usuario_Vendedor
from usuarios_permisos import *


class TestViews(TestCase):
     #Test registro cuenta normal
    def setUp(self, nombre='Erick Pinales', username="pyro1707", password = "prueba123", password_rev = "prueba123",
                email = "38192828@uaz.edu.mx", foto_perfil = False,
        ):
        
        fields = ('first_name', 'username', 'password', 'password_rev',
         'email', 'foto_perfil', 'direccion','telefono', 'descripcion')
        
        crear_grupos()
        self.empresa = Usuario_Vendedor(
            first_name = nombre,
            username = username,
            password = password,
            password_rev = password_rev,
            email = email,
            foto_perfil = foto_perfil
            
        )

        self.data = {
            'first_name' : nombre,
            'username' : username,
            'password' : password, 
            'password_rev' : password_rev,             
            'email' : email,
            'foto_perfil' : foto_perfil
        }

    #URLS   
    def test_url_empresa_registro(self):
        response= self.client.get('/usuarios/signup/')
        self.assertEquals(response.status_code,200)

    def test_template_empresa_registro(self):
        response = self.client.get('/usuarios/signup/')
        self.assertTemplateUsed(response,'sign_up.html')
    
    def test_registro_sin_nombre_usuario(self):
        response = self.client.get('/usuarios/signup/')
        self.assertTemplateUsed(response,'sign_up.html')
    
    #Test usuario
    def test_no_agrega_sin_user_name(self):
        self.data['username'] = ''
        response = self.client.post('/usuarios/signup/', self.data)
        self.assertEqual(Usuario.objects.all().count(),0)
    
    def test_no_agrega_sin_password(self):
        self.data['password'] = ''
        response = self.client.post('/usuarios/signup/', self.data)
        self.assertEqual(Usuario.objects.all().count(),0)
    
    def test_no_agrega_sin_verificar_password(self):
        self.data['password_rev'] = ''
        response = self.client.post('/usuarios/signup/', self.data)
        self.assertEqual(Usuario.objects.all().count(),0)

    def test_no_agrega_sin_direccion(self):
        self.data['direccion'] = ''
        response = self.client.post('/usuarios/signup/', self.data)
        self.assertEqual(Usuario.objects.all().count(),0)
    
    def test_no_agrega_sin_telefono(self):
        self.data['telefono'] = ''
        response = self.client.post('/usuarios/signup/', self.data)
        self.assertEqual(Usuario.objects.all().count(),0)

    def test_agregar_empresa_correctamente(self):
        response = self.client.post('/usuarios/signup/', self.data)
        self.assertEqual(response.status_code,302)
    
    def test_no_agrega_contrasena_diferentes(self):
        self.data['password'] = '------'
        self.data['password_rev'] = '123'
        response = self.client.post('/usuarios/signup/', self.data)
        self.assertEqual(Usuario.objects.all().count(),0)
    
    def test_no_agrega_usuario_caracteres_diferentes(self):
        self.data['username'] = '}'
        response = self.client.post('/usuarios/signup/', self.data)
        self.assertEqual(Usuario.objects.all().count(),0)