from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.userProfile, name="users-profile")
]