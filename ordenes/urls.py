from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('agregar/<slug>/', views.agregar_carrito, name="agregar"),
    path('eliminar-de-carrito/<slug>/', views.eliminar_de_carrito, name = 'eliminar-de-carrito'),
    path('eliminar-articulo-carrito/<slug>/', views.eliminar_un_producto_del_carrito, 
         name="eliminar-articulo-carrito"),
    path('carrito/', views.lista_carrito.as_view(), name="lista_carrito"),
    path('comprar/', views.comprar, name="comprar"),
    path('cancelar-carrito/', views.cancelar_carrito, name='cancelar_carrito')
]
