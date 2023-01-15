from django.db import models
from poste.models import Poste

# Create your models here.

class Candidature(models.Model):
    poste = models.ForeignKey(Poste,blank=True,on_delete=models.CASCADE) 
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telephone =models.CharField(max_length=45)
    cv = models.FileField(upload_to='documents/', null=True)

    def __str__(self):
        return f"la candidature de {self.nom}/{self.nom} est bien récu"
