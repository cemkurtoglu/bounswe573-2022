from django.urls import path
from social_space import views

app_name = 'social_space'

urlpatterns = [
    path('<int:space_id>', views.social_space, name='social_space'),
    path('topics/<int:space_id>', views.social_space_topics, name="social_space_topics"),
    path('create-social-space/', views.create_social_space, name="create_social_space"),
    path('join-social-space/', views.join_social_space, name="join_social_space"),
]
