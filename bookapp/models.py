from audioop import reverse
from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Book(models.Model):
    objects = None
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)


    def __str__(self):
        return self.name


