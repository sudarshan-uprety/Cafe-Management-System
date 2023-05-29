from rest_framework import serializers
from offers.models import FoodOffers,DrinkOffers,HukkaOffers,BeakeryOffers
from django.core.exceptions import ValidationError
from rest_framework.response import Response


class FoodOfferSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()
    class Meta:
        model=FoodOffers
        fields='__all__'

    def get_name(self,obj):
        return obj.name.name


class DrinkOfferSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()
    class Meta:
        model=DrinkOffers
        fields='__all__'

    def get_name(self,obj):
        return obj.name.name


class HukkaOfferSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()
    class Meta:
        model=HukkaOffers
        fields='__all__'

    def get_name(self,obj):
        return obj.name.name


class BeakeryOfferSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()
    class Meta:
        model=BeakeryOffers
        fields='__all__'

    def get_name(self,obj):
        return obj.name.name



class OfferSerializer(serializers.Serializer):
    food_offers = FoodOfferSerializer(many=True)
    drink_offers = DrinkOfferSerializer(many=True)

    def to_representation(self, instance):
        return {
            'food_offers': FoodOfferSerializer(instance['food_offers'], many=True).data,
            'drink_offers': DrinkOfferSerializer(instance['drink_offers'], many=True).data
        }