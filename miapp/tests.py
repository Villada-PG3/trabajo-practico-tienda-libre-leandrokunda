from django.test import TestCase
from .models import Categoria, Producto


class PaginaNoEncontradaTests(TestCase):
    def test_url_inexistente_muestra_pagina_personalizada(self):
        response = self.client.get("/catalogo/999")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "miapp/404.html")

    def test_producto_inexistente_muestra_pagina_personalizada(self):
        response = self.client.get("/producto/999/")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "miapp/404.html")

class BusquedaCategoriaTests(TestCase):
    def test_busqueda_en_categoria_no_incluye_productos_de_otra_categoria(self):
        categoria = Categoria.objects.create(nombre="Libros", slug="libros")
        otra_categoria = Categoria.objects.create(nombre="Juegos", slug="juegos")
        producto_categoria = Producto.objects.create(
            categoria=categoria,
            nombre="Libro azul",
            precio="10.00",
            stock=1,
        )
        Producto.objects.create(
            categoria=otra_categoria,
            nombre="Libro rojo",
            precio="12.00",
            stock=1,
        )

        response = self.client.get("/categoria/libros/?q=libro")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["productos"]),
            [producto_categoria],
        )
        self.assertContains(response, 'action="/categoria/libros/"')
