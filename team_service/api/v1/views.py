from django.shortcuts import render

from .models import Team
from .serializers import TeamSerializer
from rest_framework import viewsets

class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer