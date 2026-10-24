from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos",
        null=True,
        blank=True,
        )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100, default=0)
    precio = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.IntegerField()
    activo = models.BooleanField(default=True)
    marca = models.CharField(max_length=50, default="Marca Desconocida")
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
    def __str__(self):
        return f"{self.nombre} - {self.marca} - ${self.precio} - STOCK: {self.stock}"