from django.test import TestCase
from usuarios.models import Usuario
from usuarios_permisos import *


class TestViews(TestCase):
     #Test registro cuenta
    def setUp(self, nombre='Golden Koi', username="pyrope", password = "test123", password2 = "test123",
                    email = "38192828@uaz.edu.mx", foto = False):
        
        fields = ('first_name', 'username', 'password', 'password2',
            'email', 'foto')
        
        crear_grupos()
        self.usuario = Usuario(
            first_name = nombre,
            username = username,
            password = password,
            password2 = password2,
            email = email,
            foto = foto
        )

        self.data_usuario = {
            'first_name' : nombre,
            'username' : username,
            'password' : password, 
            'password2' : password2,             
            'email' : email,
            'foto' : foto
        }

    #URLS   
    def test_url_usuario_registro(self):
        response= self.client.get('/usuarios/signup/')
        self.assertEquals(response.status_code,200)

    def test_template_usuario_registro(self):
        response = self.client.get('/usuarios/signup/')
        self.assertTemplateUsed(response,'sign_up.html')
    
    def test_registro_sin_nombre_usuario(self):
        response = self.client.get('/usuarios/signup/')
        self.assertTemplateUsed(response,'sign_up.html')
    
    #Test usuarios
    def test_no_agrega_sin_user_name(self):
        self.data_usuario['username'] = ''
        response = self.client.post('/usuarios/signup/', self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(),0)
    
    def test_no_agrega_sin_password(self):
        self.data_usuario['password'] = ''
        response = self.client.post('/usuarios/signup/', self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(),0)
    
    def test_no_agrega_sin_verificar_password(self):
        self.data_usuario['password2'] = ''
        response = self.client.post('/usuarios/signup/', self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(),0)


    def test_agregar_usuario_correctamente(self):
        response = self.client.post('/usuarios/signup/', self.data_usuario)
        self.assertEqual(response.status_code,302)
    
    def test_no_agrega_contrasena_diferentes(self):
        self.data_usuario['password'] = '------'
        self.data_usuario['password2'] = '123'
        response = self.client.post('/usuarios/signup/', self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(),0)
    
    def test_no_agrega_usuario_caracteres_diferentes(self):
        self.data_usuario['username'] = '}'
        response = self.client.post('/usuarios/signup/', self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(),0)