# Concepto

- Es una VBC que renderiza plantillas Html
- No requiere lógica adicional si solo se mostrará contenido estático o un contexto mínimo
- Se usa cuando:
  - No se necesita acceso a datos dinámicos complejos
  - Se crean páginas como _Contactos_, _Nosotros_, etc
  - Quieres separar la lógica de la presentación

# Ejemplo 

```python
# views.py
from django.views.generic import TemplateView

class PaginaInicioView(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        # Mantiene el contexto por defecto (incluye parámetros de la URL)
        context = super().get_context_data(**kwargs)
        # Agregas las variables que quieras usar en tu HTML
        context["titulo"] = "Bienvenido a mi sitio web"
        context["articulos_destacados"] = 5
        return context

# urls.py
from django.urls import path
from .views import PaginaInicioView

urlpatterns = [
    path('inicio/', PaginaInicioView.as_view(), name='inicio'),
]
```

# ¿Cómo funciona internamente?

Cuando entra una petición GET a la ruta:

- Recibe la petición: TemplateView gestiona el flujo del método GET sin que tengas que escribir `def get(self, request):`.
- Construye el contexto: Llama automáticamente a `get_context_data()`, donde reúne las variables del sistema (y las que tú agregues) dentro de un diccionario.
- Renderiza y responde: Toma la plantilla especificada en template_name, le inyecta el diccionario del contexto y devuelve la respuesta en formato HTML (HttpResponse).

---

# Tips

## Tip 1

Si solo necesitas mostrar un HTML estático sin pasarle datos dinámicos, ni siquiera necesitas escribir una clase en _views.py_. Puedes usar **TemplateView** directamente en tu urls.py:

```python
path(
    'acerca-de/', 
    TemplateView.as_view(template_name="acerca_de.html"), 
    name='acerca'
),
```

## Tip 2

Si tienes 5 páginas estáticas que comparten la misma lógica (por ejemplo, todas necesitan cargar la lista de categorías del menú principal), podemos seguir este ejemplo: 

```python
class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        return context

class InicioView(BaseView):
    template_name = "inicio.html"

class ContactoView(BaseView):
    template_name = "contacto.html"
```