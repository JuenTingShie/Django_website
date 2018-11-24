from django import forms
from django.db import models
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title' ,'context' )

class Comment(forms.ModelForm):
    

    class Meta:
        model = Comment
        fields = ('post' ,'poster' ,'context' )