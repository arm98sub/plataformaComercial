from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import ProductoForm, ProductoFormVendedor, ServicioForm
from .models import Producto, Servicio

# Home del sitio


def index(request):
    productos = Producto.objects.all()[:3]
    servicios = Servicio.objects.all()[:3]

    return render(
        request, 'index.html', {
            'productos': productos, 'servicios': servicios})


def admin(request):
    return render(request, 'admin.html', {})


# Listado de productos/servicios
def lista(request):
    productos = Producto.objects.all()
    servicios = Servicio.objects.all()

    return render(request, 'principal/lista.html',
                  {'productos': productos, 'servicios': servicios})


def lista_productos(request):
    productos = Producto.objects.filter(vendedor=request.user)
    # servicios = Servicio.objects.all()

    return render(request, 'principal/lista_vendedor.html',
                  {'productos': productos})

# Listado de productos/servicios para administradores


def lista_admin(request):
    productos = Producto.objects.all()
    servicios = Servicio.objects.all()

    return render(request, 'principal/lista_admin.html',
                  {'productos': productos, 'servicios': servicios})

# CRUD Productos


class NuevoProducto(PermissionRequiredMixin, CreateView):
    permission_required = 'usuarios.permiso'
    model = Producto
    form_class = ProductoForm
    template_name = 'principal/nuevo_producto.html'
    success_url = reverse_lazy('principal:lista_admin')

    extra_context = {
        'etiqueta': "Nuevo",
        'boton': "Agregar",
    }





class EditarProducto(PermissionRequiredMixin, UpdateView):
    # permission_required = 'usuarios.permiso_administradores'
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('principal:lista_admin')


class EditarProducto(PermissionRequiredMixin, UpdateView):
    permission_required = 'usuarios.permiso_vendedores'
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('principal:lista_prod_vendedor')

    extra_context = {
        'etiqueta': "Actualizar",
        'boton': "Guardar",
    }


class EliminarProducto(PermissionRequiredMixin,DeleteView):
    permission_required = 'usuarios.permiso_vendedores'
    model = Producto
    success_url = reverse_lazy('principal:lista_prod_vendedor')


class VerProducto(DetailView):
    model = Producto
    template_name = "principal/detalleProducto.html"
    context_object_name = "producto"

# CRUD Servicios


class NuevoServicio(PermissionRequiredMixin, CreateView):
    permission_required = 'usuarios.permiso_administradores'
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy('principal:lista_admin')


class EditarServicio(PermissionRequiredMixin, UpdateView):
    permission_required = 'usuarios.permiso_administradores'
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy('principal:lista_admin')


class EliminarServicio(PermissionRequiredMixin, DeleteView):
    permission_required = 'usuarios.permiso_administradores'
    model = Servicio
    success_url = reverse_lazy('principal:lista_admin')


class AgregarProductoVendedor(PermissionRequiredMixin, CreateView):
    permission_required = 'usuarios.permiso_vendedores'
    model = Producto
    form_class = ProductoFormVendedor
    template_name = "principal/nuevo_producto_vendedor.html"
    success_url = reverse_lazy('principal:lista_prod_vendedor')


    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super(AgregarProductoVendedor, self).form_valid(form)

