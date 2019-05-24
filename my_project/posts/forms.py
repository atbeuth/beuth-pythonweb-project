from django import forms
from.models import Post
from django.db import models

class PostForm(forms.ModelForm):
    image_url = models.ImageField(upload_to ='media/')
    class Meta:
        model = Post
        fields = ('image_url',
                  'content',
                  'tags',)