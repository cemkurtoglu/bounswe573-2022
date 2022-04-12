from user_profile_page_main.views import profile_page
from django.shortcuts import render
from user_profile_page_settings.forms import ProfileInformationForm, ProfileInformationForm_Image
from user_profile_page_settings.models import User

# Create your views here.
def account_dashboard(request):

    user = User.objects.get(id=1)
    usStates = User.states
    genders = User.genderChoice
    maritialStatus = User.maritialStatusChoice 
    form = ProfileInformationForm(instance=user)


    if request.method == "POST":
        form = ProfileInformationForm(request.POST,request.FILES, instance=user)

        if form.is_valid():
            form.save(commit=True)
            print("Printing post: " , request.POST)
            return profile_page(request)
        else:
            print(form.errors)

    context = {'user':user,'states':usStates, 'genders':genders, 'maritialStatus':maritialStatus, 'form':form}

    return render(request,'user_profile_page_settings/account_profile_information.html',context)

def upload_photo(request):

    user = User.objects.get(id=1)
    form =  ProfileInformationForm_Image(request.POST,request.FILES, instance=user)

    if request.method == "POST":
        form = ProfileInformationForm_Image(request.POST,request.FILES, instance=user)

        if form.is_valid():
            form.save(commit=True)
            print("Printing post: " , request.POST)
            return profile_page(request)
        else:
            print(form.errors)

    context = {"form":form,'user':user}

    return render(request, 'user_profile_page_settings/image_uploader.html',context)


