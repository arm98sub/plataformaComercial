from django.test import TestCase
from usuarios.models import Usuario_Vendedor
from principal.models import Categoria, Producto
from django.db.utils import IntegrityError


class TestModels(TestCase):
    def setUp(self):
        self.empresa = Usuario_Vendedor.objects.create(
            first_name='Una prueba',
            username='Prueba1',
            password='prueba123',
            password_rev='prueba123',
            email="prueba@gmail.com",
            foto=False,
            direccion='Una direccion de prueba',
            telefono=4921234567,
            descripcion='Una direccion de prueba'
        )

        self.datos_empresa = {
            'first_name': 'Una prueba',
            'username': 'Prueba1',
            'password': 'prueba123',
            'password_rev': 'prueba123',
            'email': "prueba@gmail.com",
            'foto': False,
            'direccion': 'Una direccion de prueba',
            'telefono': 4921234567,
            'descripcion': 'Una direccion de prueba'
        }

        self.cat = Categoria.objects.create(nombre='Pruebas')
        # self.dato_categoria = {
        #     'nombre': 'Pruebas'
        # }

    # Test modelos
    # Usuario Empresa
    def test_producto_completo(self):
        producto = Producto.objects.create(
            vendedor=self.empresa,
            nombre="prueba producto",
            precio=25,
            stock=2,
            categoria=self.cat,
            descripcion="Una prueba mas"
        )

        tmp = Producto.objects.first()

        self.assertEqual(producto, tmp)

    def test_producto_sin_vendedor(self):
        try:
            producto = Producto.objects.create(
                # vendedor = self.empresa,
                nombre="prueba producto",
                precio=25,
                stock=2,
                categoria=self.cat,
                descripcion="Una prueba mas"
            )
        except IntegrityError:
            self.assertEqual(1, 1)

    def test_producto_sin_nombre(self):
        try:
            producto = Producto.objects.create(
                vendedor=self.empresa,
                # nombre = "prueba producto",
                precio=25,
                stock=2,
                categoria=self.cat,
                descripcion="Una prueba mas"
            )
        except IntegrityError:
            self.assertEqual(1, 1)

    def test_producto_sin_desc(self):
        try:
            producto = Producto.objects.create(
                vendedor=self.empresa,
                nombre="prueba producto",
                precio=25,
                stock=2,
                categoria=self.cat,
                # descripcion = "Una prueba mas"
            )
        except IntegrityError as e:
            self.assertEqual(0, 0)

    def test_producto_sin_precio(self):
        try:
            producto = Producto.objects.create(
                vendedor=self.empresa,
                nombre="prueba producto",
                # precio = 25,
                stock=2,
                categoria=self.cat,
                descripcion="Una prueba mas"
            )
        except IntegrityError as e:
            self.assertEqual(0, 0)

    def test_producto_sin_categoria(self):
        try:
            producto = Producto.objects.create(
                vendedor=self.empresa,
                nombre="prueba producto",
                precio=25,
                stock=2,
                # categoria = "Pruebas",
                descripcion="Una prueba mas"
            )
        except IntegrityError as e:
            self.assertEqual(0, 0)
