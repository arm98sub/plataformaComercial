from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'usuarios'

urlpatterns = [

    # CRUD Usuarios
    path('', views.UsuariosList.as_view(), name='lista'),
    path('lista_vendedores', views.VendedoresList.as_view(), name='lista_vendedores'),
    path('pruebona/', views.PruebaUsuarios.as_view(), name='pruebona'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo'),
    path('nuevo_vendedor/', views.NuevoVendedor.as_view(), name='nuevo_vendedor'),
    path('ver/<int:pk>', views.UsuariosDetalle.as_view(), name='ver'),
    path('editar/<int:pk>', views.UsuariosActualizar.as_view(), name='editar'),
    path('eliminar/<int:pk>', views.UsuariosEliminar.as_view(), name='eliminar'),
    path('editar_vendedor/<int:pk>', views.VendedoresActualizar.as_view(), name='editar_vendedor'),
    path('eliminar_vendedor/<int:pk>', views.VendedoresEliminar.as_view(), name='eliminar_vendedor'),

    # Sesiones
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpUsuario.as_view(), name='signup'),
    path('signup/vendor/', views.Sign_up_usuario_vendedor.as_view(),
         name='signup_vendor'),
    path('activar/<slug:uid64>/<slug:token>',
         views.ActivarCuenta.as_view(), name='activar'),

    # Grupos
    path('cambia-grupo/<int:id_gpo>/<int:id_usuario>/<str:pre_url>',
         views.cambia_grupo, name='cambia-grupo'),
    path('modificar-grupos/<int:id>', views.modificar_usuario_grupo,
         name='modificar_usuario_grupo'),

    # Municipios
    path('municipios/', views.obtiene_municipios, name='municipios'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
