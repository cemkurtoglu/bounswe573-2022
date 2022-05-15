from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from home_page.models import PostLikes, Post, PostDislikes
from user_profile_page_settings.models import User
from user_profile_page_main.forms import LikeAPost,DisLikeAPost
from django.template.defaulttags import register


# Create your views here.
def profile_page(request):

    user = User.objects.get(id=1)
    posts = user.post_set.all()

    context = {'user':user, 'posts':posts }
    return render(request,'user_profile_page_main/profile_page_main.html',context)


def user(request):
    # set profileUserId as parameter for actual user login case
    # for now lets assume public profile user have id 2
    user = User.objects.get(id=1)
    profileUser = User.objects.get(id=2)
    posts = user.post_set.all()

    context = {'user':user, 'posts':posts, 'profileUser': profileUser}
    return render(request,'user_profile_page_main/profile_page_user.html',context)


def followToggle(request, profileUserId):
    prifileUser = User.objects.get(id=profileUserId)
    currentUserObj = User.objects.get(id=1)
    following = prifileUser.following.all()

    if profileUserId != currentUserObj.id:
        if currentUserObj in following:
            prifileUser.following.remove(currentUserObj.id)
        else:
            prifileUser.following.add(currentUserObj.id)

    return HttpResponseRedirect("/profile/user/")


def post_reaction(request):
    if request.method == "POST":
        dummy_user = User.objects.get(id=1)
        post_id = request.POST.get('post_id', None)
        opinion = request.POST.get('opinion', None)  # like or dislike button clicked

        post = get_object_or_404(Post, id=post_id)

        try:
            # If child DisLike model doesn't exit then create
            post.dis_likes
        except Post.dis_likes.RelatedObjectDoesNotExist as identifier:
            PostDislikes.objects.create(postId=post)

        try:
            # If child Like model doesnot exit then create
            post.likes
        except Post.likes.RelatedObjectDoesNotExist as identifier:
            PostLikes.objects.create(postId=post)

        if opinion.lower() == 'like':

            if dummy_user in post.likes.userId.all(): # use request.user for real user
                post.likes.userId.remove(dummy_user)
            else:
                post.likes.userId.add(dummy_user)
                post.dis_likes.userId.remove(dummy_user)

        elif opinion.lower() == 'dis_like':

            if dummy_user in post.dis_likes.userId.all():
                post.dis_likes.userId.remove(dummy_user)
            else:
                post.dis_likes.userId.add(dummy_user)
                post.likes.userId.remove(dummy_user)
        else:
            return JsonResponse({"error": "invalid choice"})
        return JsonResponse({
            "success": True,
            "like_count": post.get_total_likes(),
            "dislike_count": post.get_total_dis_likes()
        })
    else:
        return JsonResponse({"error": "invalid request"})


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
                    print(self.post_id_to_be_processed)
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

