from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, ProfileSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Profile


# Create your views here.
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"detail":"Not found"},status = status.HTTP_400_BAD_REQUEST )
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({
            "token": token.key, "user": serializer.data
        })

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()        
        token = Token.objects.create(user=user)
  
        return Response({
            "token": token.key, "user": serializer.data
        })
        
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST )


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"passed for {}".format(request.user.email)})


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_profile(request):
    user_info_serializer = ProfileSerializer(data=request.data)
    if user_info_serializer.is_valid():
        user_info_serializer.save()
        return Response(user_info_serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user_info = Profile.objects.all()
    serializer = ProfileSerializer(user_info, many=True)
    return JsonResponse({'message':'ok','data':serializer.data})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def oneProfile(request,id):
    try:
        user_info = Profile.objects.get(User=id)
        
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = ProfileSerializer(user_info)
    return JsonResponse({'message':'ok','data':serializer.data})


@api_view(['POST'])

def user_logout(request):
    logout(request)
    return JsonResponse({'message':'Logout Successful'})







