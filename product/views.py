from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Product
from django.http import JsonResponse


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import uuid

# Create your views here.
@api_view(['POST'])
def create_product(request):
    request.data['product_code'] = str(uuid.uuid4())[:8]  

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response({
           "product": serializer.data
        })
        
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST )

#all products
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)  # Specify many=True for queryset
    return JsonResponse({'message': 'ok', 'data': serializer.data})

#get recieved product
#all products
@api_view(['GET'])
def product_recieve(request, location):
  
    try:
        recieve_product = Product.objects.filter(sender_location=location, product_status='Recieved')
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer =ProductSerializer(recieve_product, many=True)
    return JsonResponse({'message':'ok','data':serializer.data})

@api_view(['GET'])
def product_shipping(request, location):
  
    try:
        recieve_product = Product.objects.filter(sender_location=location, product_status='shipped')
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer =ProductSerializer(recieve_product, many=True)
    return JsonResponse({'message':'ok','data':serializer.data})

@api_view(['GET'])
def product_arrival(request, location):
  
    try:
        recieve_product = Product.objects.filter(destination=location, product_status='shipped' )
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer =ProductSerializer(recieve_product, many=True)
    return JsonResponse({'message':'ok','data':serializer.data})



@api_view(['GET','PUT'])
def product_one(request, code):
  
    try:
        recieve_product = Product.objects.get(product_code = code)
        
        if request.method == 'PUT':
            serializer = ProductSerializer(recieve_product, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
        
        
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = ProductSerializer(recieve_product, many=False)
    return JsonResponse({'message':'ok','data':serializer.data})



@api_view(['GET'])
def product_delivery(request, code, location):
  
    try:
        recieve_product = Product.objects.get(product_code = code, destination=location)
        
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = ProductSerializer(recieve_product, many=False)
    return JsonResponse({'message':'ok','data':serializer.data})









