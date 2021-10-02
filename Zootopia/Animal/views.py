from typing import Container
from django.shortcuts import render, redirect, get_object_or_404
from animal.models import Post
from django.contrib.auth import get_user_model
from .models import *
from account.models import User
from django.utils import timezone

def main (request):
  posts = Post.objects.all()
  return render (request, 'main.html', {"posts":posts})  

def detail(request, id):
  post = get_object_or_404(Post, pk = id)
  person = get_object_or_404(get_user_model(), username=request.user)

  comments = Comment.objects.filter(post = id)
  if request.method == "POST":
            comment = Comment()
            comment.user = get_object_or_404(get_user_model(), username=request.user)
            comment.post = post
            comment.body = request.POST.get('body')
            comment.date = timezone.datetime.now()
            comment.save()

  if post.likes.filter(id=request.user.id):
        message="취소"
  else:
        message="좋아요"

  return render(request, 'detail.html', {'post' :post,'comments' : comments, 'person':person, 'message' : message})

def upload (request):
   if request.method == "POST":  
      post_blog = Post()
      post_blog.name= request.POST.get('name')
      post_blog.time = timezone.datetime.now() 
      post_blog.image = request.FILES.get('image')
      post_blog.body = request.POST.get('body')
      post_blog.hash_tag = request.POST.get('hashtag')
      post_blog.species = request.POST.get('species')
      post_blog.variety = request.POST.get('variety')
      user_id = request.user.id
      user = User.objects.get(id = user_id)
      post_blog.author = user
      post_blog.save()
      return redirect('location', post_blog.id)
   else:
      return render (request, 'upload.html')  

# 검색 페이지 최근글 load
def search (request):
  # 최근 글이 5개 이하일 경우
  if Post.objects.count()<5:
    posts = Post.objects.all()[::-1]
  # 최근 글이 5개 이상일 경우
  else:     
    posts = Post.objects.all()[Post.objects.count()-5::-1]
  return render (request, 'search.html', {"posts":posts})

def result(request):
  search_word = request.GET['search']
  # 검색어를 포함하는 이름이 5개 이하일 경우
  if Post.objects.filter(name__contains=search_word).count()<5:
    names = Post.objects.filter(name__contains=search_word)
  # 검색어를 포함하는 이름이 5개 이상일 경우
  else:
    names = Post.objects.filter(name__contains=search_word)[Post.objects.filter(name__contains=search_word).count()-5::1]
  
  # 검색어를 포함하는 주소가 5개 이하일 경우
  if Post.objects.filter(address__contains=search_word).count()<5:
    addresses = Post.objects.filter(address__contains=search_word)
  # 검색어를 포함하는 주소가 5개 이상일 경우
  else:
    addresses = Post.objects.filter(address__contains=search_word)[Post.objects.filter(address__contains=search_word).count()-5::1]

  # 검색어를 포함하는 동물종이 5개 이하일 경우
  if Post.objects.filter(species__contains=search_word).count()<5:
    species = Post.objects.filter(species__contains=search_word)
  # 검색어를 포함하는 동물종이 5개 이상일 경우
  else:
    species = Post.objects.filter(species__contains=search_word)[Post.objects.filter(species__contains=search_word).count()-5::1]

  # 검색어를 포함하는 작성자가 5개 이하일 경우
  if Post.objects.filter(author__nickname__contains=search_word).count()<5:
    authors = Post.objects.filter(author__nickname__contains=search_word)
  # 검색어를 포함하는 작성자 5개 이상일 경우
  else:
    authors = Post.objects.filter(author__nickname__contains=search_word)[Post.objects.filter(author__nickname__contains=search_word).count()-5::1]

  # 검색어를 포함하는 해시태그가 5개 이하일 경우
  if Post.objects.filter(hash_tag__contains=search_word).count()<5:
    hashTags = Post.objects.filter(hash_tag__contains=search_word)
  # 검색어를 포함하는 해시태그가 5개 이상일 경우
  else:
    hashTags = Post.objects.filter(hash_tag__contains=search_word)[Post.objects.filter(hash_tag__contains=search_word).count()-5::1]

  return render (request, 'result.html', {'names':names, 'species':species, 'addresses':addresses, 'authors':authors, 'hashTags':hashTags})

def profile(request):
  return render(request,'profile.html')

def location(request, id):
  post = get_object_or_404(Post, pk = id)
  person = get_object_or_404(get_user_model(), username=request.user)
  if request.method == "POST":
    post.address = request.POST.get("address")
    post.latitude = request.POST.get("latitude")
    post.longitude = request.POST.get("longitude")
    post.save()
    return redirect('detail', post.id)
  return render(request, 'location.html', {'post' : post, 'person': person})


def delete(request, id):
    delete_blog = Post.objects.get(id=id)
    delete_blog.delete()
    return redirect('main') 

def edit(request, id):
    post_blog = Post.objects.get(id=id)

    if request.method == "POST":
      post_blog.name= request.POST.get('name')
      post_blog.time = timezone.datetime.now() 
      post_blog.body = request.POST.get('body')
      post_blog.hash_tag = request.POST.get('hashtag')
      post_blog.species = request.POST.get('species')
      post_blog.variety = request.POST.get('variety')
      picture = request.FILES.get('image')
      if picture :
        post_blog.image = picture
      post_blog.save()
      return redirect('detail', post_blog.id)
    else:        
      return render(request, 'edit.html', {'post':post_blog})

def post_like(request, id):
    post = get_object_or_404(Post, pk=id)
    user = request.user

    if post.likes.filter(id=user.id):
        post.likes.remove(user)
    else: 
        post.likes.add(user)

    return redirect('/animal/detail/'+str(id))
