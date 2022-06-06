from django.contrib.auth.models import Group
from django.test import TestCase
from usuarios.models import Usuario_Vendedor
from usuarios_permisos import *


class TestViews(TestCase):

    # Se crea un usuario de prueba
    def crear_usuario_empresa(self):
        self.credentials = {
            'username': 'prueba1',
            'password': 'prueba123',
            'password_rev': 'prueba123',
            'email': 'prueba@gmail.com',
            'foto': None,
            'direccion': 'Una direccion de prueba',
            'telefono': 4921234567,
            'descripcion': 'Una descripcion de prueba'
        }

        crear_grupos()
        crear_permisos()
        self.vendedor = Usuario_Vendedor.objects.create_user(
            **self.credentials)

        my_group = Group.objects.get(name='vendedores')
        my_group.user_set.add(self.vendedor)

    def crear_usuario_admin(self):
        self.credentials = {
            'username': 'prueba1',
            'password': 'prueba123',
            'password2': 'prueba123',
            'email': 'prueba@gmail.com',
            'foto': None,
            'is_superuser': True
        }

        crear_grupos()
        crear_permisos()
        self.usuario = Usuario.objects.create_user(**self.credentials)

        my_group = Group.objects.get(name='administradores')
        my_group.user_set.add(self.usuario)

    # Se loguea al usuario de tipo vendedor.

    def loguear_usuario(self):
        # self.crear_usuario()
        credenciales_login = {
            'username': 'prueba1',
            'password': 'prueba123'
        }
        logueo = self.client.post(
            '/usuarios/login/', credenciales_login, follow=True)
        return logueo

    # Test de productos

    def test_url_lista_productos(self):
        # Loguear al usuario empresa
        self.crear_usuario_empresa()
        response = self.loguear_usuario()

        response = self.client.get('/lista_productos_vendedor/')
        self.assertEqual(response.status_code, 200)

    def test_template_lista_prod(self):
        # loguear al usuario
        self.crear_usuario_empresa()
        response = self.loguear_usuario()

        response = self.client.get('/lista_productos_vendedor/')
        self.assertTemplateUsed(response, 'principal/lista_vendedor.html')

    def test_url_nuevo_producto(self):
        # loguear al usuario
        self.crear_usuario_empresa()
        response = self.loguear_usuario()

        response = self.client.get('/nuevo_producto_vendedor/')
        self.assertEqual(response.status_code, 200)

    def test_template_nuevo_prod(self):
        # Loguear al usuario
        self.crear_usuario_empresa()
        response = self.loguear_usuario()

        response = self.client.get('/nuevo_producto_vendedor/')
        self.assertTemplateUsed(
            response, 'principal/nuevo_producto_vendedor.html')

    def test_agregar_producto(self):
        # Loguear al usuario
        self.crear_usuario_empresa()
        response = self.loguear_usuario()

        producto = {
            'vendedor': self.vendedor,
            'nombre': "Una prueba de producto",
            # 'imagen': image,
            'precio': 19,
            'stock': 2,
            'categoria': "Comida",
            'descripcion': "Una descripcion de prueba"
        }

        response = self.client.post('/nuevo_producto_vendedor/', producto)
        self.assertEqual(response.status_code, 200)

    def test_agregar_producto_incompleto(self):
        # Loguear al usuario
        self.crear_usuario_empresa()
        response = self.loguear_usuario()

        producto = {
            'vendedor': self.vendedor,
            'nombre': "Una prueba de producto",
            'imagen': False,
            # 'precio': 19,
            'stock': 2,
            'categoria': "Comida",
            'descripcion': "Una descripcion de prueba"
        }

        response = self.client.post('/nuevo_producto_vendedor', producto)
        self.assertEqual(response.status_code, 301)

    def test_agregar_prod_sin_vend(self):
        # Loguear al usuario
        self.crear_usuario_empresa()
        response = self.loguear_usuario()

        producto = {
            # 'vendedor': self.vendedor,
            'nombre': "Una prueba de producto",
            # 'imagen': False,
            'precio': 19,
            'stock': 2,
            'categoria': "Comida",
            'descripcion': "Una descripcion de prueba"
        }

        response = self.client.post('/nuevo_producto_vendedor', producto)
        self.assertEqual(response.status_code, 301)

    def test_url_prod_admin(self):
        # Creacion y logueo del usuario
        self.crear_usuario_admin()
        self.loguear_usuario()

        # verificar que se pueda acceder a la url.
        response = self.client.get('/lista_admin/')
        self.assertEqual(response.status_code, 200)

    def test_template_prod_admin(self):
        # Creacion y logueo del usuario
        self.crear_usuario_admin()
        self.loguear_usuario()

        # Verificar template
        response = self.client.get('/lista_admin/')
        self.assertTemplateUsed(response, 'principal/lista_admin.html')

    def test_temp_prod_nuevo(self):
        # Creacion y logueo del usuario
        self.crear_usuario_admin()
        self.loguear_usuario()

        # Verificar urlpatterns
        response = self.client.get('/nuevo_producto/')
        self.assertEqual(response.status_code, 200)

    def test_tmp_nuevo_prod_admin(self):
        # Creacion y logueo del usuario
        self.crear_usuario_admin()
        self.loguear_usuario()

        # Verificar la template
        response = self.client.get('/nuevo_producto/')
        self.assertTemplateUsed(response, 'principal/nuevo_producto.html')

    def test_nuevo_prod_admin(self):
        # Creacion y logueo del usuario
        self.crear_usuario_admin()
        self.loguear_usuario()

        # Agregar un nuevo producto
        producto = {
            'vendedor': self.usuario,
            'nombre': "Una prueba de producto",
            # 'imagen': image,
            'precio': 19,
            'stock': 2,
            'categoria': "Comida",
            'descripcion': "Una descripcion de prueba"
        }

        response = self.client.post('/nuevo_producto/', producto)
        self.assertEqual(response.status_code, 200)
