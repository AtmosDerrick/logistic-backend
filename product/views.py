from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Product

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

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product)
    return JsonResponse({'message':'ok','data':serializer.data})
