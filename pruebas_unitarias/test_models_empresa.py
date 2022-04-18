from django.test import TestCase
from usuarios.models import Usuario_Vendedor
from principal.models import Producto
from django.core.exceptions import ValidationError


class TestModels(TestCase):
    #Campos vacios
    def test_nombre_vacio(self):
        empresa = Usuario_Vendedor("Avalos33","test123","test123",
        "37180266@uaz.edu.mx","Calle de la rosa # 6","492145214","Artesanias en piel")

        with self.assertRaises(ValidationError):
            empresa.full_clean()

    def test_producto_completo(self):
        empresa = Usuario_Vendedor("Avalos33", "test123", "test123",
                                   "37180266@uaz.edu.mx", "Calle de la rosa #6", "492145214", "Artesanias en piel")
        nuevo_producto = Producto(empresa, "Cinto piteado", None, 25, 5, "Cintos", "Cinto piteado color negro")
        
        with self.assertRaises(ValidationError):
            empresa.full_clean()
            nuevo_producto.full_clean()
        
    # Prueba que no se realice la creacion del producto si no se le da un vendedor.
    def test_producto_sin_vendedor(self):
        nuevo_producto = Producto("", "Cinto piteado", None, 25, 5, "Cintos", "Cinto piteado color negro")
        self.assertEqual(nuevo_producto, ValidationError)

        # with self.assertRaises(ValidationError):
        #     print("No funciono")
        #     nuevo_producto.full_clean()
        