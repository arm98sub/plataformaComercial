from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
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

# CRUD Usuarios


class UsuariosList(PermissionRequiredMixin, ListView):
    permission_required = 'users.permiso_administradores'
    model = Usuario
    template_name = 'usuario_list.html'
    lista_grupos = Group.objects.all()
    paginate_by = 5

    extra_context = {
        'us_lista': True,
        'lista_grupos': lista_grupos
    }


class UsuariosDetalle(DetailView):
    model = Usuario


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


class PruebaUsuarios(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'prueba.html'
    success_url = reverse_lazy('usuarios:login')


class UsuariosActualizar(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'users.permiso_administradores'
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('usuarios:lista')
    success_message = "El usuario %(first_name)s se actualizo con exito"


class UsuariosEliminar(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.permiso_administradores'
    model = Usuario
    success_url = reverse_lazy('usuarios:lista')


# Sesiones de Usuarios

class LoginUsuario(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        self.request.session['articulos'] = {}
        self.request.session['cantidad'] = 0
        self.request.session['total'] = 0.0

        return super().get_success_url()


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

        email.content_subtype = 'html'

        email.send()

        return super().form_valid(form)


class Sign_up_usuario_vendedor(CreateView):
    model = Usuario_Vendedor
    template_name = 'sign_up_vendor.html'
    form_class = Usuario_Vendedor_Form

    success_url = reverse_lazy('usuarios:login')


class ActivarCuenta(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(kwargs['uid64'])
            token = kwargs['token']
            user = Usuario.objects.get(id=uid)
        except:
            user = None

        if user and token_activacion.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(self.request, 'Cuenta activada con éxito')
        else:
            messages.error(
                self.request, 'Token inválido, contacta al administrador')

        return redirect('usuarios:login')


def cambia_grupo(request, id_gpo, id_usuario):
    grupo = Group.objects.get(id=id_gpo)
    usuario = Usuario.objects.get(id=id_usuario)
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
