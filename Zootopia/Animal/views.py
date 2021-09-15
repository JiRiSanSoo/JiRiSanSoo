from django.shortcuts import render
from animal.models import Post
from .models import *

def main (request):
  return render (request, 'main.html')  

def detail (request):
  return render (request, 'detail.html')  

def upload (request):
  return render (request, 'upload.html')  

def search (request):
  posts = Post.objects.all()[Post.objects.count()-5::-1]
  return render (request, 'search.html', {"posts":posts})

def result(request):
  posts = Post.objects.all()[Post.objects.count()-5::-1]
  return render (request, 'result.html', {"posts":posts})

def profile(request):
  return render(request,'profile.html')