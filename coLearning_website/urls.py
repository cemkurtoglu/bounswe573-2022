"""simple_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home_page.views import social_space, social_space_topics, blog_post
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('profile_settings/',include('user_profile_page_settings.urls')), # profile_settings/<str:pk>/
    path('profile/', include('user_profile_page_main.urls')),
    path('social_space/',social_space, name='social_space'),
    path('social_space/topics/',social_space_topics, name="social_space/topics/"),
    path('blog_post/',blog_post)
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
