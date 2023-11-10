from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    ghanacard_no = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True, null=True)
    
    
    def __str__(self):
        return self.User.username


    

