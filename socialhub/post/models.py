from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=256, blank=True)
    text = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='like', blank=True)
    like_bool = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['-published'])
        ]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    like = models.ManyToManyField(User, related_name='like_comment', blank=True)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        indexes = [
            models.Index(fields=['-published'])
        ]
