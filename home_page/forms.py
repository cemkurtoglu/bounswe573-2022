from django import forms
from user_profile_page_settings.models import User
from home_page.models import Post,Tags

class QuestionPost(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Post
        fields = ['type', 'author', 'content', 'tag', 'video']

# class VideoPost(forms.ModelForm):

#     content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

#     class Meta:
#         model = Post
#         fields = ['type', 'author', 'content', 'tag', 'video']

    
 