from django import forms
from user_profile_page_settings.models import User
from home_page.models import Post,Tags

class PostForm(forms.ModelForm):
    
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Post
        fields = ['type', 'author', 'content', 'tag', 'video']


class BlogPostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['blogContent','title','blogImage','tag','type','author']
        # type = forms.CharField(initial={'value':"Blog"})


    tag = forms.ModelChoiceField(queryset=Tags.objects.all(),to_field_name="id")
    blogContent = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','size':30}))
    title = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))

   