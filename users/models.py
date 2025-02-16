from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True) # 고유성 추가가

    class Meta:
        unique_together = ('username', 'nickname')
