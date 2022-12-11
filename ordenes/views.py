from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import View

from ordenes.models import DetalleOrden, Orden, ProductoOrdenado
from principal.models import Producto


@login_required
def agregar_carrito(request, pk):
    producto = get_object_or_404(Producto, id=pk)
    if producto.stock > 0:
        producto_ordenado, created = ProductoOrdenado.objects.get_or_create(
            producto=producto,
            usuario=request.user,
            ordenado=False
        )

        order_qs = Orden.objects.filter(usuario=request.user, ordenado=False)
        if order_qs.exists():
            orden = order_qs[0]

            if orden.productos.filter(producto__id=producto.id).exists():
                producto_ordenado.cantidad += 1

                if producto_ordenado.cantidad > producto.stock:
                    messages.error(request, "No hay suficiente stock para este producto")
                    return redirect('ordenes:lista_carrito')
                    # return render(request, reverse('ordenes:lista_carrito'))

                producto_ordenado.save()
                messages.info(request, "La cantidad a sido actualizada.")
                return redirect('ordenes:lista_carrito')
                # return render(request, reverse('ordenes:lista_carrito'))
            else:
                orden.productos.add(producto_ordenado)
                messages.info(request, "Este producto se agrego a tu carrito")
                return redirect('ordenes:lista_carrito')
                # return render(request, reverse('ordenes:lista_carrito'))
        else:
            fecha_orden = timezone.now()
            orden = Orden.objects.create(usuario=request.user, fecha_orden=fecha_orden)
            orden.productos.add(producto_ordenado)
            messages.info(request, "Este producto fue agregado a tu carrito")
            return redirect('ordenes:lista_carrito')
    else:
        messages.error(request, "Este producto no esta disponible")
        order = Orden.objects.filter(usuario=request.user, ordenado=False).delete()
        return redirect('principal:lista')


def eliminar_de_carrito(request, pk):
    """
    Elimina un producto del carrito
    @param request: Request proviniente de la vista
    @param pk: Llave primaria del objeto a eliminar
    @return: Regresa un render con la vista solicitada.
    """
    producto = get_object_or_404(Producto, id=pk)
    orden_qs = Orden.objects.filter(
        usuario=request.user,
        ordenado=False
    )

    if orden_qs.exists():
        orden = orden_qs[0]
        if orden.productos.filter(producto__id=producto.id).exists():
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
            return redirect("principal:ver_producto", slug=pk)
    else:
        # messages.info(request, "You do not have an active order")
        return redirect("principal:ver_producto", slug=pk)


@login_required
def eliminar_un_producto_del_carrito(request, pk):
    producto = get_object_or_404(Producto, id=pk)
    orden_qs = Orden.objects.filter(
        usuario=request.user,
        ordenado=False
    )
    if orden_qs.exists():
        orden = orden_qs[0]
        # if orden.productos.get(id=pk).cantidad == 1:
        #     orden.productos.remove(orden.productos.get(id=pk))
        #     return redirect('ordenes:lista_carrito')

        # checar si el producto esta ordenado
        if orden.productos.filter(producto__id=producto.id).exists():
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
            return redirect("principal:ver_producto", slug=pk)
    else:
        # messages.info(request, "No tienes una orden activa")
        return redirect("principal:ver_producto", slug=pk)


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
            productos = Producto.objects.all()
            orden = Orden.objects.get(
                usuario=self.request.user, ordenado=False)
            context = {
                'object': orden,
                'productos': productos
            }
            return render(self.request, 'lista_carrito.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Tu carrito se encuentra vacio")
            return redirect("/")

        # try:
        #     orden = Orden.objects.get(usuario=self.request.user, ordenado=False)
        # except ObjectDoesNotExist:
        #     orden = None
        #
        # if orden is not None:
        #     context = {
        #         'object': orden
        #     }
        #
        #     if orden.productos.



@login_required
@permission_required('usuarios.permiso_usuario', raise_exception=True)
def lista_carrito2(request):
    """
    Muestra el carrito de compras
    @param request: Request proviniente de la vista
    @return: Regresa la renderizacion del template.
    """
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
