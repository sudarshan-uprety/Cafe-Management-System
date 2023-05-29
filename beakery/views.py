from django.shortcuts import render
from beakery.models import Beakery
from rest_framework import generics,status
from rest_framework.response import Response
from beakery.serializers import BeakerySerializer
# Create your views here.

class AllBeakeryProduct(generics.GenericAPIView):
    serializer_class=BeakerySerializer
    def get_queryset(self):
        return Beakery.objects.all()

    def get(self,request):
        queryset=self.get_queryset()
        serializer=BeakerySerializer(queryset,many=True)
        return Response(serializer.data)
    