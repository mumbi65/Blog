from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path("my-posts/", views.myPosts, name="my-posts"),
    path("user/<int:user_id>/posts/", views.userPosts, name="user-posts"),
    path("about/", views.about, name='blog-about'),
    path("contactUs/", views.contactUs, name='blog-contactUs'),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.CreatePostView.as_view(), name="post-create"),
    path("post/update/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/delete/<int:pk>/", views.PostDeleteView.as_view(), name="post-delete")
]