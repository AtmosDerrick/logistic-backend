from rest_framework import serializers
from .models import Ship


class ProductSerializer(serializers.ModelSerializer):   
    class Meta(object):
        model = Ship
        fields = ['attendant','shipping_code', 'product', 'driver', 'shipping_datetime', 'delivered_datetime']
        
        
    