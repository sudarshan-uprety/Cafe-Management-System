from django.shortcuts import render
from hukka.models import Hukka
from rest_framework import generics,status
from rest_framework.response import Response
from hukka.serializers import HukkaSerializer
# Create your views here.


class HukkaView(generics.GenericAPIView):
    serializer_class=HukkaSerializer

    def get_queryset(self):
        return Hukka.objects.all()
    
    def get(self,request):
        queryset=self.get_queryset()
        seializer=HukkaSerializer(queryset,many=True)
        return Response(seializer.data)
    