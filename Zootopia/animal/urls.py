
from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.main, name="main"),
    path('search/', views.search, name="search"),
    path('result/', views.result, name="result"),
    path('main/', views.main, name="main"),
    path('upload/', views.upload, name="upload"),
    path('detail/', views.detail, name="detail"),
    path('profile/',views.profile, name="profile")
]
