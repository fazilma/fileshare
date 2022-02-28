from dataclasses import fields
import imp
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from databucket.forms import FileForm


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
    model = Files
    fields = ('title','description')
    success_url = reverse_lazy('databucket:menu')

    def form_valid(self, form) -> HttpResponse:
        object = form.save(commit= False)
        object.owner = self.request.user
        object.save()
        return super().form_valid(form)



class DeleteView(OwnerView, generic.DeleteView):
    model = Files

