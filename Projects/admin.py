from django.contrib import admin
from .models import Projects
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):

    list_display=["name_project", "created_at", "modified_at", "slug"]
    fields = ("name_project", "bussines", "folio", "need", "comments")
    ordering = ['name_project']

admin.site.register(Projects, ProjectsAdmin)