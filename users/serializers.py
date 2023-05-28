from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['full_name','email','password','password2','phone']

    def create_user(self, validated_data):
        user=User.objects.create(**validated_data)
        return User

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()

    class Meta:
        model=User
        fields=['email','password']