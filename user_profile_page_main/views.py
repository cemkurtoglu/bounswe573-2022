from django.shortcuts import render
from user_profile_page_settings.models import User

# Create your views here.
def profile_page(request):

    user = User.objects.get(id=1)

    context = {'user':user}

    return render(request,'user_profile_page_main/profile_page_main.html',context)



