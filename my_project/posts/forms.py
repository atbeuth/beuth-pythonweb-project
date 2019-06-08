from django import forms
from.models import Post
from django.db import models

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image_url', 'content', 'tags']