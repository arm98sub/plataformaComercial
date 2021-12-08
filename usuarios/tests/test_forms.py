from django.contrib.auth.models import User
from django.test import TestCase
from usuarios.models import Usuario, Estado, Municipio 
from usuarios.forms import  UsuarioForm
from django.core.exceptions import ValidationError


class TestFormUsuario(TestCase):

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
        
        self.datos = {
            'first_name': nombre,
            'username': nombreusaurio,
            'password': password,
            'password2': password2,
            'email': correo,
            'estado:': estado,
            'municipio': municipio
            
        }
        

    # TEST PARA USUARIO
    def test_usuario_form_nombre_vacio(self):
        self.datos['username'] = ''
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
    
    def test_usuario_form_password_invalida_vacia(self):
        self.datos['password'] = ''
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password'],
            ['Este campo es obligatorio.'])
    
    def test_usuario_form_password2_invalida_vacia(self):
        self.datos['password2'] = ''
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password2'],
            ['Este campo es obligatorio.'])
    
    
"""
    def test_usuario_form_valido(self):
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())
    
     def test_usuario_form_password_valida(self):
        self.datos['password'] = ' '
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_mas_caracteres(self):
        self.datos['username'] = 'erickkkkkkkkkkkkkk'
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())


    def test_usuario_form_password_invalida(self):
        self.datos['password'] = 'a12'
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())

 

    def test_usuario_form_nombre_mas_caracteres(self):
        self.datos['username'] = 'isaacdiazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())

"""