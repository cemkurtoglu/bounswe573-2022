from django import forms
from user_profile_page_settings.models import User

class ProfileInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'birthDate', 'website', 'phoneNumber', 'country', 'state', 'city', 'description', 'gender', 'birthPlace', 'occupation', 'maritialStatus']

class ProfileInformationForm_Image(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profileImage","backgroundImage"]