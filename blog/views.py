from django.shortcuts import render_to_response,redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render_to_response('index.html',locals())
def showpost(request,slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render_to_response('post.html',locals())
    except:
        return redirect('/')