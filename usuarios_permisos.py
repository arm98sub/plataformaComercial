import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comerciov2.settings')
django.setup()

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from usuarios.models import Usuario

grupo_administradores = Group.objects.create(name='administradores')
grupo_usuarios = Group.objects.create(name='usuarios')
grupo_vendedores = Group.objects.create(name='vendedores')
content_type = ContentType.objects.get_for_model(Usuario)

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
    content_type = content_type
)

grupo_usuarios.permissions.add(permiso_usuarios)
grupo_administradores.permissions.add(permiso_administradoes)
grupo_vendedores.permissions.add(permiso_vendedores)
# administrador = Usuario.objects.create_user('luis@asdas.mx', password='luis123')
# administrador.groups.add(grupo_administradores)

# Usuario.objects.create_superuser('admin@asdas.mx', password='admin123')

