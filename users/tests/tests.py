import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def create_user():
    """유저 생성"""
    return User.objects.create_user(username="testuser", password="testpassword")

@pytest.fixture
def api_client():
    """API 클라이언트"""
    return APIClient()

# 로그인 API 테스트 (JWT 발급)
def test_login_api(create_user, api_client):
    url = "/api/login/"
    data = {"username": "testuser", "password": "testpassword"}
    
    response = api_client.post(url, data, format="json")
    
    assert response.status_code == status.HTTP_200_OK
    assert "token" in response.data  # JWT 토큰 확인

# 보호된 API 테스트 (유효한 토큰 사용)
def test_protected_api_with_valid_token(create_user, api_client):
    url = "/api/protected/"  # 보호된 API URL
    data = {"username": "testuser", "password": "testpassword"}
    
    # 로그인하여 JWT 발급받기
    login_response = api_client.post("/api/login/", data, format="json")
    access_token = login_response.data["token"]
    
    # 보호된 API 호출 (유효한 토큰 사용)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "This is a protected API!"

# 보호된 API 테스트 (유효하지 않은 토큰 사용)
def test_protected_api_with_invalid_token(create_user, api_client):
    url = "/api/protected/"  # 보호된 API URL
    invalid_token = "invalid.token.here"
    
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {invalid_token}')
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "detail" in response.data  # 인증 오류 발생 확인
