# Consultas ORM Django - Clase 5

Este archivo contiene 10 consultas de ejemplo ejecutadas en la consola interactiva de Django (`python manage.py shell`).

```python
from miapp.models import Producto, Categoria

# 1. Obtener todos los productos registrados
Producto.objects.all()

# 2. Obtener un producto específico por su ID usando get()
Producto.objects.get(id=1)

# 3. Filtrar productos con precio mayor a $20.000 (Lookup __gt)
Producto.objects.filter(precio__gt=20000)

# 4. Búsqueda por texto insensible a mayúsculas/minúsculas (Lookup __icontains)
Producto.objects.filter(nombre__icontains="auriculares")

# 5. Excluir productos que no tengan stock
Producto.objects.exclude(stock=0)

# 6. Ordenar productos por precio de mayor a menor
Producto.objects.order_by('-precio')

# 7. Buscar productos con stock menor o igual a 5 (Lookup __lte)
Producto.objects.filter(stock__lte=5)

# 8. Navegar relación directa: Ver la categoría asociada a un producto
prod = Producto.objects.first()
print(prod.categoria)

# 9. Navegar relación inversa: Ver todos los productos de una categoría
cat = Categoria.objects.first()
cat.producto_set.all()

# 10. Consulta combinada: Productos con precio mayor a 10000 y stock disponible
Producto.objects.filter(precio__gt=10000, stock__gt=0)