from multiprocessing import context
from django.shortcuts import render
# from .models import User

def home(request):
    # users = User.objects.all()
    # context = {'users':users}
    return render(request,'home_page/home.html')