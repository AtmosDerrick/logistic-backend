from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):   
    class Meta(object):
        model = Product
        fields = ['User','sender_name','shipping_confirmation','arrival_confirmation', 'sender_contact', 'sender_email', 'sender_address', 'sender_location', 'product', 'quantity', 'weight', 'item_type', 'destination', 'handle_preference', 'price', 'reciever_name', 'reciever_contact', 'reciever_email', 'reciever_address', 'reciever_location', 'product_status', 'is_cancel', 'datetime', 'product_code']
        
        
    