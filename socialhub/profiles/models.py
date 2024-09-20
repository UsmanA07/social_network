from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    bio = models.TextField(default='no bio.', blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-created']

