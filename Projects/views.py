from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Projects
# Create your views here.

class ProjectsView(ListView):
    model = Projects
    template_name= 'projects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
        
class ProjectSlugView():
    pass