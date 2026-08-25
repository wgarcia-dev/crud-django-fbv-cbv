# Introducción

## Vistas Basadas en Funciones

- Son simples y fáciles de entender
- Son muy flexibles
- No se puede reutilizar mucho código
- Si no se lleva un orden desde el comienzo, pueden volverse muy complejas

Ejemplo: 

```python
# views.py
from django.http import HttpResponse 

def home(request): 
    return HttpResponse("<h2>Hola</h2>")

# urls.py 
from django.urls import path
from .views import home

app_name = ...
urlpatterns = [
    path("home/", home, name="home")
]
```

## Vistas Basadas en Clases

- Reutilización y herencia son las características clave
- Son fáciles de extender
- Pueden parecer muy abstractas
- Son más difíciles de aprender al inicio

Ejemplo: 

```python
# views.py
from django.http import HttpResponse 
from django.views import View

class HomeView(View):
    def get(self, request): 
        return HttpResponse("<h3>Hola</h3>")

# urls.py
from django.urls import path
from .views import HomeView

app_name=...
urlpatterns = [
    path("home/", HomeView.as_view(), name="home")
]
```

## Comparativa

<img src="./assets/comparativa-vbf-vbc.png">

