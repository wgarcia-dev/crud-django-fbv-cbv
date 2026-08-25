from apps.core.models import BaseModel
from apps.core.utils.upload_images import  generic_upload_to

from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import models
from django.urls import reverse

class User(BaseModel, AbstractUser):
    photo = models.ImageField(
        upload_to=generic_upload_to, blank=True, null=True
    )
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-date_joined"]

    def get_detail_url(self):
        return reverse(
            "users:user_detail",
            kwargs={"slug": self.slug}
        )

    def get_update_url(self):
        return reverse(
            "users:user_update",
            kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        return reverse(
            "users:user_delete",
            kwargs={"slug": self.slug}
        )

    def save(self, *args, **kwargs):
        if not self.pk or (self.pk and User.objects.get(pk=self.pk).username != self.username):
            base_slug = slugify(self.username)
            slug = base_slug
            counter = 1

            while User.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        full_name = self.get_full_name().strip()
        return full_name if full_name else self.username