from django import forms

from blog.models import Post,Comment
from gallery.models import Gallery

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title' ,'context' ,'image' )

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('post' ,'poster' ,'context' )

class GalleryForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Gallery
        fields = ('image',)