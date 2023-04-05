from django.db import models
from django.urls import reverse

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100) # varchar datatype
    breed = models.CharField(max_length=100) # varchar datatype
    description = models.TextField(max_length=250) # text datatype
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    # this instance method returns a url for the detail page for each instance
    # this concept is based on the "fat models skinny controllers"
    def get_absolute_url(self):
        return reverse('cats_detail', kwargs={'cat_id': self.id})