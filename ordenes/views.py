from ordenes.models import DetalleOrden, Orden
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from principal.models import Producto
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('usuarios.permiso_usuario', raise_exception=True)
def agregar_carrito(request):
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


@login_required
@permission_required('usuarios.permiso_usuario', raise_exception=True)
def lista_carrito(request):
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
