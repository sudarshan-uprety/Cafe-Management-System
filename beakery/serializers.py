from rest_framework import serializers
from beakery.models import Beakery
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from category.serializers  import BeakeryCategorySerializer

class BeakerySerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    class Meta:
        model=Beakery
        fields=['name','description','price','category','image']

    def get_category(self,obj):
        return obj.category.name