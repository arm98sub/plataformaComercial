from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from django.conf.urls import handler404
# from principal.views import Error404View, Error500View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('ordenes/', include('ordenes.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = Error404View.as_view()
# handler500 = Error500View.as_view()
