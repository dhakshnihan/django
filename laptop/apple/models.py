
from django.db import models 


# Create your models here.
class Tiru(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    age = models.IntegerField(max_length=30)

