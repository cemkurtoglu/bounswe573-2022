from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from home_page.forms import QuestionPost
from home_page.models import Tags

def home(request):
    user = User.objects.get(id=1)
    tags = Tags.objects.all()
    questionPost = QuestionPost(request.POST or None,instance=user)
    # videoPost = QuestionPost(request.POST or None,instance=user)
    context = {'user':user,'questionPost':questionPost, 'tags':tags}

    if request.method == "POST":
        print("\n-------------------\n")
        questionPost = QuestionPost(request.POST)
        if questionPost.is_valid():
            questionPost.save(commit=True)
            print("Printing post: " , request.POST)
            questionPost = QuestionPost()
            # return HttpResponse("Success")
        else:
            print(questionPost.errors)


    return render(request,'home_page/home.html',context)

