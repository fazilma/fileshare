
from dataclasses import fields
from django.forms import ModelForm
from databucket.models import Files


class FileForm(ModelForm):
    class Meta:
        model = Files
        fields= '__all__'
