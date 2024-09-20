from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponseRedirect
from .forms import ProfileForm


@login_required
def profile_view(request):
    profile = request.user.profile
    posts = Post.objects.filter(user=request.user)
    return render(request, 'profiles/myprofile.html', {'profile': profile,
                                                                           'posts': posts})


@login_required
def pk_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(user=user)
    context = {'posts': posts, 'user': user}
    return render(request, 'profiles/pkprofile.html', context)


def update_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile.first_name = request.POST.get('first_name')
            profile.last_name = request.POST.get('last_name')
            profile.bio = request.POST.get('bio')
            profile.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = ProfileForm()
    return render(request, 'profiles/update.html', {"form": form})
