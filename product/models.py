from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=150)
    sender_contact = models.CharField(max_length=10)
    sender_email = models.CharField(max_length=100, default='')
    sender_address = models.CharField(max_length=100)
    sender_location = models.CharField(max_length=100)
    
    
    product = models.TextField(max_length=150)
    product_code = models.CharField(max_length=150)

    quantity = models.IntegerField() 
    weight = models.IntegerField() 
    item_type = models.CharField(max_length=100)
    destination = models.CharField(max_length=150)
    handle_preference = models.CharField(max_length=150)
    price = models.IntegerField() 
    
    reciever_name = models.CharField(max_length=150)
    reciever_contact = models.CharField(max_length=10)
    reciever_email = models.CharField(max_length=100, default='')
    reciever_address = models.CharField(max_length=100)
    reciever_location = models.CharField(max_length=100)
    
    status = models.CharField(max_length=100)    
    is_cancel = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.product_code



    

