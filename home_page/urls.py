from django.urls import path
from home_page.views import home, post_question, post_video, post_blog, SignUp, LoginUser, blog_post, comment_display
from django.contrib.auth import views

app_name = 'home_page'

urlpatterns = [
    
    path('',home, name = 'home'),
    path('post/question/',post_question, name = "post_question"),
    path('post/video/',post_video, name = "post_video"),
    path('post/blog/',post_blog, name='post_blog'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('blog/<int:blog_id>',blog_post, name="blog_post"),
    path('comment/',comment_display, name="comment_display")

]
   


