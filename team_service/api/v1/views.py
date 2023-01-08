from team_service.team_service import settings
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
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (AllowAny,)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super(TeamViewSet, self).dispatch(*args, **kwargs)


class ValidateToken(APIView):
    def get(self, request, format=None):
        user = UserSerializer(request.user)
        return Response(user.data)


class SendEmailPlayer(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):

        plan_type_allowed = ['PRE', 'ENT']

        team_filter = Team.objects.get(id=request)
        pl_type = team_filter.plan_type

        if pl_type in plan_type_allowed:
            # Aquí nos conectamos a player service
            return JsonResponse({
                "status": "ok",
                "message": "this user has a permission to send email"
            })
        else:
            return JsonResponse({"status": "error"})


class GoogleLogin(SocialLoginView):
    permission_classes = (AllowAny,)
    authentication_classes = []  # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.CALLBACK_URL
    client_class = OAuth2Client
