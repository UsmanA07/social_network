from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class PostFormCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text']


class CommentFormCreate(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['id', 'text']
