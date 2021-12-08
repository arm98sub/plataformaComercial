from django import test
from django.test import TestCase
from usuarios.models import Usuario_Vendedor
from usuarios.forms import Usuario_Vendedor_Form


class TestForms(TestCase):
    def setUp(self, nombre='Talabarteria Avalos', username="Avalos33", password = "test123", password_rev = "test123",
                    email = "37180266@uaz.edu.mx", foto_perfil = False, direccion = "Callejon allende",
                    telefono = "4945148745", descripcion = "Taller de artesanias" ):

            self.empresa = Usuario_Vendedor(
                first_name = nombre,
                username = username,
                password = password,
                password_rev = password_rev,
                email = email,
                foto_perfil = foto_perfil,
                direccion = direccion,
                telefono = telefono,
                descripcion = descripcion
            )

            self.data_empresa = {
                'first_name' : nombre,
                'username' : username,
                'password' : password, 
                'password_rev' : password_rev,             
                'email' : email,
                'foto_perfil' : foto_perfil, 
                'direccion' : direccion,
                'telefono' : telefono, 
                'descripcion' : descripcion
            }
    #No valido
    def test_usuario_vendedor_form_nombre_mas_caracteres_del_limite(self):
        self.data_empresa['first_name'] = 'Daniel' * 50
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())

    def test_usuario_vendedor_form_username_vacio(self):
        self.data_empresa['username'] = ''
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())

    def test_usuario_vendedor_form_username_invalido(self):
        self.data_empresa['username'] = '}'
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_username_mas_caracteres_del_limite(self):
        self.data_empresa['username'] = 'Avalos' * 60
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_password_vacio(self):
        self.data_empresa['password'] = ''        
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_password_mas_caracteres_del_limite(self):
        self.data_empresa['password'] = 'test123' * 60
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())

    def test_usuario_vendedor_form_password_rev_vacio(self):
        self.data_empresa['password_rev'] = ''     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_password_rev_mas_caracteres_del_limite(self):
        self.data_empresa['password_rev'] = 'test123' * 60
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())

    def test_usuario_vendedor_form_email_no_valido(self):
        self.data_empresa['email'] = 'avalos@'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_email_con_espacio(self):
        self.data_empresa['email'] = 'avalos @gmail.com'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_email_mas_caracteres_del_limite(self):
        self.data_empresa['email'] = 'avalos@gmail.com' * 60
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_direccion_vacia(self):
        self.data_empresa['direccion'] = ''     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_direccion_mas_caracteres_del_limite(self):
        self.data_empresa['direccion'] = 'Constitutentes 6' * 60
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_telefono_vacia(self):
        self.data_empresa['telefono'] = ''     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())
    
    def test_usuario_vendedor_form_telefono_mas_de_10(self):
        self.data_empresa['telefono'] = '121454789652'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())

    def test_usuario_vendedor_form_telefono_vacia(self):
        self.data_empresa['telefono'] = 'ndnsnsndncjdn'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertFalse(form.is_valid())         

    #Valido
    def test_usuario_vendedor_form_username_valido(self):
        self.data_empresa['username'] = 'Avalos33'
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertTrue(form.is_valid())
    
    def test_usuario_vendedor_form_password_valido(self):
        self.data_empresa['password'] = 'test123'        
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertTrue(form.is_valid())

    def test_usuario_vendedor_form_password_rev_valido(self):
        self.data_empresa['password_rev'] = 'test123'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertTrue(form.is_valid())

    def test_usuario_vendedor_form_email_valido(self):
        self.data_empresa['email'] = 'avalos@gmail.com'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertTrue(form.is_valid())
    
    def test_usuario_vendedor_form_direccion_valida(self):
        self.data_empresa['direccion'] = 'Constitutentes 6'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertTrue(form.is_valid())
    
    def test_usuario_vendedor_form_telefono_valido(self):
        self.data_empresa['telefono'] = '4512415478'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertTrue(form.is_valid())

    def test_usuario_vendedor_form_descripcion_valida(self):
        self.data_empresa['descripcion'] = 'Taller de artesanias hechas a mano'     
        form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertTrue(form.is_valid())  
    
    def test_form_usuario_vendedor_valid(self):
        usuario_form = Usuario_Vendedor_Form(self.data_empresa)
        self.assertTrue(usuario_form.is_valid())       