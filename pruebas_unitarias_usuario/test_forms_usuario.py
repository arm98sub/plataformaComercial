from django import test
from django.test import TestCase
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm


class TestForms(TestCase):
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
        # TEST PARA USUARIO
    def test_usuario_form_nombre_vacio(self):
        self.data_usuario['username'] = ''
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_password_invalida_vacia(self):
        self.data_usuario['password'] = ''
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password'],
            ['Este campo es obligatorio.'])
    
    def test_usuario_form_password2_invalida_vacia(self):
        self.data_usuario['password2'] = ''
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password2'],
            ['Este campo es obligatorio.'])
    
    
    #No valido
    def test_usuario_form_nombre_mas_caracteres_del_limite(self):
        self.data_usuario['first_name'] = 'Pyro' * 50
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_form_username_vacio(self):
        self.data_usuario['username'] = ''
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_form_username_invalido(self):
        self.data_usuario['username'] = '}'
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_username_mas_caracteres_del_limite(self):
        self.data_usuario['username'] = 'PyroPe' * 60
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_password_vacio(self):
        self.data_usuario['password'] = ''        
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_password_mas_caracteres_del_limite(self):
        self.data_usuario['password'] = 'test123' * 60
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password2_vacio(self):
        self.data_usuario['password2'] = ''     
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_password2_mas_caracteres_del_limite(self):
        self.data_usuario['password2'] = 'test123' * 60
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_form_email_no_valido(self):
        self.data_usuario['email'] = 'pyro@'     
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_email_con_espacio(self):
        self.data_usuario['email'] = 'pyro @gmail.com'     
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_email_mas_caracteres_del_limite(self):
        self.data_usuario['email'] = 'pyro@gmail.com' * 60
        form = UsuarioForm(self.data_usuario)
        self.assertFalse(form.is_valid())
   

    #Valido
    def test_usuario_form_username_valido(self):
        self.data_usuario['username'] = 'Pyrope1707'
        form = UsuarioForm(self.data_usuario)
        self.assertTrue(form.is_valid())
    
    def test_usuario_form_password_valido(self):
        self.data_usuario['password'] = 'test123'        
        form = UsuarioForm(self.data_usuario)
        self.assertTrue(form.is_valid())

    def test_usuario_form_password2_valido(self):
        self.data_usuario['password2'] = 'test123'     
        form = UsuarioForm(self.data_usuario)
        self.assertTrue(form.is_valid())

    def test_usuario_form_email_valido(self):
        self.data_usuario['email'] = 'pyrope@gmail.com'     
        form = UsuarioForm(self.data_usuario)
        self.assertTrue(form.is_valid())
    
    def test_form_usuario_valid(self):
        usuario_form = UsuarioForm(self.data_usuario)
        self.assertTrue(usuario_form.is_valid())       