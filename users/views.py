from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import UserSerializer
from users import serializers
from users.models import User
# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    # serializer_class = MyTokenObtainPairSerializer


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



# class Login(generics.GenericAPIView):

