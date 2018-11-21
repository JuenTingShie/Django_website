from django.shortcuts import render_to_response,render
from django.shortcuts import redirect
from django.utils import timezone

from blog.models import Post,Comment

def ShowIndex(request):
    posts = Post.objects.all().order_by('-publish_time')
    return render_to_response('Index.html',locals())
def ShowPost(request,slug):
    try:
        if slug:
                post = Post.objects.get(slug = slug)
        if request.method == 'POST':
                Comment.objects.create(
                        post = post,
                        poster = request.POST['poster'],
                        context = request.POST['context'],
                )
                Comment.save(post)
        return render(request,'Post.html',{'post' : post })
    except:
        return redirect('/404')