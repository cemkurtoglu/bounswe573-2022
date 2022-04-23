from django import forms
from user_profile_page_settings.models import User
from home_page.models import PostLikes, PostDislikes

class ProfileImage(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profileImage']

class LikeAPost(forms.ModelForm):
    class Meta:
        model = PostLikes
        fields = '__all__'
        
class DisLikeAPost(forms.ModelForm):
    class Meta:
        model = PostDislikes
        fields = '__all__'
