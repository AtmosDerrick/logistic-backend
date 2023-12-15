from django.db import models
from django.contrib.auth.models import User
from product.models import Package

class Ship(models.Model):

    
    product = models.ForeignKey(Package, default=None, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    shipping_id = models.AutoField(primary_key=True)
    shipping_datetime = models.DateTimeField(auto_now=True)
    delivered_datetime = models.DateTimeField(null=True)
    delivered = models.BooleanField(default=True)

    def __str__(self):
        return str(self.shipping_id)
    
class Drop(models.Model):

    
    drop_id = models.AutoField(primary_key=True)
    drop_code = models.CharField(max_length=8)
    region = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    drop_datetime = models.DateTimeField(auto_now=True)
    manager = models.CharField(max_length=200)

    def __str__(self):
        return str(self.drop_id)


    

