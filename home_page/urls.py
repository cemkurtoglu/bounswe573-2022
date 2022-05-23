from django.urls import path
from home_page.views import blog_post
from home_page.views import home, post_question, post_video, post_blog, test_authentication_page

app_name = 'home_page'

urlpatterns = [
    
    path('',home, name = 'home'),
    path('post/question/',post_question, name = "post_question"),
    path('post/video/',post_video, name = "post_video"),
    path('post/blog/',post_blog, name='post_blog'),
    path('authentication/',test_authentication_page, name='test_authentication_page'),
    path('blog/<int:blog_id>',blog_post, name="blog_post") ## look at it

]