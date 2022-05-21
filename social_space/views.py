from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http.response import JsonResponse
from home_page.models import Post
from user_profile_page_settings.models import User
from .models import SocialSpace
from .forms import SocialSpaceForm, SocialPostForm


def social_space(request, space_id):
    user = User.objects.get(id=1)
    user_social_space = SocialSpace.objects.get(id=space_id, users__id=1)
    users_posts = Post.objects.filter(author__in=user_social_space.users.all())
    # print("-------->", users_posts)
    context = {
        'user': user,
        'social_space': user_social_space,
        'users_posts': users_posts
    }
    return render(request, 'social_space/social_space_main.html', context)


def social_space_topics(request, space_id):
    user = User.objects.get(id=1)
    user_social_space = SocialSpace.objects.get(id=space_id, users__id=1)
    post_form = SocialPostForm(request.POST or None)

    if request.method == 'POST':

        if post_form.is_valid():
            post_form.save()
            return redirect('social_space:social_space_topics', space_id=space_id)
        else:
            context = {
                'post_form': post_form,
                'user': user,
                'social_space': user_social_space,
            }
            return render(request, 'social_space/social_space_topics.html', context)
    else:
        context = {
            'post_form': post_form,
            'user': user,
            'social_space': user_social_space,
        }
        return render(request, 'social_space/social_space_topics.html', context)


def create_social_space(request):
    form = SocialSpaceForm(request.POST, request.FILES)
    if not request.method == 'POST':
        return JsonResponse({"status": "error"})
    if form.is_valid():
        space_id = form.save()
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
        user = User.objects.get(id=1)
        social_spaces = request.POST.get('social_spaces')
        for spaceId in social_spaces.split(','):
            instance = SocialSpace.objects.get(id=spaceId)
            instance.users.add(user)
        return JsonResponse({"status": "success"})
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error",
                             "message": str(e)
                             })

