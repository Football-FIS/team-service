from .models import Team
from .serializers import TeamSerializer, UserSerializer
from rest_framework import viewsets
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (AllowAny,)


class ValidateToken(APIView):
    def get(self, request, format=None):
        user = UserSerializer(request.user)
        return Response(user.data)


class SendEmailPlayer(APIView):
    permission_classes = (AllowAny,)

    # Request va a venir un parametro que es id del equipo
    # tienes que comprobar que el equipo tiene un plan que le permite
    # enviar correos y si es asi llamas a player service. 
    # Si se envia bien le devuelves a match-service un ok
    # si el equipo no tiene permisos desvuelves un mensaje de que ha ido mal
    def post(self, request, format=None):
        
        plan_type_allowed = ['PRE', 'ENT']
        
        team_filter = Team.objects.get(id=request)
        pl_type = team_filter.plan_type
        
        if pl_type in plan_type_allowed:
            #Aquí nos conectamos a player service
            return JsonResponse({"status" : "ok",
                                 "message": "this user has a permission to send email"})
        else:
            return JsonResponse({"status" : "error"})
            


class GoogleLogin(SocialLoginView):
    authentication_classes = []  # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/login"
    client_class = OAuth2Client
