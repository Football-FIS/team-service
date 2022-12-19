# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# URL statement
#
# email brunogllaga@icloud.com
# -----------------------------------------------------------

from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from .views import TeamViewSet, ValidateToken, SendEmailPlayer

schema_view = get_schema_view(
   openapi.Info(
      title="Team Service API",
      default_version='v1',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="brugonlla@alum.us.es.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'team', TeamViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('validate-token', ValidateToken.as_view()),
    path('send-email-player', SendEmailPlayer.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
