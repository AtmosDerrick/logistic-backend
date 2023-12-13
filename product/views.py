from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required





from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import uuid

# Create your views here.
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_product(request):
    user = request.user
    request.data['product_code'] = str(uuid.uuid4())[:8]  
    request.data['product_status'] = 'recieved'
 
    


    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      
        serializer.save()
    
        return Response({
           "product": serializer.data
        })
        
    return Response(serializer.errors, status = status.HTTP_200_OK )

#all products

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def product_list(request):
    user = request.user
    print(user)
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)  # Specify many=True for queryset
    return JsonResponse({'message': 'ok', 'data': serializer.data})

#get recieved product
#all products
@api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def product_recieve(request, location):
  
    try:
        recieve_product = Product.objects.filter(sender_location=location, product_status='recieved')
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer =ProductSerializer(recieve_product, many=True)
    return JsonResponse({'message':'ok','data':serializer.data})

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def product_shipping(request, location):
  
    try:
        recieve_product = Product.objects.filter(sender_location=location, product_status='shipped')
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer =ProductSerializer(recieve_product, many=True)
    return JsonResponse({'message':'ok','data':serializer.data})

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def product_arrival(request, location):
  
    try:
        recieve_product = Product.objects.filter(destination=location, product_status='shipped' )
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer =ProductSerializer(recieve_product, many=True)
    return JsonResponse({'message':'ok','data':serializer.data})



@api_view(['GET','PUT'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def product_one(request, code):
  
    try:
        recieve_product = Product.objects.get(product_code = code)
        
        if request.method == 'PUT':
            if(recieve_product.shipping_confirmation == True):
                request.data['shipping_confirmation'] = False  
                request.data['product_status'] = 'shipping' 
                serializer = ProductSerializer(recieve_product, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
            elif(recieve_product.shipping_confirmation == False):
                print(recieve_product.shipping_confirmation)
               

                return Response({"message":"Done"})
                
            else:
                request.data['shipping_confirmation'] = True  
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
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def product_delivery(request, code, location):
  
    try:
        recieve_product = Product.objects.get(product_code = code, destination=location)
        
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = ProductSerializer(recieve_product, many=False)
    return JsonResponse({'message':'ok','data':serializer.data})









