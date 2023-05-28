from django.shortcuts import render
from foods.models import Food
from rest_framework import generics,status
from rest_framework.response import Response
from foods.serializers import FoodSerializer

# Create your views here.
class AllFoods(generics.GenericAPIView):
    serializer_class=FoodSerializer

    def get_queryset(self):
        return Food.objects.all()
    

    def get(self,request):
        queryset=self.get_queryset()
        serializer=FoodSerializer(queryset,many=True)
        return Response(serializer.data)


class vegFoods(generics.GenericAPIView):
    serializer_class=FoodSerializer

    def get_queryset(self):
        return Food.objects.filter(category__name='veg')

    def get(self,request):
        queryset=self.get_queryset()
        serializer=FoodSerializer(queryset,many=True)
        return Response(serializer.data)

class NonVegFood(generics.GenericAPIView):
    serializer_class=FoodSerializer

    def get_queryset(self):
        return Food.objects.filter(category__name='non veg')

    def get(self,request):
        queryset=self.get_queryset()
        serializer=FoodSerializer(queryset,many=True)
        return Response(serializer.data)
    