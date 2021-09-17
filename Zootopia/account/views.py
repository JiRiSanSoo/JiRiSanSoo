from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your views here.

def login (request):
  if request.method =='POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      return render(request, 'login.html')
  else:    
    return render (request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('/')

def create_account (request):
  User = get_user_model()
  if request.method == "POST":
    if request.POST['password1'] == request.POST['password2']:
      user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password1'],
        nickname=request.POST['nickname'],
      )
      auth.login(request, user)
      return redirect('/')
    return render(request, 'create_account.html')
  return render(request, 'create_account.html')

def profile (request):
  return render (request, 'profile.html')