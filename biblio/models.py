from django.db import models


class Llibre (models.Model):
    titol = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    resum = models.TextField(null=True,blank=True)
    data_edicio = models.DateField()

    def __str__(self):
    	return self.titol
