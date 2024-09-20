from django.urls import path
from . import views

app_name = 'prof'

urlpatterns = [
    path('', views.profile_view, name='myprofile'),
    path('<int:pk>/', views.pk_profile, name='pk_profile'),
    path('update/<int:pk>/', views.update_profile, name='update_profile'),
]
