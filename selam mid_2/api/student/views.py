from django.shortcuts import render
from rest_framework import generics
from .models import stud
from .serializer import studSerializer

# Create your views here.
class ListCreateAPI(generics.ListCreateAPIView):
    queryset =stud.objects.all()
    serializer_class = studSerializer

class Dl(generics.RetrieveUpdateDestroyAPIView):
    queryset=stud.objects.all()
    serializer_class=studSerializer