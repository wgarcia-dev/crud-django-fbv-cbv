from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.conf import settings

from apps.products.models import Product
from apps.products.forms import ProductForm

def product_list(request):
    products = Product.objects.all()

    pages = settings.PAGE_NUMBER
    paginator = Paginator(products, pages)
    page_number = request.GET.get("page", 1)
    products = paginator.page(page_number)

    return render(request, "products/crud/product_list.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "products/product_detail.html", {"product": product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("products:product_list")
    else:
        form = ProductForm()
    return render(request, "products/crud/product_create.html", {"form": form})

def product_update(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/crud/product_update.html", {"form": form, "object": product})

def product_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        product.delete()
        return redirect("products:product_list")
    return render(request, "products/crud/product_delete.html", {"product": product})