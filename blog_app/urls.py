from . import views
from django.urls import path

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='home'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
]

