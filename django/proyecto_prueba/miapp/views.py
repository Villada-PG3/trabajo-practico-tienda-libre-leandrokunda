from django.shortcuts import render
from django.views.generic import TemplateView

class ProductosTemplateView(TemplateView):
    template_name = "miapp/productos.html"

def home(request):
    productos_destacados = [
        {"nombre": "Auriculares HP", "precio": 15000, "stock": 5},
        {"nombre": "Teclado Mecanico", "precio": 45000, "stock": 0},
        {"nombre": "Mouse Gamer", "precio": 12500, "stock": 12},
        {"nombre": "Monitor 24 pulgadas", "precio": 120000, "stock": 3},
        {"nombre": "Silla Gamer", "precio": None, "stock": 8},
        {"nombre": "Mousepad XL", "precio": 5000, "stock": 20},
    ]   
    context = {
        "titulo": "Ofertas de la semana",
        "productos": productos_destacados,  # Sin comillas para pasar la lista
        "usuario_logueado": True
    }
    # Ruta corregida a "miapp/home.html"
    return render(request, "miapp/home.html", context)

def acerca_de_mi(request):
    return render(request, 'miapp/acerca-de-mi.html')
