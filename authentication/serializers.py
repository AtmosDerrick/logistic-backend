from rest_framework import serializers
from django.contrib.auth.models import User
from .model import UserProfile
# from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ("username", "password", "first_name", "last_name", 'email')
        
        
        
class ProfileSerializer(serializers.ModelSerializer):   
    class Meta(object):
        model = UserProfile
        fields = ['User','profileImage' , 'role', 'address', 'telephone', 'ghanacard_no', 'location', 'date_created']
        
        def get_photo_url(self, obj):
            request = self.context.get('request')
            image_profile = obj.profileImage.url
            return request.build_absolute_uri(image_profile)
        
        
        
            
    