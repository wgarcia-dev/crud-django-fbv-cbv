import os
import uuid

def generic_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    app_label = instance._meta.app_label  # ej. "users" o "products"
    model_name = instance._meta.model_name  # ej. "user" o "product"

    return os.path.join(app_label, model_name, filename)