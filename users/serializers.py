from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "password", "nickname", "roles"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def get_roles(self, obj):
        return [{"role": "USER"}]  # 기본 역할을 부여
# roles 필드가 모델에 없으므로, 
# SerializerMethodField를 사용해서 역할(role)을 추가 -> ai 리뷰로 반영