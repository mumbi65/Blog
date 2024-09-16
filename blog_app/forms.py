from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    def save(self, commit=True, user=None):
        post = super().save(commit=False)
        if user:
            post.author = user
        if commit:
            post.save()
        return post

