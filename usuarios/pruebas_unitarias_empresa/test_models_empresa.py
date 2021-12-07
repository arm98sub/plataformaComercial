from django.test import TestCase
from usuarios.models import Usuario_Vendedor
from django.core.exceptions import ValidationError


class TestModels(TestCase):
    #Campos vacios
    def test_nombre_vacio(self):
        self.usuario_vendedor = Usuario_Vendedor(
            username = "Avalos33", 
            password = "test123",
            password_rev = "test123",
            email = "37180266@uaz.edu.mx",
            direccion = "Calle de la rosa # 6",
            telefono = "492145214",
            descripcion = "Artesanias en piel"
        )

        with self.assertRaises(ValidationError):
            self.usuario_vendedor.full_clean()

    def test_nombre_usuario_vacio(self):
        empresa = Usuario_Vendedor("Talabarteria Avalos","test123","test123",
        "37180266@uaz.edu.mx","Calle de la rosa # 6","492145214","Artesanias en piel")

        with self.assertRaises(ValidationError):
            empresa.full_clean()
    
    def test_contrasena_vacio(self):
        empresa = Usuario_Vendedor("Talabarteria Avalos","test123",
        "37180266@uaz.edu.mx","Calle de la rosa # 6","492145214","Artesanias en piel")

        with self.assertRaises(ValidationError):
            empresa.full_clean()

    def test_contrasena_8_caracteres_minimos(self):
        self.usuario_vendedor.password = "tesdfgfdgfd21*&||$%^g"

        try:
            self.assertRaises(ValidationError)
        except ValidationError as ex:
            mensaje = str(ex.message_dict['password'][0])
            self.assertEqual(mensaje,
            'La contraseña tiene menos de 8 caracteres')
    
    def test_contrasena_8_caracteres_minimos(self):
        self.usuario_vendedor = Usuario_Vendedor(
            username = "Avalos33", 
            password = "test123",
            password_rev = "test123",
            email = "37180266@uaz.edu.mx",
            direccion = "Calle de la rosa # 6",
            telefono = "492145214",
            descripcion = "Artesanias en piel"
        )

    def setUp(self):
        self.usuario_vendedor = Usuario_Vendedor(
            first_name = "Talabarteria Avalos",
            username = "Avalos33", 
            password = "test123",
            password_rev = "test123",
            email = "37180266@uaz.edu.mx",
            direccion = "Calle de la rosa # 6",
            telefono = "492145214",
            descripcion = "Artesanias en piel"
        )