from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poste(models.Model):
    recruteur = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    objectif_a_recruter = models.IntegerField(null=True)
    departement =models.CharField(max_length=45)
    lieu_travail =models.CharField(max_length=45)
    type_emploi = models.CharField(max_length=8,choices=(('Stage', 'Stage'),('CDD','CDD'),('CDI','CDI'),))
    email = models.CharField(max_length=45)

    def __str__(self):
        return f"une Poste de travaille pour {self.title}"