from rest_framework import serializers
from .models import Ship


class ShipingSerializer(serializers.ModelSerializer):   
    class Meta(object):
        model = Ship
        fields = ['attendant','shipping_id', 'product', 'driver', 'shipping_datetime', 'delivered_datetime','delivered']
        
        
    