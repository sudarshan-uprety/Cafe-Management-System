from rest_framework import serializers
from category.models import FoodCategory,DrinkCategory,HukkaCategory,BeakeryCategory

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodCategory
        fields='__all__'


class DrinkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=DrinkCategory
        fields='__all__'

class HukkaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=HukkaCategory
        fields='__all__'

class BeakeryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BeakeryCategory
        fields='__all__'
