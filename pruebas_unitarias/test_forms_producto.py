from unittest.case import TestCase
from principal.forms import ProductoForm
from principal.models import Producto
from usuarios.models import Usuario_Vendedor
from django.db.utils import IntegrityError


class TestForms(TestCase):
    def setUp(self):
        self.empresa = Usuario_Vendedor.objects.create(
            first_name='Una prueba',
            username='Prueba2',
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

        self.datos_prod = {
            'vendedor': self.empresa,
            'nombre': "Prueba",
            'imagen': False,
            'precio': 15,
            'stock': 1,
            'categoria': "Pruebas",
            'descripcion': "Una gran prueba"
        }

    # pruebas

    def test_formulario_completo(self):
        # Se obtiene el formulario
        form = ProductoForm(self.datos_prod)

        # Verificacion del form
        self.assertTrue(form.is_valid())
        self.empresa.full_clean()
