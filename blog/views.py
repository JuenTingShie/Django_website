from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect


from Django_website.forms import PostForm
from blog.models import Post,Comment

def ShowIndex(request):
    posts = Post.objects.all().order_by('-publish_time')
    return render(request,'Index.html',locals())
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
                author = Post(author = request.user)
                form = PostForm(request.POST ,request.FILES ,instance = author)
                if form.is_valid():
                        form.save()
                return HttpResponseRedirect('/')
        else:
                form = PostForm()
        return render(request,'blog/Edit_Post.html',locals())