from rest_framework import serializers
from hukka.models import Hukka
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from category.serializers import HukkaCategorySerializer

class HukkaSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()

    class Meta:
        model=Hukka
        fields=['name','description','price','category','image']

    def get_category(self,obj):
        return obj.category.name