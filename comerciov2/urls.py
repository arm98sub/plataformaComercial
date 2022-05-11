from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('ordenes/', include('ordenes.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
