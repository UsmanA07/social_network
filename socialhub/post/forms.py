from django import forms
from .models import Post, Likes


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class PostFormCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text']


class PostLikeForm(forms.Form):
    class Meta:
        model = Likes
        fields = ['like', 'post']
