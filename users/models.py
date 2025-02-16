from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'nickname'], name='unique_username_nickname')
        ]
