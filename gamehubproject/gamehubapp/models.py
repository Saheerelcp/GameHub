from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    quizscore = models.IntegerField()
    tictactoescore = models.IntegerField()
    stonescore= models.IntegerField()
    snakescore = models.IntegerField()