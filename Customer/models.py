from django.db import models
from Profile.models import Profile
from django.db.models.signals import pre_save
from django.utils.text import slugify
import uuid
# Create your models here.
class Customer(models.Model):
    
    name_bussines = models.CharField(("Empresa"), blank=False, max_length=15)
    representative = models.CharField(("Representante"), max_length=50)
    phone = models.CharField(("Telefono"), max_length=15)
    email = models.EmailField(max_length=200)
    slug = models.SlugField(("Slug"))
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name_bussines

def create_slug(sender, instance, **kwargs):
    uid = str(uuid.uuid4())
    instance.slug = slugify(instance.name_bussines)

pre_save.connect(create_slug, Customer)