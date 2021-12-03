from django.urls import path

from . import views

app_name = 'principal'

urlpatterns = [
    # Home de la pagina
	path('', views.index, name='principal'),
    path('admin/', views.admin, name='admin'),

    # Listado de productos/servicios
	path('lista/', views.lista, name='lista'),

    # Listado de productos/servicios para administradores
	path('lista_admin/', views.lista_admin, name='lista_admin'),

    # CRUD Productos
    path('nuevo_producto/', views.NuevoProducto.as_view(), name='nuevo_producto'),
    path('editar_producto/<int:pk>', views.EditarProducto.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:pk>', views.EliminarProducto.as_view(), name='eliminar_producto'),
    path('ver_producto/<int:pk>', views.VerProducto.as_view(), name='ver_producto'),


    # CRUD Servicios
    path('nuevo_servicio/', views.NuevoServicio.as_view(), name='nuevo_servicio'),
    path('editar_servicio/<int:pk>', views.EditarServicio.as_view(), name='editar_servicio'),
    path('eliminar_servicio/<int:pk>', views.EliminarServicio.as_view(), name='eliminar_servicio')
]