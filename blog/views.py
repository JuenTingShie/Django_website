from django.shortcuts import HttpResponse,render_to_response,redirect
from django.utils import timezone
from django.template import RequestContext

from .models import Post,Comment

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render_to_response('index.html',locals())
def Showpost(request,slug):
    post = Post.objects.get(slug=slug)
    return render_to_response('post.html',locals())
    
    if slug:
        post=Post.objects.get(slug=slug)
    if request.POST:
        Comment.objects.create(
            poster=request.POST['poster'],
            context=request.POST['comment'],
            post_time=timezone.localtime(timezone=now),
            which_post=slug
        )
        Comment.save()
    return render_to_response('post.html',locals())



#    po=request.GET['poster']
#    co=request.GET['comment']
#    Comment.objects.create(
#        poster=po,
#        context=co,
#        post_time=datetime.datetime.now()
#    )
#    return render_to_response('post.html',locals())
    