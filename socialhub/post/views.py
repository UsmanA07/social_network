from django.shortcuts import render, get_object_or_404
from .models import Post
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm, PostFormCreate
from django.http import HttpResponseRedirect, HttpResponse


@login_required
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post/post_list.html', context)


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post.title = request.POST.get('title')
                post.text = request.POST.get('text')
                post.save()
                return HttpResponseRedirect('/post/')
        else:
            form = PostForm()
    else:
        return HttpResponse('Вы не автор этого поста!!')
    return render(request, 'profiles/update.html', {"form": form})


@login_required
def post_detail(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post/detail.html', {'post': post, 'user': user})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        post.delete()
    else:
        return HttpResponse('Вы не автор этого поста!!')
    return HttpResponseRedirect('/post/')
    # return render(request, 'post/delete.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostFormCreate(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect('/post/')
    form = PostFormCreate()
    return render(request, 'post/create.html', {'form': form})


def redirect_to_post(request):
    return HttpResponseRedirect('/post/')
