from django.contrib import admin
from .models import *
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):

    list_display=["name_project", "created_at", "modified_at", "slug"]
    fields = ("name_project", "bussines", "folio", "need", "comments")
    ordering = ['folio']

admin.site.register(Projects, ProjectsAdmin)

class ProposalAdmin(admin.ModelAdmin):
    list_display=["project", "status", "created_at" ]

admin.site.register(Proposal, ProposalAdmin)