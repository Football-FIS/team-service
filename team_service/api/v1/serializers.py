from .models import Team
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = '__all__'
    extra_kwargs = {
      'id': {'read_only': True},
    }
