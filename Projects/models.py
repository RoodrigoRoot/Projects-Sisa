from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import uuid

from Customer.models import Customer
# Create your models here.
class Projects(models.Model):

    name_project = models.CharField(("Nombre del Proyecto"), max_length=50)
    bussines = models.ForeignKey(Customer, verbose_name=("Empresa"), on_delete=models.CASCADE)
    folio = models.IntegerField(("Folio"), unique=True, null=False)
    need = models.TextField(("Necesidad"))
    slug = models.SlugField(("Slug"))    
    comments = models.TextField(("Comentarios")) 
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    modified_at = models.DateTimeField(auto_now=False, auto_now_add=True) 

    def __str__(self):
        return self.name_project
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural= "Proyectos"


def create_slug(sender, instance, **kwargs):
    uid = str(uuid.uuid4())
    instance.slug = slugify("{}-{}{}".format(instance.folio, instance.name_project, uid[:8]))

pre_save.connect(create_slug, Projects)
