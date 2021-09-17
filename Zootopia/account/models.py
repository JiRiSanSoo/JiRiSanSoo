from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser) :
    nickname = models.CharField(max_length=30, blank=True, null=True)     # 유저 닉네임 모델
    profile_picture = models.ImageField(upload_to='account/', blank=True, null=True)   # 유저 프로필 사진 모델
    introduce = models.TextField(max_length = 100, blank=True, null=True)  # 유저 자기소개 모델