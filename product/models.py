from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Package(models.Model):
  
    User = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True,  blank=True)

    sender_name = models.CharField(max_length=150)
    sender_contact = models.CharField(max_length=10) 
    sender_location = models.CharField(max_length=100)
    
    
    package_name = models.TextField(max_length=150 )
    package_code = models.CharField(max_length=150)
    quantity = models.IntegerField() 
    item_type = models.CharField(max_length=100)
    handle_preference = models.CharField(max_length=150)
    price = models.IntegerField() 
    
    reciever_name = models.CharField(max_length=150)
    reciever_contact = models.CharField(max_length=10)
    reciever_address = models.CharField(max_length=100)
    
    shipping_confirmation = models.BooleanField(null=True)
    arrival_confirmation = models.BooleanField(null=True)

    product_status = models.CharField(max_length=100)    
    is_cancel = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.package_name)



    

