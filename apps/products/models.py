from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

from apps.core.models import BaseModel
from apps.core.utils.upload_images import  generic_upload_to

class Product(BaseModel):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=generic_upload_to, blank=True, null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(0.05)
    ])
    stock = models.PositiveBigIntegerField(validators=[
        MinValueValidator(1)
    ])
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-name"]

    def get_detail_url(self):
        return reverse(
            "products:product_detail",
            kwargs={"slug": self.slug}
        )

    def get_update_url(self):
        return reverse(
            "products:product_update",
            kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        return reverse(
            "products:product_delete",
            kwargs={"slug": self.slug}
        )

    def save(self, *args, **kwargs):
        if not self.pk or (self.pk and Product.objects.get(pk=self.pk).name != self.name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name