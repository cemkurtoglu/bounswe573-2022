from django.urls import path
from user_profile_page_main.views import profile_page, post_like, post_dislike

app_name = 'user_profile_page_main'

urlpatterns = [
    
    path('',profile_page, name = 'profile_page'),
    path('postLike/',post_like, name="post_like"),
    path('postDislike/', post_dislike, name="post_dislike")

]