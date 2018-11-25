from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,render
from django.shortcuts import redirect
from django.utils import timezone

from Django_website.forms import PostForm,CommentForm
from blog.models import Post,Comment

def ShowIndex(request):
    posts = Post.objects.all().order_by('-publish_time')
    return render_to_response('Index.html',locals())
def ShowPost(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        if request.method == 'POST':
                Comment.objects.create(
                        post = Post.objects.get(slug = slug),
                        poster = request.POST['poster'],
                        context = request.POST['context'],
                )
                Comment.save(post)
                return redirect('/post/'+slug)
        return render(request,'Post.html',locals())
    except:
        return redirect('/404')

@login_required
def EditPost(request):
        if request.method == 'POST':
                form = PostForm(request.POST ,request.FILES )
                if form.is_valid():
                        form.save(Post)
                return redirect('/')
        else:
                form = PostForm()
        return render(request,'blog/Edit_Post.html',locals())