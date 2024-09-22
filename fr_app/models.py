from django.db import models

# Create your models here.
from django.db import models
# Create your models here.


class Food(models.Model):
    fName = models.TextField(max_length=20)
    fPrice = models.IntegerField()


class Restaurant(models.Model):
    rName = models.TextField(max_length=20)
    rLocation = models.TextField(max_length=20)
