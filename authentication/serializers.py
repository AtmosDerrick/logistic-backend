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
        fields = ['User','profileImage' ,'first_name', 'last_name', 'role', 'address', 'telephone', 'ghanacard_no', 'location', 'date_created']
        
        def get_photo_url(self, obj):
            request = self.context.get(request)
            imageProfile = obj.fingerprint.url
            return request.build_absolute_url(imageProfile)
        
        
    