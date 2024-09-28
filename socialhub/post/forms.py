from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class PostFormCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text']

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)



