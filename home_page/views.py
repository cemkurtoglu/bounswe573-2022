from django.http import HttpResponse 
from django.shortcuts import render
from .models import User, Post
from social_space.models import SocialSpace
from home_page.forms import PostForm, BlogPostForm
from home_page.models import Tags
from django.views.decorators.csrf import csrf_exempt
import os


def home(request):
    user = User.objects.get(id=1)
    tags = Tags.objects.all()
    postForm = PostForm(request.POST or None,instance=user)
    postBlog = BlogPostForm(request.POST or None,instance=user)
    social_spaces = SocialSpace.objects.all()
    user_spaces = SocialSpace.objects.filter(users__id=user.id)
    post_list = Post.objects.all()

    # videoPost = QuestionPost(request.POST or None,instance=user)
    context = {
        'user': user,
        'postForm': postForm,
        'tags': tags,
        'postBlog': postBlog,
        'social_spaces': social_spaces,
        'post_list': post_list,
        'user_spaces': user_spaces
    }
    return render(request, 'home_page/home.html', context)


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

@csrf_exempt
def post_video(request):

    if request.method == "POST":
        print("\n-------------------\n")
        postForm = PostForm(request.POST, request.FILES)
        if postForm.is_valid():
            postForm.save(commit=True)
            print("Printing post: " , request.POST)
            return HttpResponse("Success")
        else:
            print(postForm.errors.as_json)


@csrf_exempt
def post_blog(request):
    postBlog = BlogPostForm(request.POST, request.FILES)
    if request.method == "POST":
        print("\n-------------------\n")
        if postBlog.is_valid():
            postBlog.save(commit=True)
            print("Printing post: " , request.POST)
            return HttpResponse("Success")
        else:
            print(postBlog.errors.as_json)


def blog_post(request):
    user = User.objects.get(id=1)
    context = {'user':user}
    return render(request,'home_page/blog_post.html',context)

#delete later on
def test_authentication_page(request):
    return render(request,'authentication/authentication.html')