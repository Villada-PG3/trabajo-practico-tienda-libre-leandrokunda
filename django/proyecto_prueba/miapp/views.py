from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.c
class ProductosTemplateView(TemplateView):
    template_name = "productos.html"

def home(request):
    return render(request, 'miapp/home.html')

def acerca_de_mi(request):
    return render(request, 'miapp/acerca-de-mi.html')