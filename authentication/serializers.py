from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
class ProfileSerializer(serializers.ModelSerializer):   
    class Meta(object):
        model = Profile
        fields = ['User', 'first_name', 'last_name', 'role', 'address', 'telephone', 'ghanacard_no', 'location', 'date_created']
        
        
    