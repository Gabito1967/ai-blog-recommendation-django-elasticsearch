import os
from urllib.parse import urljoin
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime


class PostImageStorage(FileSystemStorage):
    """Custom storage for django_ckeditor_5 images."""

    def __init__(self, *args, **kwargs):
        today = datetime.today()
        custom_path = f"uploads/{today.year}/{today.month}/{today.day}/"  # Dynamic folder structure
        location = os.path.join(settings.MEDIA_ROOT, custom_path)
        base_url = urljoin(settings.MEDIA_URL, custom_path)

        kwargs.update({
            "location": location,
            "base_url": base_url,
        })

        super().__init__(*args, **kwargs)