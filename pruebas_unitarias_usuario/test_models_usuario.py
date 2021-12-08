from django.test import TestCase
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.core.exceptions import ValidationError


class TestModels(TestCase):
    def setUp(self, nombre='Golden Koi', username="pyrope", password = "test123", password2 = "test123",
                    email = "38192828@uaz.edu.mx", foto = False):
        
            fields = ('first_name', 'username', 'password', 'password2',
            'email', 'foto')

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

    #Campos vacios
    def test_user_name_es_no_vacio(self):
        self.usuario.username = ''
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
    
    def test_user_name_es_no_acepta_caracteres(self):
        self.usuario.username = '}'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
    
    def test_user_name_es_no_acepta_espacios(self):
        self.usuario.username = 'Pyro 17'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
    
    def test_user_name_es_no_mas_de_150_caracteres(self):
        self.usuario.username = 'Pyro17' * 50
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_password_no_vacio(self):
        self.usuario.password = ''
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
    
    def test_password_no_mas_de_70_caracteres(self):
        self.usuario.password = 'test123'* 50
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_correo_con_formato_correcto(self):
        self.usuario.email = 'pyro@'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
    
    def test_correo_no_acepta_con_espacios(self):
        self.usuario.email = '38192828@ uaz.edu.mx'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
    
   
    
        