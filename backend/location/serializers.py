from rest_framework import serializers
from .models import Location, Customer, ServiceProvider
from django.contrib.auth.models import User

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'location']

class ServiceProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer()

    class Meta:
        model = ServiceProvider
        fields = ['id', 'user', 'location']
