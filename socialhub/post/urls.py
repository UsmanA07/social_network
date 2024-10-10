from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('create-comment/<int:pk>', views.comment_create, name='comment_create'),
    path('detail/<int:pk>', views.post_detail, name='post_detail'),
    path('delete/<int:pk>', views.post_delete, name='post_delete'),
    path('update/<int:pk>', views.post_update, name='post_update'),
    path('comment_like/', views.comment_like, name='comment_like'),
    path('like/', views.post_like, name='like'),

]
