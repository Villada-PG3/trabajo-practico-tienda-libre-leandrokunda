from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Producto
from django.shortcuts import get_object_or_404
class ProductosTemplateView(TemplateView):
    template_name = "miapp/productos.html"

def home(request):
    productos_destacados = Producto.objects.order_by("-id")[:3]  
    context = {
        "titulo": "Recien Agregados",
        "productos": productos_destacados,  # Sin comillas para pasar la lista
        "usuario_logueado": True
    }
    # Ruta corregida a "miapp/home.html"
    return render(request, "miapp/home.html", context)
    

def acerca_de_mi(request):
    return render(request, 'miapp/acerca-de-mi.html')

def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by("-id")
    context = {"productos": productos}
    return render(request, "miapp/catalogo.html", context)

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {"producto": producto}
    return render(request, "miapp/detalle.html", context)