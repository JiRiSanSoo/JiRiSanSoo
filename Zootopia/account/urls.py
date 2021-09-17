from django.urls import path, include
from . import views

urlpatterns = [
  path('login/', views.login, name="login"),
  path('create_account/', views.create_account, name="create_account"),
  path('profile/', views.profile, name="profile"),
   path('logout/', views.logout, name="logout"),
]
