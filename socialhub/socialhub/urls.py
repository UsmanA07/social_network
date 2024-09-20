from django.contrib import admin
from django.urls import path, include
from post import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('profile/', include('profiles.urls', namespace='prof')),
    path('post/', include('post.urls', namespace='post')),
    path('', views.redirect_to_post)
]
