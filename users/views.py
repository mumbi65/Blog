from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"Registration successful for account {username}")
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

def login(request):
    return render(request, "users/login.html")


def logout_user(request):
    logout(request)
    return render(request, "users/logout.html")

@login_required
def userProfile(request):
    if request.method == "POST":
       p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
       u_form = UserUpdateForm(request.POST, instance=request.user)
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, "Update successful")
           return redirect("users-profile")
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        context = {
            "p_form": p_form,
            "u_form": u_form
        }
    return render(request, "users/profile.html", context)