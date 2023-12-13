from django.db import models
from django.contrib.auth.models import User

def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.first_name), filename])

# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User, related_name='profile', null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100,choices=[("worker","worker"), ("driver","driver"), ("admin", "admin")])
    address = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    ghanacard_no = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    profileImage = models.ImageField(upload_to = upload_path, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)
    
    
    def __str__(self):
        return self.first_name



    

