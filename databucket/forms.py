
from dataclasses import fields
from django.forms import ModelForm
from databucket.models import Files
from django import forms



class FileForm(ModelForm):
    file_uploaded = forms.FileField(required=False, label= 'File to Upload < 1 GB')
    upload_field_name= 'file_uploaded'
    max_upload_limit_size= 1024 * 1024 *1024
    class Meta:
        model = Files
        fields =('title', 'description', 'file_uploaded')
    

    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file_uploaded')
        if file is None:
            return
        if len(file) > self.max_upload_limit_size:
            self.add_error('picture', "File must be < "+self.max_upload_limit_size+" bytes")

    def save(self, commit=True):
        instance = super(FileForm, self).save(commit=False)
        if commit:
            instance.save()

        return instance
