from django.test import TestCase

class PaginaNoEncontradaTests(TestCase):
	def test_url_inexistente_muestra_pagina_personalizada(self):
		response = self.client.get("/catalogo/999")

		self.assertEqual(response.status_code, 404)
		self.assertTemplateUsed(response, "miapp/404.html")

	def test_producto_inexistente_muestra_pagina_personalizada(self):
		response = self.client.get("/producto/999/")

		self.assertEqual(response.status_code, 404)
		self.assertTemplateUsed(response, "miapp/404.html")
