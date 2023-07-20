from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.FloatField()
    description=models.CharField(max_length=250)
    image=models.CharField(max_length=2500)
class Order(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    items=models.CharField(max_length=250)
    address=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    phoneno=models.CharField(max_length=250)
    delivery=models.BooleanField(default=False)