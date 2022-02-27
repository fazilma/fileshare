from django.contrib import admin
from databucket.models import Files


class FilesAdmin(admin.ModelAdmin):
    exclude = ('')

# Register your models here.
admin.site.register(Files)