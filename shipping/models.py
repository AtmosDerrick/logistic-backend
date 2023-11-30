from django.db import models
from django.contrib.auth.models import User

class Ship(models.Model):
    attendant = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    product = models.CharField(max_length=150, null=True)
    driver = models.CharField(max_length=150)
    shipping_id = models.AutoField(primary_key=True)
    shipping_datetime = models.DateTimeField(auto_now=True)
    delivered_datetime = models.DateTimeField(null=True)
    delivered = models.BooleanField(default=True)

    def __str__(self):
        return self.product


    

