from django.shortcuts import render_to_response
from django.shortcuts import redirect

from blog.models import Post

def ShowIndex(request):
    posts = Post.objects.all().order_by('-publish_time')
    return render_to_response('Index.html',locals())
def ShowPost(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        return render_to_response('Post.html',locals())
    except:
        return redirect('/404')