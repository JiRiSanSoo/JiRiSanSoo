from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.deletion import CASCADE


class Post(models.Model):
  
  # 동물 이름
  name = models.CharField(max_length=20, default="이름없음")
  # 동물 종
  species = models.CharField(max_length=20, null=True)
  # 동물 품종
  variety = models.CharField(max_length=20, null=True)
  # 내용
  body = models.TextField(max_length=100)
  # 해쉬태그
  hash_tag = models.CharField(max_length=30, null=True)
  # 사진
  image = models.ImageField(upload_to='post/', blank=True, null=True)
  # 작성자
  author = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True)
  # 작성 시간
  time =  models.DateTimeField(auto_now_add=True)
  # 위도
  latitude = models.FloatField(default=0.0) 
  # 경도
  longitude = models.FloatField(default=0.0)
  # 주소
  address = models.CharField(max_length=20, default="위치")
  # 좋아요
  likes = models.ManyToManyField('account.User', through='Like', through_fields=('post', 'user'), related_name='likes')    

  def __str__(self):
    return self.name

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True) 
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=200)
    date = models.DateTimeField('data published', default=0)