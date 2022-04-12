from django.urls import path
from user_profile_page_main.views import profile_page

app_name = 'user_profile_page_main'

urlpatterns = [
    
    path('',profile_page, name = 'profile_page')

]