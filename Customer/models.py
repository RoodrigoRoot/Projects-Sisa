from django.db import models
from Profile.models import Profile
from django.db.models.signals import pre_save
import uuid
# Create your models here.
class Customer(models.Model):
    
    name_bussines = models.CharField(("Empresa"), blank=False, max_length=15)
    representative = models.CharField(("Encargado de Proyecto"), max_length=50)
    slug = models.SlugField(null=False, blank=False, unique=True)
    project = models.TextField()
    phone = models.CharField(("Telefono"), max_length=15)

    