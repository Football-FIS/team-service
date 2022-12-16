from .models import Team
from rest_framework import serializers
from django.contrib.auth.models import User


class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = '__all__'
    extra_kwargs = {
      'id': {'read_only': True},
    }


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name', 'last_name', 'email')
    extra_kwargs = {
      'id': {'read_only': True},
    }

