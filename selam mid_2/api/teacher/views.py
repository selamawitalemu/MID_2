from django.shortcuts import render
from rest_framework import generics
from .models import teac
from .serializer import teacSerializer

# Create your views here.
class ListCreateAPI(generics.ListCreateAPIView):
    queryset =teac.objects.all()
    serializer_class = teacSerializer

class Dl(generics.RetrieveUpdateDestroyAPIView):
    queryset=teac.objects.all()
    serializer_class=teacSerializer    