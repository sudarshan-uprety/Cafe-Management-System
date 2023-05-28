from django.shortcuts import render
from category.models import FoodCategory
from rest_framework import generics,status
from rest_framework.response import Response
from category.serializers import FoodCategorySerializer,DrinkCategorySerializer,HukkaCategorySerializer,BeakeryCategorySerializer
from category.models import FoodCategory,DrinkCategory,HukkaCategory,BeakeryCategory
# Create your views here.


class FoodCategoryView(generics.GenericAPIView):
    serializer_class=FoodCategorySerializer

    def get_queryset(self):
        return FoodCategory.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        serializer=CategorySerializer(queryset,many=True)
        return Response(serializer.data)
    
class DrinkCategoryView(generics.GenericAPIView):
    serializer_class=DrinkCategorySerializer

    def get_queryset(self):
        return DrinkCategory.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        serializer=DrinkCategorySerializer(queryset,many=True)
        return Response(serializer.data)

class HukkaCategoryView(generics.GenericAPIView):
    serializer_class=HukkaCategorySerializer

    def get_queryset(self):
        return HukkaCategory.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        serializer=HukkaCategorySerializer(queryset,many=True)
        return Response(serializer.data)

class BeakeryCategoryView(generics.GenericAPIView):
    serializer_class=BeakeryCategorySerializer

    def get_queryset(self):
        return BeakeryCategory.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        serializer=BeakeryCategorySerializer(queryset,many=True)
        return Response(serializer.data)