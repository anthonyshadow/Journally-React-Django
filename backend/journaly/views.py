from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, JournalSerializer
from .models import User, Journal

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class JournalView(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()
