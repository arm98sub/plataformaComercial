from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [

    # CRUD Usuarios
    path('', views.UsuariosList.as_view(), name='lista'),
    path('pruebona/', views.PruebaUsuarios.as_view(), name='pruebona'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo'),
    path('ver/<int:pk>', views.UsuariosDetalle.as_view(), name='ver'),
    path('editar/<int:pk>', views.UsuariosActualizar.as_view(), name='editar'),
    path('eliminar/<int:pk>', views.UsuariosEliminar.as_view(), name='eliminar'),

    # Sesiones
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpUsuario.as_view(), name='signup'),
    path('signup/vendor/', views.Sign_up_usuario_vendedor.as_view(),
         name='signup_vendor'),
    path('activar/<slug:uid64>/<slug:token>',
         views.ActivarCuenta.as_view(), name='activar'),

    # Grupos
    path('cambia-grupo/<int:id_gpo>/<int:id_usuario>',
         views.cambia_grupo, name='cambia-grupo'),
    path('modificar-grupos/<int:id>', views.modificar_usuario_grupo,
         name='modificar_usuario_grupo'),

    # Municipios
    path('municipios/', views.obtiene_municipios, name='municipios'),
]
