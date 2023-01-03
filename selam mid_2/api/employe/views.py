from django.shortcuts import render
from rest_framework import generics
from .models import emplo
from .serializer import emploSerializer

# Create your views here.
class ListCreateAPI(generics.ListCreateAPIView):
    queryset =emplo.objects.all()
    serializer_class = emploSerializer

class Dl(generics.RetrieveUpdateDestroyAPIView):
    queryset=emplo.objects.all()
    serializer_class=emploSerializer    