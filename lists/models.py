from django.db import models

class List(models.Model):
    pass
# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')
    """list is an attribute of class Item with a relationship to List"""
    # list = models.ForeignKey(List, on_delete=models.CASCADE)



"""For learning"""
class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
