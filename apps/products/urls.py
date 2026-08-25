from django.urls import path
from apps.products.views import product_list, product_detail, product_create, product_update, product_delete

app_name = "products"

urlpatterns = [
    path("product-list/", product_list, name="product_list"),
    path("product-create/", product_create, name="product_create"),
    path("product-detail/<slug:slug>/", product_detail, name="product_detail"),
    path("product-update/<slug:slug>/", product_update, name="product_update"),
    path("product-delete/<slug:slug>/", product_delete, name="product_delete"),
]