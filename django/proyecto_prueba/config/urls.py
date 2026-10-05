from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static, serve
from miapp.views import ProductosTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("productos/", ProductosTemplateView.as_view()),
    path("", include("miapp.urls")),
]

handler404 = "miapp.views.pagina_no_encontrada"

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)