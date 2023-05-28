from rest_framework import serializers
from drinks.models import Drink
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from category.serializers import DrinkCategorySerializer

class DrinkSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    class Meta:
        model=Drink
        fields=['name','description','price','category','image']

    def get_category(self,obj):
        return obj.category.name

        