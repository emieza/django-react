from django.db import models
from django.contrib.auth.models import AbstractUser


class Llibre (models.Model):
    titol = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    resum = models.TextField(null=True,blank=True)
    data_edicio = models.DateField()
    def __str__(self):
    	return self.titol


class Usuari(AbstractUser):
    auth_token = models.CharField(max_length=32,blank=True,null=True)
    # + altres atributs que es vulguin afegir...

