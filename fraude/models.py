from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class Analyse(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    nom_fichier = models.CharField(max_length=200, blank=True)


class Transaction(models.Model):
    analyse = models.ForeignKey(Analyse, on_delete=models.CASCADE, related_name="transactions")
    type = models.CharField(max_length=20)
    montant = models.FloatField()
    heure = models.IntegerField()
    score = models.FloatField()
    decision = models.CharField(max_length=10)