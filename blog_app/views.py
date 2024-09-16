from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def Home(requests):
    context = {
        'posts': Post.objects.all(),
    }
    return render(requests, "blog_app/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = "blog_app/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 3

class PostDetailView(DetailView):
    model = Post

@login_required
def createPost(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            saved_post = form.save(user=request.user)
            return redirect("post-detail", pk=saved_post.pk)
    else:
        form = PostCreateForm()
    return render(request, "blog_app/create_post.html", {"form": form})

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "excerpt", "content"]
    template_name = "blog_app/create_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', "excerpt", 'content']
    template_name = "blog_app/create_post.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required  
def myPosts(request):
    context = {
        "posts": Post.objects.filter(author = request.user).all(),
        "title": "My"
    }
    return render(request, "blog_app/home.html", context)

def userPosts(request, user_id):
    user_posts = Post.objects.filter(author__id = user_id).all()
    context = {
        "posts": user_posts,
        "title": user_posts[0].author.username
    }
    return render(request, "blog_app/home.html", context)

def about(requests):
    return render(requests, "blog_app/about.html")

def contactUs(requests):
    return render(requests, "blog_app/contact.html")

