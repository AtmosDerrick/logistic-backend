from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import ShipingSerializer, DropSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Ship, Drop
from django.http import JsonResponse





from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from product.models import Product

import uuid

# Create your views here.

# Create your views here.
@api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def create_shipping(request):
    serializer = ShipingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response({
           "shipping": serializer.data
        })
        
    return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND )

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def allShipping(request):
    shipping_products = Ship.objects.all()
    serializer = ShipingSerializer(shipping_products, many=True)  # Specify many=True for queryset
    return JsonResponse({'message': 'ok', 'data': serializer.data})

#creating drops
@api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def create_shipping(request):
    serializer = Drop(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response({
           "shipping": serializer.data
        })
        
    return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND )
