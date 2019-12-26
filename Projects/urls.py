from django.urls import path
from .views import *

urlpatterns = [
    path("<str:slug>", ProjectSlugView.as_view(), name="project_slug"),
    path("", ProjectsView.as_view(), name="projects"),
    
]
