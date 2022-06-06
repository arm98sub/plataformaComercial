from django.test import TestCase
from usuarios.models import Usuario_Vendedor
from principal.models import Producto
from django.core.exceptions import ValidationError


class TestModels(TestCase):
    def setUp(self, nombre='Talabarteria Avalos', username="Avalos33", password="test123", password_rev="test123",
              email="37180266@uaz.edu.mx", foto=False, direccion="Callejon allende",
              telefono="4945148745", descripcion="Taller de artesanias"):
        fields = ('first_name', 'username', 'password', 'password_rev',
                  'email', 'foto', 'direccion', 'telefono', 'descripcion')

        self.empresa = Usuario_Vendedor(
            first_name=nombre,
            username=username,
            password=password,
            password_rev=password_rev,
            email=email,
            foto=foto,
            direccion=direccion,
            telefono=telefono,
            descripcion=descripcion
        )

        self.data_empresa = {
            'first_name': nombre,
            'username': username,
            'password': password,
            'password_rev': password_rev,
            'email': email,
            'foto': foto,
            'direccion': direccion,
            'telefono': telefono,
            'descripcion': descripcion
        }

    # Campos vacios
    def test_user_name_es_no_vacio(self):
        self.empresa.username = ''
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_user_name_es_no_acepta_caracteres(self):
        self.empresa.username = '}'
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_user_name_es_no_acepta_espacios(self):
        self.empresa.username = 'Avalos 33'
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_user_name_es_no_mas_de_150_caracteres(self):
        self.empresa.username = 'Avalos33' * 50
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_password_no_vacio(self):
        self.empresa.password = ''
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_password_no_mas_de_70_caracteres(self):
        self.empresa.password = 'test123' * 50
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_correo_con_formato_correcto(self):
        self.empresa.email = 'avalos@'
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_correo_no_acepta_con_espacios(self):
        self.empresa.email = '37180266@ uaz.edu.mx'
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_telefono_no_acepta_vacio(self):
        self.empresa.telefono = ''
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_telefono_no_acepta_mas_de_10_caracteres(self):
        self.empresa.telefono = '452142154200'
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()

    def test_descripcion_no_acepta_mas_de_255_caracteres(self):
        self.empresa.telefono = 'Taller de artesanias' * 50
        with self.assertRaises(ValidationError):
            self.empresa.full_clean()
