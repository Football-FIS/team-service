from django.shortcuts import render

from .models import Team
from .serializers import TeamSerializer
from rest_framework import viewsets
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings


class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

class GoogleLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/login"
    client_class = OAuth2Client