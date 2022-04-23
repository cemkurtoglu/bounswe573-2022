from django.http import HttpResponse
from django.shortcuts import render
from home_page.models import PostLikes
from user_profile_page_settings.models import User
from home_page.models import PostLikes, PostDislikes
from user_profile_page_main.forms import LikeAPost,DisLikeAPost
from django.template.defaulttags import register



# Create your views here.
def profile_page(request):

    user = User.objects.get(id=1)
    posts = user.post_set.all()
    likes = PostLikes.objects.all()
    disLikes = PostDislikes.objects.all()
    engagements = LikesAndDislikes.total_likes_and_dislikes(posts, likes, disLikes)

    context = {'user':user, 'posts':posts, 'likes':likes, 'disLikes':disLikes, 'engagements':engagements}
    return render(request,'user_profile_page_main/profile_page_main.html',context)

def post_like(request):
    postLikes = LikesAndDislikes(request)
    postLikes.like_post()
    return HttpResponse("Success")

def post_dislike(request):
    postDislike = LikesAndDislikes(request)
    postDislike.dislike_post()
    return HttpResponse("Success")

      

class LikesAndDislikes:


    def __init__(self, request):
        self.like_id_to_be_deleted = 0
        self.post_id_to_be_processed = 0
        self.request = request
        

    def total_likes_and_dislikes(posts, likes, dislikes):
        numLikes = 0
        numDislikes = 0
        engagements = {}

        for post in posts:
            for like in likes:
                # print(str(post.id))
                # print(str(like.postId.id))
                if post.id == like.postId.id:
                    numLikes += 1
            for dislike in dislikes:
                if post.id == dislike.postId.id:
                    numDislikes += 1
            engagements[post.id] = (numLikes,numDislikes)
            numLikes = 0
            numDislikes = 0

        # print(engagements)
        return engagements    
    
    def like_post(self):
        self.like_or_dislike(PostLikes, LikeAPost)
    
    def dislike_post(self):
        self.like_or_dislike(PostDislikes, DisLikeAPost)
    
    def like_or_dislike(self, classModel, formModel):
        
        form = formModel(self.request.POST)
        if self.request.method == "POST":
            
            form = formModel(self.request.POST)
            # print(form)
            if form.is_valid():
            
                if not self.like_or_dislike_exists(form, classModel):
                    form.save(commit=True)
                else:
                    print(str(self.like_id_to_be_deleted))
                    object = self.get_or_none(classModel, id=self.like_id_to_be_deleted)
                    if(object != None):
                        object.delete()

            else:
                print(form.errors)


    def like_or_dislike_exists(self, form, classModel):
        
        likes = classModel.objects.all()
        
        if len(likes) <= 0:
            return False
        else:
            for like in likes:

                if form.cleaned_data['userId'] == like.userId and form.cleaned_data['postId'] == like.postId:
                    self.like_id_to_be_deleted = like.id
                    self.post_id_to_be_processed = like.postId
                    return True
                else:
                    return False


    def get_or_none(self, classmodel, **kwargs):
        try:
            return classmodel.objects.get(**kwargs)
        except classmodel.DoesNotExist:
            return None

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)