from re import M
from attr import field
from rest_framework import serializers
from .models import User, Journal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'bio', 'location', 'password', 'age')

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('journal_title', 'text') 