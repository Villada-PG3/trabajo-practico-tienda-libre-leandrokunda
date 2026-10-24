from .models import Categoria

def categorias_processor(request):
    """Hace que las categorías estén disponibles en todas las plantillas."""
    return {
        'categorias_list': Categoria.objects.all()
    }