from django import forms
from user_profile_page_settings.models import User

class ProfileInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileInformationForm_Image(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profileImage","backgroundImage"]