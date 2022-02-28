import uuid
import zlib
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from databucket.forms import FileForm
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
from django.core.files.storage import FileSystemStorage
import mimetypes

from databucket.models import Files

class Menu(View):
    template_name='databucket/menu.html'
    def get(self, request):
        return render(request, self.template_name )

class OwnerView(View,LoginRequiredMixin):
    
    model = Files

    def get_queryset(self) :
        qs = super().get_queryset()
        return qs.filter(owner = self.request.user)


class FilesListView(OwnerView,ListView):
    model = Files
    

class CreateView(OwnerView,generic.CreateView):
    template_name = 'databucket/files_form.html'
    success_url = reverse_lazy('databucket:menu')

    def get(self, request,pk=None):
        form = FileForm()
        ctx = {'form':form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form  = FileForm(request.POST, request.FILES or None)
        file10mb = 10*1024*1024
        if not form.is_valid():
            print('validateing form')
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        file = form.save(commit=False)
        f = request.FILES['file_uploaded']   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            content_type = f.content_type
            name = f.name
            decompress = True
            compressed=False
            file_location=''
            if(name.endswith('.zip') or name.endswith('.tar.gz') or len(bytearr)< file10mb):
                decompress=False
            
            if decompress:
                compressed=True
                compressed_date = zlib.compress(bytearr)
                file_location = './fileshare/'+name+'.zip'
                with open(file_location ,'wb+') as destination:
                    for chunk in bytearr.chunks():
                        destination.write(chunk)
            else:
                file_location = './fileshare/'+name
                with open(file_location ,'wb+') as destination:
                    destination.write(bytearr)

            file.compressed = compressed
            file.content_type = content_type
            file.filename = name
            file.file_storage_path = os.path.abspath(file_location)

            #instance.picture = bytearr  # Overwrite with the actual image data
        # Add owner to the model before saving
        
        file.owner = self.request.user
        file.save()
        return redirect(self.success_url)

class DeleteView(OwnerView, generic.DeleteView):
    model = Files

class Share(OwnerView):

    template_name='databucket/file_share.html'

    def get(self, request,pk):
        file = get_object_or_404(self.model, pk=pk)
        f = open(file.file_storage_path,'rb')
        data = f
        if(file and file.compressed):  
            data = zlib.decompress(f)

        if data:
            fs = FileSystemStorage(location = './media/')
            filename = fs.save(file.filename,data)
            file_url = request.META['HTTP_HOST']+'/databucket/shared'+fs.url(filename)
            return render(request, self.template_name, {'file_url':file_url} )
        return render(request, self.template_name )

def download_file(request, file_loc):
    fs = FileSystemStorage(location = './media/')
    file=fs.open(file_loc)
    fl_path = fs.path(file_loc)
    filename = file.name

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='multipart/form-data')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response