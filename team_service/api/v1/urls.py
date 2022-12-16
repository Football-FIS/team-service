# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# URL statement
#
# email brunogllaga@icloud.com
# -----------------------------------------------------------

from django.urls import path, include
from rest_framework import routers

from .views import TeamViewSet, ValidateToken, SendEmailPlayer


router = routers.DefaultRouter()
router.register(r'team', TeamViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('validate-token', ValidateToken.as_view()),
    path('send-email-player', SendEmailPlayer.as_view())
]
