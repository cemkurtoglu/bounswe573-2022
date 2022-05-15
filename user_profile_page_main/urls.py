from django.urls import path
from user_profile_page_main.views import profile_page, post_like, post_dislike, post_reaction, user
from user_profile_page_main import views

app_name = 'user_profile_page_main'

urlpatterns = [
    
    path('',profile_page, name = 'profile_page'),
    path('post-reaction/', post_reaction, name="post_reaction"),
    path('postLike/',post_like, name="post_like"),
    path('postDislike/', post_dislike, name="post_dislike"),
    path('user/',user, name='user'),
    path("followToggle/<int:profileUserId>/", views.followToggle, name="followToggle")

]