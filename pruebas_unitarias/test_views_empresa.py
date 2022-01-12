#from django.test import TestCase
#from django.contrib.auth.models import Usuario_Vendedor

# class TestViews(TestCase):
#     #Test registro cuenta empresarial 
#     def test_template_login_usuario(self):
#         response = self.client.get('/login/')
#         self.assertTemplateUsed(response,'accounts/login.html')

#     def test_login_url(self):
#         response = self.client.get('/login/')
#         self.assertEqual(response.status_code,200)

#     def test_login_boton_inicio_sesion(self):
#         response = self.client.get('/login/')
#         boton = 'id="botonInicioSesion"'
#         self.assertInHTML(boton, response.rendered_content)
    
#     #Test delete
#     def test_template_borrar_usuario(self):
#         response = self.client.get('/delete/')
#         self.assertTemplateUsed(response,'home/borrar_usuario.html')