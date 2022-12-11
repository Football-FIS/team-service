# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# URL statement
#
# email brunogllaga@icloud.com
# -----------------------------------------------------------

from django.urls import path, include
from rest_framework import routers

from .views import TeamViewSet



router = routers.DefaultRouter()
router.register(r'team', TeamViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
