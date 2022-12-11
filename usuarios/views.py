from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
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
from django.contrib.auth.models import User
from django.core.mail import send_mail


# CRUD Usuarios


class UsuariosList(PermissionRequiredMixin, ListView):
    """ Permite listar los usuarios existentes
    """
    permission_required = 'users.permiso_administradores'
    model = Usuario
    template_name = 'usuario_list.html'
    lista_grupos = Group.objects.all()
    extra_context = {
        'us_lista': True,
        'lista_grupos': lista_grupos
    }


class VendedoresList(PermissionRequiredMixin, ListView):
    permission_required = 'users.permiso_administradores'
    model = Usuario_Vendedor
    template_name = 'usuario_vendedor_list.html'
    lista_grupos = Group.objects.all()

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


class NuevoVendedor(PermissionRequiredMixin, CreateView):
    permission_required = 'users.permiso_administradores'
    model = Usuario_Vendedor
    form_class = Usuario_Vendedor_Form
    success_url = reverse_lazy('usuarios:lista_vendedores')

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


class UsuariosActualizar(SuccessMessageMixin, UpdateView):
    # permission_required = 'users.permiso_usuarios'
    # permission_required = 'users.permiso_administradores'

    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('usuarios:lista')
    success_message = "El usuario %(first_name)s se actualizó con éxito"



class VendedoresEliminar(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.permiso_administradores'
    model = Usuario_Vendedor
    success_url = reverse_lazy('usuarios:lista_vendedores')


class VendedoresActualizar(SuccessMessageMixin, UpdateView):
    model = Usuario_Vendedor
    form_class = Usuario_Vendedor_Form
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('usuarios:lista_vendedores')
    success_message = "El vendedor %(first_name)s se actualizó con éxito"


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


# Para usuarios CLIENTES
class SignUpUsuario(SuccessMessageMixin, CreateView):
    model = Usuario
    template_name = 'sign_up.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:login')

    success_message = "Se envió un enlace al correo '%(email)s' para verificar su cuenta"
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
                                       'uid': uid,
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


class Sign_up_usuario_vendedor(SuccessMessageMixin, CreateView):
    model = Usuario_Vendedor
    template_name = 'sign_up_vendor.html'
    form_class = Usuario_Vendedor_Form

    success_url = reverse_lazy('usuarios:login')
    success_message = "El administrador verificará su cuenta y se le notificará cuando se active"

    # Para solicitar activacion de cuenta empresarial#
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        dominio = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        # token = token_activacion.make_token(user)

        message = render_to_string('activar_cuenta_vendedores.html',
                                   {
                                       'usuario': user,
                                       'dominio': dominio,
                                       'uid': uid,
                                       #    'token': token,
                                   }
                                   )

        subject = "Un nuevo vendedor ha solicitado la activacion de su cuenta"
        to = 'bboyshady1904@gmail.com'

        email = EmailMessage(
            subject,
            message,
            to=[to],
        )

        email.content_subtype = 'html'

        email.send()

        return super().form_valid(form)


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
            user.groups.add(Group.objects.get(name='usuarios'))
            user.save()
            messages.success(self.request, 'Cuenta activada con éxito')
        else:
            messages.error(
                self.request, 'Token inválido, contacta al administrador')

        return redirect('usuarios:login')


def cambia_grupo(request, id_gpo, id_usuario, pre_url):
    grupo = Group.objects.get(id=id_gpo)
    usuario = User.objects.get(id=id_usuario)


    if grupo in usuario.groups.all():
        if usuario.groups.count() <= 1:
            messages.error(
                request, 'El usuario debe pertenecer a un grupo como minimo')
        else:
            usuario.groups.remove(grupo)
            messages.success(
                request, f'El usuario {usuario} ya no  pertenece al grupo {grupo}')
    else:
        # Activacion de Vendedores
        if usuario.is_active == False:
            usuario.is_active = True
            usuario.vende = True
            usuario.groups.add(grupo)
            usuario.save()
            messages.success(
            request, f'El usuario {usuario.username} se agrego al grupo {grupo}')

            # Enviar correo al vendedor, para notificar que su cuenta fue activada o no
            send_mail('Tu cuenta para la Plataforma Digital Comercial ha sido activada exitosamente',
            'Hola,  "{usuario.username}", el administrador revisó tus datos y ahora puedes comenzar a vender tus productos',
            'plataformadigitalc@gmail.com',
            [usuario.email],
            fail_silently=False)
            return render(request, 'usuarios/usuario_vendedor_list.html')
        else:
            usuario.groups.add(grupo)
            usuario.save()
            messages.success(
            request, f'El usuario {usuario} se agrego al grupo {grupo}')

    return redirect(f'usuarios:{pre_url}')
    


def modificar_usuario_grupo(request, id):
    grupos = [grupo.id for grupo in Group.objects.all()]
    usuario = Usuario.objects.get(id=id)
    usuario.groups.clear()
    permission_required = 'usuarios.edit_usuario'

    for item in request.POST:
        if request.POST[item] == 'on':
            usuario.groups.add(Group.objects.get(id=int(item)))

        messages.success(request, f'El usuario {usuario} pertenece al grupo')

    if "vendedores" in usuario.groups.all().values("name"):
        return redirect('usuarios:lista_vendedores')
    elif "usuarios" in usuario.groups.all().values("name"):
        return redirect('usuarios:lista')
    else:
        return redirect('usuarios:lista')


# Metodo para municipios


def obtiene_municipios(request):
    if request.method == 'GET':
        return JsonResponse({'error': 'Petición incorrecta'}, safe=False, status=403)
    id_estado = request.POST.get('id')
    municipios = Municipio.objects.filter(estado_id=id_estado)
    json = []
    if not municipios:
        json.append({'error': 'No se encontraron municipios para ese estado'})

    for municipio in municipios:
        json.append({'id': municipio.id, 'nombre': municipio.nombre})
    return JsonResponse(json, safe=False)
