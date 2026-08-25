# Concepto principal 

En Django, **View** es la clase base de la que heredan todas las demás Vistas Basadas en Clases (CBV). Te da un control directo y limpio sobre cada método HTTP (GET, POST, etc.).

# Ejemplo

```python
# views.py
from django.shortcuts import render
from django.views import View

class MiVistaSimple(View):
    def get(self, request):
        contexto = {"mensaje": "¡Hola desde una Vista Basada en Clases!"}
        return render(request, "mi_plantilla.html", contexto)

# urls.py
from django.urls import path
from .views import MiVistaSimple

urlpatterns = [
    path('hola/', MiVistaSimple.as_view(), name='hola'),
]
```

# ¿Por qué usar View?

A diferencia de una función normal, si alguien envía una petición que no has definido (por ejemplo, un POST), Django responderá automáticamente con un error **405 Method Not Allowed**, ahorrándote validaciones manuales.