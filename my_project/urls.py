from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger 설정
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL 패턴 설정
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# 테스트 코드
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

# APIClient fixture
@pytest.fixture
def api_client():
    return APIClient()

# 사용자 생성 fixture
@pytest.fixture
def create_user():
    return User.objects.create_user(username='testuser', password='testpassword')

# JWT 토큰 발급 fixture
@pytest.fixture
def get_tokens(create_user):
    refresh = RefreshToken.for_user(create_user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# JWT 토큰 발급 테스트
def test_obtain_jwt_token(api_client, create_user):
    response = api_client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

# 보호된 뷰 접근 테스트
def test_access_protected_view(api_client, get_tokens):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_tokens['access'])
    response = api_client.get('/protected-view/')
    assert response.status_code == 200

# JWT 토큰 갱신 테스트
def test_refresh_jwt_token(api_client, get_tokens):
    response = api_client.post('/api/token/refresh/', {'refresh': get_tokens['refresh']})
    assert response.status_code == 200
    assert 'access' in response.data
