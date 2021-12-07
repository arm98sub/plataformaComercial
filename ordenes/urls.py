from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('agregar/', views.agregar_carrito, name="agregar"),
    path('carrito/', views.lista_carrito, name="lista_carrito"),
    path('comprar/', views.comprar, name="comprar"),
    path('cancelar-carrito/', views.cancelar_carrito, name='cancelar_carrito')
]
