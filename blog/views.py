from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect


from Django_website.forms import PostForm,CommentForm
from blog.models import Post,Comment

def ShowIndex(request):
    posts = Post.objects.all().order_by('-publish_time')
    return render(request,'Index.html',locals())
def ShowPost(request,slug):
#    try:
        post = Post.objects.get(slug = slug)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/post/'+slug)
        return render(request,'Post.html',locals())
#    except:
#        return redirect('/404')

def EditPost(request,id):
    post = Post.objects.get(id = id)
    if request.user.has_perm('blog.change_Post'):
        if id:
            form = PostForm(instance = post)
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES, instance = post,)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/post/'+post.slug)
        return render(request,'blog/Edit_Post.html',locals())
    else:
        return HttpResponseRedirect('/accounts/login/?next=/post/edit_/'+str(id))

@login_required
def NewPost(request):
    if request.user.has_perm('blog.add_Post'):
        if request.method == 'POST':
            author = Post(author = request.user)
            form = PostForm(request.POST, request.FILES, instance = author)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = PostForm()
        return render(request,'blog/Edit_Post.html',locals())
    else:
        return HttpResponseRedirect('/dashboard/new_post/')
