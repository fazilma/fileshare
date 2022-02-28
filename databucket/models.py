from re import M
from ssl import create_default_context
from turtle import update
from django.conf import settings
from django.db import models


class Files(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.CharField(
        max_length=2000
    )
    file_storage_path = models.CharField(max_length=2000)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content_type = models.CharField(max_length=200, null=True)
    filename = models.CharField(max_length=200,null=True)
    compressed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
