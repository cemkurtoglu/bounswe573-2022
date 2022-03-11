from django.shortcuts import render
from .models import User

def home(request):
    users = User.objects.all()
    return render(request,'main_app/home.html',{'users':users})