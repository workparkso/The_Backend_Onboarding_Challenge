from django.contrib.auth import get_user_model, authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import SignupSerializer

# JWT 관련 기능 추가
User = get_user_model()

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
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

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """로그인 API"""
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({"token": str(refresh.access_token)}, status=200)
        
        return Response({"error": "Invalid credentials"}, status=400)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """JWT 인증이 필요한 API"""
        return Response({"message": "This is a protected API!"})

class CustomTokenRefreshView(TokenRefreshView):
    pass
