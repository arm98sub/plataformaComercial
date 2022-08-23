from ordenes.models import DetalleOrden, Orden, ProductoOrdenado
from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist


from django.shortcuts import redirect, render, get_object_or_404
from principal.models import Producto
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def agregar_carrito(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    producto_ordenado, created = ProductoOrdenado.objects.get_or_create(
        producto=producto,
        usuario=request.user,
        ordenado=False
    )
    order_qs = Orden.objects.filter(usuario=request.user, ordenado=False)
    if order_qs. exists():
        orden = order_qs[0]

        if orden.productos.filter(producto__slug=producto.slug).exists():
            producto_ordenado.cantidad += 1
            producto_ordenado.save()
            messages.info(request, "La cantidad a sido actualizada.")
            return redirect('ordenes:lista_carrito')
        else:
            orden.productos.add(producto_ordenado)
            messages.info(request, "Este productp se agrego a tu carrito")
            return redirect('ordenes:lista_carrito')
    else:
        fecha_orden = timezone.now()
        orden = Orden.objects.create(
            usuario=request.user, fecha_orden=fecha_orden)
        orden.productos.add(producto_ordenado)
        messages.info(request, "Este producto fue agregado a tu carrito")
        return redirect('ordenes:lista_carrito')

def eliminar_de_carrito(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    orden_qs = Orden.objects.filter(
        usuario= request.user,
        ordenado = False
    )
    if orden_qs.exists():
        orden = orden_qs[0]
        if orden.productos.filter(producto__slug=producto.slug).exists():
            producto_ordenado = ProductoOrdenado.objects.filter(
                producto=producto,
                usuario=request.user,
                ordenado=False
            )[0]
            orden.productos.remove(producto_ordenado)
            producto_ordenado.delete()
            # messages.info(request, "This item was removed from your cart.")
            return redirect("ordenes:lista_carrito")
        else:
            # messages.info(request, "This item was not in your cart")
            return redirect("principal:ver_producto", slug=slug)
    else:
        # messages.info(request, "You do not have an active order")
        return redirect("principal:ver_producto", slug=slug)

@login_required
def eliminar_un_producto_del_carrito(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    orden_qs = Orden.objects.filter(
        usuario=request.user,
        ordenado=False
    )
    if orden_qs.exists():
        orden = orden_qs[0]
        # checar si el producto esta ordenado
        if orden.productos.filter(producto__slug=producto.slug).exists():
            producto_ordenado = ProductoOrdenado.objects.filter(
                producto=producto,
                usuario=request.user,
                ordenado=False
            )[0]
            if producto_ordenado.cantidad > 1:
                producto_ordenado.cantidad -= 1
                producto_ordenado.save()
            else:
                orden.productos.remove(producto_ordenado)
                # messages.info(request, "La cantidad se ha actualizado.")
            return redirect('ordenes:lista_carrito')
        else:
            # messages.info(request, "El producto no se encontro en tu carrito")
            return redirect("principal:ver_producto", slug=slug)
    else:
        # messages.info(request, "No tienes una orden activa")
        return redirect("principal:ver_producto", slug=slug)


# @login_required
# @permission_required('usuarios.permiso_usuario', raise_exception=True)

def add_to_cart(request):
    if request.method == "POST":
        pk = request.POST.get('id')
        cantidad = 1
        producto = get_object_or_404(Producto, pk=pk)
        if producto.stock > 0:
            producto.stock -= int(cantidad)
            producto.save()
            id = str(pk)
            total = float(producto.precio) * float(cantidad)
            request.session['total'] = request.session['total'] + total
            request.session['cantidad'] = request.session['cantidad'] + \
                int(cantidad)

            if id in request.session['articulos']:
                request.session['articulos'][id]['cuantos'] = request.session['articulos'][id]['cuantos']
                + int(cantidad)
            else:
                request.session['articulos'][id] = {'precio': float(
                    producto.precio), 'cuantos': int(cantidad)}

    return redirect('ordenes:lista_carrito')


class lista_carrito(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            orden = Orden.objects.get(
                usuario=self.request.user, ordenado=False)
            context = {
                'object': orden
            }
            return render(self.request, 'lista_carrito.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "No tienes una orden activa")
            return redirect("/")


@login_required
@permission_required('usuarios.permiso_usuario', raise_exception=True)
def lista_carrito2(request):
    articulos = request.session['articulos']
    total = request.session['total']
    cantidad = request.session['cantidad']
    datos = list()

    for articulo in articulos:
        prod = Producto.objects.get(id=int(articulo))
        item = {
            'imagen': prod.imagen,
            'nombre': prod.nombre,
            'precio': articulos[articulo]['precio'],
            'cantidad': articulos[articulo]['cuantos'],
            'subtotal': int(articulos[articulo]['precio']) * int(articulos[articulo]['cuantos'])
        }
        datos.append(item)

    context = {'datos': datos,
               'total': total,
               'cantidad': cantidad,
               }
    return render(request, 'lista_carrito.html', context=context)


@login_required
@permission_required('usuarios.permiso_usuario', raise_exception=True)
def comprar(request):
    orden = Orden(usuario=1)
    orden.save()

    articulos = request.session['articulos']

    for articulo in articulos:
        prod = Producto.objects.get(id=int(articulo))
        precio = articulos[articulo]['precio']
        cantidad = articulos[articulo]['cuantos']
        detail = DetalleOrden(
            producto=prod,
            orden=orden,
            cantidad=cantidad,
            precio=precio)
        detail.save()

    request.session['total'] = 0.0
    request.session['cantidad'] = 0
    request.session['articulos'] = {}

    return redirect('principal:principal')


@login_required
@permission_required('usuarios.permiso_usuario', raise_exception=True)
def cancelar_carrito(request):
    articulos = request.session['articulos']

    for articulo in articulos:
        prod = Producto.objects.get(id=int(articulo))
        cantidad = articulos[articulo]['cuantos']
        prod.stock = prod.stock + cantidad
        prod.save()

    request.session['total'] = 0.0
    request.session['cantidad'] = 0
    request.session['articulos'] = {}
    return redirect('principal:iniciar')
