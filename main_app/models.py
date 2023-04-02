from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100) # varchar datatype
    breed = models.CharField(max_length=100) # varchar datatype
    description = models.TextField(max_length=250) # text datatype
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name