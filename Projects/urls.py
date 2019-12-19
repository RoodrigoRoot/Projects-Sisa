from django.urls import path
from .views import *
urlpatterns = [
    path("", ProjectsView.as_view(), name="projects"),
    path("/<str:slug>", ProjectsView.as_view(), name="projects_slug"),
]
