from .models import Team
from .serializers import TeamSerializer, UserSerializer
from rest_framework import viewsets
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticated,)


class ValidateToken(APIView):
    def get(self, request, format=None):
        user = UserSerializer(request.user)
        return Response(user.data)


class SendEmailPlayer(APIView):
    permission_classes = (AllowAny,)

    # Request va a venir un parametro que es id del equipo
    # tienes que comprobar que el equipo tiene un plan que le permite
    # enviar correos y si es asi llamas a player service. 
    # Si se envia bien le devuelves a mathc-sservice un ok
    # si el equipo no tiene permisos desvuelves un mensaje de que ha ido mal
    def post(self, request, format=None):
        return Response("hola")


class GoogleLogin(SocialLoginView):
    authentication_classes = []  # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/login"
    client_class = OAuth2Client
