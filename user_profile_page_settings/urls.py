from django.urls import path
from user_profile_page_settings.views import account_dashboard, upload_photo

app_name = 'user_profile_page_settings'

urlpatterns = [
    
    path('',account_dashboard, name = 'settings'),
    path('image_upload/', upload_photo, name='upload_photo')


]