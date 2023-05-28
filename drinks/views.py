from django.shortcuts import render
from drinks.models import Drink
from rest_framework import generics,status
from rest_framework.response import Response
from drinks.serializers import DrinkSerializer
# Create your views here.

class AllDrinks(generics.GenericAPIView):
    serializer_class=DrinkSerializer

    def get_queryset(self):
        return Drink.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        seiralizer=DrinkSerializer(queryset,many=True)
        return Response(seiralizer.data)


class AlcoholDrinks(generics.GenericAPIView):
    serializer_class=DrinkSerializer

    def get_queryset(self):
        return Drink.objects.filter(category__name='alcohol')
    
    def get(self,request):
        queryset=self.get_queryset()
        serializer=DrinkSerializer(queryset,many=True)
        return Response(serializer.data)
    

class NonAlcoholDrinks(generics.GenericAPIView):
    serializer_class=DrinkSerializer

    def get_queryset(self):
        return Drink.objects.filter(category__name='non alcoho')
    
    def get(self,request):
        queryset=self.get_queryset()
        serializer=DrinkSerializer(queryset,many=True)
        return Response(serializer.data)
    