from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer

User = get_user_model()

@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    """회원가입 API"""
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "username": user.username,
            "nickname": user.nickname,
            "roles": user.roles,
        }, status=201)
    return Response(serializer.errors, status=400)

@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    """로그인 API"""
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({"token": str(refresh.access_token)}, status=200)
    
    return Response({"error": "Invalid credentials"}, status=400)
