from django.shortcuts import render
from django.shortcuts import render
from offers.models import FoodOffers,DrinkOffers,HukkaOffers,BeakeryOffers
from menu.models import Food, Drink
from rest_framework import generics,status
from rest_framework.response import Response
from offers.serializers import FoodOfferSerializer,DrinkOfferSerializer,OfferSerializer,HukkaOfferSerializer,BeakeryOfferSerializer
# Create your views here.

class FoodOffersView(generics.GenericAPIView):
    serializer_class=FoodOfferSerializer

    def get_queryset(self):
        return FoodOffers.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        seiraliazer=FoodOfferSerializer(queryset,many=True)
        return Response(seiraliazer.data)
    
class DrinkOffersView(generics.GenericAPIView):
    serializer_class=FoodOfferSerializer

    def get_queryset(self):
        return DrinkOffers.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        seiraliazer=DrinkOfferSerializer(queryset,many=True)
        return Response(seiraliazer.data)


class HukkaOffersView(generics.GenericAPIView):
    serializer_class=HukkaOfferSerializer

    def get_queryset(self):
        return HukkaOffers.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        seiralizer=HukkaOfferSerializer(queryset,many=True)
        return Response(seiralizer.data)


class BeakeryOffersView(generics.GenericAPIView):
    serializer_class=BeakeryOfferSerializer

    def get_queryset(self):
        return BeakeryOffers.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        seiralizer=BeakeryOfferSerializer(queryset,many=True)
        return Response(seiralizer.data)


class AllOffersView(generics.GenericAPIView):
    serializer_class=OfferSerializer

    def get_queryset(self):
        return {
            'food_offers':FoodOffers.objects.all(),
            'drink_offers':DrinkOffers.objects.all()
            }
    
    def get(self, request):
        queryset=self.get_queryset()
        serializer = OfferSerializer(queryset)
        return Response(serializer.data)
