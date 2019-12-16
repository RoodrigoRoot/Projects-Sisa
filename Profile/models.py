from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    AREAS = [('Soporte','Soporte'),
            ('Implementacion', 'Implementacion'),
            ('Pre-Venta','Pre-Venta')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.CharField(choices=AREAS, max_length=15)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.area)
        
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'