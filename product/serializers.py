from rest_framework import serializers
from .models import Package


class ProductSerializer(serializers.ModelSerializer):   
    class Meta(object):
        model = Package
        fields = ['User','sender_name','shipping_confirmation','arrival_confirmation', 'sender_contact',  'package_name', 'quantity', 'item_type', 'handle_preference', 'price', 'reciever_name', 'reciever_contact',  'reciever_address', 'product_status', 'is_cancel', 'datetime', 'package_code']
        
        
    