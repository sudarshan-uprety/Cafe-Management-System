from rest_framework import serializers
from foods.models import Food
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from category.serializers import FoodCategorySerializer

class FoodSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    class Meta:
        model=Food
        fields=['name','description','price','category','image']

    def get_category(self,obj):
        return obj.category.name