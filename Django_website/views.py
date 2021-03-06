from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import redirect

from blog.models import Post
def history(request):
    return render(request,'history.html',{})
def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request,'registration/Signup.html',{'form' : UserCreationForm()})

def error404(request):
    return render(request,'404.html',{})

@login_required
def Dashboard(request):
    posts = Post.objects.all().order_by('-publish_time')
    return render(request,'Dashboard.html',locals())