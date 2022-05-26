from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http.response import JsonResponse
from home_page.models import Post
from user_profile_page_settings.models import User
from .models import SocialSpace, SocialPost
from .forms import SocialSpaceForm, SocialPostForm


def social_space(request, space_id):
    # user = User.objects.get(id=1)
    user_social_space = SocialSpace.objects.get(id=space_id, users__id=request.user.id)
    users_posts = Post.objects.filter(author__in=user_social_space.users.all())
    # print("-------->", users_posts)
    context = {
        'user': request.user,
        'social_space': user_social_space,
        'users_posts': users_posts
    }
    return render(request, 'social_space/social_space_main.html', context)


def social_space_topics(request, space_id, type):
    # user = User.objects.get(id=1)
    social_space_posts = SocialPost.objects.filter(social_space=space_id, post_type=type)
    post_form = SocialPostForm(request.POST or None)

    if request.method == 'POST':

        if post_form.is_valid():
            post_form.save()
            return redirect('social_space:social_space_topics', space_id=space_id, type=type)
        else:
            context = {
                'post_form': post_form,
                'user': request.user,
                'social_space_posts': social_space_posts,
                'social_space_id': space_id,
                'topic_type': type
            }
            return render(request, 'social_space/social_space_topics.html', context)
    else:
        context = {
            'post_form': post_form,
            'user': request.user,
            'social_space_posts': social_space_posts,
            'social_space_id': space_id,
            'topic_type': type
        }
        return render(request, 'social_space/social_space_topics.html', context)


def create_social_space(request):
    form = SocialSpaceForm(request.POST, request.FILES)
    if not request.method == 'POST':
        return JsonResponse({"status": "error"})
    if form.is_valid():
        space_id = form.save(id=request.user.id)
        context = {
            "status": "success",
            "space_id": space_id.id
        }
        return JsonResponse(context)
    else:
        return JsonResponse({"status": "error"})


def join_social_space(request):
    if not request.method == 'POST':
        return JsonResponse({"status": "error"})
    try:
        # user = User.objects.get(id=1)
        social_spaces = request.POST.get('social_spaces')
        for spaceId in social_spaces.split(','):
            instance = SocialSpace.objects.get(id=spaceId)
            instance.users.add(request.user)
        return JsonResponse({"status": "success"})
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error",
                             "message": str(e)
                             })