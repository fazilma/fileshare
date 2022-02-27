from unicodedata import name
from django.urls import path, reverse_lazy

from . import views

app_name = 'databucket'

urlpatterns = [
    path('', views.Menu.as_view(), name= 'menu'),
    path('list', views.FilesListView.as_view(), name='files_list'),
    path('create', views.CreateView.as_view(success_url=reverse_lazy('databucket:files_list')), name='create'),
    path('<int:pk>/delete', views.DeleteView.as_view(success_url=reverse_lazy('databucket:files_list')), name = 'delete'),
    ]