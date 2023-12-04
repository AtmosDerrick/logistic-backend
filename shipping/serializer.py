from rest_framework import serializers
from .models import Ship, Drop


class ShipingSerializer(serializers.ModelSerializer):   
    class Meta(object):
        model = Ship
        fields = ['shipping_id', 'product', 'driver', 'shipping_datetime', 'delivered_datetime','delivered']
        
class DropSerializer(serializers.ModelSerializer):   
    class Meta(object):
        model = Drop
        fields = ['shipping_id', 'drop_code', 'region', 'city', 'drop_datetime','manager']
        
        
        
        
    