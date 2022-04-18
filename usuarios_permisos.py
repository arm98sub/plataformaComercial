import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comerciov2.settings')
django.setup()

from usuarios.models import Usuario
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group

content_type = ContentType.objects.get_for_model(Usuario)


def crear_grupos():
    grupo_vendedores = Group.objects.get_or_create(name='vendedores')
    grupo_usuarios = Group.objects.get_or_create(name='usuarios')
    grupo_administradores = Group.objects.get_or_create(name='administradores')


def crear_permisos():
    permiso_usuarios = Permission.objects.create(
        codename='permiso_usuario',
        name='Permiso requerido para el grupo usuarios',
        content_type=content_type
    )

    permiso_administradoes = Permission.objects.create(
        codename='permiso_administradores',
        name='Permiso requerido para el grupo administradores',
        content_type=content_type
    )

    permiso_vendedores = Permission.objects.create(
        codename='permiso_vendedores',
        name='Permiso requerido para el grupo vendedores',
        content_type=content_type
    )

    grupo_usuarios = Group.objects.get(name='usuarios')
    grupo_usuarios.permissions.add(permiso_usuarios)

    grupo_administradores = Group.objects.get(name='administradores')
    grupo_administradores.permissions.add(permiso_administradoes)

    grupo_vendedores = Group.objects.get(name='vendedores')
    grupo_vendedores.permissions.add(permiso_vendedores)


def eliminar_permisos():
    per_usuario = Permission.objects.get(codename='permiso_usuario')
    per_admin = Permission.objects.get(codename='permiso_administradores')
    per_vend = Permission.objects.get(codename='permiso_vendedores')

    per_usuario.delete()
    per_admin.delete()
    per_vend.delete()


crear_grupos()
crear_permisos()
