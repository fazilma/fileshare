from re import M
from django.conf import settings
from django.db import models


class Files(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.CharField(
        max_length=2000
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
