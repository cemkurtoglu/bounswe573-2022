from django import forms
from .models import *


class SocialSpaceForm(forms.ModelForm):
    users = forms.CharField(max_length=100)

    class Meta:
        model = SocialSpace
        fields = ['name', 'icon']

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        print(args)
        print(kwargs)
        owner = User.objects.get(id=kwargs.get("id"))

        def save_m_to_m():
            user_str = self.cleaned_data.get('users')
            instance.users.add(owner)
            for userid in user_str.split(','):
                user = User.objects.get(id=userid)
                instance.users.add(user)

        instance.save()
        save_m_to_m()

        return instance


class SocialPostForm(forms.ModelForm):
    class Meta:
        model = SocialPost
        fields = '__all__'