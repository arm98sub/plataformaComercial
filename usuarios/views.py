from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites. shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .token import token_activacion
from .models import Usuario, Municipio, Usuario_Vendedor
from .forms import UsuarioForm, Usuario_Vendedor_Form

'''
Vistas para el apartado de usuarios.
Plataforma Ditial el Comercial
autores:
    Alan Aguayo Ramirez
    Daniel Avalos Bueno
    Salatiel Reyes Gaytan
    Erick Alexandro Gonzalez Pinales
version: 2.0
'''
# CRUD Usuarios


class UsuariosList(PermissionRequiredMixin, ListView):
    permission_required = 'users.permiso_administradores'
    paginate_by: 1
    model = Usuario
    template_name = 'usuario_list.html'
    lista_grupos = Group.objects.all()
    lista_usuarios = Usuario_Vendedor.objects.all()

    extra_context = {
        'vendedores': lista_usuarios,
        'lista_grupos': lista_grupos
    }

# Permite vizualizar la informacion de un usuario.
class UsuariosDetalle(DetailView):
    model = Usuario

# Permite vizualizar la informacion de un Vendedor.
class VendedorDetalle(DetailView):
    model = Usuario_Vendedor

# Clase que permite la creacion de nuevos usuarios.
class NuevoUsuario(PermissionRequiredMixin, CreateView):
    permission_required = 'users.permiso_administradores'
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:lista')

    extra_context = {
        'etiqueta': 'Nuevo',
        'boton': 'Agregar',
        'us_nuevo': True
    }

class NuevoVendedor(PermissionRequiredMixin, CreateView):
    permission_required = 'users.permiso_administradores'
    model = Usuario_Vendedor
    form_class = Usuario_Vendedor_Form
    success_url = reverse_lazy('usuarios:lista')

    extra_context = {
        'etiqueta': 'Nuevo',
        'boton': 'Agregar',
        'vn_nuevo': True
    }



# Una prueba solo para aprender a usar Django xD
class PruebaUsuarios(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'prueba.html'
    success_url = reverse_lazy('usuarios:login')

# Permite actualizar la informacion de usuario.
class UsuariosActualizar(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'users.permiso_administradores'
    model = User
    form_class = UsuarioForm
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('usuarios:lista')
    # success_message = "El usuario %(first_name)s se actualizo con exito"


class VendedorActualizar(PermissionRequiredMixin, UpdateView):
    permission_required = 'users.permiso_administradores'
    model = Usuario_Vendedor
    form_class = Usuario_Vendedor_Form
    # template_name = 'usuarios/usuario_vendedor_update_form.html'
    extra_context = {'modificar': True}
    success_url = reverse_lazy('usuarios:lista')

# Permite eliminar un usuario de la lista.
class UsuariosEliminar(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.permiso_administradores'
    model = Usuario
    success_url = reverse_lazy('usuarios:lista')


class VendedorEliminar(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.permiso_administradores'
    model = Usuario_Vendedor
    success_url = reverse_lazy('usuarios:lista')


# Sesiones de Usuarios
class LoginUsuario(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        self.request.session['articulos'] = {}
        self.request.session['cantidad'] = 0
        self.request.session['total'] = 0.0

        return super().get_success_url()

# Permite realizar el registro de usuarios, utilizando una activacion por correo.
class SignUpUsuario(CreateView):
    model = Usuario
    template_name = 'sign_up.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:login')

    extra_context = {
        'etiqueta': "Nuevo",
        'boton': "Agregar",
    }

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        dominio = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user)

        message = render_to_string('confirmar_cuenta.html',
                                   {
                                       'usuario': user,
                                       'dominio': dominio,
                                       'uid':  uid,
                                       'token': token,
                                   }
                                   )

        subject = 'Activación de Cuenta | Plataforma digital comercial'
        to = user.email

        email = EmailMessage(
            subject,
            message,
            to=[to],
        )

        messages.success(self.request, f'Verifica tu correo({user.email}) para activar tu cuenta')
        email.content_subtype = 'html'

        email.send()

        return super().form_valid(form)

# Permite crear cuentas de usuario de tipo vendedor, usando una activacion de cuenta por correo.
class Sign_up_usuario_vendedor(CreateView):
    model = Usuario_Vendedor
    template_name = 'sign_up_vendor.html'
    form_class = Usuario_Vendedor_Form

    success_url = reverse_lazy('usuarios:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        dominio = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user)

        message = render_to_string('confirmar_cuenta.html',
                                   {
                                       'usuario': user,
                                       'dominio': dominio,
                                       'uid':  uid,
                                       'token': token,
                                   }
                                   )

        subject = 'Activación de Cuenta | Plataforma digital comercial'
        to = user.email

        email = EmailMessage(
            subject,
            message,
            to=[to],
        )

        messages.success(self.request, f'Verifica tu correo({user.email}) para activar tu cuenta \n{user.id}')
        email.content_subtype = 'html'

        email.send()

        return super().form_valid(form)


# Activa las cuentas, en base a la URL creada al momento de realizar el registro.
class ActivarCuenta(TemplateView):
    
    def get(self, request, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(kwargs['uid64'])
            token = kwargs['token']
            user = Usuario.objects.get(id=uid)
        except:
            user = Usuario_Vendedor.objects.get(id=uid)

        if user and token_activacion.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(self.request, 'Cuenta activada con éxito')
        else:
            messages.error(
                self.request, 'Token inválido, contacta al administrador')

        return redirect('usuarios:login')

# Cambia el grupo del usuario seleccionado, ya sea para quitar privilegios o aumentarlos.
def cambia_grupo(request, id_gpo, id_usuario):
    grupo = Group.objects.get(id=id_gpo)

    try:
        usuario = Usuario.objects.get(id=id_usuario)
    except:
        usuario = Usuario_Vendedor.get(id = id_usuario)

    if grupo in usuario.groups.all():
        if usuario.groups.count() <= 1:
            messages.error(
                request, 'El usuario debe pertenecer a un grupo como minimo')
        else:
            usuario.groups.remove(grupo)
            messages.success(
                request, f'El usuario {usuario} ya no  pertenece al grupo {grupo}')
    else:
        usuario.groups.add(grupo)
        messages.success(
            request, f'El usuario {usuario} se agrego al grupo {grupo}')
    return redirect('usuarios:lista')

# Permite eliminar o modificar un usuario de un grupo(No recuerdo para que la creamos)
def modificar_usuario_grupo(request, id):
    grupos = [grupo.id for grupo in Group.objects.all()]
    usuario = Usuario.objects.get(id=id)
    usuario.groups.clear()
    permission_required = 'usuarios.edit_usuario'

    for item in request.POST:
        if request.POST[item] == 'on':
            usuario.groups.add(Group.objects.get(id=int(item)))

        messages.success(request, f'El usuario {usuario} pertenece al grupo')

    return redirect('usuarios:lista')

# Metodo para municipios


def obtiene_municipios(request):
    if request.method == 'GET':
        return JsonResponse({'error': 'Petición incorrecta'}, safe=False,  status=403)
    id_estado = request.POST.get('id')
    municipios = Municipio.objects.filter(estado_id=id_estado)
    json = []
    if not municipios:
        json.append({'error': 'No se encontraron municipios para ese estado'})

    for municipio in municipios:
        json.append({'id': municipio.id, 'nombre': municipio.nombre})
    return JsonResponse(json, safe=False)
