from django.db import models
from django.utils import timezone

class Post(models.Model):
  # 동물 이름
  name = models.CharField(max_length=20)
  # 동물 종
  species = models.CharField(max_length=20)
  # 내용
  body = models.TextField(max_length=100)
  # 해쉬태그
  hash_tag = models.CharField(max_length=30)
  # 사진
  image = models.ImageField(upload_to='post/', blank=True, null=True)
  # 작성자
  time =  models.DateTimeField(auto_now_add=True)
  # 작성 시간
  latitude = models.FloatField(default=0.0) 
  #위도
  longitude = models.FloatField(default=0.0) 
  #경도

  def __str__(self):
    return self.name

