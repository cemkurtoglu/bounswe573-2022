from multiprocessing import context
from django.shortcuts import render
from .models import User

def home(request):
    user = User.objects.get(id=1)
    context = {'user':user}
    return render(request,'home_page/home.html',context)