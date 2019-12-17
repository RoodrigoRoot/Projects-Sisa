from django.db import models
from Profile.models import Profile
from django.db.models.signals import pre_save
import uuid
# Create your models here.
class Customer(models.Model):
    
    name_bussines = models.CharField(("Empresa"), blank=False, max_length=15)
    representative = models.CharField(("Representante"), max_length=50)
    phone = models.CharField(("Telefono"), max_length=15)
    email = models.EmailField(max_length=200)
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name_bussines

#class Project(models.Model):

#    name_project = models.CharField(("Nombre del Proyecto"), max_length=150)
#    slug = models.SlugField((""))
