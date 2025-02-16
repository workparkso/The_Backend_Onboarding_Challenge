from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),  # users 앱 등록
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),  # JWT 토큰 검증 API 추가
]
