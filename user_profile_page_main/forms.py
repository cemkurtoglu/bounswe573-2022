from django import forms
from user_profile_page_settings.models import User

class ProfileImage(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profileImage']

