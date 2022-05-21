from django.db import models
from user_profile_page_settings.models import User

post_type_choices = (
    ("general", "General"),
    ("community", "Community"),
    ("collaborative", "Collaborative"),
)


# Create your models here.
class SocialSpace(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name="social_spaces")
    description = models.CharField(max_length=280, blank=True, null=True)
    icon = models.ImageField(null=True, blank=True, upload_to='social_space/icons/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class SocialPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    social_space = models.ForeignKey(SocialSpace, on_delete=models.CASCADE)

    content = models.CharField(max_length=280)
    post_type = models.CharField(max_length=100, choices=post_type_choices, default="general")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.content
