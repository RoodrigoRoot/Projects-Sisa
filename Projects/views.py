from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from .models import Projects
# Create your views here.

class ProjectsView(ListView):
    model = Projects
    template_name= 'projects_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
class ProjectSlugView(DetailView):

    model = Projects    
    template_name = "project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    