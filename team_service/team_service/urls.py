from django.contrib import admin
from django.urls import path, include
from api.v1.views import GoogleLogin


urlpatterns = [
    path('api/v1/', include('api.v1.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('social-login/google/', GoogleLogin.as_view(), name='google_login'),
]
