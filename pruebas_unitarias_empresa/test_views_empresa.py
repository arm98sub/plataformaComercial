from django.test import TestCase
from usuarios.models import Usuario_Vendedor
from usuarios_permisos import *


class TestViews(TestCase):
     #Test registro cuenta empresarial
    def setUp(self, nombre='Talabarteria Avalos', username="Avalos33", password = "test123", password_rev = "test123",
                email = "37180266@uaz.edu.mx", foto_perfil = False, direccion = "Callejon allende",
                telefono = "4945148745", descripcion = "Taller de artesanias" ):
        fields = ('first_name', 'username', 'password', 'password_rev',
         'email', 'foto_perfil', 'direccion','telefono', 'descripcion')
        
        crear_grupos()
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

    #URLS   
    def test_url_empresa_registro(self):
        response= self.client.get('/usuarios/signup/vendor/')
        self.assertEquals(response.status_code,200)

    def test_template_empresa_registro(self):
        response = self.client.get('/usuarios/signup/vendor/')
        self.assertTemplateUsed(response,'sign_up_vendor.html')
    
    def test_registro_sin_nombre_usuario(self):
        response = self.client.get('/usuarios/signup/vendor/')
        self.assertTemplateUsed(response,'sign_up_vendor.html')
    
    #Test empresas
    def test_no_agrega_sin_user_name(self):
        self.data_empresa['username'] = ''
        response = self.client.post('/usuarios/signup/vendor/', self.data_empresa)
        self.assertEqual(Usuario_Vendedor.objects.all().count(),0)
    
    def test_no_agrega_sin_password(self):
        self.data_empresa['password'] = ''
        response = self.client.post('/usuarios/signup/vendor/', self.data_empresa)
        self.assertEqual(Usuario_Vendedor.objects.all().count(),0)
    
    def test_no_agrega_sin_verificar_password(self):
        self.data_empresa['password_rev'] = ''
        response = self.client.post('/usuarios/signup/vendor/', self.data_empresa)
        self.assertEqual(Usuario_Vendedor.objects.all().count(),0)

    def test_no_agrega_sin_direccion(self):
        self.data_empresa['direccion'] = ''
        response = self.client.post('/usuarios/signup/vendor/', self.data_empresa)
        self.assertEqual(Usuario_Vendedor.objects.all().count(),0)
    
    def test_no_agrega_sin_telefono(self):
        self.data_empresa['telefono'] = ''
        response = self.client.post('/usuarios/signup/vendor/', self.data_empresa)
        self.assertEqual(Usuario_Vendedor.objects.all().count(),0)

    def test_agregar_empresa_correctamente(self):
        response = self.client.post('/usuarios/signup/vendor/', self.data_empresa)
        self.assertEqual(response.status_code,302)
    
    def test_no_agrega_contrasena_diferentes(self):
        self.data_empresa['password'] = '------'
        self.data_empresa['password_rev'] = '123'
        response = self.client.post('/usuarios/signup/vendor/', self.data_empresa)
        self.assertEqual(Usuario_Vendedor.objects.all().count(),0)
    
    def test_no_agrega_usuario_caracteres_diferentes(self):
        self.data_empresa['username'] = '}'
        response = self.client.post('/usuarios/signup/vendor/', self.data_empresa)
        self.assertEqual(Usuario_Vendedor.objects.all().count(),0)