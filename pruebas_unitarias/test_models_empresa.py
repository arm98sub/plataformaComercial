from django.test import TestCase
from usuarios.models import Usuario_Vendedor, Estado, Municipio
from django.core.exceptions import ValidationError


class TestModels(TestCase):
    #Campos vacios
    def test_nombre_vacio(self):
        empresa = Usuario_Vendedor("Avalos33","test123","test123",
        "37180266@uaz.edu.mx","Calle de la rosa # 6","492145214","Artesanias en piel")

        with self.assertRaises(ValidationError):
            empresa.full_clean()

    def test_nombre_usuario_vacio(self):
        empresa = Usuario_Vendedor("Talabarteria Avalos","test123","test123",
        "37180266@uaz.edu.mx","Calle de la rosa # 6","492145214","Artesanias en piel")

        with self.assertRaises(ValidationError):
            empresa.full_clean()
    
    def test_nombre_usuario_vacio(self):
        empresa = Usuario_Vendedor("Talabarteria Avalos","test123","test123",
        "37180266@uaz.edu.mx","Calle de la rosa # 6","492145214","Artesanias en piel")

        with self.assertRaises(ValidationError):
            empresa.full_clean()