from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.user.id), filename])

class UserProfile(models.Model):
    
    role = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    ghanacard_no = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    profileImage = models.ImageField(upload_to=upload_path, blank=True, null=True)

    def __str__(self):
        return self.first_name

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = [  "role", "address", "telephone", "ghanacard_no", "location", "profileImage"]
