from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import UserSerializer,LoginSerializer
from users import serializers
from users.models import User
from django.contrib.auth import authenticate,logout
# Create your views here.

def get_token_for_user(user):
    refresh=RefreshToken.for_user(user)
    return {
        'access':str(refresh.access_token),
        'refresh':str(refresh),

    }

class CreateUser(generics.GenericAPIView):
    """
    An endpoint to create a new user
    """
    serializer_class=UserSerializer
    permission_classes = (AllowAny,)


    def get_queryset(self):
        return User.objects.none()

    def get(self,request):
        serializer=UserSerializer()
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
    def post(self,request,*args, **kwargs):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']
        password2 = serializer.validated_data['password2']
        if password!=password2:
            return Response({"error":"password and confirm password do not match"},status=401)
        validated_data=serializer.validated_data
        validated_data.pop('password2')
        user=User.objects.create_user(**validated_data)
        return Response({"message":"User register successfully."})


class LoginView(generics.GenericAPIView):
    """
    An endpoints to login
    """
    serializer_class=LoginSerializer
    permission_classes=(AllowAny,)

    def get(self,request):
        return User.objects.none()


    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.validated_data['email']
        password=serializer.validated_data['password']
        user=authenticate(request,email=email,password=password)
        print(user)
        if user is not None:
            user = User.objects.get(email=email)
            token = get_token_for_user(user)
            return Response({"success": "You are logged in", "token": token})
        return Response({"error": "Invalid Credentials"}, status=401)