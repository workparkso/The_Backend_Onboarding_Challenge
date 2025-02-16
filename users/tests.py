import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_signup(api_client):
    """회원가입 가능여부 테스트용(과제로 주어진 조건이자, 회원가입이 잘 되는지 확인하는 용도)"""
    data = {
        "username": "JIN HO",
        "password": "12341234",
        "nickname": "Mentos"
    }

    response = api_client.post("/users/signup", data)
    
    assert response.status_code == 201
    assert response.data["username"] == "JIN HO"
    assert response.data["nickname"] == "Mentos"
    assert response.data["roles"] == [{"role": "USER"}]

@pytest.mark.django_db
def test_login(api_client):
    """로그인 가능여부 테스트용(과제로 주어진 조건이자, 로그인이 잘 되는지 확인하는 용도)"""
    user = User.objects.create_user(username="JIN HO", password="12341234", nickname="Mentos")
    
    data = {
        "username": "JIN HO",
        "password": "12341234"
    }
    
    response = api_client.post("/users/login", data)
    
    assert response.status_code == 200
    assert "token" in response.data

# 고유성을 가지고 추가 테스트(1)!

@pytest.mark.django_db
def test_unique_username(api_client):
    """username이 고유한지 테스트"""
    User.objects.create_user(username="JIN HO", password="12341234", nickname="Mentos")
    
    data = {
        "username": "JIN HO",
        "password": "56785678",
        "nickname": "AnotherNickname"
    }
    
    response = api_client.post("/users/signup", data)
    
    assert response.status_code == 400
    assert "username" in response.data

@pytest.mark.django_db
def test_unique_nickname(api_client):
    """nickname이 고유한지 테스트"""
    User.objects.create_user(username="AnotherUser", password="12341234", nickname="Mentos")
    
    data = {
        "username": "NewUser",
        "password": "56785678",
        "nickname": "Mentos"
    }
    
    response = api_client.post("/users/signup", data)
    
    assert response.status_code == 400
    assert "nickname" in response.data

# 비밀번호 유효성을 따지는 추가 테스트(2)!
# 크게 중요한 파트는 아님
@pytest.mark.django_db
def test_password_too_short(api_client):
    """비밀번호가 너무 짧은 경우 테스트"""
    data = {
        "username": "JIN HO",
        "password": "123",
        "nickname": "Mentos"
    }
    
    response = api_client.post("/users/signup", data)
    
    assert response.status_code == 400
    assert "password" in response.data

@pytest.mark.django_db
def test_password_too_simple(api_client):
    """비밀번호가 너무 단순한 경우 테스트"""
    data = {
        "username": "JIN HO",
        "password": "password",
        "nickname": "Mentos"
    }
    
    response = api_client.post("/users/signup", data)
    
    assert response.status_code == 400
    assert "password" in response.data
