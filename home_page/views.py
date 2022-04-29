from django.http import HttpResponse 
from django.shortcuts import render
from .models import User
from home_page.forms import PostForm, BlogPostForm
from home_page.models import Tags
import os

def home(request):
    user = User.objects.get(id=1)
    tags = Tags.objects.all()
    postForm = PostForm(request.POST or None,instance=user)
    postBlog = BlogPostForm(request.POST or None,instance=user)

    # videoPost = QuestionPost(request.POST or None,instance=user)
    context = {'user':user,'postForm':postForm, 'tags':tags, 'postBlog':postBlog}

    


    return render(request,'home_page/home.html',context)

def post_question(request):
    
    user = User.objects.get(id=1)
    postForm = PostForm(request.POST or None,instance=user)


    if request.method == "POST":
        print("\n-------------------\n")
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            postForm.save(commit=True)
            print("Printing post: " , request.POST)
            postForm = PostForm()
            return HttpResponse("Success")
        else:
            print(postForm.errors)

def post_video(request):
    
    user = User.objects.get(id=1)
    postForm = PostForm(request.POST or None,instance=user)


    if request.method == "POST":
        print("\n-------------------\n")
        postForm = PostForm(request.POST, request.FILES)
        if postForm.is_valid():
            postForm.save(commit=True)
            print("Printing post: " , request.POST)
            postForm = PostForm()
            return HttpResponse("Success")
        else:
            print(postForm.errors.as_json)

def post_blog(request):
    user = User.objects.get(id=1)
    postBlog = BlogPostForm(request.POST, request.FILES, instance=user)
    if request.method == "POST":
        print("\n-------------------\n")
        if postBlog.is_valid():
            postBlog.save(commit=True)
            print("Printing post: " , request.POST)
            return HttpResponse("Success")
        else:
            print(postBlog.errors.as_json)
        

