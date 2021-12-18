from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
  userDetails = serializers.ReadOnlyField()
  class Meta:
    model = Order
    fields = '__all__'
