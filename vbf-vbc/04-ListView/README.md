# Concepto inicial 

- Lista objetos de un modelo 
- Internamente, realiza una consulta **.all()** y pasa los resultados a la plantilla mediante el contexto 

# Ejemplo 

```python
# views.py
from django.shortcuts import render
from django.views.generic import ListView 
from .models import Book 

class BookListView(ListView): 
    model = Book
    template_name = "book/book_list.html"
    paginate_by = 4
    context_object_name = "books"

# urls.py
app_name = "book"

urlpatterns = [
    path("", BookListView.as_view(), name="home")
]
```

```html
{% extends "base.html" %}
{% load static %}

{% block title_pag %}Lista de libros 📚{% endblock title_pag %}

{% block styles %}
    <link rel="stylesheet" href="{% static 'book/css/book_list.css' %}">
{% endblock styles %}

{% block content %}
    <div class="books-container-main">
        <h2 class="title">Lista de libros 📚</h2>

        <div class="books-grid">
            {% for book in books %}
                <div class="book-card">
                    <h3 class="book-title">{{ book.title }}</h3>
                    <p class="books-field"><strong>Autor:</strong> {{ book.author.username }}</p>
                    <p class="books-field"><strong>Páginas:</strong> {{ book.pages }}</p>
                    <p class="books-field"><strong>Fecha:</strong> {{ book.created_at }}</p>
                </div>
            {% empty %}
                <p class="empty-message">No hay libros disponibles por el momento...</p>
            {% endfor %}
        </div>
        
        {% comment %} Sirve para indicar si hay paginación {% endcomment %}
        {% if is_paginated %}
            <div class="container-paginator">
                <div class="paginator-group">
                    {% if page_obj.has_previous %}
                        <a class="paginator-btn" href="?page=1">Primero</a>
                        <a class="paginator-btn" href="?page={{ page_obj.previous_page_number }}">Anterior</a>
                    {% endif %}
                </div>

                <span class="paginator-info">Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}</span>

                <div class="paginator-group">
                    {% if page_obj.has_next %}
                        <a class="paginator-btn" href="?page={{ page_obj.next_page_number }}">Siguiente</a>
                        <a class="paginator-btn" href="?page={{ page_obj.paginator.num_pages }}">Último</a>
                    {% endif %}
                </div>
            </div>
        {% endif %}
    </div>
{% endblock content %}
```

<img src="./assets/demostracion.png">