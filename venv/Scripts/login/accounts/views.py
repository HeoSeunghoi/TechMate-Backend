from operator import ge
from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics

# Create your views here.

class Usercreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer